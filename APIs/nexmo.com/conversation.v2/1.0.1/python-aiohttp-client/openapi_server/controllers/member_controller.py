from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_members200_response import GetMembers200Response
from openapi_server import util


async def get_members(request: web.Request, conversation_id, page_size=None, order=None, cursor=None) -> web.Response:
    """List Members

    

    :param conversation_id: The ID of the conversation
    :type conversation_id: str
    :param page_size: The number of results returned per page.   The default value is &#x60;10&#x60;. The maximum value is &#x60;100&#x60;.
    :type page_size: int
    :param order: Show the most (&#x60;desc&#x60;) / least (&#x60;asc&#x60;) recently created entries first
    :type order: str
    :param cursor: The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in &#x60;_links.next.href&#x60; in the response which contains a &#x60;cursor&#x60; value 
    :type cursor: str

    """
    return web.Response(status=200)
