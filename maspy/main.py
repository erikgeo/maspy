import matchering as mg
from pathlib import Path, WindowsPath
from typing import Union, Iterable, List
from pydub import AudioSegment
from tqdm import tqdm

AudioSegment.converter = Path(__file__).parents[1] / "ffmpeg" / "ffmpeg.exe"


def find_target_files(
    target_folder_path: Union[str, WindowsPath],
    wildcard: str,
) -> Iterable:
    return Path(target_folder_path).glob(wildcard)


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


def batch_convert_wav_to_mp3(
    audio_files: List[Union[str, WindowsPath]],
    remove_unconverted=False,
):
    for audio_file in tqdm(audio_files, desc="Converting mastered audio to mp3"):
        audio_data = AudioSegment.from_wav(audio_file)
        audio_file = Path(audio_file)
        audio_data.export(
            (audio_file.parent / (audio_file.stem + ".mp3")),
            format="mp3",
            bitrate="192k",
        )
        if remove_unconverted:
            audio_file.unlink()


if __name__ == "__main__":

    # Master
    target_file_paths = find_target_files(
        r"C:\Users\epvon\Music\Band\Band Nijkerk\Opnames\WIP",
        "*.mp3",
    )
    batch_master(
        target_file_paths,
        r"C:\Users\epvon\Music\Band\Band Nijkerk\Opnames\reference_track.mp3",
        r"C:\Users\epvon\Music\Band\Band Nijkerk\Opnames\WIP",
    )

    # Convert
    mastered_wav_files = find_target_files(
        r"C:\Users\epvon\Music\Band\Band Nijkerk\Opnames\WIP",
        "*.wav",
    )
    batch_convert_wav_to_mp3(
        mastered_wav_files,
        remove_unconverted=True,
    )
