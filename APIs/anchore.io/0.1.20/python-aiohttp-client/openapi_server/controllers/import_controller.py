from typing import List, Dict
from aiohttp import web

from openapi_server.models.anchore_image import AnchoreImage
from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server import util


async def import_image_archive(request: web.Request, archive_file) -> web.Response:
    """Import an anchore image tar.gz archive file. This is a deprecated API replaced by the \&quot;/imports/images\&quot; route

    

    :param archive_file: anchore image tar archive.
    :type archive_file: str

    """
    return web.Response(status=200)
