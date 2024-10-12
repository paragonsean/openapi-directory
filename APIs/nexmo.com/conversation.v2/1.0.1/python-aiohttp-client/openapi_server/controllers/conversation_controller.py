from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_conversations200_response import GetConversations200Response
from openapi_server import util


async def get_conversations(request: web.Request, page_size=None, order=None, cursor=None, date_start=None, date_end=None) -> web.Response:
    """List Conversations

    Please note that not all data is available in the list endpoint. Once  you&#39;ve identified the conversation you need to work with, use the  [GET /conversations/:id](#get-conversation) endpoint to fetch all of the conversation details 

    :param page_size: The number of results returned per page.   The default value is &#x60;10&#x60;. The maximum value is &#x60;100&#x60;.
    :type page_size: int
    :param order: Show the most (&#x60;desc&#x60;) / least (&#x60;asc&#x60;) recently created entries first
    :type order: str
    :param cursor: The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in &#x60;_links.next.href&#x60; in the response which contains a &#x60;cursor&#x60; value 
    :type cursor: str
    :param date_start: Search for conversations created after this ISO8601 date
    :type date_start: str
    :param date_end: Search for conversations created before this ISO8601 date
    :type date_end: str

    """
    return web.Response(status=200)
