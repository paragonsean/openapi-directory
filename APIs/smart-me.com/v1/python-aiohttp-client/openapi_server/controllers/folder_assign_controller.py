from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def folder_assign_post(request: web.Request, source, target) -> web.Response:
    """Assign a folder (source) or meter to another folder (target). Can be used to create a folder structure.

    

    :param source: The ID of the meter or folder that should be assign
    :type source: str
    :param target: The ID of the meter or folder that should be the parent
    :type target: str

    """
    return web.Response(status=200)
