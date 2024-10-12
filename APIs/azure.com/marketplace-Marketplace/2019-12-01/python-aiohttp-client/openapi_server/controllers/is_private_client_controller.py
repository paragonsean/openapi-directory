from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def private_store_client_get(request: web.Request, api_version, subscription_id) -> web.Response:
    """private_store_client_get

    Check if client is private or not.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)
