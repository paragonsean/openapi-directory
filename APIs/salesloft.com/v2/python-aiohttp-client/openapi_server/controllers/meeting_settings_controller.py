from typing import List, Dict
from aiohttp import web

from openapi_server.models.meeting_setting import MeetingSetting
from openapi_server import util


async def v2_meetings_settings_id_json_put(request: web.Request, id, allow_booking_on_behalf=None, allow_booking_overtime=None, allow_event_overlap=None, availability_limit=None, availability_limit_enabled=None, buffer_time_duration=None, calendar_type=None, default_meeting_length=None, description=None, enable_calendar_sync=None, enable_dynamic_location=None, location=None, primary_calendar_connection_failed=None, primary_calendar_id=None, primary_calendar_name=None, reschedule_meetings_enabled=None, schedule_buffer_enabled=None, schedule_delay=None, share_event_detail=None, time_zone=None, times_available=None, title=None) -> web.Response:
    """Update a meeting setting

    Updates a meeting setting, by ID only. 

    :param id: MeetingSetting ID
    :type id: str
    :param allow_booking_on_behalf: Allow other team members to schedule on you behalf.
    :type allow_booking_on_behalf: bool
    :param allow_booking_overtime: Allow team members to insert available time outside your working hours.
    :type allow_booking_overtime: bool
    :param allow_event_overlap: Allow team members to double book events on your calendar.
    :type allow_event_overlap: bool
    :param availability_limit: The number of days out the user allows a prospect to schedule a meeting
    :type availability_limit: int
    :param availability_limit_enabled: If Availability Limits have been turned on
    :type availability_limit_enabled: bool
    :param buffer_time_duration: Default buffer duration in minutes set by a user
    :type buffer_time_duration: int
    :param calendar_type: Calendar type
    :type calendar_type: str
    :param default_meeting_length: Default meeting length in minutes set by the user
    :type default_meeting_length: int
    :param description: Default description of the meeting
    :type description: str
    :param enable_calendar_sync: Determines if a user enabled Calendar Sync feature
    :type enable_calendar_sync: bool
    :param enable_dynamic_location: Determines if location will be filled via third-party service (Zoom, GoToMeeting, etc.)
    :type enable_dynamic_location: bool
    :param location: Default location of the meeting
    :type location: str
    :param primary_calendar_connection_failed: Determines if the user lost calendar connection
    :type primary_calendar_connection_failed: bool
    :param primary_calendar_id: ID of the primary calendar
    :type primary_calendar_id: str
    :param primary_calendar_name: Display name of the primary calendar
    :type primary_calendar_name: str
    :param reschedule_meetings_enabled: Determines if a user enabled reschedule meetings feature
    :type reschedule_meetings_enabled: bool
    :param schedule_buffer_enabled: Determines if meetings are scheduled with a 15 minute buffer between them
    :type schedule_buffer_enabled: bool
    :param schedule_delay: The number of hours in advance a user requires someone to a book a meeting with them
    :type schedule_delay: int
    :param share_event_detail: Allow team members to see the details of events on your calendar.
    :type share_event_detail: bool
    :param time_zone: Time zone for current calendar
    :type time_zone: str
    :param times_available: Times available set by a user that can be used to book meetings
    :type times_available: dict | bytes
    :param title: Default title of the meeting
    :type title: str

    """
    times_available = object.from_dict(times_available)
    return web.Response(status=200)
