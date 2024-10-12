from typing import List, Dict
from aiohttp import web

from openapi_server.models.bill_stage_sitting_search_result import BillStageSittingSearchResult
from openapi_server.models.house import House
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def get_sittings(request: web.Request, house=None, date_from=None, date_to=None, skip=None, take=None) -> web.Response:
    """Returns a list of Sittings.

    

    :param house: 
    :type house: dict | bytes
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param skip: 
    :type skip: int
    :param take: 
    :type take: int

    """
    house = .from_dict(house)
    date_from = util.deserialize_datetime(date_from)
    date_to = util.deserialize_datetime(date_to)
    return web.Response(status=200)
