from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server import util


async def keywords_delete_file_keyword(request: web.Request, file_guid, guid) -> web.Response:
    """Delete a keyword from the file

    Returns: No Content (204) if succeeded. Not found (404) if the keyword or the link can&#39;t be found.

    :param file_guid: 
    :type file_guid: str
    :param guid: 
    :type guid: str

    """
    return web.Response(status=200)
