from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_district_list_rank import APIDistrictListRank
from openapi_server.models.api_school_list_rank import APISchoolListRank
from openapi_server import util


async def rankings_get_rank(request: web.Request, st, app_id, app_key, year=None, level=None, page=None, per_page=None) -> web.Response:
    """Returns a SchoolDigger school ranking list

    

    :param st: Two character state (e.g. &#39;CA&#39;)
    :type st: str
    :param app_id: Your API app id
    :type app_id: str
    :param app_key: Your API app key
    :type app_key: str
    :param year: The ranking year (leave blank for most recent year)
    :type year: int
    :param level: Level of ranking: &#39;Elementary&#39;, &#39;Middle&#39;, or &#39;High&#39;
    :type level: str
    :param page: Page number to retrieve (optional, default: 1)
    :type page: int
    :param per_page: Number of schools to retrieve on a page (50 max) (optional, default: 10)
    :type per_page: int

    """
    return web.Response(status=200)


async def rankings_get_rank_district(request: web.Request, st, app_id, app_key, year=None, page=None, per_page=None) -> web.Response:
    """Returns a SchoolDigger district ranking list

    

    :param st: Two character state (e.g. &#39;CA&#39;)
    :type st: str
    :param app_id: Your API app id
    :type app_id: str
    :param app_key: Your API app key
    :type app_key: str
    :param year: The ranking year (leave blank for most recent year)
    :type year: int
    :param page: Page number to retrieve (optional, default: 1)
    :type page: int
    :param per_page: Number of districts to retrieve on a page (50 max) (optional, default: 10)
    :type per_page: int

    """
    return web.Response(status=200)
