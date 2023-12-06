"""Datasets for the stimulus generator.

To add new datasets, create a new file with a language pair code (e.g.) EngCym
for English-Cymraeg based on one of the existing files, and add any newly
introduced language codes to the KNOWN_LANGUAGES constant in this file.
"""
from importlib import import_module
from typing import Final
from ..types import AudioStimulus, PictureStimulus


KNOWN_LANGUAGES: Final[tuple[str, ...]] = (
    "Eng", "Cym",
    "Ger", "Ltz",
    "Ita", "Lmo",
)

KNOWN_LANGUAGE_PAIRS: Final[tuple[str, ...]] = (
    "EngCym",
    "GerLtz",
    # "ItaLmo",
)


def get_audio_stimuli(
        lang_pair: str
        ) -> tuple[list[AudioStimulus], dict[str, AudioStimulus]]:
    if lang_pair not in KNOWN_LANGUAGE_PAIRS:
        raise RuntimeError(
            "Attempting to retreive audio stimuli for "
            f"unknown language pair {lang_pair!r}."
        )
    dataset = import_module(f".{lang_pair}", __package__)
    return (dataset.astimlist.copy(), dataset.astimdict.copy())


def get_picture_stimuli(
        lang_pair: str
        ) -> tuple[list[PictureStimulus], dict[str, PictureStimulus]]:
    if lang_pair not in KNOWN_LANGUAGE_PAIRS:
        raise RuntimeError(
            "Attempting to retreive picture stimuli for "
            f"unknown language pair {lang_pair!r}."
        )
    dataset = import_module(f".{lang_pair}", __package__)
    return (dataset.pstimlist.copy(), dataset.pstimdict.copy())
