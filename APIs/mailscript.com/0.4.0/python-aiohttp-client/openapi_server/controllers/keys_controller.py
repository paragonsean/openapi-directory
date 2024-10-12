from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_key_request import AddKeyRequest
from openapi_server.models.add_key_response import AddKeyResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_keys_response import GetAllKeysResponse
from openapi_server.models.key import Key
from openapi_server.models.update_key_request import UpdateKeyRequest
from openapi_server import util


async def add_key(request: web.Request, address, body) -> web.Response:
    """Add address key

    

    :param address: ID of address
    :type address: str
    :param body: Key body
    :type body: dict | bytes

    """
    body = AddKeyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_key(request: web.Request, address, key) -> web.Response:
    """Delete address key

    

    :param address: ID of address
    :type address: str
    :param key: ID of key
    :type key: str

    """
    return web.Response(status=200)


async def get_all_keys(request: web.Request, address) -> web.Response:
    """List address keys

    

    :param address: ID of address
    :type address: str

    """
    return web.Response(status=200)


async def get_key(request: web.Request, address, key) -> web.Response:
    """Get address key

    

    :param address: ID of address
    :type address: str
    :param key: ID of key
    :type key: str

    """
    return web.Response(status=200)


async def update_key(request: web.Request, address, key, body) -> web.Response:
    """Update an address key

    

    :param address: ID of address
    :type address: str
    :param key: ID of key
    :type key: str
    :param body: Key body
    :type body: dict | bytes

    """
    body = UpdateKeyRequest.from_dict(body)
    return web.Response(status=200)
