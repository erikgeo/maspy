import matchering as mg
from pathlib import Path, WindowsPath
from typing import Union, List
from pydub import AudioSegment
from tqdm import tqdm


def batch_master(
    target_files: List[Union[str, WindowsPath]],
    reference_file: Union[str, WindowsPath],
    output_folder: Union[str, WindowsPath],
):
    for target_file in tqdm(target_files, desc="Mastering songs..."):
        mg.process(
            target=target_file,
            reference=reference_file,
            results=[
                mg.pcm16(Path(output_folder) / (target_file.stem + "_mastered.wav")),
            ],
        )


def batch_convert_to_mp3(
    audio_files: List[Union[str, WindowsPath]],
    remove_original=False,
):
    for audio_file in tqdm(audio_files, desc="Converting audio to mp3"):
        audio_data = AudioSegment.from_file(audio_file)
        audio_file = Path(audio_file)
        audio_data.export(
            (audio_file.parent / (audio_file.stem + ".mp3")),
            format="mp3",
            bitrate="192k",
        )
        if remove_original:
            audio_file.unlink()
