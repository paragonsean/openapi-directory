from typing import List, Dict
from aiohttp import web

from openapi_server.models.meter_folder_information import MeterFolderInformation
from openapi_server.models.meter_folder_information_to_post import MeterFolderInformationToPost
from openapi_server import util


async def meter_folder_information_get(request: web.Request, id) -> web.Response:
    """Beta: Gets the General Information for a Meter or a Folder

    Beta: Gets the General Information for a Meter or a Folder

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def meter_folder_information_post(request: web.Request, body) -> web.Response:
    """Sets the Name of a Meter or a Folder

    Sets the Name of a Meter or a Folder

    :param body: 
    :type body: dict | bytes

    """
    body = MeterFolderInformationToPost.from_dict(body)
    return web.Response(status=200)
