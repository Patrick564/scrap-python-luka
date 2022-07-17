import logging, json

import azure.functions as func

from typing import List, Dict

from ..utils.data_from_jsonl import get_currency_data


EXCHANGE_SITES_LIST: List[str] = ['inka_money', 'rextie', 'dollar_house', 'cambi']


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    current_values: Dict[str, List[str]] = {
        exange_site: get_currency_data(exange_site) for exange_site in EXCHANGE_SITES_LIST
    }

    return func.HttpResponse(json.dumps({'b': current_values}), status_code=200)
