from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server import util


async def download_file(request: web.Request, subdir, filename, dir, download=None, rotation=None) -> web.Response:
    """Download File

    Get File

    :param subdir: 
    :type subdir: str
    :param filename: 
    :type filename: str
    :param dir: 
    :type dir: str
    :param download: 
    :type download: str
    :param rotation: 
    :type rotation: int

    """
    return web.Response(status=200)
