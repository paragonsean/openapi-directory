from typing import List, Dict
from aiohttp import web

from openapi_server.models.cache_post_request import CachePostRequest
from openapi_server.models.problem_detail import ProblemDetail
from openapi_server import util


async def cache_nonce_get(request: web.Request, nonce) -> web.Response:
    """Cache: Get Subdocument

    An endpoint for broswer retreive html documents that were cached durin the rendering process via a nonce (token)

    :param nonce: A one-time use token for retieving items in the users cache
    :type nonce: str
    :type nonce: str

    """
    return web.Response(status=200)


async def cache_post(request: web.Request, body) -> web.Response:
    """Cache: Store Subdocument

    An endpoint for Presalytics Renderers to cache html subdocuments for subsequent retrieval by the browser.  Documents Are retrieved via token expire after 1 minute.

    :param body: parameters to identify an update a collaborator across multiple stories
    :type body: dict | bytes

    """
    body = CachePostRequest.from_dict(body)
    return web.Response(status=200)
