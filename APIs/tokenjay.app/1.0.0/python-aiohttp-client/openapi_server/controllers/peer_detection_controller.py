from typing import List, Dict
from aiohttp import web

from openapi_server.models.node_peer import NodePeer
from openapi_server import util


async def get_peers_list(request: web.Request, unreachable=None, closed_api=None, limit=None) -> web.Response:
    """Lists known peers sorted by block height

    

    :param unreachable: Set to true to show unreachable peers in the list
    :type unreachable: bool
    :param closed_api: Set to true to show peers not open to be connected
    :type closed_api: bool
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)
