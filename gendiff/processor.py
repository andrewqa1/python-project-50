import json
from typing import List, Tuple


def find_diffs(
        first_file_path: str,
        second_file_path: str
) -> List[Tuple[str, str, str]]:
    difference = []

    first_dict = json.load(open(first_file_path))
    second_dict = json.load(open(second_file_path))

    union_of_keys = set.union(set(first_dict.keys()), set(second_dict.keys()))

    for key in sorted(union_of_keys):

        if key not in second_dict:
            difference.append((key, first_dict[key], 'removed'))

        elif key not in first_dict:
            difference.append((key, second_dict[key], 'added'))

        elif first_dict[key] != second_dict[key]:
            difference.append((key, first_dict[key], 'removed'))
            difference.append((key, second_dict[key], 'added'))

        else:
            difference.append((key, first_dict[key], 'unchanged'))

    return difference
