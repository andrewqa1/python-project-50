from gendiff.output import show_difference
from gendiff.processor import find_diffs


def generate_diff(
        first_file_path: str,
        second_file_path: str
) -> None:
    data = find_diffs(first_file_path, second_file_path)
    show_difference(data)
