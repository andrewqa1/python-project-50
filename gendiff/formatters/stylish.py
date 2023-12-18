from typing import List, Union


def _indent(depth: int) -> str:
    return ' ' * (depth * 4 - 2)


def _stringify(data: Union[str, dict, bool, None], depth=0) -> str:

    if data is None:
        return 'null'

    if isinstance(data, bool):
        return str(data).lower()

    if isinstance(data, dict):
        result = []
        for key in data.keys():
            result.append(f'{_indent(depth + 1)}  '
                          f'{key}: {_stringify(data[key], depth + 1)}')
        results = '\n'.join(result)
        return f'{{\n{results}\n{_indent(depth)}  }}'

    return data


def _render(difference: List[dict], depth=0) -> str:
    result = ''

    for dict_ in difference:
        if dict_['type'] == 'nested':
            result += f'{_indent(depth)}  {dict_["key"]}: ' \
                      f'{{\n{_render(dict_["children"], depth + 1)}' \
                      f'{_indent(depth)}  }}\n'
        elif dict_['type'] == 'added':
            result += f'{_indent(depth)}+ {dict_["key"]}: ' \
                      f'{_stringify(dict_["value"], depth)}\n'
        elif dict_['type'] == 'removed':
            result += f'{_indent(depth)}- {dict_["key"]}: ' \
                      f'{_stringify(dict_["value"], depth)}\n'
        elif dict_['type'] == 'changed':
            result += f'{_indent(depth)}- {dict_["key"]}: ' \
                      f'{_stringify(dict_["value1"], depth)}\n'
            result += f'{_indent(depth)}+ {dict_["key"]}: ' \
                      f'{_stringify(dict_["value2"], depth)}\n'
        else:
            result += f'{_indent(depth)}  {dict_["key"]}: ' \
                      f'{_stringify(dict_["value"])}\n'
    return result


def get_stylish_diff(difference: List[dict]) -> str:
    return f'{{\n{_render(difference, 1)}}}'
