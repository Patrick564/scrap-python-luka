import json
from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()


def get_currency_data(file_name: str = '') -> List[str]:
    values: List[str] = []

    file = open(f'{file_name}.jsonl', 'r')

    for field in file:
        values.append(json.loads(field))

    file.close()

    return values


@app.get('/')
async def root():
    exange_sites_list: List[str] = ['inka_money', 'rextie', 'dollar_house', 'cambi']

    current_values: Dict[str, List[str]] = {
        exange_site: get_currency_data(exange_site) for exange_site in exange_sites_list
    }

    return {
        'data': current_values
    }
