from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_video_version_request import CreateVideoVersionRequest
from openapi_server.models.error import Error
from openapi_server.models.video_versions import VideoVersions
from openapi_server import util


async def create_video_version(request: web.Request, video_id, body) -> web.Response:
    """Add a version to a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateVideoVersionRequest.from_dict(body)
    return web.Response(status=200)
