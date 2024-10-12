from typing import List, Dict
from aiohttp import web

from openapi_server.models.community_content_get_community_content200_response import CommunityContentGetCommunityContent200Response
from openapi_server import util


async def community_content_get_community_content(request: web.Request, media_filter, page, sort) -> web.Response:
    """community_content_get_community_content

    Returns community content.

    :param media_filter: The type of media to get
    :type media_filter: int
    :param page: Zero based page
    :type page: int
    :param sort: The sort mode.
    :type sort: int

    """
    return web.Response(status=200)
