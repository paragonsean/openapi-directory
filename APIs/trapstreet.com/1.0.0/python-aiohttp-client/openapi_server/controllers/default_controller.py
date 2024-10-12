from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_get200_response import AddressGet200Response
from openapi_server import util


async def address_get(request: web.Request, address) -> web.Response:
    """address_get

    

    :param address: 
    :type address: str

    """
    return web.Response(status=200)
