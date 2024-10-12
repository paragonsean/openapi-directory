from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_l7_firewall_rules_application_categories(request: web.Request, network_id) -> web.Response:
    """Return the L7 firewall application categories and their associated applications for an MX network

    Return the L7 firewall application categories and their associated applications for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)
