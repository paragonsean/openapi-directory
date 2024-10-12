from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_saml_role_request import CreateOrganizationSamlRoleRequest
from openapi_server.models.update_organization_saml_role_request import UpdateOrganizationSamlRoleRequest
from openapi_server import util


async def create_organization_saml_role(request: web.Request, organization_id, body) -> web.Response:
    """Create a SAML role

    Create a SAML role

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationSamlRoleRequest.from_dict(body)
    return web.Response(status=200)


async def get_organization_saml_role(request: web.Request, organization_id, saml_role_id) -> web.Response:
    """Return a SAML role

    Return a SAML role

    :param organization_id: 
    :type organization_id: str
    :param saml_role_id: 
    :type saml_role_id: str

    """
    return web.Response(status=200)


async def get_organization_saml_roles(request: web.Request, organization_id) -> web.Response:
    """List the SAML roles for this organization

    List the SAML roles for this organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_saml_role(request: web.Request, organization_id, saml_role_id, body=None) -> web.Response:
    """Update a SAML role

    Update a SAML role

    :param organization_id: 
    :type organization_id: str
    :param saml_role_id: 
    :type saml_role_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationSamlRoleRequest.from_dict(body)
    return web.Response(status=200)
