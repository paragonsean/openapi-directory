from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def city_get(request: web.Request, key, lng, lat, format=None) -> web.Response:
    """city_get

    Get City name by using latitude and longitude

    :param key: 
    :type key: str
    :param lng: 
    :type lng: 
    :param lat: 
    :type lat: 
    :param format: 
    :type format: str

    """
    return web.Response(status=200)
