from pathlib import Path, WindowsPath
from typing import Union, Iterable


def find_target_files(
    target_folder_path: Union[str, WindowsPath],
    wildcard: str,
) -> Iterable:
    return Path(target_folder_path).glob(wildcard)
