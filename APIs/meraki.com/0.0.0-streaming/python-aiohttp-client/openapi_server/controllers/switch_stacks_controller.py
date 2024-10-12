from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_switch_stacks(request: web.Request, network_id) -> web.Response:
    """List the switch stacks in a network

    List the switch stacks in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)
