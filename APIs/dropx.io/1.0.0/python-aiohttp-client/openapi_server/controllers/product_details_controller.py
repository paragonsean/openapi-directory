from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def products_get(request: web.Request, pids) -> web.Response:
    """Get product details by providing the product IDs

    Returns product details

    :param pids: search array of ids
    :type pids: str

    """
    return web.Response(status=200)
