from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.stage_reference_search_result import StageReferenceSearchResult
from openapi_server import util


async def api_v1_stages_get(request: web.Request, skip=None, take=None) -> web.Response:
    """Returns a list of Bill stages.

    

    :param skip: 
    :type skip: int
    :param take: 
    :type take: int

    """
    return web.Response(status=200)
