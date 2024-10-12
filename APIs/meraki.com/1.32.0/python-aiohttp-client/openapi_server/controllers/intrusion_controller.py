from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_appliance_security_intrusion_request import UpdateNetworkApplianceSecurityIntrusionRequest
from openapi_server.models.update_organization_appliance_security_intrusion_request import UpdateOrganizationApplianceSecurityIntrusionRequest
from openapi_server import util


async def get_network_appliance_security_intrusion_2(request: web.Request, network_id) -> web.Response:
    """Returns all supported intrusion settings for an MX network

    Returns all supported intrusion settings for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_appliance_security_intrusion_2(request: web.Request, organization_id) -> web.Response:
    """Returns all supported intrusion settings for an organization

    Returns all supported intrusion settings for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_security_intrusion_2(request: web.Request, network_id, body=None) -> web.Response:
    """Set the supported intrusion settings for an MX network

    Set the supported intrusion settings for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceSecurityIntrusionRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_appliance_security_intrusion_2(request: web.Request, organization_id, body) -> web.Response:
    """Sets supported intrusion settings for an organization

    Sets supported intrusion settings for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationApplianceSecurityIntrusionRequest.from_dict(body)
    return web.Response(status=200)
