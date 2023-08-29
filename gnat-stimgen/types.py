from typing import Literal, NamedTuple

Valence = Literal["pos", "neg"]


class PictureStimulus(NamedTuple):
    filename: str
    description: str
    valence: Valence


class AudioStimulus(NamedTuple):
    filename: str
    description: str
    language: str
    compatible_pos: list[PictureStimulus]
    compatible_neg: list[PictureStimulus]
