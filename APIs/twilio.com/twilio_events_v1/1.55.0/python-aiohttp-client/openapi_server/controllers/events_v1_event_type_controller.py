from typing import List, Dict
from aiohttp import web

from openapi_server.models.events_v1_event_type import EventsV1EventType
from openapi_server.models.list_event_type_response import ListEventTypeResponse
from openapi_server import util


async def fetch_event_type(request: web.Request, type) -> web.Response:
    """fetch_event_type

    Fetch a specific Event Type.

    :param type: A string that uniquely identifies this Event Type.
    :type type: str

    """
    return web.Response(status=200)


async def list_event_type(request: web.Request, schema_id=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_event_type

    Retrieve a paginated list of all the available Event Types.

    :param schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
    :type schema_id: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
