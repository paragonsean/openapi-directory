from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def districts_in_a_region(request: web.Request, country, region) -> web.Response:
    """Returns all districts in region

    Returns a post code and all districts in a specified region

    :param country: Country name in lowercase eg( tanzania)
    :type country: str
    :param region: Name of the region eg (Mbeya)
    :type region: str

    """
    return web.Response(status=200)
