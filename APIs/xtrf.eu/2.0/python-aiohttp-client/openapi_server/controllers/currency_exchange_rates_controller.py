from typing import List, Dict
from aiohttp import web

from openapi_server.models.currency_history_dto import CurrencyHistoryDTO
from openapi_server import util


async def create_exchange_rate(request: web.Request, iso_code, body) -> web.Response:
    """Adding currency exchange rates.

    Adding currency exchange rates via API

    :param iso_code: iso code, https://www.xe.com/iso4217.php
    :type iso_code: str
    :param body: Adding new currency exchange rates
    :type body: dict | bytes

    """
    body = CurrencyHistoryDTO.from_dict(body)
    return web.Response(status=200)


async def get_by_iso_code(request: web.Request, iso_code) -> web.Response:
    """Returns currency exchange rates.

    Returns currency exchange rates.

    :param iso_code: iso code, https://www.xe.com/iso4217.php
    :type iso_code: str

    """
    return web.Response(status=200)
