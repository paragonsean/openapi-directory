from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_calendar_event_request import CreateCalendarEventRequest
from openapi_server.models.create_calendar_event_response import CreateCalendarEventResponse
from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.fetch_calendar_event_response import FetchCalendarEventResponse
from openapi_server.models.fetch_calendar_events_response import FetchCalendarEventsResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.update_calendar_event_request import UpdateCalendarEventRequest
from openapi_server.models.update_calendar_event_response import UpdateCalendarEventResponse
from openapi_server import util


async def create_calendar_event(request: web.Request, body) -> web.Response:
    """Create calendar event

    Create a calendar event for a patient. Attribute &#x60;all_day&#x60; must be set to &#x60;true&#x60; and &#x60;end_at&#x60; cannot be set for &#x60;plan-check-in&#x60; event type.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateCalendarEventRequest.from_dict(body)
    return web.Response(status=200)


async def delete_calendar_event(request: web.Request, id) -> web.Response:
    """Delete a calendar event

    Delete a calendar event by id

    :param id: Calendar event identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_calendar_event(request: web.Request, id) -> web.Response:
    """Get a calendar event

    Get a calendar event by id

    :param id: Calendar event identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_calendar_events(request: web.Request, filter_patient=None, filter_groups=None, filter_organization=None, filter_attendees=None, filter_type=None, filter_completed=None, filter_start_at=None, filter_end_at=None, filter_completed_at=None, filter_created_at=None, filter_updated_at=None, page_number=None, page_size=None, page_limit=None, page_cursor=None, include=None) -> web.Response:
    """List calendar events

    Get a list of calendar events

    :param filter_patient: Patient id to fetch calendar event. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, &#x60;filter[organization]&#x60;, or &#x60;filter[attendees]&#x60;. 
    :type filter_patient: str
    :param filter_groups: Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, &#x60;filter[organization]&#x60;, or &#x60;filter[attendees]&#x60;. 
    :type filter_groups: str
    :param filter_organization: Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, &#x60;filter[organization]&#x60;, or &#x60;filter[attendees]&#x60;. 
    :type filter_organization: str
    :param filter_attendees: Comma-separated list of coach or patient ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, &#x60;filter[organization]&#x60;, or &#x60;filter[attendees]&#x60;. 
    :type filter_attendees: str
    :param filter_type: Calendar event type
    :type filter_type: str
    :param filter_completed: If not specified, return all calendar events. If set to &#x60;true&#x60; return only events marked as completed, if set to &#x60;false&#x60;, return only events not marked as completed yet.
    :type filter_completed: bool
    :param filter_start_at: The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for events starting in November 2017 (America/New_York): &#x60;filter[start_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60; 
    :type filter_start_at: str
    :param filter_end_at: The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for events ending in November 2017 (America/New_York): &#x60;filter[end_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60; 
    :type filter_end_at: str
    :param filter_completed_at: The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for events completed in November 2017 (America/New_York): &#x60;filter[completed_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60; 
    :type filter_completed_at: str
    :param filter_created_at: The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for events created in November 2017 (America/New_York): &#x60;filter[created_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60; 
    :type filter_created_at: str
    :param filter_updated_at: The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for events updated in November 2017 (America/New_York): &#x60;filter[updated_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60; 
    :type filter_updated_at: str
    :param page_number: Page number
    :type page_number: int
    :param page_size: Page size
    :type page_size: int
    :param page_limit: Page limit
    :type page_limit: int
    :param page_cursor: Page cursor
    :type page_cursor: str
    :param include: List of related resources to include in the response
    :type include: str

    """
    return web.Response(status=200)


async def update_calendar_event(request: web.Request, id, body) -> web.Response:
    """Update a calendar event

    Update a calendar event for a patient. Attribute &#x60;all_day&#x60; must be true and &#x60;end_at&#x60; cannot be specified for &#x60;plan-check-in&#x60; event type. To mark a calendar event as &#39;completed&#39;, set &#x60;completed_at&#x60; and &#x60;completed_by&#x60; to desired values.  To mark a completed calendar event as &#39;not completed&#39;, set &#x60;completed_at&#x60; and &#x60;completed_by&#x60; to &#x60;null&#x60;. Attendees can be added or removed, but response status cannot be updated. Use the calendar event response api for response status updates instead.

    :param id: Calendar event identifier
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateCalendarEventRequest.from_dict(body)
    return web.Response(status=200)
