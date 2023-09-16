import sys
import random
import re
import click as cli
import xlsxwriter
from .datasets import get_audio_stimuli, get_picture_stimuli
from .validation import validate_pstimlist, validate_astimlist
from .types import PictureStimulus, AudioStimulus, StimulusSequence, BlockRow


def validate_stimuli(
        pstimlist: list[PictureStimulus],
        astimlist: list[AudioStimulus],
        languages: tuple[str, str]
        ) -> bool:
    """Validate the picture and audio stimulus lists."""
    validation_passed = True

    cli.echo("Validating picture stimulus set...")
    errors, warnings = validate_pstimlist(pstimlist)
    if errors:
        for error in errors:
            cli.secho("  E ", nl=False, err=True, fg="red")
            cli.echo(error)
    if warnings:
        for warning in warnings:
            cli.secho("  W ", nl=False, err=True, fg="yellow")
            cli.echo(warning)
    if not errors and not warnings:
        cli.secho("  OK ", nl=False, fg="green")
        cli.echo("Picture stimulus list validated with no errors or warnings.")
    elif errors:
        cli.secho("  XX ", nl=False, fg="red")
        cli.secho(
            f"Picture stimulus validation failed with {len(errors)} errors, "
            f"{len(warnings)} warnings.",
            fg="black", bg="white"
        )
        validation_passed = False
    elif warnings:
        cli.secho("  !! ", nl=False, fg="yellow")
        cli.echo(
            "Picture stimulus list validated with no errors but "
            f"{len(warnings)} warnings."
        )

    cli.echo("Validating audio stimulus set...")
    errors, warnings = validate_astimlist(astimlist, languages)
    if errors:
        for error in errors:
            cli.secho("  E ", nl=False, err=True, fg="red")
            cli.echo(error)
    if warnings:
        for warning in warnings:
            cli.secho("  W ", nl=False, err=True, fg="yellow")
            cli.echo(warning)
    if not errors and not warnings:
        cli.secho("  OK ", nl=False, fg="green")
        cli.echo("Audio stimulus list validated with no errors or warnings.")
    elif errors:
        cli.secho("  !! ", nl=False, fg="red")
        cli.secho(
            f"Audio stimulus validation failed with {len(errors)} errors, "
            f"{len(warnings)} warnings.",
            fg="black", bg="white"
        )
        validation_passed = False
    elif warnings:
        cli.secho("  OK ", nl=False, fg="yellow")
        cli.echo(
            "Audio stimulus list validated with no errors but "
            f"{len(warnings)} warnings."
        )

    return validation_passed


def load_stimuli_lists(
        language_pair: str
        ) -> tuple[
            list[PictureStimulus], dict[str, PictureStimulus],
            list[AudioStimulus], dict[str, AudioStimulus]
        ]:
    """Load stimuli lists for *language_pair*."""
    cli.echo(
        f"Loading stimulus lists for language pair {language_pair}..", nl=False
    )
    try:
        pstimlist, _ = get_picture_stimuli(language_pair)
        astimlist, _ = get_audio_stimuli(language_pair)
        cli.secho(" OK.", fg="green")
    except (RuntimeError, ModuleNotFoundError) as e:
        cli.secho(" XX.", fg="red")
        cli.secho("XX ", nl=False, err=True, fg="red")
        cli.secho(str(e), err=True, fg="black", bg="white")
        return ([], [])
    return (pstimlist, astimlist)


def build_stimulus_sequences(
        astimlist: list[AudioStimulus]
        ) -> list[StimulusSequence]:
    sequences: list[StimulusSequence] = []

    cli.echo("Building stimulus sequences...", nl=False)
    for astim in astimlist:
        for pstim in astim.compatibles:
            seq = StimulusSequence(astim, pstim)
            sequences.append(seq)
    cli.secho(" OK.", fg="green")
    return sequences


def make_block(
        condition: tuple[str, str],
        languages: tuple[str, str],
        stimseqs: list[StimulusSequence],
        ) -> tuple[list[BlockRow], list[StimulusSequence]]:
    rows: list[BlockRow] = []
    l1, l2 = languages
    patterns = (
        f"{l1}>pos",
        f"{l1}>neg",
        f"{l2}>pos",
        f"{l2}>neg"
    )
    afnames_drawn: set[str] = set()
    pfnames_drawn: set[str] = set()
    for pattern in patterns:
        # Draw 20 per pattern, don't repeat afnames or pfnames
        for i in range(0, 20):
            # Find first item in list that fits conditions
            for stimseq in stimseqs:
                if (
                    stimseq.pattern == pattern
                    and stimseq.first.filename not in afnames_drawn
                    and stimseq.second.filename not in pfnames_drawn
                   ):
                    afnames_drawn.add(stimseq.first.filename)
                    pfnames_drawn.add(stimseq.second.filename)
                    rows.append(BlockRow(stimseq, condition, languages))
                    stimseqs.remove(stimseq)
                    break

    return (rows, stimseqs)


