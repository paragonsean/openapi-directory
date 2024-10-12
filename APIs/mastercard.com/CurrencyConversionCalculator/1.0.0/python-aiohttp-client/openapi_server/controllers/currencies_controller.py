from typing import List, Dict
from aiohttp import web

from openapi_server.models.settlement_currency_request import SettlementCurrencyRequest
from openapi_server import util


async def get_currency_rate_data_using_get(request: web.Request, ) -> web.Response:
    """getCurrencyRateData

    List of supported currencies.


    """
    return web.Response(status=200)
