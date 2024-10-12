from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_insights_assessments_comment import FlexV1InsightsAssessmentsComment
from openapi_server.models.list_insights_assessments_comment_response import ListInsightsAssessmentsCommentResponse
from openapi_server import util


async def create_insights_assessments_comment(request: web.Request, agent_id, category_id, category_name, comment, offset, segment_id, authorization=None) -> web.Response:
    """create_insights_assessments_comment

    To create a comment assessment for a conversation

    :param agent_id: The id of the agent.
    :type agent_id: str
    :param category_id: The ID of the category
    :type category_id: str
    :param category_name: The name of the category
    :type category_name: str
    :param comment: The Assessment comment.
    :type comment: str
    :param offset: The offset
    :type offset: 
    :param segment_id: The id of the segment.
    :type segment_id: str
    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)


async def list_insights_assessments_comment(request: web.Request, authorization=None, segment_id=None, agent_id=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_insights_assessments_comment

    To create a comment assessment for a conversation

    :param authorization: The Authorization HTTP request header
    :type authorization: str
    :param segment_id: The id of the segment.
    :type segment_id: str
    :param agent_id: The id of the agent.
    :type agent_id: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
