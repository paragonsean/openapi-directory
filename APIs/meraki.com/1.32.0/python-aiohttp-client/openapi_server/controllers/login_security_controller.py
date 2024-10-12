from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_login_security200_response import GetOrganizationLoginSecurity200Response
from openapi_server.models.update_organization_login_security_request import UpdateOrganizationLoginSecurityRequest
from openapi_server import util


async def get_organization_login_security_1(request: web.Request, organization_id) -> web.Response:
    """Returns the login security settings for an organization.

    Returns the login security settings for an organization.

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_login_security_1(request: web.Request, organization_id, body=None) -> web.Response:
    """Update the login security settings for an organization

    Update the login security settings for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationLoginSecurityRequest.from_dict(body)
    return web.Response(status=200)
