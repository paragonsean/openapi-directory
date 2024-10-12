from typing import List, Dict
from aiohttp import web

from openapi_server.models.role_representation import RoleRepresentation
from openapi_server import util


async def realm_groups_id_role_mappings_clients_client_available_get(request: web.Request, realm, id, client) -> web.Response:
    """Get available client-level roles that can be mapped to the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_groups_id_role_mappings_clients_client_composite_get(request: web.Request, realm, id, client) -> web.Response:
    """Get effective client-level role mappings   This recurses any composite roles

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_groups_id_role_mappings_clients_client_delete(request: web.Request, realm, id, client, body) -> web.Response:
    """Delete client-level roles from user role mapping

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param client: 
    :type client: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_groups_id_role_mappings_clients_client_get(request: web.Request, realm, id, client) -> web.Response:
    """Get client-level role mappings for the user, and the app

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_groups_id_role_mappings_clients_client_post(request: web.Request, realm, id, client, body) -> web.Response:
    """Add client-level roles to the user role mapping

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param client: 
    :type client: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_users_id_role_mappings_clients_client_available_get(request: web.Request, realm, id, client) -> web.Response:
    """Get available client-level roles that can be mapped to the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_users_id_role_mappings_clients_client_composite_get(request: web.Request, realm, id, client) -> web.Response:
    """Get effective client-level role mappings   This recurses any composite roles

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_users_id_role_mappings_clients_client_delete(request: web.Request, realm, id, client, body) -> web.Response:
    """Delete client-level roles from user role mapping

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param client: 
    :type client: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_users_id_role_mappings_clients_client_get(request: web.Request, realm, id, client) -> web.Response:
    """Get client-level role mappings for the user, and the app

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_users_id_role_mappings_clients_client_post(request: web.Request, realm, id, client, body) -> web.Response:
    """Add client-level roles to the user role mapping

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param client: 
    :type client: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)
