from maspy import batch_master, batch_convert_to_mp3
from maspy.utils import find_target_files

if __name__ == "__main__":

    # Convert m4a to mp3 if needed
    target_file_paths = find_target_files(
        r"C:\Users\epvon\Music\Band\Band Nijkerk\Opnames\WIP",
        "*.m4a",
    )
    batch_convert_to_mp3(
        target_file_paths,
        remove_original=True,
    )

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
    batch_convert_to_mp3(
        mastered_wav_files,
        remove_original=True,
    )
