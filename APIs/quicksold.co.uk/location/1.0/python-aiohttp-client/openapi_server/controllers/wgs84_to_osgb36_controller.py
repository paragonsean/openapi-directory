from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_response import ApiResponse
from openapi_server import util


async def wgs84_to_osgb36_using_get(request: web.Request, latitude, longitude) -> web.Response:
    """wgs84ToOsgb36

    

    :param latitude: latitude
    :type latitude: str
    :param longitude: longitude
    :type longitude: str

    """
    return web.Response(status=200)
