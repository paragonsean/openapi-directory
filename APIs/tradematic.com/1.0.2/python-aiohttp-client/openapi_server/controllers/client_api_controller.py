from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key import APIKey
from openapi_server.models.client_apikeys_keyid_delete200_response import ClientApikeysKeyidDelete200Response
from openapi_server.models.client_apikeys_post200_response import ClientApikeysPost200Response
from openapi_server.models.client_users_login_post200_response import ClientUsersLoginPost200Response
from openapi_server.models.client_users_register_post200_response import ClientUsersRegisterPost200Response
from openapi_server.models.client_users_register_post_request import ClientUsersRegisterPostRequest
from openapi_server.models.error import Error
from openapi_server.models.user import User
from openapi_server import util


async def client_apikeys_get(request: web.Request, ) -> web.Response:
    """Get API keys

    Get API keys


    """
    return web.Response(status=200)


async def client_apikeys_keyid_delete(request: web.Request, keyid) -> web.Response:
    """Delete API key

    Delete API key

    :param keyid: 
    :type keyid: int

    """
    return web.Response(status=200)


async def client_apikeys_post(request: web.Request, ) -> web.Response:
    """Create new API key

    Create new API key


    """
    return web.Response(status=200)


async def client_users_get(request: web.Request, ) -> web.Response:
    """Get users list

    Get users list


    """
    return web.Response(status=200)


async def client_users_login_post(request: web.Request, ) -> web.Response:
    """Logs user into the system

    Logs user into the system


    """
    return web.Response(status=200)


async def client_users_register_post(request: web.Request, body) -> web.Response:
    """Register a new user

    Register a new user

    :param body: 
    :type body: dict | bytes

    """
    body = ClientUsersRegisterPostRequest.from_dict(body)
    return web.Response(status=200)


async def client_users_userid_get(request: web.Request, userid) -> web.Response:
    """Get user by ID

    Get user by ID

    :param userid: 
    :type userid: int

    """
    return web.Response(status=200)
