from typing import List, Dict
from aiohttp import web

from openapi_server.models.last_media_request import LastMediaRequest
from openapi_server.models.last_media_result import LastMediaResult
from openapi_server.models.start_video_request import StartVideoRequest
from openapi_server.models.start_video_result import StartVideoResult
from openapi_server import util


async def last_media_post(request: web.Request, body) -> web.Response:
    """Get informations about last media playback

    

    :param body: 
    :type body: dict | bytes

    """
    body = LastMediaRequest.from_dict(body)
    return web.Response(status=200)


async def start_video_post(request: web.Request, body) -> web.Response:
    """Start the playback

    Start the playback of the speficied video. 

    :param body: 
    :type body: dict | bytes

    """
    body = StartVideoRequest.from_dict(body)
    return web.Response(status=200)
