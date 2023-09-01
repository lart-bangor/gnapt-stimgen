from .types import PictureStimulus, AudioStimulus


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


def validate_astimlist(astimlist: list[AudioStimulus]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    # E Check total number of items (should be 80)
    if len(astimlist) < 80:
        errors.append(
            "Audio stimulus list too short: expected 80 items, "
            f"{len(astimlist)} given."
        )
    if len(astimlist) > 80:
        errors.append(
            "Audio stimulus list too long: expected 80 items, "
            f"{len(astimlist)} given."
        )

    # E Check for number of languages coded
    languages_coded = {x.language for x in astimlist}
    if len(languages_coded) < 2:
        errors.append(
            "Audio stimulus list codes too few languages: 2 expected, "
            f"{len(languages_coded)} given (namely {languages_coded!r})."
        )
    if len(languages_coded) > 2:
        errors.append(
            "Audio stimulus list codes too many languages: 2 expected, "
            f"{len(languages_coded)} given (namely {languages_coded!r})."
        )

    # E Check balance of languages coded
    if len(languages_coded) >= 2:
        l1, l2 = list(languages_coded)[:2]
        count_l1: int = len([x for x in astimlist if x.language == l1])
        count_l2: int = len([x for x in astimlist if x.language == l1])
        if count_l1 != count_l2:
            errors.append(
                "Unbalanced language distribution of audio stimulus items: "
                f"expected 40*{l1}:40*{l2}, {count_l1}*{l1}:{count_l2}*{l2} given."
            )

    # E Check for number of compatible positive and negative pictures
    COMPATIBLE_ITEMS_REQUIRED: int = 4
    compatible_item_counts: dict[str, tuple[int, int]] = {
        x.filename: (len(x.compatible_pos), len(x.compatible_neg)) for x in astimlist
    }
    too_few_positive: set[str] = {
        k for k, v in compatible_item_counts.items() if v[0] < COMPATIBLE_ITEMS_REQUIRED
    }
    too_few_negative: set[str] = {
        k for k, v in compatible_item_counts.items() if v[1] < COMPATIBLE_ITEMS_REQUIRED
    }
    too_many_positive: set[str] = {
        k for k, v in compatible_item_counts.items() if v[0] > COMPATIBLE_ITEMS_REQUIRED
    }
    too_many_negative: set[str] = {
        k for k, v in compatible_item_counts.items() if v[1] > COMPATIBLE_ITEMS_REQUIRED
    }
    if too_few_positive:
        errors.append(
            "One or more audio stimulus items have too few compatible positive "
            f"picture stimuli: check items {too_few_positive!r}."
        )
    if too_few_negative:
        errors.append(
            "One or more audio stimulus items have too few compatible negative "
            f"picture stimuli: check items {too_few_negative!r}."
        )
    if too_many_positive:
        errors.append(
            "One or more audio stimulus items have too many compatible positive "
            f"picture stimuli: check items {too_many_positive!r}."
        )
    if too_many_negative:
        errors.append(
            "One or more audio stimulus items have too many compatible negative "
            f"picture stimuli: check items {too_many_negative!r}."
        )

    # E Check for distinctness of compatible positive and negative pictures
    overlapping_positives: set[AudioStimulus] = set()
    overlapping_negatives: set[AudioStimulus] = set()
    for stim in astimlist:
        if len(set(stim.compatible_pos)) != len(stim.compatible_pos):
            overlapping_positives.add(stim.filename)
        if len(set(stim.compatible_neg)) != len(stim.compatible_neg):
            overlapping_negatives.add(stim.filename)
    if overlapping_positives:
        errors.append(
            "One or more audio stimulus items have repeated compatible positive "
            f"picture stimuli: check items {overlapping_positives!r}."
        )
    if overlapping_negatives:
        errors.append(
            "One or more audio stimulus items have repeated compatible negative "
            f"picture stimuli: check items {overlapping_negatives!r}."
        )

    # E Check for distribution of compatible positive and negative pictures
    positive_picture_associations: dict[str, set[AudioStimulus]] = {}
    negative_picture_associations: dict[str, set[AudioStimulus]] = {}
    for stim in astimlist:
        for pstim in stim.compatible_pos:
            if pstim.filename not in positive_picture_associations:
                positive_picture_associations[pstim.filename] = {stim.filename}
            else:
                positive_picture_associations[pstim.filename].add(stim.filename)
        for pstim in stim.compatible_neg:
            if pstim.filename not in negative_picture_associations:
                negative_picture_associations[pstim.filename] = {stim.filename}
            else:
                negative_picture_associations[pstim.filename].add(stim.filename)
    uneven_positive_pictures: dict[str, set[AudioStimulus]] = {
        k: v for k, v in positive_picture_associations.items() if len(v) != 8
    }
    uneven_negative_pictures: dict[str, set[AudioStimulus]] = {
        k: v for k, v in negative_picture_associations.items() if len(v) != 8
    }
    if uneven_positive_pictures:
        e_list: list[str] = [
            (
                f"    - {pfname!r} associated to {len(afnames)} audio stimuli "
                f"(should be 8), check items {afnames!r}."
            )
            for pfname, afnames in uneven_positive_pictures.items()
        ]
        e_appendix = "\n".join(e_list)
        errors.append(
            "One or more positive picture stimuli are marked as compatible "
            f"with an uneven number of audio stimuli: {e_appendix}"
        )
    if uneven_negative_pictures:
        e_list: list[str] = [
            (
                f"    - {pfname!r} associated to {len(afnames)} audio stimuli "
                f"(should be 8), check items {afnames!r}."
            )
            for pfname, afnames in uneven_negative_pictures.items()
        ]
        e_appendix = "\n".join(e_list)
        errors.append(
            "One or more negative picture stimuli are marked as compatible "
            f"with an uneven number of audio stimuli: {e_appendix}"
        )

    # E Check for duplicate filenames
    fnames: list[str] = [x.filename for x in astimlist]
    if len(fnames) != len(set(fnames)):
        fnames_seen: set[str] = set()
        fname_duplicates: set[str] = set()
        for fname in fnames:
            if fname in fnames_seen:
                fname_duplicates.add(fname)
            else:
                fnames_seen.add(fname)
        errors.append(
            f"Audio stimulus filename(s) repeated: {fname_duplicates!r}."
        )

    # W Check for invalid language fields
    known_languages = ("Eng", "Cym", "Ger", "Ltz", "Lmo", "Ita")
    invalid_languages = {x.language for x in astimlist if x.language not in known_languages}
    if len(invalid_languages) > 0:
        warnings.append(
            "Possibly invalid values for audio stimulus languages found: "
            f"{invalid_languages!r}."
        )

    # W Check for duplicate descriptions
    descs: list[str] = [x.description for x in astimlist]
    if len(descs) != len(set(descs)):
        # FIND DUPLICATES
        desc_index: dict[str, set[str]] = {}
        for stim in astimlist:
            if stim.description in desc_index:
                desc_index[stim.description].add(stim.filename)
            else:
                desc_index[stim.description] = {stim.filename}
        desc_index = {tuple(f) for _, f in desc_index.items() if len(f) > 1}
        warnings.append(
            "Several audio stimulus descriptions are identical: check items "
            f"{desc_index!r}."
        )

    # W Check for filenames indicative of different language
    if len(languages_coded) >= 2:
        l1, l2 = list(languages_coded)[:2]
        l1_l2: set[str] = {x.filename for x in astimlist if l1.lower() in x.filename.lower() and x.language.lower() == l2.lower()}
        l2_l1: set[str] = {x.filename for x in astimlist if l2.lower() in x.filename.lower() and x.language.lower() == l1.lower()}
        if l1_l2:
            warnings.append(
                f"One or more audio stimulus filenames hint at language {l1} "
                f"although the item is coded as {l2}: check items "
                f"{l1_l2!r}."
            )
        if l2_l1:
            warnings.append(
                f"One or more audio stimulus filenames hint at language {l2} "
                f"although the item is coded as {l1}: check items "
                f"{l2_l1!r}."
            )

    # Return errors and warnings, if any
    return (errors, warnings)
