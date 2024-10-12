from typing import List, Dict
from aiohttp import web

from openapi_server.models.getcurrencyrate200_response import Getcurrencyrate200Response
from openapi_server import util


async def getcurrencyrate(request: web.Request, license, symbol) -> web.Response:
    """Gets a foreign currency rate for one US Dollar

    Use a currency symbol (EUR, GBP, CNY, JPY, AUD, etc.) to obtain a live currency foreign exchange rate for one US Dollar. See the API home page for list of all supported currencies.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param symbol: Currency symbol to retrieve current rate for
    :type symbol: str

    """
    return web.Response(status=200)
