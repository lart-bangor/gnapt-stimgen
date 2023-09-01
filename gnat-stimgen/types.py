from typing import Literal, NamedTuple

Valence = Literal["pos", "neg"]


class PictureStimulus(NamedTuple):
    filename: str
    description: str
    valence: Valence

    def __str__(self) -> str:
        return f"PictureStim({self.filename}, {self.valence}, {self.description})"


class AudioStimulus(NamedTuple):
    filename: str
    description: str
    language: str
    compatible_pos: list[PictureStimulus]
    compatible_neg: list[PictureStimulus]

    @property
    def compatibles(self) -> list[PictureStimulus]:
        return self.compatible_pos + self.compatible_neg

    def __str__(self) -> str:
        return f"AudioStim({self.filename}, {self.language}, {self.description})"


class StimulusSequence(NamedTuple):
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
    def lang_triggerID(self) -> int:
        if self.stimseq.first.language == self.languages[0]:
            return 1
        elif self.stimseq.first.language == self.languages[1]:
            return 2
        return 5  # 5 as error sentinel (never used in the GNAT experiment)

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
        if self.stimseq.second.valence == "pos":
            return int(f"{self.lang_triggerID}1")
        elif self.stimseq.second.valence == "neg":
            return int(f"{self.lang_triggerID}2")
        else:
            return int(f"{self.lang_triggerID}5")

    def __str__(self) -> str:
        return (
            f"{self.condition[0]}/{self.condition[1]}"
            f"\t{self.soundstimuli}\t{self.sounddescription}"
            f"\t{self.soundcorrAns}\t{self.lang_triggerID}"
            f"\t{self.imagestimuli}\t{self.imagedescription}"
            f"\t{self.imagecorrAns}\t{self.img_triggerID}"
        )
