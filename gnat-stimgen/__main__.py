from .datasets.EngCym import pstimlist, pstimdict, astimdict
from .validation import validate_pstimlist


def main():
    from pprint import pprint
    pprint(pstimdict)
    print("==================")
    pprint(astimdict)
    print("==================")
    errors, warnings = validate_pstimlist(pstimlist)
    if errors:
        for error in errors:
            print(f"E {error}")
    if warnings:
        for warning in warnings:
            print(f"W {warning}")
    if not errors and not warnings:
        print("pstimlist checked with no errors or warnings.")


if __name__ == "__main__":
    main()
