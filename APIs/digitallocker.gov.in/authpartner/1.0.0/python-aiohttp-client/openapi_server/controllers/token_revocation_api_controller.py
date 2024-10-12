from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_token_revocation_id_request import GetTokenRevocationIdRequest
from openapi_server import util


async def get_token_revocation_id(request: web.Request, body=None) -> web.Response:
    """Revoke Token.

    Client applications can revoke a previously obtained refresh or access token when it is no longer needed. This is done by making a request to the token revocation endpoint. DigiLocker will invalidate the specified token and, if applicable, other tokens based on the same authorisation grant. This API may be used to sign out a user from DigiLocker. This API will work for server based web applications, mobile application and limited input devices.

    :param body: 
    :type body: dict | bytes

    """
    body = GetTokenRevocationIdRequest.from_dict(body)
    return web.Response(status=200)
