from typing import List, Dict
from aiohttp import web

from openapi_server.models.management_permission_reference import ManagementPermissionReference
from openapi_server.models.role_representation import RoleRepresentation
from openapi_server import util


async def realm_roles_by_id_role_id_composites_clients_client_get(request: web.Request, realm, role_id, client) -> web.Response:
    """Get client-level roles for the client that are in the role’s composite

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_id: 
    :type role_id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_roles_by_id_role_id_composites_delete(request: web.Request, realm, role_id, body) -> web.Response:
    """Remove a set of roles from the role’s composite

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_id: Role id
    :type role_id: str
    :param body: A set of roles to be removed
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_roles_by_id_role_id_composites_get(request: web.Request, realm, role_id) -> web.Response:
    """Get role’s children   Returns a set of role’s children provided the role is a composite.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_id: Role id
    :type role_id: str

    """
    return web.Response(status=200)


async def realm_roles_by_id_role_id_composites_post(request: web.Request, realm, role_id, body) -> web.Response:
    """Make the role a composite role by associating some child roles

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_id: Role id
    :type role_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_roles_by_id_role_id_composites_realm_get(request: web.Request, realm, role_id) -> web.Response:
    """Get realm-level roles that are in the role’s composite

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_id: 
    :type role_id: str

    """
    return web.Response(status=200)


async def realm_roles_by_id_role_id_delete(request: web.Request, realm, role_id) -> web.Response:
    """Delete the role

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_id: id of role
    :type role_id: str

    """
    return web.Response(status=200)


async def realm_roles_by_id_role_id_get(request: web.Request, realm, role_id) -> web.Response:
    """Get a specific role’s representation

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_id: id of role
    :type role_id: str

    """
    return web.Response(status=200)


async def realm_roles_by_id_role_id_management_permissions_get(request: web.Request, realm, role_id) -> web.Response:
    """Return object stating whether role Authoirzation permissions have been initialized or not and a reference

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_id: 
    :type role_id: str

    """
    return web.Response(status=200)


async def realm_roles_by_id_role_id_management_permissions_put(request: web.Request, realm, role_id, body) -> web.Response:
    """Return object stating whether role Authoirzation permissions have been initialized or not and a reference

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_id: 
    :type role_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ManagementPermissionReference.from_dict(body)
    return web.Response(status=200)


async def realm_roles_by_id_role_id_put(request: web.Request, realm, role_id, body) -> web.Response:
    """Update the role

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_id: id of role
    :type role_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RoleRepresentation.from_dict(body)
    return web.Response(status=200)
