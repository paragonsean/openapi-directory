from typing import List, Dict
from aiohttp import web

from openapi_server.models.mappings_representation import MappingsRepresentation
from openapi_server.models.role_representation import RoleRepresentation
from openapi_server import util


async def realm_client_scopes_id_scope_mappings_clients_client_available_get(request: web.Request, realm, id, client) -> web.Response:
    """The available client-level roles   Returns the roles for the client that can be associated with the client’s scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id_scope_mappings_clients_client_composite_get(request: web.Request, realm, id, client) -> web.Response:
    """Get effective client roles   Returns the roles for the client that are associated with the client’s scope.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id_scope_mappings_clients_client_delete(request: web.Request, realm, id, client, body) -> web.Response:
    """Remove client-level roles from the client’s scope.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str
    :param client: 
    :type client: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_client_scopes_id_scope_mappings_clients_client_get(request: web.Request, realm, id, client) -> web.Response:
    """Get the roles associated with a client’s scope   Returns roles for the client.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id_scope_mappings_clients_client_post(request: web.Request, realm, id, client, body) -> web.Response:
    """Add client-level roles to the client’s scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str
    :param client: 
    :type client: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_client_scopes_id_scope_mappings_get(request: web.Request, realm, id) -> web.Response:
    """Get all scope mappings for the client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id_scope_mappings_realm_available_get(request: web.Request, realm, id) -> web.Response:
    """Get realm-level roles that are available to attach to this client’s scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id_scope_mappings_realm_composite_get(request: web.Request, realm, id) -> web.Response:
    """Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id_scope_mappings_realm_delete(request: web.Request, realm, id, body) -> web.Response:
    """Remove a set of realm-level roles from the client’s scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_client_scopes_id_scope_mappings_realm_get(request: web.Request, realm, id) -> web.Response:
    """Get realm-level roles associated with the client’s scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id_scope_mappings_realm_post(request: web.Request, realm, id, body) -> web.Response:
    """Add a set of realm-level roles to the client’s scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_clients_id_scope_mappings_clients_client_available_get(request: web.Request, realm, id, client) -> web.Response:
    """The available client-level roles   Returns the roles for the client that can be associated with the client’s scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_clients_id_scope_mappings_clients_client_composite_get(request: web.Request, realm, id, client) -> web.Response:
    """Get effective client roles   Returns the roles for the client that are associated with the client’s scope.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_clients_id_scope_mappings_clients_client_delete(request: web.Request, realm, id, client, body) -> web.Response:
    """Remove client-level roles from the client’s scope.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param client: 
    :type client: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_clients_id_scope_mappings_clients_client_get(request: web.Request, realm, id, client) -> web.Response:
    """Get the roles associated with a client’s scope   Returns roles for the client.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param client: 
    :type client: str

    """
    return web.Response(status=200)


async def realm_clients_id_scope_mappings_clients_client_post(request: web.Request, realm, id, client, body) -> web.Response:
    """Add client-level roles to the client’s scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param client: 
    :type client: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_clients_id_scope_mappings_get(request: web.Request, realm, id) -> web.Response:
    """Get all scope mappings for the client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_scope_mappings_realm_available_get(request: web.Request, realm, id) -> web.Response:
    """Get realm-level roles that are available to attach to this client’s scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_scope_mappings_realm_composite_get(request: web.Request, realm, id) -> web.Response:
    """Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_scope_mappings_realm_delete(request: web.Request, realm, id, body) -> web.Response:
    """Remove a set of realm-level roles from the client’s scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_clients_id_scope_mappings_realm_get(request: web.Request, realm, id) -> web.Response:
    """Get realm-level roles associated with the client’s scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_scope_mappings_realm_post(request: web.Request, realm, id, body) -> web.Response:
    """Add a set of realm-level roles to the client’s scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param body: 
    :type body: list | bytes

    """
    body = [RoleRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)
