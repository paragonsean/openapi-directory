from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_phone_countries_get(request: web.Request, x_api_key=None) -> web.Response:
    """Get available countries

    

    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_phone_generate_get(request: web.Request, country_code, quantity, x_api_key=None) -> web.Response:
    """Get bulk telephone numbers for a country

    

    :param country_code: 
    :type country_code: str
    :param quantity: 
    :type quantity: int
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_phone_imeiget(request: web.Request, quantity, x_api_key=None) -> web.Response:
    """Get bulk imeis

    

    :param quantity: 
    :type quantity: int
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_phone_validate_get(request: web.Request, telephone, country_code=None, x_api_key=None) -> web.Response:
    """Validate a phone number

    

    :param telephone: 
    :type telephone: str
    :param country_code: 
    :type country_code: str
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)
