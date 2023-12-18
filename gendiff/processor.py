from typing import List


def find_diffs(
        first_data: dict,
        second_data: dict
) -> List[dict]:
    difference = []

    union_of_keys = set.union(set(first_data.keys()), set(second_data.keys()))

    for key in sorted(union_of_keys):

        if key not in second_data:
            difference.append({
                'key': key,
                'value': first_data[key],
                'type': 'removed'
            })

        elif key not in first_data:
            difference.append({
                'key': key,
                'value': second_data[key],
                'type': 'added'
            })

        elif isinstance(first_data[key], dict) and isinstance(
                second_data[key], dict
        ):
            difference.append({
                'key': key,
                'type': 'nested',
                'children': find_diffs(first_data[key], second_data[key])
            })

        elif first_data[key] != second_data[key]:
            difference.append({
                'key': key,
                'value1': first_data[key],
                'value2': second_data[key],
                'type': 'changed'
            })

        else:
            difference.append({
                'key': key,
                'value': first_data[key],
                'type': 'unchanged'
            })

    return difference
