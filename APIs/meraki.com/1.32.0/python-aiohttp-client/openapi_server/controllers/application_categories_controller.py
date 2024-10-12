from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_appliance_firewall_l7_firewall_rules_application_categories_3(request: web.Request, network_id) -> web.Response:
    """Return the L7 firewall application categories and their associated applications for an MX network

    Return the L7 firewall application categories and their associated applications for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_traffic_shaping_application_categories_2(request: web.Request, network_id) -> web.Response:
    """Returns the application categories for traffic shaping rules.

    Returns the application categories for traffic shaping rules.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)
