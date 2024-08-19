from typing import List, Dict
from aiohttp import web

from openapi_server.models.token_price import TokenPrice
from openapi_server import util


async def get_token_price(request: web.Request, token_id) -> web.Response:
    """Lists price and available volume for a certain token

    

    :param token_id: 
    :type token_id: str

    """
    return web.Response(status=200)


async def get_token_prices(request: web.Request, ) -> web.Response:
    """Lists all token prices and available volume

    


    """
    return web.Response(status=200)
