import sys
import random
import click as cli
from .datasets import get_audio_stimuli, get_picture_stimuli
from .validation import validate_pstimlist, validate_astimlist
from .types import PictureStimulus, AudioStimulus, StimulusSequence, BlockRow


def validate_stimuli(
        pstimlist: list[PictureStimulus],
        astimlist: list[AudioStimulus]
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
    errors, warnings = validate_astimlist(astimlist)
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
    except RuntimeError as e:
        cli.secho(" XX.", fg="red")
        cli.secho("XX ", nl=False, err=True, fg="red")
        cli.secho(str(e), err=True, fg="black", bg="white")
        return ([], [], [], [])
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
                if stimseq.pattern == pattern and stimseq.first.filename not in afnames_drawn and stimseq.second.filename not in pfnames_drawn:
                    afnames_drawn.add(stimseq.first.filename)
                    pfnames_drawn.add(stimseq.second.filename)
                    rows.append(BlockRow(stimseq, condition, (l1, l2)))
                    stimseqs.remove(stimseq)
                    break

    return (rows, stimseqs)


# def randomize_stimseqs(stimseqs: list[StimulusSequence]) -> list[StimulusSequence]:
#     if len(stimseqs) > 2080:
#         print("  W not all possible randomizations of the stimulus sequences can be generated.")
#     stimseqs_cp = stimseqs.copy()
#     random.shuffle(stimseqs_cp)
#     return stimseqs_cp


def write_block(name: str, rows: list[BlockRow]):
    with open(f"./{name}.tsv", "w") as fh:
        fh.write(
            "goConditions\t"
            "soundstimuli\t"
            "sounddescription\t"
            "soundcorrAns\t"
            "lang_triggerID\t"
            "imagestimuli\t"
            "imagedescription\t"
            "imagecorrAns\t"
            "img_triggerId\n"
        )
        for row in rows:
            fh.write(str(row))
            fh.write("\n")


@cli.command()
@cli.argument("language_pair", required=False)
def main(language_pair: str | None = None):
    """Stimulus generator for the Go-No Go Association Task ('23/24).

    The optional argument LANGUAGE_PAIR can be one of EngCym, GerLtz, or
    ItaLmo (default: EngCym).
    """

    if not language_pair:
        language_pair = "EngCym"
        cli.secho("!! ", nl=False, fg="yellow")
        cli.echo("No language pair specified, assuming EngCym.")

    pstimlist, astimlist = load_stimuli_lists(
        language_pair
    )
    if not pstimlist:
        sys.exit(1)

    random.shuffle(astimlist)

    if not validate_stimuli(pstimlist, astimlist):
        sys.exit(1)

    stimseqs = build_stimulus_sequences(astimlist)
    print("Stimseqs original length:", len(stimseqs))

    # @TODO - This code needs to be independent of hardcoded Eng/Cym and use
    #         variable l1/l2 instead.
    target_languages = ("Eng", "Cym")
    blocks_to_generate = {
        "block1": (("Eng", "neg"), target_languages),
        "block2": (("Eng", "neg"), target_languages),
        "block3": (("Cym", "pos"), target_languages),
        "block4": (("Cym", "pos"), target_languages),
        "block5": (("Cym", "neg"), target_languages),
        "block6": (("Cym", "neg"), target_languages),
        "block7": (("Eng", "pos"), target_languages),
        "block8": (("Eng", "pos"), target_languages),
    }
    for block_name, block_spec in blocks_to_generate.items():
        cli.echo(f"Generating block '{block_name}'... ", nl=False)
        block, stimseqs = make_block(*block_spec, stimseqs)
        cli.secho("OK.", fg="green")
        cli.echo(f"Writing block '{block_name}' to file...")
        cli.secho("  i ", fg="blue", nl=False)
        cli.echo(f"Path of file: ./{block_name}.tsv")
        write_block(block_name, block)
        cli.secho("  OK ", fg="green", nl=False)
        cli.echo("File written successfully.")

    # block1, nstimseqs = make_block(("Eng", "neg"), ("Eng", "Cym"), stimseqs)
    # print("Stimseqs after block1:", len(nstimseqs))
    # block2, nstimseqs = make_block(("Eng", "neg"), ("Eng", "Cym"), nstimseqs)
    # print("Stimseqs after block2:", len(nstimseqs))
    # block3, nstimseqs = make_block(("Cym", "pos"), ("Eng", "Cym"), nstimseqs)
    # print("Stimseqs after block3:", len(nstimseqs))
    # block4, nstimseqs = make_block(("Cym", "pos"), ("Eng", "Cym"), nstimseqs)
    # print("Stimseqs after block4:", len(nstimseqs))
    # block5, nstimseqs = make_block(("Cym", "neg"), ("Eng", "Cym"), nstimseqs)
    # print("Stimseqs after block5:", len(nstimseqs))
    # block6, nstimseqs = make_block(("Cym", "neg"), ("Eng", "Cym"), nstimseqs)
    # print("Stimseqs after block6:", len(nstimseqs))
    # block7, nstimseqs = make_block(("Eng", "pos"), ("Eng", "Cym"), nstimseqs)
    # print("Stimseqs after block7:", len(nstimseqs))
    # block8, nstimseqs = make_block(("Eng", "pos"), ("Eng", "Cym"), nstimseqs)
    # print("Stimseqs after block8:", len(nstimseqs))
    # write_block("block1", block1)
    # write_block("block2", block2)
    # write_block("block3", block3)
    # write_block("block4", block4)
    # write_block("block5", block5)
    # write_block("block6", block6)
    # write_block("block7", block7)
    # write_block("block8", block8)

    # print("Stimseqs left over:", len(nstimseqs))

    cli.secho("SUCCESS :)", fg="bright_green", bold=True)

    sys.exit(0)


if __name__ == "__main__":
    main()
