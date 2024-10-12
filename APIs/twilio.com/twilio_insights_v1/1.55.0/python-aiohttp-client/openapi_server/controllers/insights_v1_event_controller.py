from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_enum_twilio_edge import EventEnumTwilioEdge
from openapi_server.models.list_event_response import ListEventResponse
from openapi_server import util


async def list_event(request: web.Request, call_sid, edge=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_event

    Get a list of Call Insight Events for a Call.

    :param call_sid: The unique SID identifier of the Call.
    :type call_sid: str
    :param edge: The Edge of this Event. One of &#x60;unknown_edge&#x60;, &#x60;carrier_edge&#x60;, &#x60;sip_edge&#x60;, &#x60;sdk_edge&#x60; or &#x60;client_edge&#x60;.
    :type edge: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
