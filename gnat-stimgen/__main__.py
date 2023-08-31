import sys
import click as cli
from .datasets import get_audio_stimuli, get_picture_stimuli
from .validation import validate_pstimlist, validate_astimlist
from .types import PictureStimulus, AudioStimulus


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
        pstimlist, pstimdict = get_picture_stimuli(language_pair)
        astimlist, astimdict = get_audio_stimuli(language_pair)
        cli.secho(" OK.", fg="green")
    except RuntimeError as e:
        cli.secho(" XX.", fg="red")
        cli.secho("XX ", nl=False, err=True, fg="red")
        cli.secho(str(e), err=True, fg="black", bg="white")
        return ([], [], [], [])
    return (pstimlist, pstimdict, astimlist, astimdict)


@cli.command()
@cli.argument("language_pair", required=False)
def main(language_pair: str | None = None):
    """Stimulus generator for the Go-No Go Association Task ('23/24)"""

    if not language_pair:
        language_pair = "EngCym"
        cli.secho("!! ", nl=False, fg="yellow")
        cli.echo("No language pair specified, assuming EngCym.")

    pstimlist, pstimdict, astimlist, astimdict = load_stimuli_lists(
        language_pair
    )
    if not pstimlist:
        sys.exit(1)

    if not validate_stimuli(pstimlist, astimlist):
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
