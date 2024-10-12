from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_events200_response import GetEvents200Response
from openapi_server import util


async def get_events(request: web.Request, conversation_id, page_size=None, order=None, cursor=None, start_id=None, end_id=None, event_type=None) -> web.Response:
    """List Events

    

    :param conversation_id: The ID of the conversation
    :type conversation_id: str
    :param page_size: The number of results returned per page.   The default value is &#x60;10&#x60;. The maximum value is &#x60;100&#x60;.
    :type page_size: int
    :param order: Show the most (&#x60;desc&#x60;) / least (&#x60;asc&#x60;) recently created entries first
    :type order: str
    :param cursor: The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in &#x60;_links.next.href&#x60; in the response which contains a &#x60;cursor&#x60; value 
    :type cursor: str
    :param start_id: The ID to start returning events at
    :type start_id: str
    :param end_id: The ID to end returning events at
    :type end_id: str
    :param event_type: The type of event to search for. Does not currently support custom events
    :type event_type: str

    """
    return web.Response(status=200)
