"""Types for experimental items for the GNAT."""
from typing import Literal, NamedTuple

# Literal string alias for picture valence
Valence = Literal["pos", "neg"]


class PictureStimulus(NamedTuple):
    """Represents a picture/image stimulus."""
    filename: str
    description: str
    valence: Valence

    def __str__(self) -> str:
        return (
            f"PictureStim({self.filename}, "
            f"{self.valence}, "
            f"{self.description})"
        )


class AudioStimulus(NamedTuple):
    """Represents an audio stimulus."""
    filename: str
    description: str
    language: str
    compatible_pos: list[PictureStimulus]
    compatible_neg: list[PictureStimulus]

    @property
    def compatibles(self) -> list[PictureStimulus]:
        return self.compatible_pos + self.compatible_neg

    def __str__(self) -> str:
        return (
            f"AudioStim({self.filename}, "
            f"{self.language}, "
            f"{self.description})"
        )


class StimulusSequence(NamedTuple):
    """Represents a sequence of an audio stimulus and a picture stimulus."""
    first: AudioStimulus
    second: PictureStimulus

    @property
    def pattern(self) -> str:
        return f"{self.first.language}>{self.second.valence}"

    @property
    def identifier(self) -> str:
        return f"{self.first.filename}>{self.second.filename}"

    def __str__(self) -> str:
        return f"StimSeq({self.identifier}, {self.pattern})"


class BlockRow(NamedTuple):
    """Represents a row of a trial for an experimental block."""
    stimseq: StimulusSequence
    condition: tuple[str, str]
    languages: tuple[str, str]

    @property
    def soundstimuli(self) -> str:
        return f"stimuli/{self.stimseq.first.filename}"

    @property
    def sounddescription(self) -> str:
        return self.stimseq.first.description

    @property
    def soundcorrAns(self) -> str:
        if self.stimseq.first.language == self.condition[0]:
            return "space"
        return "None"

    @property
    def block_triggerID(self) -> int:
        if self.condition == (self.languages[0], "pos"):
            return 1
        if self.condition == (self.languages[0], "neg"):
            return 2
        if self.condition == (self.languages[1], "pos"):
            return 3
        if self.condition == (self.languages[1], "neg"):
            return 4
        return 9  # 9 as error sentinel (never used in the GNAT experiment)

    @property
    def lang_triggerID(self) -> int:
        if self.stimseq.first.language == self.languages[0]:
            return 1
        if self.stimseq.first.language == self.languages[1]:
            return 2
        return 9  # 9 as error sentinel (never used in the GNAT experiment)

    @property
    def imagestimuli(self) -> str:
        return f"stimuli/{self.stimseq.second.filename}"

    @property
    def imagedescription(self) -> str:
        return self.stimseq.second.description

    @property
    def imagecorrAns(self) -> str:
        if self.stimseq.second.valence == self.condition[1]:
            return "space"
        return "None"

    @property
    def img_triggerID(self) -> int:
        if self.stimseq.first.language == self.languages[0]:  # Eng
            if self.stimseq.second.valence == "pos":  # EngPosPic
                return 3
            if self.stimseq.second.valence == "neg":  # EngNegPic
                return 5
        if self.stimseq.first.language == self.languages[1]:  # Cym
            if self.stimseq.second.valence == "pos":  # CymPosPic
                return 4
            if self.stimseq.second.valence == "neg":  # CymNegPic
                return 6
        return 9  # 9 as error sentinel (never used in the GNAT experiment)
        # if self.stimseq.second.valence == "pos":
        #     return int(f"{self.lang_triggerID}1")
        # elif self.stimseq.second.valence == "neg":
        #     return int(f"{self.lang_triggerID}2")
        # else:
        #     return int(f"{self.lang_triggerID}5")

    def __str__(self) -> str:
        return (
            f"{self.condition[0]}/{self.condition[1]}"
            f"\t{self.soundstimuli}"
            f"\t{self.sounddescription}"
            f"\t{self.soundcorrAns}"
            f"\t{self.block_triggerID}{self.lang_triggerID}"
            f"\t{self.imagestimuli}"
            f"\t{self.imagedescription}"
            f"\t{self.imagecorrAns}"
            f"\t{self.block_triggerID}{self.img_triggerID}"
        )
