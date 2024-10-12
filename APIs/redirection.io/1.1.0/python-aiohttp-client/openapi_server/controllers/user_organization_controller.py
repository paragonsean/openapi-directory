from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_organization_creation_write import UserOrganizationCreationWrite
from openapi_server.models.user_organization_read import UserOrganizationRead
from openapi_server.models.user_organization_write import UserOrganizationWrite
from openapi_server import util


async def delete_user_organization_item(request: web.Request, id) -> web.Response:
    """Removes the UserOrganization resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_user_organization_item(request: web.Request, id) -> web.Response:
    """Retrieves a UserOrganization resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_user_organization_collection(request: web.Request, user_organization=None) -> web.Response:
    """Creates a UserOrganization resource.

    

    :param user_organization: The new UserOrganization resource
    :type user_organization: dict | bytes

    """
    user_organization = UserOrganizationCreationWrite.from_dict(user_organization)
    return web.Response(status=200)


async def put_user_organization_item(request: web.Request, id, user_organization=None) -> web.Response:
    """Replaces the UserOrganization resource.

    

    :param id: 
    :type id: str
    :param user_organization: The updated UserOrganization resource
    :type user_organization: dict | bytes

    """
    user_organization = UserOrganizationWrite.from_dict(user_organization)
    return web.Response(status=200)
