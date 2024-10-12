from typing import List, Dict
from aiohttp import web

from openapi_server.models.folder_data import FolderData
from openapi_server import util


async def folder_get(request: web.Request, id) -> web.Response:
    """Gets the Values for a folder or a meter

    Gets the Values for a folder or a meter

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
