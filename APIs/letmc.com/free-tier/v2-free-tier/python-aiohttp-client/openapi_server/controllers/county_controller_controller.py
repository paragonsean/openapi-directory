from typing import List, Dict
from aiohttp import web

from openapi_server.models.branch_model_results import BranchModelResults
from openapi_server.models.county_model import CountyModel
from openapi_server.models.county_model_results import CountyModelResults
from openapi_server import util


async def county_controller_get_counties_branches(request: web.Request, short_name, county_id, offset, count) -> web.Response:
    """A collection of branches that manage a specific county

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param county_id: The unique ID of the County
    :type county_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def v2_tier1_short_name_county_counties_county_idget(request: web.Request, short_name, county_id) -> web.Response:
    """Get a specific county given its unique Object ID (OID)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param county_id: The unique ID of the County
    :type county_id: str

    """
    return web.Response(status=200)


async def v2_tier1_short_name_county_counties_get(request: web.Request, short_name, offset, count) -> web.Response:
    """A collection of all counties available for a company

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)
