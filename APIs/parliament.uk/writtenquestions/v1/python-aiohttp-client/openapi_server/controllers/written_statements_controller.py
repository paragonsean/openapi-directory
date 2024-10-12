from typing import List, Dict
from aiohttp import web

from openapi_server.models.house_enum import HouseEnum
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.statements_view_model_item import StatementsViewModelItem
from openapi_server.models.statements_view_model_search_result import StatementsViewModelSearchResult
from openapi_server import util


async def api_writtenstatements_statements_date_uin_get(request: web.Request, _date, uin, expand_member=None) -> web.Response:
    """Returns a written statemnet

    

    :param _date: Written statement on date specified
    :type _date: str
    :param uin: Written statement with uid specified
    :type uin: str
    :param expand_member: Expand the details of Members in the results
    :type expand_member: bool

    """
    _date = util.deserialize_datetime(_date)
    return web.Response(status=200)


async def api_writtenstatements_statements_get(request: web.Request, made_when_from=None, made_when_to=None, search_term=None, u_in=None, answering_bodies=None, members=None, house=None, skip=None, take=None, expand_member=None) -> web.Response:
    """Returns a list of written statements

    

    :param made_when_from: Written statements made on or after the date specified. Date format yyyy-mm-dd
    :type made_when_from: str
    :param made_when_to: Written statements made on or before the date specified. Date format yyyy-mm-dd
    :type made_when_to: str
    :param search_term: Written questions / statements containing the search term specified, searches item content
    :type search_term: str
    :param u_in: Written questions / statements with the uin specified
    :type u_in: str
    :param answering_bodies: Written questions / statements relating to the answering bodies with the IDs specified
    :type answering_bodies: List[int]
    :param members: Written questions / statements relating to the members with the IDs specified
    :type members: List[int]
    :param house: Written questions / statements relating to the House specified
    :type house: dict | bytes
    :param skip: Number of records to skip, default is 0
    :type skip: int
    :param take: Number of records to take, default is 20
    :type take: int
    :param expand_member: Expand the details of Members in the results
    :type expand_member: bool

    """
    made_when_from = util.deserialize_datetime(made_when_from)
    made_when_to = util.deserialize_datetime(made_when_to)
    house = .from_dict(house)
    return web.Response(status=200)


async def api_writtenstatements_statements_id_get(request: web.Request, id, expand_member=None) -> web.Response:
    """Returns a written statement

    

    :param id: Written statement with ID specified
    :type id: int
    :param expand_member: Expand the details of Members in the results
    :type expand_member: bool

    """
    return web.Response(status=200)
