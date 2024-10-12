from typing import List, Dict
from aiohttp import web

from openapi_server.models.bill import Bill
from openapi_server.models.bill_sort_order import BillSortOrder
from openapi_server.models.bill_stage_details import BillStageDetails
from openapi_server.models.bill_summary_search_result import BillSummarySearchResult
from openapi_server.models.house import House
from openapi_server.models.originating_house import OriginatingHouse
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.stage_summary_search_result import StageSummarySearchResult
from openapi_server import util


async def api_v1_bills_bill_id_stages_get(request: web.Request, bill_id, skip=None, take=None) -> web.Response:
    """Returns all Bill stages.

    

    :param bill_id: Stages relating to a Bill with Bill ID specified
    :type bill_id: int
    :param skip: 
    :type skip: int
    :param take: 
    :type take: int

    """
    return web.Response(status=200)


async def get_bill(request: web.Request, bill_id) -> web.Response:
    """Return a Bill.

    

    :param bill_id: Bill with ID specified
    :type bill_id: int

    """
    return web.Response(status=200)


async def get_bill_stage_details(request: web.Request, bill_id, bill_stage_id) -> web.Response:
    """Returns a Bill stage.

    

    :param bill_id: Bill stage relating to Bill with Bill ID specified
    :type bill_id: int
    :param bill_stage_id: Bill stage with ID specified
    :type bill_stage_id: int

    """
    return web.Response(status=200)


async def get_bills(request: web.Request, search_term=None, session=None, current_house=None, originating_house=None, member_id=None, department_id=None, bill_stage=None, bill_stages_excluded=None, is_defeated=None, is_withdrawn=None, bill_type=None, sort_order=None, bill_ids=None, skip=None, take=None) -> web.Response:
    """Returns a list of Bills.

    

    :param search_term: 
    :type search_term: str
    :param session: 
    :type session: int
    :param current_house: 
    :type current_house: dict | bytes
    :param originating_house: 
    :type originating_house: dict | bytes
    :param member_id: 
    :type member_id: int
    :param department_id: 
    :type department_id: int
    :param bill_stage: 
    :type bill_stage: List[int]
    :param bill_stages_excluded: 
    :type bill_stages_excluded: List[int]
    :param is_defeated: 
    :type is_defeated: bool
    :param is_withdrawn: 
    :type is_withdrawn: bool
    :param bill_type: 
    :type bill_type: List[int]
    :param sort_order: 
    :type sort_order: dict | bytes
    :param bill_ids: 
    :type bill_ids: List[int]
    :param skip: 
    :type skip: int
    :param take: 
    :type take: int

    """
    current_house = .from_dict(current_house)
    originating_house = .from_dict(originating_house)
    sort_order = .from_dict(sort_order)
    return web.Response(status=200)
