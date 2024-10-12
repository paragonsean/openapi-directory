from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.live import Live
from openapi_server import util


async def get_lives_0(request: web.Request, page=None, per_page=None) -> web.Response:
    """List lives matches

    List currently running live matches, available from pandascore with live websocket data.

    :param page: Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60;
    :type page: dict | bytes
    :param per_page: Equivalent to &#x60;page[size]&#x60;
    :type per_page: int

    """
    page = .from_dict(page)
    return web.Response(status=200)
