from typing import List, Dict
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server.models.event_editable import EventEditable
from openapi_server.models.map import Map
from openapi_server import util


async def events_get(request: web.Request, timeframe_start=None, timeframe_end=None, bounds=None) -> web.Response:
    """List your own events

    List your own events.

    :param timeframe_start: Begin of time range of event (ISO 8601 date format).
    :type timeframe_start: str
    :param timeframe_end: End of time range of event (ISO 8601 date format).
    :type timeframe_end: str
    :param bounds: To refine your event index request to contain only events within                                                             a geographical box pass the followng bounds parameters.                                                             F. e. to get events within &#39;Hamburg, St. Pauli&#39;:                                                             bounds[sw_lat]&#x3D;53.54831449741324                                                             bounds[sw_lon]&#x3D;9.943227767944336                                                             bounds[ne_lat]&#x3D;53.5571103674878                                                             bounds[ne_lon]&#x3D;9.9776029586792
    :type bounds: str

    """
    return web.Response(status=200)


async def events_id_delete(request: web.Request, id) -> web.Response:
    """Delete event

    Delete event.

    :param id: Event id
    :type id: int

    """
    return web.Response(status=200)


async def events_id_get(request: web.Request, id) -> web.Response:
    """Get event

    Get basic information about an event

    :param id: Id of event
    :type id: int

    """
    return web.Response(status=200)


async def events_id_patch(request: web.Request, id, event=None) -> web.Response:
    """Update event

    Update event. Wrap event parameters in [event].

    :param id: Event id
    :type id: int
    :param event: Event attributes
    :type event: dict | bytes

    """
    event = EventEditable.from_dict(event)
    return web.Response(status=200)


async def spots_id_events_get(request: web.Request, id, timeframe_start=None, timeframe_end=None, bounds=None) -> web.Response:
    """List events for a given spot

    List maps for a given spot.

    :param id: Id of spot
    :type id: int
    :param timeframe_start: Begin of time range of event (ISO 8601 date format).
    :type timeframe_start: str
    :param timeframe_end: End of time range of event (ISO 8601 date format).
    :type timeframe_end: str
    :param bounds: To refine your event index request to contain only events within                                                             a geographical box pass the followng bounds parameters.                                                             F. e. to get events within &#39;Hamburg, St. Pauli&#39;:                                                             bounds[sw_lat]&#x3D;53.54831449741324                                                             bounds[sw_lon]&#x3D;9.943227767944336                                                             bounds[ne_lat]&#x3D;53.5571103674878                                                             bounds[ne_lon]&#x3D;9.9776029586792
    :type bounds: str

    """
    return web.Response(status=200)


async def spots_id_events_post(request: web.Request, id, event=None) -> web.Response:
    """Create event

    Create event. Wrap map parameters in [event].

    :param id: Spot id
    :type id: int
    :param event: Event attributes
    :type event: dict | bytes

    """
    event = EventEditable.from_dict(event)
    return web.Response(status=200)
