from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server import util


async def key_pkhead_0(request: web.Request, pk) -> web.Response:
    """key_pkhead_0

    HEAD info on Authentiq ID 

    :param pk: Public Signing Key - Authentiq ID (43 chars)
    :type pk: str

    """
    return web.Response(status=200)


async def sign_retrieve_head_0(request: web.Request, job) -> web.Response:
    """sign_retrieve_head_0

    HEAD to get the status of a verification job

    :param job: Job ID (20 chars)
    :type job: str

    """
    return web.Response(status=200)
