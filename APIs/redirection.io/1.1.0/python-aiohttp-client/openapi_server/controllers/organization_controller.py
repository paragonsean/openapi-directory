from typing import List, Dict
from aiohttp import web

from openapi_server.models.organization_read import OrganizationRead
from openapi_server.models.organization_write import OrganizationWrite
from openapi_server import util


async def delete_organization_item(request: web.Request, id) -> web.Response:
    """Removes the Organization resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organization_item(request: web.Request, id) -> web.Response:
    """Retrieves a Organization resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_organization_collection(request: web.Request, organization=None) -> web.Response:
    """Creates a Organization resource.

    

    :param organization: The new Organization resource
    :type organization: dict | bytes

    """
    organization = OrganizationWrite.from_dict(organization)
    return web.Response(status=200)


async def put_organization_item(request: web.Request, id, organization=None) -> web.Response:
    """Replaces the Organization resource.

    

    :param id: 
    :type id: str
    :param organization: The updated Organization resource
    :type organization: dict | bytes

    """
    organization = OrganizationWrite.from_dict(organization)
    return web.Response(status=200)
