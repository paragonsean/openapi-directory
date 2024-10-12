from typing import List, Dict
from aiohttp import web

from openapi_server.models.mappings_representation import MappingsRepresentation
from openapi_server.models.role_representation import RoleRepresentation
from openapi_server import util


async def realm_groups_id_role_mappings_get(request: web.Request, realm, id) -> web.Response:
    """Get role mappings

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_groups_id_role_mappings_realm_available_get(request: web.Request, realm, id) -> web.Response:
    """Get realm-level roles that can be mapped

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_groups_id_role_mappings_realm_composite_get(request: web.Request, realm, id) -> web.Response:
    """Get effective realm-level role mappings   This will recurse all composite roles to get the result.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_groups_id_role_mappings_realm_delete(request: web.Request, realm, id, body) -> web.Response:
    """Delete realm-level role mappings

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_groups_id_role_mappings_realm_get(request: web.Request, realm, id) -> web.Response:
    """Get realm-level role mappings

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_groups_id_role_mappings_realm_post(request: web.Request, realm, id, body) -> web.Response:
    """Add realm-level role mappings to the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param body: Roles to add
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_users_id_role_mappings_get(request: web.Request, realm, id) -> web.Response:
    """Get role mappings

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_id_role_mappings_realm_available_get(request: web.Request, realm, id) -> web.Response:
    """Get realm-level roles that can be mapped

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_id_role_mappings_realm_composite_get(request: web.Request, realm, id) -> web.Response:
    """Get effective realm-level role mappings   This will recurse all composite roles to get the result.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_id_role_mappings_realm_delete(request: web.Request, realm, id, body) -> web.Response:
    """Delete realm-level role mappings

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_users_id_role_mappings_realm_get(request: web.Request, realm, id) -> web.Response:
    """Get realm-level role mappings

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_id_role_mappings_realm_post(request: web.Request, realm, id, body) -> web.Response:
    """Add realm-level role mappings to the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param body: Roles to add
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)
