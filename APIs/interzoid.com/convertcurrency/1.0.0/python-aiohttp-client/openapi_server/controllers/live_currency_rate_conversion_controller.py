from typing import List, Dict
from aiohttp import web

from openapi_server.models.convertcurrency200_response import Convertcurrency200Response
from openapi_server import util


async def convertcurrency(request: web.Request, license, _from, to, amount) -> web.Response:
    """Converts amount in one currency to that of another

    Provide an amount in one currency (EUR, GBP, CNY, JPY, AUD, etc.), and also a second currency to convert it to. The API will return the result using current foreign exchange rates. See the API home page for a list of all supported currencies.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param _from: Currency symbol for the converted from amount
    :type _from: str
    :param to: Currency symbol for the converted to amount
    :type to: str
    :param amount: The amount of currency to be converted
    :type amount: str

    """
    return web.Response(status=200)
