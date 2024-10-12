from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_a_key_request import CreateAKeyRequest
from openapi_server.models.update_a_key_request import UpdateAKeyRequest
from openapi_server import util


async def create_a_key(request: web.Request, body=None) -> web.Response:
    """Create a key

    Create a key

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAKeyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_a_key(request: web.Request, ) -> web.Response:
    """Delete a key

    Delete a key


    """
    return web.Response(status=200)


async def get_keys(request: web.Request, offset=None, limit=None) -> web.Response:
    """Get keys

    Get keys

    :param offset: 
    :type offset: str
    :param limit: 
    :type limit: str

    """
    return web.Response(status=200)


async def get_one_key(request: web.Request, ) -> web.Response:
    """Get one key

    Get one key


    """
    return web.Response(status=200)


async def update_a_key(request: web.Request, body=None) -> web.Response:
    """Update a key

    Update a key

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAKeyRequest.from_dict(body)
    return web.Response(status=200)
