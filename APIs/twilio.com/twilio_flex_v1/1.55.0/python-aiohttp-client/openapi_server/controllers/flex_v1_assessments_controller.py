from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_insights_assessments import FlexV1InsightsAssessments
from openapi_server.models.list_insights_assessments_response import ListInsightsAssessmentsResponse
from openapi_server import util


async def create_insights_assessments(request: web.Request, agent_id, answer_id, answer_text, category_name, category_sid, metric_id, metric_name, offset, questionnaire_sid, segment_id, authorization=None) -> web.Response:
    """create_insights_assessments

    Add assessments against conversation to dynamo db. Used in assessments screen by user. Users can select the questionnaire and pick up answers for each and every question.

    :param agent_id: The id of the Agent
    :type agent_id: str
    :param answer_id: The id of the answer selected by user
    :type answer_id: str
    :param answer_text: The answer text selected by user
    :type answer_text: str
    :param category_name: The name of the category
    :type category_name: str
    :param category_sid: The SID of the category 
    :type category_sid: str
    :param metric_id: The question SID selected for assessment
    :type metric_id: str
    :param metric_name: The question name of the assessment
    :type metric_name: str
    :param offset: The offset of the conversation.
    :type offset: 
    :param questionnaire_sid: Questionnaire SID of the associated question
    :type questionnaire_sid: str
    :param segment_id: Segment Id of the conversation
    :type segment_id: str
    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)


async def list_insights_assessments(request: web.Request, authorization=None, segment_id=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_insights_assessments

    Get assessments done for a conversation by logged in user

    :param authorization: The Authorization HTTP request header
    :type authorization: str
    :param segment_id: The id of the segment.
    :type segment_id: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_insights_assessments(request: web.Request, assessment_sid, answer_id, answer_text, offset, authorization=None) -> web.Response:
    """update_insights_assessments

    Update a specific Assessment assessed earlier

    :param assessment_sid: The SID of the assessment to be modified
    :type assessment_sid: str
    :param answer_id: The id of the answer selected by user
    :type answer_id: str
    :param answer_text: The answer text selected by user
    :type answer_text: str
    :param offset: The offset of the conversation
    :type offset: 
    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)
