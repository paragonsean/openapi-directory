from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_early_access_features_opt_in_request import CreateOrganizationEarlyAccessFeaturesOptInRequest
from openapi_server.models.update_organization_early_access_features_opt_in_request import UpdateOrganizationEarlyAccessFeaturesOptInRequest
from openapi_server import util


async def create_organization_early_access_features_opt_in_2(request: web.Request, organization_id, body) -> web.Response:
    """Create a new early access feature opt-in for an organization

    Create a new early access feature opt-in for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationEarlyAccessFeaturesOptInRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_early_access_features_opt_in_2(request: web.Request, organization_id, opt_in_id) -> web.Response:
    """Delete an early access feature opt-in

    Delete an early access feature opt-in

    :param organization_id: 
    :type organization_id: str
    :param opt_in_id: 
    :type opt_in_id: str

    """
    return web.Response(status=200)


async def get_organization_early_access_features_2(request: web.Request, organization_id) -> web.Response:
    """List the available early access features for organization

    List the available early access features for organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_early_access_features_opt_in_2(request: web.Request, organization_id, opt_in_id) -> web.Response:
    """Show an early access feature opt-in for an organization

    Show an early access feature opt-in for an organization

    :param organization_id: 
    :type organization_id: str
    :param opt_in_id: 
    :type opt_in_id: str

    """
    return web.Response(status=200)


async def get_organization_early_access_features_opt_ins_2(request: web.Request, organization_id) -> web.Response:
    """List the early access feature opt-ins for an organization

    List the early access feature opt-ins for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_early_access_features_opt_in_2(request: web.Request, organization_id, opt_in_id, body=None) -> web.Response:
    """Update an early access feature opt-in for an organization

    Update an early access feature opt-in for an organization

    :param organization_id: 
    :type organization_id: str
    :param opt_in_id: 
    :type opt_in_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationEarlyAccessFeaturesOptInRequest.from_dict(body)
    return web.Response(status=200)
