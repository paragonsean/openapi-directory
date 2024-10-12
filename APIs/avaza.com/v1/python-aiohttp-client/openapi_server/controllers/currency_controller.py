from typing import List, Dict
from aiohttp import web

from openapi_server.models.currency_list import CurrencyList
from openapi_server import util


async def currency_get(request: web.Request, ) -> web.Response:
    """Gets list of Currencies

    


    """
    return web.Response(status=200)
