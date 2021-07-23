import logging

import settings
import aiohttp

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
    
    logger.debug(f'url for add is {url}')
    async with aiohttp.ClientSession() as session:
        await session.post(url, json=data)

async def deleteFromElastic(index, id):
    logger = get_logger(__name__)

    url = f'{settings.ELASTIC_HOST}/{index}/_doc/{id}'
    async with aiohttp.ClientSession() as session:
        await session.delete(url)
    logger.debug(f'url for add is {url}')

async def getFromElastic(index, id):
    url = f'{settings.ELASTIC_HOST}/{index}/_doc/{id}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()