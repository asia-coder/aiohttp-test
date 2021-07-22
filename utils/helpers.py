import logging

import settings
import requests
from envparse import env

QuestionIndex = "question"
ChoiceIndex = "choice"


def get_logger(name: str='__main__', handler=None, formatter=None):
    if not handler:
        handler = settings.LOG_HANDLER

    if not formatter:
        formatter = settings.LOF_FORMATTER

    if not handler.formatter:
        handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(settings.LOG_LEVEL)

    return logger

async def addToElastic(index, id, data):
    logger = get_logger(__name__)
    url = f'{settings.ELASTIC_HOST}/{index}/_doc/{id}'
    # url = url.format(settings.ELASTIC_HOST, index, id)
    logger.debug(f'url for add is {url}')

    requests.post(url, json=data)

async def deleteFromElastic(index, id):
    logger = get_logger(__name__)
    url = f'{settings.ELASTIC_HOST}/{index}/_doc/{id}'
    requests.delete(url)
    logger.debug(f'url for add is {url}')