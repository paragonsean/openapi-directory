from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_content_filtering_categories(request: web.Request, network_id) -> web.Response:
    """List all available content filtering categories for an MX network

    List all available content filtering categories for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)
