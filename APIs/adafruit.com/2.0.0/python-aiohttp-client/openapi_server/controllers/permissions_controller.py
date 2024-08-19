from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_permission_request import CreatePermissionRequest
from openapi_server.models.permission import Permission
from openapi_server import util


async def all_permissions(request: web.Request, username, type, type_id) -> web.Response:
    """All permissions for current user and type

    The Permissions endpoint returns information about the user&#39;s permissions. 

    :param username: a valid username string
    :type username: str
    :param type: 
    :type type: str
    :param type_id: 
    :type type_id: str

    """
    return web.Response(status=200)


async def create_permission(request: web.Request, username, type, type_id, permission) -> web.Response:
    """Create a new Permission

    

    :param username: a valid username string
    :type username: str
    :param type: 
    :type type: str
    :param type_id: 
    :type type_id: str
    :param permission: 
    :type permission: dict | bytes

    """
    permission = CreatePermissionRequest.from_dict(permission)
    return web.Response(status=200)


async def destroy_permission(request: web.Request, username, type, type_id, id) -> web.Response:
    """Delete an existing Permission

    

    :param username: a valid username string
    :type username: str
    :param type: 
    :type type: str
    :param type_id: 
    :type type_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_permission(request: web.Request, username, type, type_id, id) -> web.Response:
    """Returns Permission based on ID

    

    :param username: a valid username string
    :type username: str
    :param type: 
    :type type: str
    :param type_id: 
    :type type_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def replace_permission(request: web.Request, username, type, type_id, id, permission) -> web.Response:
    """Replace an existing Permission

    

    :param username: a valid username string
    :type username: str
    :param type: 
    :type type: str
    :param type_id: 
    :type type_id: str
    :param id: 
    :type id: str
    :param permission: 
    :type permission: dict | bytes

    """
    permission = CreatePermissionRequest.from_dict(permission)
    return web.Response(status=200)


async def update_permission(request: web.Request, username, type, type_id, id, permission) -> web.Response:
    """Update properties of an existing Permission

    

    :param username: a valid username string
    :type username: str
    :param type: 
    :type type: str
    :param type_id: 
    :type type_id: str
    :param id: 
    :type id: str
    :param permission: 
    :type permission: dict | bytes

    """
    permission = CreatePermissionRequest.from_dict(permission)
    return web.Response(status=200)
