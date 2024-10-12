from typing import List, Dict
from aiohttp import web

from openapi_server.models.folder_menu_item import FolderMenuItem
from openapi_server.models.folder_settings import FolderSettings
from openapi_server import util


async def folder_settings_delete(request: web.Request, id) -> web.Response:
    """Deletes a folder

    

    :param id: The ID of the folder
    :type id: str

    """
    return web.Response(status=200)


async def folder_settings_get(request: web.Request, id) -> web.Response:
    """Gets the settings of a folder or meter

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def folder_settings_post(request: web.Request, id, body) -> web.Response:
    """Add or edit a folder or a meter. To add a new folder use and empty ID

    

    :param id: The ID of the folder or meter to edit. Use and empty ID to add a new folder
    :type id: str
    :param body: The folder or meter data
    :type body: dict | bytes

    """
    body = FolderSettings.from_dict(body)
    return web.Response(status=200)
