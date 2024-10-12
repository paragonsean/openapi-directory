from typing import List, Dict
from aiohttp import web

from openapi_server.models.answered import Answered
from openapi_server.models.house_enum import HouseEnum
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.question_status_enum import QuestionStatusEnum
from openapi_server.models.questions_view_model_item import QuestionsViewModelItem
from openapi_server.models.questions_view_model_search_result import QuestionsViewModelSearchResult
from openapi_server import util


async def api_writtenquestions_questions_date_uin_get(request: web.Request, _date, uin, expand_member=None) -> web.Response:
    """Returns a written question

    

    :param _date: Written question on date specified
    :type _date: str
    :param uin: Written question with uid specified
    :type uin: str
    :param expand_member: Expand the details of Members in the results
    :type expand_member: bool

    """
    _date = util.deserialize_datetime(_date)
    return web.Response(status=200)


async def api_writtenquestions_questions_get(request: web.Request, asking_member_id=None, answering_member_id=None, tabled_when_from=None, tabled_when_to=None, answered=None, answered_when_from=None, answered_when_to=None, question_status=None, include_withdrawn=None, expand_member=None, corrected_when_from=None, corrected_when_to=None, search_term=None, u_in=None, answering_bodies=None, members=None, house=None, skip=None, take=None) -> web.Response:
    """Returns a list of written questions

    

    :param asking_member_id: Written questions asked by member with member ID specified
    :type asking_member_id: int
    :param answering_member_id: Written questions answered by member with member ID specified
    :type answering_member_id: int
    :param tabled_when_from: Written questions tabled on or after the date specified. Date format yyyy-mm-dd
    :type tabled_when_from: str
    :param tabled_when_to: Written questions tabled on or before the date specified. Date format yyyy-mm-dd
    :type tabled_when_to: str
    :param answered: Written questions that have been answered, unanswered or either.
    :type answered: dict | bytes
    :param answered_when_from: Written questions answered on or after the date specified. Date format yyyy-mm-dd
    :type answered_when_from: str
    :param answered_when_to: Written questions answered on or before the date specified. Date format yyyy-mm-dd
    :type answered_when_to: str
    :param question_status: Written questions with the status specified
    :type question_status: dict | bytes
    :param include_withdrawn: Include written questions that have been withdrawn
    :type include_withdrawn: bool
    :param expand_member: Expand the details of Members in the results
    :type expand_member: bool
    :param corrected_when_from: Written questions corrected on or after the date specified. Date format yyyy-mm-dd
    :type corrected_when_from: str
    :param corrected_when_to: Written questions corrected on or before the date specified. Date format yyyy-mm-dd
    :type corrected_when_to: str
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

    """
    tabled_when_from = util.deserialize_datetime(tabled_when_from)
    tabled_when_to = util.deserialize_datetime(tabled_when_to)
    answered = .from_dict(answered)
    answered_when_from = util.deserialize_datetime(answered_when_from)
    answered_when_to = util.deserialize_datetime(answered_when_to)
    question_status = .from_dict(question_status)
    corrected_when_from = util.deserialize_datetime(corrected_when_from)
    corrected_when_to = util.deserialize_datetime(corrected_when_to)
    house = .from_dict(house)
    return web.Response(status=200)


async def api_writtenquestions_questions_id_get(request: web.Request, id, expand_member=None) -> web.Response:
    """Returns a written question

    

    :param id: written question with ID specified
    :type id: int
    :param expand_member: Expand the details of Members in the result
    :type expand_member: bool

    """
    return web.Response(status=200)
