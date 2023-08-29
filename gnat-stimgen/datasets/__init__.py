from ..types import AudioStimulus, PictureStimulus


def get_audio_stimuli(lang_pair: str) -> tuple[list[AudioStimulus], dict[str, AudioStimulus]]:
    if lang_pair not in ("EngCym"):
        raise RuntimeError(
            f"Attempting to retreive audio stimuli for unknown language pair {lang_pair!r}."
        )
    if lang_pair == "EngCym":
        from .EngCym import astimlist, astimdict
        return (astimlist.copy(), astimdict.copy())


def get_picture_stimuli(lang_pair: str) -> tuple[list[PictureStimulus], dict[str, PictureStimulus]]:
    if lang_pair not in ("EngCym"):
        raise RuntimeError(
            f"Attempting to retreive picture stimuli for unknown language pair {lang_pair!r}."
        )
    if lang_pair == "EngCym":
        from .EngCym import pstimlist, pstimdict
        return (pstimlist.copy(), pstimdict.copy())
