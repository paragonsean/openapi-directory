from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_snmp_settings(request: web.Request, network_id) -> web.Response:
    """Return the SNMP settings for a network

    Return the SNMP settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_snmp(request: web.Request, organization_id) -> web.Response:
    """Return the SNMP settings for an organization

    Return the SNMP settings for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)
