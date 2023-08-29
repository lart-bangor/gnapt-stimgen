from .datasets import get_audio_stimuli, get_picture_stimuli
from .validation import validate_pstimlist, validate_astimlist


def main():
    pstimlist, pstimdict = get_picture_stimuli("EngCym")
    astimlist, astimdict = get_audio_stimuli("EngCym")

    print("Validating picture stimulus set...")
    errors, warnings = validate_pstimlist(pstimlist)
    if errors:
        for error in errors:
            print(f"  E {error}")
    if warnings:
        for warning in warnings:
            print(f"  W {warning}")
    if not errors and not warnings:
        print("  OK pstimlist checked with no errors or warnings.")

    print("Validating audio stimulus set...")
    errors, warnings = validate_astimlist(astimlist)
    if errors:
        for error in errors:
            print(f"  E {error}")
    if warnings:
        for warning in warnings:
            print(f"  W {warning}")
    if not errors and not warnings:
        print("  OK astimlist checked with no errors or warnings.")


if __name__ == "__main__":
    main()
