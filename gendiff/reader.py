import json
import yaml


def get_data(file_path: str) -> dict:
    extension = file_path.split('.')[-1].lower()

    extension_map = {
        'json': json.load,
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load
    }

    if extension not in extension_map.keys():
        raise ValueError('Wrong extension!')

    return extension_map[extension](open(file_path, 'r'))
