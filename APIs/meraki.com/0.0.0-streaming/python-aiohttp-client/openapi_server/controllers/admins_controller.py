from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_admin_request import CreateOrganizationAdminRequest
from openapi_server.models.update_organization_admin_request import UpdateOrganizationAdminRequest
from openapi_server import util


async def create_organization_admin(request: web.Request, organization_id, body) -> web.Response:
    """Create a new dashboard administrator

    Create a new dashboard administrator

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAdminRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_admin(request: web.Request, organization_id, admin_id) -> web.Response:
    """Revoke all access for a dashboard administrator within this organization

    Revoke all access for a dashboard administrator within this organization

    :param organization_id: 
    :type organization_id: str
    :param admin_id: 
    :type admin_id: str

    """
    return web.Response(status=200)


async def get_organization_admins(request: web.Request, organization_id) -> web.Response:
    """List the dashboard administrators in this organization

    List the dashboard administrators in this organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_admin(request: web.Request, organization_id, admin_id, body=None) -> web.Response:
    """Update an administrator

    Update an administrator

    :param organization_id: 
    :type organization_id: str
    :param admin_id: 
    :type admin_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAdminRequest.from_dict(body)
    return web.Response(status=200)
