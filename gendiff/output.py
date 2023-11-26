from typing import List, Tuple


def to_nice_difference(data: List[Tuple[str, str, str]]) -> str:

    result = ''

    operations_map = {
        'removed': '-',
        'added': '+',
        'unchanged': ''
    }

    for info in data:
        result += f'{operations_map[info[2]]} {info[0]}: {info[1]}\n'

    return result.strip()
