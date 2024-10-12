from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.key_revoke200_response import KeyRevoke200Response
from openapi_server.models.key_revoke_nosecret200_response import KeyRevokeNosecret200Response
from openapi_server import util


async def key_revoke_0(request: web.Request, pk, secret) -> web.Response:
    """key_revoke_0

    Revoke an Identity (Key) with a revocation secret

    :param pk: Public Signing Key - Authentiq ID (43 chars)
    :type pk: str
    :param secret: revokation secret
    :type secret: str

    """
    return web.Response(status=200)


async def key_revoke_nosecret_0(request: web.Request, email, phone, code=None) -> web.Response:
    """key_revoke_nosecret_0

    Revoke an Authentiq ID using email &amp; phone.  If called with &#x60;email&#x60; and &#x60;phone&#x60; only, a verification code  will be sent by email. Do a second call adding &#x60;code&#x60; to  complete the revocation. 

    :param email: primary email associated to Key (ID)
    :type email: str
    :param phone: primary phone number, international representation
    :type phone: str
    :param code: verification code sent by email
    :type code: str

    """
    return web.Response(status=200)


async def sign_delete_0(request: web.Request, job) -> web.Response:
    """sign_delete_0

    delete a verification job

    :param job: Job ID (20 chars)
    :type job: str

    """
    return web.Response(status=200)
