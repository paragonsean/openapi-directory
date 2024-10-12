from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.create_role_request import CreateRoleRequest
from openapi_server.models.create_role_response import CreateRoleResponse
from openapi_server.models.get_custom_permission_response import GetCustomPermissionResponse
from openapi_server.models.list_permissions_response import ListPermissionsResponse
from openapi_server.models.list_roles_response import ListRolesResponse
from openapi_server.models.response import Response
from openapi_server import util


async def create_role(request: web.Request, body) -> web.Response:
    """Create role

    Creates custom role 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateRoleRequest.from_dict(body)
    return web.Response(status=200)


async def delete_role(request: web.Request, name) -> web.Response:
    """Delete role

    Deletes custom role 

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def get_permission(request: web.Request, id) -> web.Response:
    """Get permission

    Gets custom permission 

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def list_permissions(request: web.Request, ) -> web.Response:
    """List permissions

    Lists all available permissions 


    """
    return web.Response(status=200)


async def list_roles(request: web.Request, ) -> web.Response:
    """List roles

    Lists all available roles 


    """
    return web.Response(status=200)
