from typing import List, Dict
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server.models.event_include import EventInclude
from openapi_server.models.event_list import EventList
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def event_detail_events_event_id_get(request: web.Request, event_id, include=None, apikey=None, x_api_key=None) -> web.Response:
    """Event Detail

    Get details on a single event by ID.

    :param event_id: 
    :type event_id: str
    :param include: Additional includes for the Event response.
    :type include: list | bytes
    :param apikey: 
    :type apikey: str
    :param x_api_key: 
    :type x_api_key: str

    """
    include = [EventInclude.from_dict(d) for d in include]
    return web.Response(status=200)


async def event_list_events_get(request: web.Request, jurisdiction=None, deleted=None, before=None, after=None, require_bills=None, include=None, apikey=None, page=None, per_page=None, x_api_key=None) -> web.Response:
    """Event List

    

    :param jurisdiction: Filter by jurisdiction name or ID.
    :type jurisdiction: str
    :param deleted: Return events marked as deleted?
    :type deleted: bool
    :param before: Limit results to those starting before a given datetime.
    :type before: str
    :param after: Limit results to those starting before a given datetime.
    :type after: str
    :param require_bills: Limit results to events with associated bills.
    :type require_bills: bool
    :param include: Additional includes for the Event response.
    :type include: list | bytes
    :param apikey: 
    :type apikey: str
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param x_api_key: 
    :type x_api_key: str

    """
    include = [EventInclude.from_dict(d) for d in include]
    return web.Response(status=200)
