from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.file_keyword_model import FileKeywordModel
from openapi_server import util


async def keywords_link_keyword_to_file(request: web.Request, file_guid, guid) -> web.Response:
    """Link existing keyword to file

    

    :param file_guid: 
    :type file_guid: str
    :param guid: 
    :type guid: str

    """
    return web.Response(status=200)
