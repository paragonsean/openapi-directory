from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_initial_access_create_presentation import ClientInitialAccessCreatePresentation
from openapi_server.models.client_initial_access_presentation import ClientInitialAccessPresentation
from openapi_server import util


async def realm_clients_initial_access_get(request: web.Request, realm) -> web.Response:
    """realm_clients_initial_access_get

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_clients_initial_access_id_delete(request: web.Request, realm, id) -> web.Response:
    """realm_clients_initial_access_id_delete

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_initial_access_post(request: web.Request, realm, body) -> web.Response:
    """Create a new initial access token.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClientInitialAccessCreatePresentation.from_dict(body)
    return web.Response(status=200)
