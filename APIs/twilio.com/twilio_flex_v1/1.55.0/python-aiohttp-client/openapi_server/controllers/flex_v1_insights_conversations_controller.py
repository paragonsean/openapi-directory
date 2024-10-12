from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_insights_conversations_response import ListInsightsConversationsResponse
from openapi_server import util


async def list_insights_conversations(request: web.Request, authorization=None, segment_id=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_insights_conversations

    To get conversation with segment id

    :param authorization: The Authorization HTTP request header
    :type authorization: str
    :param segment_id: Unique Id of the segment for which conversation details needs to be fetched
    :type segment_id: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
