from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def apod_get(request: web.Request, _date=None, hd=None) -> web.Response:
    """Returns images

    Returns the picture of the day

    :param _date: The date of the APOD image to retrieve
    :type _date: str
    :param hd: Retrieve the URL for the high resolution image
    :type hd: bool

    """
    return web.Response(status=200)
