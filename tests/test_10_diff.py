from typing import Callable
import pytest
from gendiff.differ import generate_diff


@pytest.mark.parametrize('extension', ['json', 'yaml'])
def test_generate_diff(extension: str):

    stylish_result = open('./tests/fixtures/result_stylish', 'r').read().strip()
    plain_result = open('./tests/fixtures/result_plain', 'r').read().strip()
    json_result = open('./tests/fixtures/result_json', 'r').read().strip()

    assert isinstance(generate_diff, Callable), 'generate_diff must be a function'
    assert generate_diff(
        f'./tests/fixtures/file1.{extension}',
        f'./tests/fixtures/file2.{extension}',
        'stylish'
    ) == stylish_result
    assert generate_diff(
        f'./tests/fixtures/file1.{extension}',
        f'./tests/fixtures/file2.{extension}',
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
