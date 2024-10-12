from typing import List, Dict
from aiohttp import web

from openapi_server.models.preview_response import PreviewResponse
from openapi_server import util


async def previews_read(request: web.Request, file_id) -> web.Response:
    """Get preview image of uploaded file

    This GET-Method returns the URL where the preview image of uploaded file can downloaded from.

    :param file_id: Id of the file for which the preview_img_url is generated.
    :type file_id: str

    """
    return web.Response(status=200)
