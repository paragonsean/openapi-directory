from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def tanzania_regions(request: web.Request, country) -> web.Response:
    """Returns all regions present in Tanzania

    Fetches all regions present in Tanzania and then return a response as json

    :param country: Country name in lowercase eg (Tanzania)
    :type country: str

    """
    return web.Response(status=200)