def write_block(name: str, rows: list[BlockRow]):
    # Write as excel file
    workbook = xlsxwriter.Workbook(f"./{name}.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write_row(
        0, 0,
        (
            "goConditions",
            "soundstimuli",
            "sounddescription",
            "soundcorrAns",
            "lang_triggerId",
            "imagestimuli",
            "imagedescription",
            "imagecorrAns",
            "img_triggerId"
        )
    )
    row_index = 1
    for row in rows:
        worksheet.write_row(
            row_index, 0,
            str(row).split("\t")
        )
        row_index += 1
    workbook.close()
    # Write as TSV file
    # with open(f"./{name}.tsv", "w") as fh:
    #     fh.write(
    #         "goConditions\t"
    #         "soundstimuli\t"
    #         "sounddescription\t"
    #         "soundcorrAns\t"
    #         "lang_triggerID\t"
    #         "imagestimuli\t"
    #         "imagedescription\t"
    #         "imagecorrAns\t"
    #         "img_triggerId\n"
    #     )
    #     for row in rows:
    #         fh.write(str(row))
    #         fh.write("\n")


def exit_fail():
    cli.secho("FAILED 😭", fg="bright_red")
    sys.exit(1)


def exit_success():
    cli.secho("SUCCESS 😄", fg="bright_green", bold=True)
    sys.exit(0)


@cli.command()
@cli.argument("language_pair", required=False)
def main(language_pair: str | None = None):
    """Stimulus generator for the Go-No Go Association Task ('23/24).

    The optional argument LANGUAGE_PAIR can be one of EngCym, GerLtz, or
    ItaLmo (default: EngCym).
    """

    # Determine and load language pair
    if not language_pair:
        language_pair = "EngCym"
        cli.secho("!! ", nl=False, fg="yellow")
        cli.echo("No language pair specified, assuming EngCym.")

    m = re.search(r"([A-Z][a-z]{2})([A-Z][a-z]{2})", language_pair)
    if not m:
        cli.secho("XX ", err=True, fg="red", nl=False)
        cli.secho(
            f"'{language_pair}' is not a valid language pair code "
            f"(must match XxxYyy).",
            bg="white", err=True
        )
        exit_fail()
    languages: tuple[str, str] = m.groups()

    # Load stimulus lists
    pstimlist, astimlist = load_stimuli_lists(language_pair)
    if not pstimlist:
        exit_fail()

    # Randomize audio stimulus list
    cli.echo("Randomizing audio stimulus pairs.. ", nl=False)
    random.shuffle(astimlist)
    cli.secho("OK.", fg="green")

    # Validate stimulus lists
    if not validate_stimuli(pstimlist, astimlist, languages):
        exit_fail()

    # Build stimulus sequences
    stimseqs = build_stimulus_sequences(astimlist)
    print("Stimseqs original length:", len(stimseqs))

    # Generate and write experimental blocks
    blocks_to_generate = {
        "block1": ((languages[0], "neg"), languages),
        "block2": ((languages[0], "neg"), languages),
        "block3": ((languages[1], "pos"), languages),
        "block4": ((languages[1], "pos"), languages),
        "block5": ((languages[1], "neg"), languages),
        "block6": ((languages[1], "neg"), languages),
        "block7": ((languages[0], "pos"), languages),
        "block8": ((languages[0], "pos"), languages),
    }
    for block_name, block_spec in blocks_to_generate.items():
        # Generate block
        cli.echo(f"Generating block '{block_name}'... ")
        cli.secho("  i ", fg="blue", nl=False)
        cli.secho(f"Go conditions: {block_spec[0]}")
        block, stimseqs = make_block(*block_spec, stimseqs)
        cli.secho("  OK ", fg="green", nl=False)
        cli.echo("Block generated successfully.")
        # Write block
        cli.echo(f"Writing block '{block_name}' to file...")
        cli.secho("  i ", fg="blue", nl=False)
        cli.echo(f"Path of file: ./{block_name}.xlsx")
        write_block(block_name, block)
        cli.secho("  OK ", fg="green", nl=False)
        cli.echo("File written successfully.")

    exit_success()


if __name__ == "__main__":
    main()
