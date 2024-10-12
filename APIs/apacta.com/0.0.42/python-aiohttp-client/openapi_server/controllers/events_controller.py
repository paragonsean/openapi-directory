from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.events_event_id_get200_response import EventsEventIdGet200Response
from openapi_server.models.events_get200_response import EventsGet200Response
from openapi_server.models.events_is_user_free_get200_response import EventsIsUserFreeGet200Response
from openapi_server.models.events_post_request import EventsPostRequest
from openapi_server import util


async def events_event_id_delete(request: web.Request, event_id) -> web.Response:
    """Delete event

    

    :param event_id: 
    :type event_id: str

    """
    return web.Response(status=200)


async def events_event_id_get(request: web.Request, event_id) -> web.Response:
    """Show event

    

    :param event_id: 
    :type event_id: str

    """
    return web.Response(status=200)


async def events_event_id_put(request: web.Request, event_id) -> web.Response:
    """Edit event

    

    :param event_id: 
    :type event_id: str

    """
    return web.Response(status=200)


async def events_get(request: web.Request, user_id=None, project_id=None, start_gt=None, start_lt=None, start_eq=None, end_gt=None, end_lt=None, end_eq=None, tags=None, without_users=None) -> web.Response:
    """Show list of events

    

    :param user_id: 
    :type user_id: str
    :type user_id: str
    :param project_id: 
    :type project_id: str
    :type project_id: str
    :param start_gt: 
    :type start_gt: str
    :param start_lt: 
    :type start_lt: str
    :param start_eq: 
    :type start_eq: str
    :param end_gt: 
    :type end_gt: str
    :param end_lt: 
    :type end_lt: str
    :param end_eq: 
    :type end_eq: str
    :param tags: List events with given tag ids separated by comma. Example tags&#x3D;0377d6ce-db5e-4b1e-ac3a-8ca39ea3142e,8cec327e-a559-4b40-9ed6-316b9de46743
    :type tags: str
    :param without_users: List events without attached user
    :type without_users: bool

    """
    return web.Response(status=200)


async def events_is_user_free_get(request: web.Request, user_id, start, end) -> web.Response:
    """Check if user is available at given datetime range

    

    :param user_id: 
    :type user_id: str
    :type user_id: str
    :param start: 
    :type start: str
    :param end: 
    :type end: str

    """
    return web.Response(status=200)


async def events_post(request: web.Request, body=None) -> web.Response:
    """Create event

    

    :param body: 
    :type body: dict | bytes

    """
    body = EventsPostRequest.from_dict(body)
    return web.Response(status=200)
