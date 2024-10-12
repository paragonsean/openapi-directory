from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def user_to_folder_assign_delete(request: web.Request, source, target) -> web.Response:
    """Deletes a user to folder assignement

    

    :param source: The ID of the user that should be de-assign
    :type source: str
    :param target: The ID of the folder
    :type target: str

    """
    return web.Response(status=200)


async def user_to_folder_assign_post(request: web.Request, source, target, old_folder) -> web.Response:
    """Assign a user to a folder

    

    :param source: The ID of the user that should be assign
    :type source: str
    :param target: The ID of the folder that should be the parent
    :type target: str
    :param old_folder: The ID of the old folder (in case of a drag and drop to a new folder)
    :type old_folder: str

    """
    return web.Response(status=200)
