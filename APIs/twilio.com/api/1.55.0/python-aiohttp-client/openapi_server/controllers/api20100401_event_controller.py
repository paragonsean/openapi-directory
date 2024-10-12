from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_call_event_response import ListCallEventResponse
from openapi_server import util


async def list_call_event(request: web.Request, account_sid, call_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_call_event

    Retrieve a list of all events for a call.

    :param account_sid: The unique SID identifier of the Account.
    :type account_sid: str
    :param call_sid: The unique SID identifier of the Call.
    :type call_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
