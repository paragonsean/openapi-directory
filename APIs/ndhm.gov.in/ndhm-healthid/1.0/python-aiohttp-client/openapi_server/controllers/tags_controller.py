from typing import List, Dict
from aiohttp import web

from openapi_server.models.tag_request import TagRequest
from openapi_server import util


async def add_tag_using_post(request: web.Request, tag_request, accept_language=None) -> web.Response:
    """Add tag against HealthId.

    

    :param tag_request: tagRequest
    :type tag_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    tag_request = TagRequest.from_dict(tag_request)
    return web.Response(status=200)


async def delete_tag_using_delete(request: web.Request, tag_request, accept_language=None) -> web.Response:
    """Delete tag against HealthId.

    

    :param tag_request: tagRequest
    :type tag_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    tag_request = TagRequest.from_dict(tag_request)
    return web.Response(status=200)


async def get_tags_using_get(request: web.Request, x_token, accept_language=None) -> web.Response:
    """Get list of Tags against HealthID.

    

    :param x_token: Auth Token
    :type x_token: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)
