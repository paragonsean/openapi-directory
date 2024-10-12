from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_create_api_model import ClientCreateApiModel
from openapi_server.models.client_delete_api_model import ClientDeleteApiModel
from openapi_server.models.client_details_api_model import ClientDetailsApiModel
from openapi_server.models.client_update_api_model import ClientUpdateApiModel
from openapi_server import util


async def client_api_all(request: web.Request, x_auth_key, x_auth_secret) -> web.Response:
    """Return all clients for the account

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def client_api_can_delete(request: web.Request, id, x_auth_key, x_auth_secret) -> web.Response:
    """Check if the provided client can be deleted

    

    :param id: 
    :type id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def client_api_delete(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Delete an existing client

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClientDeleteApiModel.from_dict(body)
    return web.Response(status=200)


async def client_api_details(request: web.Request, id, x_auth_key, x_auth_secret) -> web.Response:
    """Return client details. Activities and invoices included.

    

    :param id: 
    :type id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def client_api_new(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Create a client

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClientCreateApiModel.from_dict(body)
    return web.Response(status=200)


async def client_api_update(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Update an existing client

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClientUpdateApiModel.from_dict(body)
    return web.Response(status=200)
