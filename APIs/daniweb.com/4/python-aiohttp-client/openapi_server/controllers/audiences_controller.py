from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_get_audiences import EndpointGetAudiences
from openapi_server.models.endpoint_get_audiences_id import EndpointGetAudiencesID
from openapi_server.models.endpoint_post_audiences_id_memberships import EndpointPostAudiencesIDMemberships
from openapi_server import util


async def audiences_get(request: web.Request, offset=None, limit=None) -> web.Response:
    """audiences_get

    Fetch all Daniapp audience segments that comprise the current access token&#39;s bubble.

    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def audiences_id_memberships_post(request: web.Request, id) -> web.Response:
    """audiences_id_memberships_post

    Create a membership record for the OAuth&#39;ed end-user based on the current audience segment/bubble combination.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def audiences_idget(request: web.Request, id) -> web.Response:
    """audiences_idget

    Fetch an array of Daniapp audience segments that comprise the current access token&#39;s bubble.

    :param id: 
    :type id: List[int]

    """
    return web.Response(status=200)
