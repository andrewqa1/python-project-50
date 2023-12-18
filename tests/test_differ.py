from typing import Callable
import pytest
from gendiff.differ import generate_diff


@pytest.mark.parametrize('extension', ['json', 'yaml'])
def test_generate_diff(extension: str):

    stylish_result = open('./tests/fixtures/stylish_result', 'r').read()
    plain_result = open('./tests/fixtures/plain_result', 'r').read()
    json_result = open('./tests/fixtures/json_result', 'r').read()

    assert isinstance(generate_diff, Callable), 'generate_diff must be a function'
    assert generate_diff(
        f'./tests/fixtures/file1.{extension}',
        f'./tests/fixtures/file2.{extension}',
        'stylish'
    ) == stylish_result
    assert generate_diff(
        f'./tests/fixtures/file1.{extension}',
        f'./tests/fixtures/file2.{extension}',
        'plain'
    ) == plain_result
    assert generate_diff(
        f'./tests/fixtures/file1.{extension}',
        f'./tests/fixtures/file2.{extension}',
        'json'
    ) == json_result
