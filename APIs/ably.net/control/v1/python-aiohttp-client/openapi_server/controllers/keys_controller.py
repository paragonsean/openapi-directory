from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.key_patch import KeyPatch
from openapi_server.models.key_post import KeyPost
from openapi_server.models.key_response import KeyResponse
from openapi_server import util


async def apps_app_id_keys_get(request: web.Request, app_id) -> web.Response:
    """Lists app keys

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def apps_app_id_keys_key_id_patch(request: web.Request, app_id, key_id, body=None) -> web.Response:
    """Updates a key

    

    :param app_id: 
    :type app_id: str
    :param key_id: 
    :type key_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = KeyPatch.from_dict(body)
    return web.Response(status=200)


async def apps_app_id_keys_key_id_revoke_post(request: web.Request, app_id, key_id) -> web.Response:
    """Revokes a key

    

    :param app_id: 
    :type app_id: str
    :param key_id: 
    :type key_id: str

    """
    return web.Response(status=200)


async def apps_app_id_keys_post(request: web.Request, app_id, body=None) -> web.Response:
    """Creates a key

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = KeyPost.from_dict(body)
    return web.Response(status=200)
