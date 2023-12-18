import json
from typing import List


def get_json_diff(difference: List[dict]) -> str:
    return json.dumps(difference, indent=2)
