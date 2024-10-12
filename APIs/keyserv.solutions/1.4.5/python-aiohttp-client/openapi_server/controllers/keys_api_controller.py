from typing import List, Dict
from aiohttp import web

from openapi_server.models.keys_api_current200_response import KeysApiCurrent200Response
from openapi_server.models.keys_api_expiry200_response import KeysApiExpiry200Response
from openapi_server.models.keys_api_find200_response import KeysApiFind200Response
from openapi_server import util


async def keys_api_current(request: web.Request, serial) -> web.Response:
    """keys_api_current

    

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def keys_api_custom(request: web.Request, serial) -> web.Response:
    """keys_api_custom

    

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def keys_api_expiry(request: web.Request, serial) -> web.Response:
    """keys_api_expiry

    

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def keys_api_find(request: web.Request, serial) -> web.Response:
    """keys_api_find

    

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)
