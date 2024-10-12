from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.event_category import EventCategory
from openapi_server.models.event_response import EventResponse
from openapi_server.models.events_list import EventsList
from openapi_server import util


async def delete_event(request: web.Request, event_id, x_anchore_account=None) -> web.Response:
    """Delete Event

    Delete an event by its event ID

    :param event_id: Event ID of the event to be deleted
    :type event_id: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def delete_events(request: web.Request, before=None, since=None, level=None, x_anchore_account=None) -> web.Response:
    """Delete Events

    Delete all or a subset of events filtered using the optional query parameters

    :param before: Delete events that occurred before the timestamp
    :type before: str
    :param since: Delete events that occurred after the timestamp
    :type since: str
    :param level: Delete events that match the level - INFO or ERROR
    :type level: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_event(request: web.Request, event_id, x_anchore_account=None) -> web.Response:
    """Get Event

    Lookup an event by its event ID

    :param event_id: Event ID of the event for lookup
    :type event_id: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def list_event_types(request: web.Request, ) -> web.Response:
    """List Event Types

    Returns list of event types in the category hierarchy


    """
    return web.Response(status=200)


async def list_events(request: web.Request, source_servicename=None, source_hostid=None, event_type=None, resource_type=None, resource_id=None, level=None, since=None, before=None, page=None, limit=None, x_anchore_account=None) -> web.Response:
    """List Events

    Returns a paginated list of events in the descending order of their occurrence. Optional query parameters may be used for filtering results

    :param source_servicename: Filter events by the originating service
    :type source_servicename: str
    :param source_hostid: Filter events by the originating host ID
    :type source_hostid: str
    :param event_type: Filter events by a prefix match on the event type (e.g. \&quot;user.image.\&quot;)
    :type event_type: str
    :param resource_type: Filter events by the type of resource - tag, imageDigest, repository etc
    :type resource_type: str
    :param resource_id: Filter events by the id of the resource
    :type resource_id: str
    :param level: Filter events by the level - INFO or ERROR
    :type level: str
    :param since: Return events that occurred after the timestamp
    :type since: str
    :param before: Return events that occurred before the timestamp
    :type before: str
    :param page: Pagination controls - return the nth page of results. Defaults to first page if left empty
    :type page: int
    :param limit: Number of events in the result set. Defaults to 100 if left empty
    :type limit: int
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)
