from typing import List, Dict
from aiohttp import web

from openapi_server.models.organization import Organization
from openapi_server import util


async def workspace_slug_organizations_get(request: web.Request, workspace_slug, query=None, page=None, direction=None, items=None, sort=None) -> web.Response:
    """List organizations in a workspace

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param query: 
    :type query: str
    :param page: 
    :type page: str
    :param direction: 
    :type direction: str
    :param items: 
    :type items: str
    :param sort: 
    :type sort: str

    """
    return web.Response(status=200)


async def workspace_slug_organizations_organization_id_get(request: web.Request, workspace_slug, organization_id) -> web.Response:
    """Get an organization

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def workspace_slug_organizations_organization_id_put(request: web.Request, workspace_slug, organization_id, body=None) -> web.Response:
    """Update an organization

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Organization.from_dict(body)
    return web.Response(status=200)
