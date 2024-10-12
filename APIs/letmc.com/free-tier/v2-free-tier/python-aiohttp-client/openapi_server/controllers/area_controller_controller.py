from typing import List, Dict
from aiohttp import web

from openapi_server.models.area_model import AreaModel
from openapi_server.models.area_model_results import AreaModelResults
from openapi_server import util


async def v2_tier1_short_name_area_areas_area_idget(request: web.Request, short_name, area_id) -> web.Response:
    """Get a specific area given its unique Object ID (OID)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param area_id: The unique ID of the Area
    :type area_id: str

    """
    return web.Response(status=200)


async def v2_tier1_short_name_area_areas_get(request: web.Request, short_name, offset, count) -> web.Response:
    """A collection of all the areas for a company

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)
