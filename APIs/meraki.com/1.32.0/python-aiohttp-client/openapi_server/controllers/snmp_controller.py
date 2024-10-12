from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_snmp_request import UpdateNetworkSnmpRequest
from openapi_server.models.update_organization_snmp_request import UpdateOrganizationSnmpRequest
from openapi_server import util


async def get_network_snmp_1(request: web.Request, network_id) -> web.Response:
    """Return the SNMP settings for a network

    Return the SNMP settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_snmp_1(request: web.Request, organization_id) -> web.Response:
    """Return the SNMP settings for an organization

    Return the SNMP settings for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_network_snmp_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the SNMP settings for a network

    Update the SNMP settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSnmpRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_snmp_1(request: web.Request, organization_id, body=None) -> web.Response:
    """Update the SNMP settings for an organization

    Update the SNMP settings for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationSnmpRequest.from_dict(body)
    return web.Response(status=200)
