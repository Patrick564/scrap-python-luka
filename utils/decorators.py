from ast import arg
import json, subprocess, tempfile

from datetime import datetime as dt

from typing import Callable


TIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'
TMP_DIR: str = tempfile.gettempdir()


def refresh_if_past_time(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        last_response_time: dt
        time_range: int

        with open(f'{TMP_DIR}/{args[0]}.jsonl', 'r') as f:
            last_line = json.loads(f.readlines()[-1])['response_time']
            last_response_time = dt.strptime(last_line, TIME_FORMAT)
            time_range = (dt.now() - last_response_time).seconds

        if time_range > 180:
            subprocess.run(['python3', f'./currency/spiders/{args[0]}.py'])

        return func(*args, **kwargs)

    return wrapper
