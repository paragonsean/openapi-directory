from typing import List, Dict
from aiohttp import web

from openapi_server.models.attendee_by_group import AttendeeByGroup
from openapi_server.models.group import Group
from openapi_server.models.historical_meeting_by_group import HistoricalMeetingByGroup
from openapi_server.models.history_meeting_by_group import HistoryMeetingByGroup
from openapi_server.models.organizer_by_group import OrganizerByGroup
from openapi_server.models.organizer_req import OrganizerReq
from openapi_server.models.organizer_short import OrganizerShort
from openapi_server.models.upcoming_meeting_by_group import UpcomingMeetingByGroup
from openapi_server import util


async def groups_get(request: web.Request, authorization) -> web.Response:
    """Get groups

    List all groups for an account. This API call is only available to users with the admin role.

    :param authorization: Access token
    :type authorization: str

    """
    return web.Response(status=200)


async def groups_group_key_attendees_get(request: web.Request, authorization, group_key, start_date=None, end_date=None) -> web.Response:
    """Get attendees by group

    Returns all attendees for all meetings within specified date range held by organizers within the specified group. This API call is only available to users with the admin role. This API call can be used only for groups with maximum 50 organizers.

    :param authorization: Access token
    :type authorization: str
    :param group_key: The key of the group
    :type group_key: int
    :param start_date: Start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    :type start_date: str
    :param end_date: End of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    :type end_date: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def groups_group_key_historical_meetings_get(request: web.Request, authorization, group_key, start_date, end_date) -> web.Response:
    """Get historical meetings by group

    Get historical meetings for the specified group that started within the specified date/time range. This API call is only available to users with the admin role. This API call is restricted to groups with a maximum of 50 organizers. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.

    :param authorization: Access token
    :type authorization: str
    :param group_key: The key of the group
    :type group_key: int
    :param start_date: Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    :type start_date: str
    :param end_date: Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    :type end_date: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def groups_group_key_meetings_get(request: web.Request, authorization, group_key, history, start_date, end_date) -> web.Response:
    """DEPRECATED: Get historical meetings by group

    DEPRECATED: Please use the new API calls &#39;Get historical meetings by group&#39; and &#39;Get upcoming meetings by group&#39;. Get meetings for a specified group. Additional filters can be used to view only meetings within a specified date range. This API call is only available to users with the admin role.

    :param authorization: Access token
    :type authorization: str
    :param group_key: The key of the group
    :type group_key: int
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


async def groups_group_key_organizers_get(request: web.Request, authorization, group_key) -> web.Response:
    """Get organizers by group

    Returns all the organizers within a specific group. This API call is only available to users with the admin role.

    :param authorization: Access token
    :type authorization: str
    :param group_key: The key of the group
    :type group_key: int

    """
    return web.Response(status=200)


async def groups_group_key_organizers_post(request: web.Request, authorization, group_key, body) -> web.Response:
    """Create organizer in group

    Creates a new organizer and sends an email to the email address defined in request. This API call is only available to users with the admin role. You may also pass &#39;G2W&#39; or &#39;G2T&#39; or &#39;OPENVOICE&#39; as productType variables, creating organizers for those products. A G2W or G2T organizer will also have access to G2M.

    :param authorization: Access token
    :type authorization: str
    :param group_key: The key of the group
    :type group_key: int
    :param body: The details of the organizer to be created
    :type body: dict | bytes

    """
    body = OrganizerReq.from_dict(body)
    return web.Response(status=200)


async def groups_group_key_upcoming_meetings_get(request: web.Request, authorization, group_key) -> web.Response:
    """Get upcoming meetings by group

    Get upcoming meetings for a specified group. This API call is only available to users with the admin role. This API call can be used only for groups with maximum 50 organizers.

    :param authorization: Access token
    :type authorization: str
    :param group_key: The key of the group
    :type group_key: int

    """
    return web.Response(status=200)
