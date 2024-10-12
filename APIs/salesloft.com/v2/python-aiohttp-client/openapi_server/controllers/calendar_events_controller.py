from typing import List, Dict
from aiohttp import web

from openapi_server.models.calendar_event import CalendarEvent
from openapi_server import util


async def v2_calendar_events_get(request: web.Request, per_page=None, page=None, include_paging_counts=None, sort_by=None, sort_direction=None, start_time=None, end_time=None, user_guid=None, calendar_id=None) -> web.Response:
    """List calendar events

    Returns all calendar events, paginated and filtered by the date.

    :param per_page: How many records to show per page in the range [1, 100]. Defaults to 25
    :type per_page: int
    :param page: The current page to fetch results from. Defaults to 1
    :type page: int
    :param include_paging_counts: Whether to include total_pages and total_count in the metadata. Defaults to false
    :type include_paging_counts: bool
    :param sort_by: Key to sort on, must be one of: start_time. Defaults to start_time
    :type sort_by: str
    :param sort_direction: Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    :type sort_direction: str
    :param start_time: Lower bound (inclusive) for a calendar event&#39;s end time to filter by. Must be in ISO 8601 format.  Example: &#x60;2022-02-14T10:12:59+00:00&#x60;. 
    :type start_time: str
    :param end_time: Upper bound (exclusive) for a calendar event&#39;s start time to filter by. Must be in ISO 8601 format.  Example: &#x60;2022-02-14T10:12:59+00:00&#x60;. 
    :type end_time: str
    :param user_guid: user_guid of the user who created or included as a guest to the event. 
    :type user_guid: str
    :param calendar_id: calendar_id of the user who created or included as a guest to the event. 
    :type calendar_id: str

    """
    return web.Response(status=200)


async def v2_calendar_events_upsert_post(request: web.Request, calendar_id, end_time, i_cal_uid, id, start_time, all_day=None, attendees=None, canceled_at=None, description=None, location=None, organizer=None, recurring=None, status=None, title=None, updated_at=None) -> web.Response:
    """Upsert a calendar event

      Upserts a calendar event object.   Upsert key is a combination of &#x60;id&#x60; and &#x60;i_cal_uid&#x60; scoped to the given &#x60;calendar_id&#x60;.   Bulk operations:   This endpoint is used for bulk operations, see https://developers.salesloft.com/bulk.html for integration instructions.   Use &#x60;calendar/events/upsert&#x60; as an event type, and this spec as a data spec.   This endpoint should be used directly for the time sensitive calendar event updates. 

    :param calendar_id:   Calendar ID of the calendar event owner.   For the External Calendar connection use &#x60;external_{salesloft_user_guid}&#x60; format.   Example: &#x60;external_00210d1a-df8a-459f-af75-89b953b618b0&#x60;. 
    :type calendar_id: str
    :param end_time:   End time of the calendar event, as a combined date-time value in the ISO 8601 format with a time zone offset.   Example: &#x60;2022-02-14T10:12:59+00:00&#x60;. 
    :type end_time: str
    :param i_cal_uid:   icalUID of the calendar event. Unique identifier for a calendar event across calendars.    Used as an upsert key. 
    :type i_cal_uid: str
    :param id:   Id of the calendar event, different for each occurrence in a recurring series.    Used as an upsert key. 
    :type id: str
    :param start_time:   Start time of the calendar event, as a combined date-time value in the ISO 8601 format with a time zone offset.   Example: &#x60;2022-02-14T10:12:59+00:00&#x60;. 
    :type start_time: str
    :param all_day: Should be set to &#x60;true&#x60; for all day calendar events.
    :type all_day: bool
    :param attendees:   List of attendees of the calendar event.   Example:   &#x60;&#x60;&#x60;     {       ...       \\\&quot;attendees\\\&quot;: [         {           \\\&quot;name\\\&quot;: \\\&quot;Alice\\\&quot;,           \\\&quot;email\\\&quot;: \\\&quot;alice@example.com\\\&quot;,           \\\&quot;status\\\&quot;: \\\&quot;accepted\\\&quot;,           \\\&quot;organizer\\\&quot;: true         },         {           \\\&quot;name\\\&quot;: \\\&quot;Bob\\\&quot;,           \\\&quot;email\\\&quot;: \\\&quot;bob@example.com\\\&quot;,           \\\&quot;status\\\&quot;: \\\&quot;needsAction\\\&quot;,           \\\&quot;organizer\\\&quot;: false         }       ]     }   &#x60;&#x60;&#x60;   &#x60;name&#x60;: full name of the attendee    &#x60;email&#x60;: email address of the attendee    &#x60;status&#x60;: one of the following - needsAction, accepted, tentative, declined    &#x60;organizer&#x60;: whether the attendee is the organizer of the calendar event 
    :type attendees: dict | bytes
    :param canceled_at:   Cancellation time of the calendar event, as a combined date-time value in the ISO 8601 format with a time zone offset.   Example: &#x60;2022-02-14T10:12:59+00:00&#x60;. 
    :type canceled_at: str
    :param description: Description of the calendar event
    :type description: str
    :param location: Location of the calendar event as free-form text.
    :type location: str
    :param organizer:   Email address of the organizer 
    :type organizer: str
    :param recurring: Should be set to &#x60;true&#x60; if this is one of recurring series calendar event.
    :type recurring: bool
    :param status:   Status of the calendar event. Depending on the status, the calendar event will or will not impact user&#39;s availability.   Possible values: &#x60;confirmed&#x60;, &#x60;tentative&#x60;, &#x60;cancelled&#x60;.   Example: &#x60;confirmed&#x60;. 
    :type status: str
    :param title: Title of the calendar event
    :type title: str
    :param updated_at:   Last modification time of the event in the ISO 8601 format with a time zone offset. The event will not be updated if the &#39;updated_at&#39; timestamp from the payload is earlier than the one in the database.   Example: &#x60;2022-02-14T10:12:59+00:00&#x60;. 
    :type updated_at: str

    """
    end_time = util.deserialize_date(end_time)
    start_time = util.deserialize_date(start_time)
    attendees = object.from_dict(attendees)
    return web.Response(status=200)
