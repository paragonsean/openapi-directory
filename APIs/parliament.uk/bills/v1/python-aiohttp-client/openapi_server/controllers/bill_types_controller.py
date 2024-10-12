from typing import List, Dict
from aiohttp import web

from openapi_server.models.bill_type_category import BillTypeCategory
from openapi_server.models.bill_type_search_result import BillTypeSearchResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def api_v1_bill_types_get(request: web.Request, category=None, skip=None, take=None) -> web.Response:
    """Returns a list of Bill types.

    

    :param category: 
    :type category: dict | bytes
    :param skip: 
    :type skip: int
    :param take: 
    :type take: int

    """
    category = .from_dict(category)
    return web.Response(status=200)
