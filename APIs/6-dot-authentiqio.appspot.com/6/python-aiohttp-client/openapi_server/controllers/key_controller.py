from typing import List, Dict
from aiohttp import web

from openapi_server.models.authentiq_id import AuthentiqID
from openapi_server.models.error import Error
from openapi_server.models.jwt import JWT
from openapi_server.models.key_bind200_response import KeyBind200Response
from openapi_server.models.key_register201_response import KeyRegister201Response
from openapi_server.models.key_revoke200_response import KeyRevoke200Response
from openapi_server.models.key_revoke_nosecret200_response import KeyRevokeNosecret200Response
from openapi_server import util


async def key_bind(request: web.Request, pk, body) -> web.Response:
    """key_bind

    Update Authentiq ID by replacing the object.  v4: &#x60;JWT(sub,email,phone)&#x60; to bind email/phone hash;   v5: POST issuer-signed email &amp; phone scopes and PUT to update registration &#x60;JWT(sub, pk, devtoken, ...)&#x60;  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

    :param pk: Public Signing Key - Authentiq ID (43 chars)
    :type pk: str
    :param body: Authentiq ID to register
    :type body: dict | bytes

    """
    body = AuthentiqID.from_dict(body)
    return web.Response(status=200)


async def key_pkhead(request: web.Request, pk) -> web.Response:
    """key_pkhead

    HEAD info on Authentiq ID 

    :param pk: Public Signing Key - Authentiq ID (43 chars)
    :type pk: str

    """
    return web.Response(status=200)


async def key_register(request: web.Request, body) -> web.Response:
    """key_register

    Register a new ID &#x60;JWT(sub, devtoken)&#x60;  v5: &#x60;JWT(sub, pk, devtoken, ...)&#x60;  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

    :param body: Authentiq ID to register
    :type body: dict | bytes

    """
    body = AuthentiqID.from_dict(body)
    return web.Response(status=200)


async def key_retrieve(request: web.Request, pk) -> web.Response:
    """key_retrieve

    Get public details of an Authentiq ID. 

    :param pk: Public Signing Key - Authentiq ID (43 chars)
    :type pk: str

    """
    return web.Response(status=200)


async def key_revoke(request: web.Request, pk, secret) -> web.Response:
    """key_revoke

    Revoke an Identity (Key) with a revocation secret

    :param pk: Public Signing Key - Authentiq ID (43 chars)
    :type pk: str
    :param secret: revokation secret
    :type secret: str

    """
    return web.Response(status=200)


async def key_revoke_nosecret(request: web.Request, email, phone, code=None) -> web.Response:
    """key_revoke_nosecret

    Revoke an Authentiq ID using email &amp; phone.  If called with &#x60;email&#x60; and &#x60;phone&#x60; only, a verification code  will be sent by email. Do a second call adding &#x60;code&#x60; to  complete the revocation. 

    :param email: primary email associated to Key (ID)
    :type email: str
    :param phone: primary phone number, international representation
    :type phone: str
    :param code: verification code sent by email
    :type code: str

    """
    return web.Response(status=200)


async def key_update(request: web.Request, pk, body) -> web.Response:
    """key_update

    update properties of an Authentiq ID. (not operational in v4; use PUT for now)  v5: POST issuer-signed email &amp; phone scopes in a self-signed JWT  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

    :param pk: Public Signing Key - Authentiq ID (43 chars)
    :type pk: str
    :param body: Authentiq ID to register
    :type body: dict | bytes

    """
    body = AuthentiqID.from_dict(body)
    return web.Response(status=200)
