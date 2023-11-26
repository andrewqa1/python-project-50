from os import read
from typing import Callable

from gendiff.differ import generate_diff


def read_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()


def test_generate_diff():

    result = read_file('./tests/fixtures/result')

    assert isinstance(generate_diff, Callable), 'generate_diff must be a function'
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result
