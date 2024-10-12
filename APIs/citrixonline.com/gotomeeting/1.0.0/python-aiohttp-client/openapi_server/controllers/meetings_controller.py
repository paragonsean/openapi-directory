from typing import List, Dict
from aiohttp import web

from openapi_server.models.attendee_by_meeting import AttendeeByMeeting
from openapi_server.models.historical_meeting import HistoricalMeeting
from openapi_server.models.meeting_by_id import MeetingById
from openapi_server.models.meeting_created import MeetingCreated
from openapi_server.models.meeting_history import MeetingHistory
from openapi_server.models.meeting_req_create import MeetingReqCreate
from openapi_server.models.meeting_req_update import MeetingReqUpdate
from openapi_server.models.start_url import StartUrl
from openapi_server.models.upcoming_meeting import UpcomingMeeting
from openapi_server import util


async def historical_meetings_get(request: web.Request, authorization, start_date, end_date) -> web.Response:
    """Get historical meetings

    Get historical meetings for the currently authenticated organizer that started within the specified date/time range. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.

    :param authorization: Access token
    :type authorization: str
    :param start_date: Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    :type start_date: str
    :param end_date: Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    :type end_date: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def meetings_get(request: web.Request, authorization, history=None, start_date=None, end_date=None) -> web.Response:
    """DEPRECATED: Get historical meetings

    DEPRECATED: Please use the new API calls &#39;Get historical meetings&#39; and &#39;Get upcoming meetings&#39;.  Gets historical meetings for the current authenticated organizer. Requires date range for filtering results to only meetings within specified dates. History searches will contain the parameter &#39;meetingInstanceKey&#39; which is used in conjunction with the call &#39;Get Attendees by Meeting&#39; to get attendee information for a past meeting.

    :param authorization: Access token
    :type authorization: str
    :param history: When &#39;true&#39;, returns all past meetings within date range
    :type history: bool
    :param start_date: If history&#x3D;true, required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    :type start_date: str
    :param end_date: If history&#x3D;true, required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    :type end_date: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def meetings_meeting_id_attendees_get(request: web.Request, authorization, meeting_id) -> web.Response:
    """Get attendees by meeting

    List all attendees for specified meetingId of historical meeting. The historical meetings can be fetched using &#39;Get historical meetings&#39;, &#39;Get historical meetings by organizer&#39;, and &#39;Get historical meetings by group&#39;. For users with the admin role this call returns attendees for any meeting. For any other user the call will return attendees for meetings on which the user is a valid organizer.

    :param authorization: Access token
    :type authorization: str
    :param meeting_id: The meeting ID
    :type meeting_id: int

    """
    return web.Response(status=200)


async def meetings_meeting_id_delete(request: web.Request, authorization, meeting_id) -> web.Response:
    """Delete meeting

    Deletes the meeting identified by the meetingId.

    :param authorization: Access token
    :type authorization: str
    :param meeting_id: The meeting ID
    :type meeting_id: int

    """
    return web.Response(status=200)


async def meetings_meeting_id_get(request: web.Request, authorization, meeting_id) -> web.Response:
    """Get meeting

    Returns the meeting details for the specified meeting.

    :param authorization: Access token
    :type authorization: str
    :param meeting_id: The meeting ID
    :type meeting_id: int

    """
    return web.Response(status=200)


async def meetings_meeting_id_put(request: web.Request, authorization, meeting_id, body) -> web.Response:
    """Update meeting

    Updates an existing meeting specified by meetingId.

    :param authorization: Access token
    :type authorization: str
    :param meeting_id: The meeting ID
    :type meeting_id: int
    :param body: The meeting details
    :type body: dict | bytes

    """
    body = MeetingReqUpdate.from_dict(body)
    return web.Response(status=200)


async def meetings_meeting_id_start_get(request: web.Request, authorization, meeting_id) -> web.Response:
    """Start meeting

    Returns a host URL that can be used to start a meeting. When this URL is opened in a web browser, the GoToMeeting client will be downloaded and launched and the meeting will start. The end user is not required to login to a client.

    :param authorization: Access token
    :type authorization: str
    :param meeting_id: The meeting ID
    :type meeting_id: int

    """
    return web.Response(status=200)


async def meetings_post(request: web.Request, authorization, body) -> web.Response:
    """Create meeting

    Create a new meeting based on the parameters specified.

    :param authorization: Access token
    :type authorization: str
    :param body: The meeting details
    :type body: dict | bytes

    """
    body = MeetingReqCreate.from_dict(body)
    return web.Response(status=200)


async def upcoming_meetings_get(request: web.Request, authorization) -> web.Response:
    """Get upcoming meetings

    Gets upcoming meetings for the current authenticated organizer.

    :param authorization: Access token
    :type authorization: str

    """
    return web.Response(status=200)
