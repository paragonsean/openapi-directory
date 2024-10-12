from typing import List, Dict
from aiohttp import web

from openapi_server.models.client import Client
from openapi_server.models.o_auth2_error import OAuth2Error
from openapi_server.models.problem_detail import ProblemDetail
from openapi_server import util


async def client(request: web.Request, ) -> web.Response:
    """List clients

    Retrieve a list of clients. 


    """
    return web.Response(status=200)


async def client_client_id(request: web.Request, client_id) -> web.Response:
    """Delete a client

    Delete a previously registered client. 

    :param client_id: Client identifier
    :type client_id: str

    """
    return web.Response(status=200)


async def create_client(request: web.Request, body) -> web.Response:
    """Register a client

    Register a new client with this Authentiq Connect provider.  This endpoint is compatible with [OIDC&#39;s Client Registration](http://openid.net/specs/openid-connect-registration-1_0.html) extension. 

    :param body: Client Object
    :type body: dict | bytes

    """
    body = Client.from_dict(body)
    return web.Response(status=200)


async def get_client(request: web.Request, client_id) -> web.Response:
    """View a client

    Retrieve the configuration of a previously registered client. 

    :param client_id: Client identifier
    :type client_id: str

    """
    return web.Response(status=200)


async def update_client(request: web.Request, client_id, body) -> web.Response:
    """Update a client

    Update the configuration of a previously registered client. 

    :param client_id: Client identifier
    :type client_id: str
    :param body: Client Object
    :type body: dict | bytes

    """
    body = Client.from_dict(body)
    return web.Response(status=200)
