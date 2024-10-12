from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def basic_auth_user_passwd_get(request: web.Request, user, passwd) -> web.Response:
    """Prompts the user for authorization using HTTP Basic Auth.

    

    :param user: 
    :type user: str
    :param passwd: 
    :type passwd: str

    """
    return web.Response(status=200)


async def bearer_get(request: web.Request, authorization=None) -> web.Response:
    """Prompts the user for authorization using bearer authentication.

    

    :param authorization: 
    :type authorization: str

    """
    return web.Response(status=200)


async def digest_auth_qop_user_passwd_algorithm_get(request: web.Request, qop, user, passwd, algorithm) -> web.Response:
    """Prompts the user for authorization using Digest Auth + Algorithm.

    

    :param qop: auth or auth-int
    :type qop: str
    :param user: 
    :type user: str
    :param passwd: 
    :type passwd: str
    :param algorithm: MD5, SHA-256, SHA-512
    :type algorithm: str

    """
    return web.Response(status=200)


async def digest_auth_qop_user_passwd_algorithm_stale_after_get(request: web.Request, qop, user, passwd, algorithm, stale_after) -> web.Response:
    """Prompts the user for authorization using Digest Auth + Algorithm.

    allow settings the stale_after argument. 

    :param qop: auth or auth-int
    :type qop: str
    :param user: 
    :type user: str
    :param passwd: 
    :type passwd: str
    :param algorithm: MD5, SHA-256, SHA-512
    :type algorithm: str
    :param stale_after: 
    :type stale_after: str

    """
    return web.Response(status=200)


async def digest_auth_qop_user_passwd_get(request: web.Request, qop, user, passwd) -> web.Response:
    """Prompts the user for authorization using Digest Auth.

    

    :param qop: auth or auth-int
    :type qop: str
    :param user: 
    :type user: str
    :param passwd: 
    :type passwd: str

    """
    return web.Response(status=200)


async def hidden_basic_auth_user_passwd_get(request: web.Request, user, passwd) -> web.Response:
    """Prompts the user for authorization using HTTP Basic Auth.

    

    :param user: 
    :type user: str
    :param passwd: 
    :type passwd: str

    """
    return web.Response(status=200)
