from typing import List, Dict
from aiohttp import web

from openapi_server.models.claims import Claims
from openapi_server.models.error import Error
from openapi_server.models.jwt1 import JWT1
from openapi_server.models.key_bind200_response import KeyBind200Response
from openapi_server.models.key_revoke200_response import KeyRevoke200Response
from openapi_server.models.sign_request201_response import SignRequest201Response
from openapi_server.models.sign_update200_response import SignUpdate200Response
from openapi_server import util


async def sign_confirm(request: web.Request, job) -> web.Response:
    """sign_confirm

    this is a scope confirmation

    :param job: Job ID (20 chars)
    :type job: str

    """
    return web.Response(status=200)


async def sign_delete(request: web.Request, job) -> web.Response:
    """sign_delete

    delete a verification job

    :param job: Job ID (20 chars)
    :type job: str

    """
    return web.Response(status=200)


async def sign_request(request: web.Request, body, test=None) -> web.Response:
    """sign_request

    scope verification request See: https://github.com/skion/authentiq/wiki/JWT-Examples 

    :param body: Claims of scope
    :type body: dict | bytes
    :param test: test only mode, using test issuer
    :type test: int

    """
    body = Claims.from_dict(body)
    return web.Response(status=200)


async def sign_retrieve(request: web.Request, job) -> web.Response:
    """sign_retrieve

    get the status / current content of a verification job

    :param job: Job ID (20 chars)
    :type job: str

    """
    return web.Response(status=200)


async def sign_retrieve_head(request: web.Request, job) -> web.Response:
    """sign_retrieve_head

    HEAD to get the status of a verification job

    :param job: Job ID (20 chars)
    :type job: str

    """
    return web.Response(status=200)


async def sign_update(request: web.Request, job) -> web.Response:
    """sign_update

    authority updates a JWT with its signature See: https://github.com/skion/authentiq/wiki/JWT-Examples 

    :param job: Job ID (20 chars)
    :type job: str

    """
    return web.Response(status=200)
