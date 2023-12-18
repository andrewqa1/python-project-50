from gendiff.formatters import get_formatted_data
from gendiff.processor import find_diffs

from gendiff.reader import get_data


def generate_diff(
        first_file_path: str,
        second_file_path: str,
        style: str
) -> str:

    first_data = get_data(first_file_path)
    second_data = get_data(second_file_path)

    difference = find_diffs(first_data, second_data)

    return get_formatted_data(difference, style)
