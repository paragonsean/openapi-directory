from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_response import FileResponse
from openapi_server import util


async def uploads_create(request: web.Request, file) -> web.Response:
    """Upload a new image

    This POST-Method uploads a new file on the server.

    :param file: File which should be uploaded. Supported file types are: JPEG and PNG
    :type file: str

    """
    return web.Response(status=200)
