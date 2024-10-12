from typing import List, Dict
from aiohttp import web

from openapi_server.models.response_item import ResponseItem
from openapi_server import util


async def balance_lookup(request: web.Request, api_key) -> web.Response:
    """Check Balance

    Get Account balance and expiry

    :param api_key: The API key, which you can get from bintable.com website.
    :type api_key: str

    """
    return web.Response(status=200)
