from typing import List, Dict
from aiohttp import web

from openapi_server.models.track_snippet_get_get200_response import TrackSnippetGetGet200Response
from openapi_server import util


async def track_snippet_get_get(request: web.Request, track_id, format=None, param_callback=None) -> web.Response:
    """track_snippet_get_get

    

    :param track_id: The musiXmatch track id
    :type track_id: str
    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str

    """
    return web.Response(status=200)
