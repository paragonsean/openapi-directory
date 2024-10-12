from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_saml_idp_request import CreateOrganizationSamlIdpRequest
from openapi_server.models.get_organization_saml200_response import GetOrganizationSaml200Response
from openapi_server.models.get_organization_saml_idps200_response_inner import GetOrganizationSamlIdps200ResponseInner
from openapi_server.models.update_organization_saml_idp_request import UpdateOrganizationSamlIdpRequest
from openapi_server.models.update_organization_saml_request import UpdateOrganizationSamlRequest
from openapi_server import util


async def create_organization_saml_idp_1(request: web.Request, organization_id, body) -> web.Response:
    """Create a SAML IdP for your organization.

    Create a SAML IdP for your organization.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationSamlIdpRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_saml_idp_1(request: web.Request, organization_id, idp_id) -> web.Response:
    """Remove a SAML IdP in your organization.

    Remove a SAML IdP in your organization.

    :param organization_id: 
    :type organization_id: str
    :param idp_id: 
    :type idp_id: str

    """
    return web.Response(status=200)


async def get_organization_saml_1(request: web.Request, organization_id) -> web.Response:
    """Returns the SAML SSO enabled settings for an organization.

    Returns the SAML SSO enabled settings for an organization.

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_saml_idp_1(request: web.Request, organization_id, idp_id) -> web.Response:
    """Get a SAML IdP from your organization.

    Get a SAML IdP from your organization.

    :param organization_id: 
    :type organization_id: str
    :param idp_id: 
    :type idp_id: str

    """
    return web.Response(status=200)


async def get_organization_saml_idps_1(request: web.Request, organization_id) -> web.Response:
    """List the SAML IdPs in your organization.

    List the SAML IdPs in your organization.

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_saml_1(request: web.Request, organization_id, body=None) -> web.Response:
    """Updates the SAML SSO enabled settings for an organization.

    Updates the SAML SSO enabled settings for an organization.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationSamlRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_saml_idp_1(request: web.Request, organization_id, idp_id, body=None) -> web.Response:
    """Update a SAML IdP in your organization

    Update a SAML IdP in your organization

    :param organization_id: 
    :type organization_id: str
    :param idp_id: 
    :type idp_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationSamlIdpRequest.from_dict(body)
    return web.Response(status=200)
