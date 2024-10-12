from typing import List, Dict
from aiohttp import web

from openapi_server.models.authentiq_id import AuthentiqID
from openapi_server.models.error import Error
from openapi_server.models.key_bind200_response import KeyBind200Response
from openapi_server.models.sign_update200_response import SignUpdate200Response
from openapi_server import util


async def key_bind_0(request: web.Request, pk, body) -> web.Response:
    """key_bind_0

    Update Authentiq ID by replacing the object.  v4: &#x60;JWT(sub,email,phone)&#x60; to bind email/phone hash;   v5: POST issuer-signed email &amp; phone scopes and PUT to update registration &#x60;JWT(sub, pk, devtoken, ...)&#x60;  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

    :param pk: Public Signing Key - Authentiq ID (43 chars)
    :type pk: str
    :param body: Authentiq ID to register
    :type body: dict | bytes

    """
    body = AuthentiqID.from_dict(body)
    return web.Response(status=200)


async def sign_update_0(request: web.Request, job) -> web.Response:
    """sign_update_0

    authority updates a JWT with its signature See: https://github.com/skion/authentiq/wiki/JWT-Examples 

    :param job: Job ID (20 chars)
    :type job: str

    """
    return web.Response(status=200)
