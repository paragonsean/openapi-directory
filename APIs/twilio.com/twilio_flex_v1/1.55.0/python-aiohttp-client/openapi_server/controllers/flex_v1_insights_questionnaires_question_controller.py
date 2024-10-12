from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_insights_questionnaires_question import FlexV1InsightsQuestionnairesQuestion
from openapi_server.models.list_insights_questionnaires_question_response import ListInsightsQuestionnairesQuestionResponse
from openapi_server import util


async def create_insights_questionnaires_question(request: web.Request, allow_na, answer_set_id, category_sid, question, authorization=None, description=None) -> web.Response:
    """create_insights_questionnaires_question

    To create a question for a Category

    :param allow_na: The flag to enable for disable NA for answer.
    :type allow_na: bool
    :param answer_set_id: The answer_set for the question.
    :type answer_set_id: str
    :param category_sid: The SID of the category
    :type category_sid: str
    :param question: The question.
    :type question: str
    :param authorization: The Authorization HTTP request header
    :type authorization: str
    :param description: The description for the question.
    :type description: str

    """
    return web.Response(status=200)


async def delete_insights_questionnaires_question(request: web.Request, question_sid, authorization=None) -> web.Response:
    """delete_insights_questionnaires_question

    

    :param question_sid: The SID of the question
    :type question_sid: str
    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)


async def list_insights_questionnaires_question(request: web.Request, authorization=None, category_sid=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_insights_questionnaires_question

    To get all the question for the given categories

    :param authorization: The Authorization HTTP request header
    :type authorization: str
    :param category_sid: The list of category SIDs
    :type category_sid: List[str]
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_insights_questionnaires_question(request: web.Request, question_sid, allow_na, authorization=None, answer_set_id=None, category_sid=None, description=None, question=None) -> web.Response:
    """update_insights_questionnaires_question

    To update the question

    :param question_sid: The SID of the question
    :type question_sid: str
    :param allow_na: The flag to enable for disable NA for answer.
    :type allow_na: bool
    :param authorization: The Authorization HTTP request header
    :type authorization: str
    :param answer_set_id: The answer_set for the question.
    :type answer_set_id: str
    :param category_sid: The SID of the category
    :type category_sid: str
    :param description: The description for the question.
    :type description: str
    :param question: The question.
    :type question: str

    """
    return web.Response(status=200)
