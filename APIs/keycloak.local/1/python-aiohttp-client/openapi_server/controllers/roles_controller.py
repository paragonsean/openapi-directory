from typing import List, Dict
from aiohttp import web

from openapi_server.models.group_representation import GroupRepresentation
from openapi_server.models.management_permission_reference import ManagementPermissionReference
from openapi_server.models.role_representation import RoleRepresentation
from openapi_server.models.user_representation import UserRepresentation
from openapi_server import util


async def realm_clients_id_roles_get(request: web.Request, realm, id, brief_representation=None, first=None, max=None, search=None) -> web.Response:
    """Get all roles for the realm or client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param brief_representation: 
    :type brief_representation: bool
    :param first: 
    :type first: int
    :param max: 
    :type max: int
    :param search: 
    :type search: str

    """
    return web.Response(status=200)


async def realm_clients_id_roles_post(request: web.Request, realm, id, body) -> web.Response:
    """Create a new role for the realm or client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RoleRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_clients_id_roles_role_name_composites_clients_client_get(request: web.Request, realm, id, role_name, client) -> web.Response:
    """An app-level roles for the specified app for the role’s composite

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_name: role’s name (not id!)
    :type role_name: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_clients_id_roles_role_name_composites_delete(request: web.Request, realm, id, role_name, body) -> web.Response:
    """Remove roles from the role’s composite

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_name: role’s name (not id!)
    :type role_name: str
    :param body: roles to remove
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_clients_id_roles_role_name_composites_get(request: web.Request, realm, id, role_name) -> web.Response:
    """Get composites of the role

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_name: role’s name (not id!)
    :type role_name: str

    """
    return web.Response(status=200)


async def realm_clients_id_roles_role_name_composites_post(request: web.Request, realm, id, role_name, body) -> web.Response:
    """Add a composite to the role

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_name: role’s name (not id!)
    :type role_name: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_clients_id_roles_role_name_composites_realm_get(request: web.Request, realm, id, role_name) -> web.Response:
    """Get realm-level roles of the role’s composite

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_name: role’s name (not id!)
    :type role_name: str

    """
    return web.Response(status=200)


async def realm_clients_id_roles_role_name_delete(request: web.Request, realm, id, role_name) -> web.Response:
    """Delete a role by name

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_name: role’s name (not id!)
    :type role_name: str

    """
    return web.Response(status=200)


async def realm_clients_id_roles_role_name_get(request: web.Request, realm, id, role_name) -> web.Response:
    """Get a role by name

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_name: role’s name (not id!)
    :type role_name: str

    """
    return web.Response(status=200)


async def realm_clients_id_roles_role_name_groups_get(request: web.Request, realm, id, role_name, brief_representation=None, first=None, max=None) -> web.Response:
    """Return List of Groups that have the specified role name

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_name: 
    :type role_name: str
    :param brief_representation: if false, return a full representation of the GroupRepresentation objects
    :type brief_representation: bool
    :param first: 
    :type first: int
    :param max: 
    :type max: int

    """
    return web.Response(status=200)


async def realm_clients_id_roles_role_name_management_permissions_get(request: web.Request, realm, id, role_name) -> web.Response:
    """Return object stating whether role Authoirzation permissions have been initialized or not and a reference

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_name: 
    :type role_name: str

    """
    return web.Response(status=200)


async def realm_clients_id_roles_role_name_management_permissions_put(request: web.Request, realm, id, role_name, body) -> web.Response:
    """Return object stating whether role Authoirzation permissions have been initialized or not and a reference

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_name: 
    :type role_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = ManagementPermissionReference.from_dict(body)
    return web.Response(status=200)


async def realm_clients_id_roles_role_name_put(request: web.Request, realm, id, role_name, body) -> web.Response:
    """Update a role by name

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_name: role’s name (not id!)
    :type role_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = RoleRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_clients_id_roles_role_name_users_get(request: web.Request, realm, id, role_name, first=None, max=None) -> web.Response:
    """Return List of Users that have the specified role name

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_name: 
    :type role_name: str
    :param first: 
    :type first: int
    :param max: 
    :type max: int

    """
    return web.Response(status=200)


async def realm_roles_get(request: web.Request, realm, brief_representation=None, first=None, max=None, search=None) -> web.Response:
    """Get all roles for the realm or client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param brief_representation: 
    :type brief_representation: bool
    :param first: 
    :type first: int
    :param max: 
    :type max: int
    :param search: 
    :type search: str

    """
    return web.Response(status=200)


async def realm_roles_post(request: web.Request, realm, body) -> web.Response:
    """Create a new role for the realm or client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: dict | bytes

    """
    body = RoleRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_roles_role_name_composites_clients_client_get(request: web.Request, realm, role_name, client) -> web.Response:
    """An app-level roles for the specified app for the role’s composite

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_name: role’s name (not id!)
    :type role_name: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_roles_role_name_composites_delete(request: web.Request, realm, role_name, body) -> web.Response:
    """Remove roles from the role’s composite

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_name: role’s name (not id!)
    :type role_name: str
    :param body: roles to remove
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_roles_role_name_composites_get(request: web.Request, realm, role_name) -> web.Response:
    """Get composites of the role

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_name: role’s name (not id!)
    :type role_name: str

    """
    return web.Response(status=200)


async def realm_roles_role_name_composites_post(request: web.Request, realm, role_name, body) -> web.Response:
    """Add a composite to the role

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_name: role’s name (not id!)
    :type role_name: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_roles_role_name_composites_realm_get(request: web.Request, realm, role_name) -> web.Response:
    """Get realm-level roles of the role’s composite

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_name: role’s name (not id!)
    :type role_name: str

    """
    return web.Response(status=200)


async def realm_roles_role_name_delete(request: web.Request, realm, role_name) -> web.Response:
    """Delete a role by name

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_name: role’s name (not id!)
    :type role_name: str

    """
    return web.Response(status=200)


async def realm_roles_role_name_get(request: web.Request, realm, role_name) -> web.Response:
    """Get a role by name

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_name: role’s name (not id!)
    :type role_name: str

    """
    return web.Response(status=200)


async def realm_roles_role_name_groups_get(request: web.Request, realm, role_name, brief_representation=None, first=None, max=None) -> web.Response:
    """Return List of Groups that have the specified role name

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_name: 
    :type role_name: str
    :param brief_representation: if false, return a full representation of the GroupRepresentation objects
    :type brief_representation: bool
    :param first: 
    :type first: int
    :param max: 
    :type max: int

    """
    return web.Response(status=200)


async def realm_roles_role_name_management_permissions_get(request: web.Request, realm, role_name) -> web.Response:
    """Return object stating whether role Authoirzation permissions have been initialized or not and a reference

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_name: 
    :type role_name: str

    """
    return web.Response(status=200)


async def realm_roles_role_name_management_permissions_put(request: web.Request, realm, role_name, body) -> web.Response:
    """Return object stating whether role Authoirzation permissions have been initialized or not and a reference

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_name: 
    :type role_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = ManagementPermissionReference.from_dict(body)
    return web.Response(status=200)


async def realm_roles_role_name_put(request: web.Request, realm, role_name, body) -> web.Response:
    """Update a role by name

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_name: role’s name (not id!)
    :type role_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = RoleRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_roles_role_name_users_get(request: web.Request, realm, role_name, first=None, max=None) -> web.Response:
    """Return List of Users that have the specified role name

    

    :param realm: realm name (not id!)
    :type realm: str
    :param role_name: 
    :type role_name: str
    :param first: 
    :type first: int
    :param max: 
    :type max: int

    """
    return web.Response(status=200)
