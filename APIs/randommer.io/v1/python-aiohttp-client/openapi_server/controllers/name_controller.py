from typing import List, Dict
from aiohttp import web

from openapi_server.models.name_type import NameType
from openapi_server import util


async def api_name_brand_name_post(request: web.Request, starting_words, x_api_key=None) -> web.Response:
    """Generate brand name suggestions

    

    :param starting_words: 
    :type starting_words: str
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_name_business_name_post(request: web.Request, number, culture_code=None, x_api_key=None) -> web.Response:
    """Get business names for a specific culture

    

    :param number: 
    :type number: int
    :param culture_code: 
    :type culture_code: str
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_name_cultures_get(request: web.Request, x_api_key=None) -> web.Response:
    """Get available cultures

    

    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_name_get(request: web.Request, name_type, quantity, x_api_key=None) -> web.Response:
    """Get name

    

    :param name_type: 
    :type name_type: dict | bytes
    :param quantity: 
    :type quantity: int
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    name_type = .from_dict(name_type)
    return web.Response(status=200)


async def api_name_suggestions_get(request: web.Request, starting_words, x_api_key=None) -> web.Response:
    """Get business name suggestions

    

    :param starting_words: 
    :type starting_words: str
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)
