from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_secret200_response import AddSecret200Response
from openapi_server.models.delete_secret200_response import DeleteSecret200Response
from openapi_server.models.get_all_secrets200_response import GetAllSecrets200Response
from openapi_server.models.get_secret200_response import GetSecret200Response
from openapi_server.models.secrets import Secrets
from openapi_server.models.update_secret200_response import UpdateSecret200Response
from openapi_server import util


async def add_secret(request: web.Request, body) -> web.Response:
    """Create a secret

    Add a secret

    :param body: 
    :type body: dict | bytes

    """
    body = Secrets.from_dict(body)
    return web.Response(status=200)


async def delete_secret(request: web.Request, name) -> web.Response:
    """Delete a secret

    Remove the secret by his unique name

    :param name: Unique name of the secret
    :type name: str

    """
    return web.Response(status=200)


async def get_all_secrets(request: web.Request, ) -> web.Response:
    """List all secrets

    Get the list of all secrets without their value


    """
    return web.Response(status=200)


async def get_secret(request: web.Request, name) -> web.Response:
    """Get one secret

    Get one secret by his unique name

    :param name: Unique name of the secret
    :type name: str

    """
    return web.Response(status=200)


async def update_secret(request: web.Request, body) -> web.Response:
    """Update a secret

    Update a secret and override the value, the name cannot be overridden

    :param body: 
    :type body: dict | bytes

    """
    body = Secrets.from_dict(body)
    return web.Response(status=200)
