from typing import List, Dict
from aiohttp import web

from openapi_server.models.amendment_detail import AmendmentDetail
from openapi_server.models.amendment_search_item_search_result import AmendmentSearchItemSearchResult
from openapi_server.models.decision import Decision
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def get_amendment(request: web.Request, bill_id, bill_stage_id, amendment_id) -> web.Response:
    """Returns an amendment.

    

    :param bill_id: Amendment relating to a bill with bill ID specified
    :type bill_id: int
    :param bill_stage_id: Amendment relating to a bill stage with bill stage ID specified
    :type bill_stage_id: int
    :param amendment_id: Amendment with amendment ID specified
    :type amendment_id: int

    """
    return web.Response(status=200)


async def get_amendments(request: web.Request, bill_id, bill_stage_id, search_term=None, decision=None, member_id=None, skip=None, take=None) -> web.Response:
    """Returns a list of amendments.

    

    :param bill_id: Amendments relating to a Bill with Bill ID specified
    :type bill_id: int
    :param bill_stage_id: Amendments relating to a Bill stage with Bill stage ID specified
    :type bill_stage_id: int
    :param search_term: 
    :type search_term: str
    :param decision: 
    :type decision: dict | bytes
    :param member_id: 
    :type member_id: int
    :param skip: 
    :type skip: int
    :param take: 
    :type take: int

    """
    decision = .from_dict(decision)
    return web.Response(status=200)
