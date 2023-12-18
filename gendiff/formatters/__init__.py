from typing import List

from gendiff.formatters.json import get_json_diff
from gendiff.formatters.plain import get_plain_diff
from gendiff.formatters.stylish import get_stylish_diff


def get_formatted_data(difference: List[dict], style: str) -> str:
    if style == 'stylish':
        return get_stylish_diff(difference)

    if style == 'plain':
        return get_plain_diff(difference)

    if style == 'json':
        return get_json_diff(difference)

    raise ValueError('Unknown style! Choices are: "stylish", "plain", "json"')
