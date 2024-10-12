from typing import List, Dict
from aiohttp import web

from openapi_server.models.supported_currency_response_v2 import SupportedCurrencyResponseV2
from openapi_server import util


async def list_supported_currencies_v2(request: web.Request, ) -> web.Response:
    """List Supported Currencies

    List the supported currencies.


    """
    return web.Response(status=200)
