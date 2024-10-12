from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_topology_link_layer_2(request: web.Request, network_id) -> web.Response:
    """List the LLDP and CDP information for all discovered devices and connections in a network.

    List the LLDP and CDP information for all discovered devices and connections in a network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)
