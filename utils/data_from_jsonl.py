import json

from typing import List


def get_currency_data(file_name: str = '') -> List[str]:
    values: List[str] = []

    with open(f'{file_name}.jsonl', 'r') as f:
        for field in f:
            field_to_json = json.loads(field)

            values.append(field_to_json)

    return values
