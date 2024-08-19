from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.key_patch import KeyPatch
from openapi_server.models.key_post import KeyPost
from openapi_server.models.key_response import KeyResponse
from openapi_server import util


async def apps_app_id_keys_get(request: web.Request, app_id) -> web.Response:
    """Lists app keys

    Lists the API keys associated with the application ID.

    :param app_id: The application ID.
    :type app_id: str

    """
    return web.Response(status=200)


async def apps_app_id_keys_key_id_patch(request: web.Request, app_id, key_id, body=None) -> web.Response:
    """Updates a key

    Update the API key with the specified key ID, for the application with the specified application ID.

    :param app_id: The application ID.
    :type app_id: str
    :param key_id: The API key ID.
    :type key_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = KeyPatch.from_dict(body)
    return web.Response(status=200)


async def apps_app_id_keys_key_id_revoke_post(request: web.Request, app_id, key_id) -> web.Response:
    """Revokes a key

    Revokes the API key with the specified ID, with the Application ID. This deletes the key.

    :param app_id: The application ID.
    :type app_id: str
    :param key_id: The key ID.
    :type key_id: str

    """
    return web.Response(status=200)


async def apps_app_id_keys_post(request: web.Request, app_id, body=None) -> web.Response:
    """Creates a key

    Creates an API key for the application specified.

    :param app_id: The application ID.
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = KeyPost.from_dict(body)
    return web.Response(status=200)
