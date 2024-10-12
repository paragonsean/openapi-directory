from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_firewalled_service(request: web.Request, network_id, service) -> web.Response:
    """Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

    Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

    :param network_id: 
    :type network_id: str
    :param service: 
    :type service: str

    """
    return web.Response(status=200)


async def get_network_firewalled_services(request: web.Request, network_id) -> web.Response:
    """List the appliance services and their accessibility rules

    List the appliance services and their accessibility rules

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)
