from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.event import Event
from openapi_server.models.events_count import EventsCount
from openapi_server import util


async def get_event(request: web.Request, id) -> web.Response:
    """Get event

    

    :param id: Unique identifier of the event
    :type id: str

    """
    return web.Response(status=200)


async def get_events_count(request: web.Request, from_date=None, to_date=None, direction=None, states=None) -> web.Response:
    """Get events count

    

    :param from_date: Return events that occurred after this point in time
    :type from_date: int
    :param to_date: Return events that occurred before this point in time
    :type to_date: int
    :param direction: Filter by event direction
    :type direction: str
    :param states: Filter events by state
    :type states: str

    """
    return web.Response(status=200)


async def list_events(request: web.Request, types=None, from_date=None, to_date=None, direction=None, states=None, offset=None, size=None, order=None, sort=None) -> web.Response:
    """List events

    

    :param types: Record type
    :type types: str
    :param from_date: Return events that occurred after this point in time
    :type from_date: int
    :param to_date: Return events that occurred before this point in time
    :type to_date: int
    :param direction: Filter by event direction
    :type direction: str
    :param states: Filter events by state
    :type states: str
    :param offset: Page number of events to return
    :type offset: int
    :param size: Return this amount of events in the response
    :type size: int
    :param order: Sort in either ascending or descending order&#39;
    :type order: str
    :param sort: Sort events by property
    :type sort: str

    """
    return web.Response(status=200)
