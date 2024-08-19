from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.share_file_response import ShareFileResponse
from openapi_server.models.tools_share_file_request import ToolsShareFileRequest
from openapi_server import util


async def tools_share_file(request: web.Request, body) -> web.Response:
    """Share file - use to host a file and generate a short link to be used directly in a message or as a link to media for a MMS

    

    :param body: 
    :type body: str

    """
    return web.Response(status=200)
