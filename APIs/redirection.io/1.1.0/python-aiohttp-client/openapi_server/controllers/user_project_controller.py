from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_project_creation_write import UserProjectCreationWrite
from openapi_server.models.user_project_read import UserProjectRead
from openapi_server.models.user_project_write import UserProjectWrite
from openapi_server import util


async def delete_user_project_item(request: web.Request, id) -> web.Response:
    """Removes the UserProject resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_user_project_item(request: web.Request, id) -> web.Response:
    """Retrieves a UserProject resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_user_project_collection(request: web.Request, user_project=None) -> web.Response:
    """Creates a UserProject resource.

    

    :param user_project: The new UserProject resource
    :type user_project: dict | bytes

    """
    user_project = UserProjectCreationWrite.from_dict(user_project)
    return web.Response(status=200)


async def put_user_project_item(request: web.Request, id, user_project=None) -> web.Response:
    """Replaces the UserProject resource.

    

    :param id: 
    :type id: str
    :param user_project: The updated UserProject resource
    :type user_project: dict | bytes

    """
    user_project = UserProjectWrite.from_dict(user_project)
    return web.Response(status=200)
