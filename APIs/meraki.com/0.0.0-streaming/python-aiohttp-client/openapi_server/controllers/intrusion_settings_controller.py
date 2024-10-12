from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_security_intrusion_settings_request import UpdateNetworkSecurityIntrusionSettingsRequest
from openapi_server.models.update_organization_security_intrusion_settings_request import UpdateOrganizationSecurityIntrusionSettingsRequest
from openapi_server import util


async def get_network_security_intrusion_settings(request: web.Request, network_id) -> web.Response:
    """Returns all supported intrusion settings for an MX network

    Returns all supported intrusion settings for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_security_intrusion_settings(request: web.Request, organization_id) -> web.Response:
    """Returns all supported intrusion settings for an organization

    Returns all supported intrusion settings for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_network_security_intrusion_settings(request: web.Request, network_id, body=None) -> web.Response:
    """Set the supported intrusion settings for an MX network

    Set the supported intrusion settings for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSecurityIntrusionSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_security_intrusion_settings(request: web.Request, organization_id, body) -> web.Response:
    """Sets supported intrusion settings for an organization

    Sets supported intrusion settings for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationSecurityIntrusionSettingsRequest.from_dict(body)
    return web.Response(status=200)
