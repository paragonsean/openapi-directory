from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def get_attachment(request: web.Request, video_id, media_source_id, index) -> web.Response:
    """Get video attachment.

    

    :param video_id: Video ID.
    :type video_id: str
    :type video_id: str
    :param media_source_id: Media Source ID.
    :type media_source_id: str
    :param index: Attachment Index.
    :type index: int

    """
    return web.Response(status=200)
