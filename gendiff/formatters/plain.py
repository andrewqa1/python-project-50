from typing import List, Union


def _prepare_str(data: Union[str, dict, list, bool, None]) -> str:

    if data is None:
        return 'null'

    if isinstance(data, dict) or isinstance(data, list):
        return '[complex value]'

    if isinstance(data, bool):
        return str(data).lower()

    return f'\'{data}\''


def _render(difference: List[dict], root='') -> str:
    result = ''
    root += '.' if root else ''

    for dict_ in difference:
        if dict_['type'] == 'nested':
            result += f'{_render(dict_["children"], root + dict_["key"])}'
        elif dict_['type'] == 'added':
            result += f'Property \'{root}{dict_["key"]}\' ' \
                      f'was added with value: {_prepare_str(dict_["value"])}\n'
        elif dict_['type'] == 'removed':
            result += f'Property \'{root}{dict_["key"]}\' was removed\n'
        elif dict_['type'] == 'changed':
            result += f'Property \'{root}{dict_["key"]}\' ' \
                      f'was updated. From {_prepare_str(dict_["value1"])} ' \
                      f'to {_prepare_str(dict_["value2"])}\n'

    return result


def get_plain_diff(difference: List[dict]) -> str:
    return _render(difference).strip()
