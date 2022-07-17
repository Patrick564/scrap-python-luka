import json, tempfile, subprocess

from typing import List


TMP_DIR: str = tempfile.gettempdir()


def get_currency_data(file_name: str = '') -> List[str]:
    values: List[str] = []

    subprocess.run(['python3', f'./currency/spiders/{file_name}.py'])

    with open(f'{TMP_DIR}/{file_name}.jsonl', 'r') as f:
        for field in f:
            field_to_json = json.loads(field)

            values.append(field_to_json)

    return values
