from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_url import FileUrl
from openapi_server import util


async def svgconvert(request: web.Request, file=None) -> web.Response:
    """converts pptx file to svg image

    

    :param file: 
    :type file: str

    """
    return web.Response(status=200)
