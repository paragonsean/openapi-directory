from typing import List, Dict
from aiohttp import web

from openapi_server.models.folder_menu_configuration import FolderMenuConfiguration
from openapi_server import util


async def folder_menu_get(request: web.Request, filter=None) -> web.Response:
    """Gets the folder menu items (each item might contain child items)

    

    :param filter: (optional) Filter for the folders and meters:               all: load everything              assigned: load only folders and meters that are assigend to a folder              unassigend: load only meters that are not assigend to a folder              user: load only folder and all users assigned to this folders              subuserlist: load all subusers as a list
    :type filter: str

    """
    return web.Response(status=200)


async def folder_menu_post(request: web.Request, body) -> web.Response:
    """Creates and updates the folder menu items

    

    :param body: 
    :type body: dict | bytes

    """
    body = FolderMenuConfiguration.from_dict(body)
    return web.Response(status=200)
