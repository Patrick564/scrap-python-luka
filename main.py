from fastapi import FastAPI

from typing import List, Dict, Callable

import json, subprocess
from datetime import datetime as dt

# from scrapy.crawler import CrawlerProcess

app = FastAPI()

# crawl = CrawlerProcess()

TIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'


def refresh_last_currency(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        last_response_time: dt
        time_range: int

        with open(f'{args[0]}.jsonl', 'r') as f:
            last_line = json.loads(f.readlines()[-1])['response_time']
            last_response_time = dt.strptime(last_line, TIME_FORMAT)
            time_range = (dt.now() - last_response_time).seconds

        if time_range > 180:
            subprocess.run([
                'poetry',
                'run',
                'scrapy',
            ])
            # crawl.crawl(f'{args[0]}')
            # crawl.start()

        func(*args, **kwargs)

        # print('refresh_last_currency after')

    return wrapper


@refresh_last_currency
def get_currency_data(file_name: str = '') -> List[str]:
    values: List[str] = []

    file = open(f'{file_name}.jsonl', 'r')

    for field in file:
        field_to_json = json.loads(field)

        values.append(field_to_json)

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
