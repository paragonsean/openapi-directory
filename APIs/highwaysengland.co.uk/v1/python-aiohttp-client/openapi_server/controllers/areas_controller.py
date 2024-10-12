from typing import List, Dict
from aiohttp import web

from openapi_server.models.area_response import AreaResponse
from openapi_server import util


async def areas_get(request: web.Request, version) -> web.Response:
    """Returns list of areas

    

    :param version: 
    :type version: str

    """
    return web.Response(status=200)


async def vversion_areas_area_ids_get(request: web.Request, area_ids, version) -> web.Response:
    """Returns details of selected area

    

    :param area_ids: 
    :type area_ids: str
    :param version: 
    :type version: str

    """
    return web.Response(status=200)
