from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_insights_questionnaires import FlexV1InsightsQuestionnaires
from openapi_server.models.list_insights_questionnaires_response import ListInsightsQuestionnairesResponse
from openapi_server import util


async def create_insights_questionnaires(request: web.Request, name, authorization=None, active=None, description=None, question_sids=None) -> web.Response:
    """create_insights_questionnaires

    To create a Questionnaire

    :param name: The name of this questionnaire
    :type name: str
    :param authorization: The Authorization HTTP request header
    :type authorization: str
    :param active: The flag to enable or disable questionnaire
    :type active: bool
    :param description: The description of this questionnaire
    :type description: str
    :param question_sids: The list of questions sids under a questionnaire
    :type question_sids: List[str]

    """
    return web.Response(status=200)


async def delete_insights_questionnaires(request: web.Request, questionnaire_sid, authorization=None) -> web.Response:
    """delete_insights_questionnaires

    To delete the questionnaire

    :param questionnaire_sid: The SID of the questionnaire
    :type questionnaire_sid: str
    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)


async def fetch_insights_questionnaires(request: web.Request, questionnaire_sid, authorization=None) -> web.Response:
    """fetch_insights_questionnaires

    To get the Questionnaire Detail

    :param questionnaire_sid: The SID of the questionnaire
    :type questionnaire_sid: str
    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)


async def list_insights_questionnaires(request: web.Request, authorization=None, include_inactive=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_insights_questionnaires

    To get all questionnaires with questions

    :param authorization: The Authorization HTTP request header
    :type authorization: str
    :param include_inactive: Flag indicating whether to include inactive questionnaires or not
    :type include_inactive: bool
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_insights_questionnaires(request: web.Request, questionnaire_sid, active, authorization=None, description=None, name=None, question_sids=None) -> web.Response:
    """update_insights_questionnaires

    To update the questionnaire

    :param questionnaire_sid: The SID of the questionnaire
    :type questionnaire_sid: str
    :param active: The flag to enable or disable questionnaire
    :type active: bool
    :param authorization: The Authorization HTTP request header
    :type authorization: str
    :param description: The description of this questionnaire
    :type description: str
    :param name: The name of this questionnaire
    :type name: str
    :param question_sids: The list of questions sids under a questionnaire
    :type question_sids: List[str]

    """
    return web.Response(status=200)
