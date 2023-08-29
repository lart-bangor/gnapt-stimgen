from .types import PictureStimulus


def validate_pstimlist(pstimlist: list[PictureStimulus]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    # E Check total number of items (should be 80)
    if len(pstimlist) < 80:
        errors.append(
            "Picture stimulus list too short: expected 80 items, "
            f"{len(pstimlist)} given."
        )
    if len(pstimlist) > 80:
        errors.append(
            "Picture stimulus list too long: expected 80 items, "
            f"{len(pstimlist)} given."
        )

    # E Check for invalid valence fields
    invalid_valences = {x.valence for x in pstimlist if x.valence not in ("pos", "neg")}
    count_invalid = len(invalid_valences)
    if count_invalid > 0:
        errors.append(
            "Invalid values for picture stimulus valence: only {'pos', 'neg'} "
            f"allowed, {invalid_valences!r} found."
        )

    # E Check balance of positive and negative items
    count_pos = len([x for x in pstimlist if x.valence == "pos"])
    count_neg = len([x for x in pstimlist if x.valence == "neg"])
    if count_pos != count_neg:
        errors.append(
            "Unbalanced valence distribution of picture stimulus items: "
            f"expected 40*pos:40*neg, {count_pos}*pos:{count_neg}*neg given."
        )

    # E Check for duplicate filenames
    fnames: list[str] = [x.filename for x in pstimlist]
    if len(fnames) != len(set(fnames)):
        fnames_seen: set[str] = set()
        fname_duplicates: set[str] = set()
        for fname in fnames:
            if fname in fnames_seen:
                fname_duplicates.add(fname)
            else:
                fnames_seen.add(fname)
        errors.append(
            f"Picture stimulus filename(s) repeated: {fname_duplicates!r}."
        )

    # W Check for duplicate descriptions
    descs: list[str] = [x.description for x in pstimlist]
    if len(descs) != len(set(descs)):
        # FIND DUPLICATES]
        desc_index: dict[str, set[str]] = {}
        for stim in pstimlist:
            if stim.description in desc_index:
                desc_index[stim.description].add(stim.filename)
            else:
                desc_index[stim.description] = {stim.filename}
        desc_index = {tuple(f) for _, f in desc_index.items() if len(f) > 1}
        warnings.append(
            "Several picture stimulus descriptions are identical: check items "
            f"{desc_index!r}."
        )

    # W Check for filenames indicative of opposing valence
    pos_neg: set[str] = {x.filename for x in pstimlist if "pos" in x.filename.lower() and x.valence == "neg"}
    neg_pos: set[str] = {x.filename for x in pstimlist if "neg" in x.filename.lower() and x.valence == "pos"}
    if pos_neg:
        warnings.append(
            "One or more picture stimulus filenames hint at positive valence "
            "although the item is coded as negative: check items "
            f"{pos_neg!r}."
        )
    if neg_pos:
        warnings.append(
            "One or more picture stimulus filenames hint at negative valence "
            "although the item is coded as positive: check items "
            f"{neg_pos!r}."
        )

    # Return errors and warnings, if any
    return (errors, warnings)
