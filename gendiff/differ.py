from gendiff.output import to_nice_difference
from gendiff.processor import find_diffs


def generate_diff(
        first_file_path: str,
        second_file_path: str
) -> str:
    data = find_diffs(first_file_path, second_file_path)
    return to_nice_difference(data)
