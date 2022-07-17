import logging, subprocess, json

import azure.functions as func

from ..utils.data_from_jsonl import get_currency_data


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    subprocess.run(['python3', './currency/spiders/cambi.py'])

    a = get_currency_data('cambi')

    return func.HttpResponse(json.dumps({'b': a}), status_code=200)
