import json, tempfile

from typing import List

from ..utils.decorators import refresh_if_past_time


TMP_DIR: str = tempfile.gettempdir()


@refresh_if_past_time
def get_currency_data(file_name: str = '') -> List[str]:
    values: List[str] = []

    with open(f'{TMP_DIR}/{file_name}.jsonl', 'r') as f:
        for field in f:
            field_to_json = json.loads(field)

            values.append(field_to_json)

    return values
