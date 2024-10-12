from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def pricing(request: web.Request, country=None, format=None) -> web.Response:
    """pricing

    

    :param country: The countries ISO code to get pricings for. Allowed values are de, fr, at. Omit to show pricings for all channels.
    :type country: str
    :param format: Determines the response format. Allowed values are json and csv. The default value is json.
    :type format: str

    """
    return web.Response(status=200)
