from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_scope_representation import ClientScopeRepresentation
from openapi_server import util


async def realm_client_scopes_get(request: web.Request, realm) -> web.Response:
    """Get client scopes belonging to the realm   Returns a list of client scopes belonging to the realm

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id_delete(request: web.Request, realm, id) -> web.Response:
    """Delete the client scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id_get(request: web.Request, realm, id) -> web.Response:
    """Get representation of the client scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id_put(request: web.Request, realm, id, body) -> web.Response:
    """Update the client scope

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClientScopeRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_client_scopes_post(request: web.Request, realm, body) -> web.Response:
    """Create a new client scope   Client Scope’s name must be unique!

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClientScopeRepresentation.from_dict(body)
    return web.Response(status=200)
