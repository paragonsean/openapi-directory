from typing import List, Dict
from aiohttp import web

from openapi_server.models.response_item import ResponseItem
from openapi_server import util


async def bin_lookup(request: web.Request, bin, api_key) -> web.Response:
    """Lookup for bin

    By passing in the appropriate BIN, you can lookup for card meta data in bintable.com API 

    :param bin: pass the required BIN code
    :type bin: str
    :param api_key: The API key, which you can get from bintable.com website.
    :type api_key: str

    """
    return web.Response(status=200)
