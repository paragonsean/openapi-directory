from typing import List, Dict
from aiohttp import web

from openapi_server.models.attendee_by_organizer import AttendeeByOrganizer
from openapi_server.models.historical_meeting import HistoricalMeeting
from openapi_server.models.meeting_by_organizer import MeetingByOrganizer
from openapi_server.models.organizer import Organizer
from openapi_server.models.organizer_req import OrganizerReq
from openapi_server.models.organizer_short import OrganizerShort
from openapi_server.models.organizer_status import OrganizerStatus
from openapi_server.models.upcoming_meeting import UpcomingMeeting
from openapi_server import util


async def organizers_delete(request: web.Request, authorization, email) -> web.Response:
    """Delete organizer by email

    Deletes the individual organizer specified by the email address. This API call is only available to users with the admin role.

    :param authorization: Access token
    :type authorization: str
    :param email: The email address of the organizer
    :type email: str

    """
    return web.Response(status=200)


async def organizers_get(request: web.Request, authorization, email=None) -> web.Response:
    """Get organizer by email / Get all organizers

    Gets the individual organizer specified by the organizer&#39;s email address. If an email address is not specified, all organizers are returned. This API call is only available to users with the admin role.

    :param authorization: Access token
    :type authorization: str
    :param email: The email address of the organizer
    :type email: str

    """
    return web.Response(status=200)


async def organizers_organizer_key_attendees_get(request: web.Request, authorization, organizer_key, start_date, end_date) -> web.Response:
    """Get attendees by organizer

    Lists all attendees for all meetings within a specified date range for a specified organizer. This API call is only available to users with the admin role.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param start_date: A required start of date range in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    :type start_date: str
    :param end_date: A required end of date range in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    :type end_date: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def organizers_organizer_key_delete(request: web.Request, authorization, organizer_key) -> web.Response:
    """Delete organizer

    Deletes the individual organizer specified by the organizer key. This API call is only available to users with the admin role.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int

    """
    return web.Response(status=200)


async def organizers_organizer_key_get(request: web.Request, authorization, organizer_key) -> web.Response:
    """Get organizer

    Returns the individual organizer specified by the key. This API call is only available to users with the admin role. Non-admin users can only make this call for their own organizerKey.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int

    """
    return web.Response(status=200)


async def organizers_organizer_key_historical_meetings_get(request: web.Request, authorization, organizer_key, start_date, end_date) -> web.Response:
    """Get historical meetings by organizer

    Get historical meetings for the specified organizer that started within the specified date/time range. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param start_date: Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    :type start_date: str
    :param end_date: Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    :type end_date: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def organizers_organizer_key_meetings_get(request: web.Request, authorization, organizer_key, scheduled=None, history=None, start_date=None, end_date=None) -> web.Response:
    """DEPRECATED: Get meetings by organizer

    DEPRECATED: Please use the new API calls &#39;Get historical meetings by organizer&#39; and &#39;Get upcoming meetings by organizer&#39;. Gets future (scheduled) or past (history) meetings for a specified organizer. Include &#39;history&#x3D;true&#39; and the past start and end dates in the URL to retrieve past meetings. Enter &#39;scheduled&#x3D;true&#39; (without dates) to get scheduled meetings.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param scheduled: When &#39;true&#39;, returns all future meetings. Date range not supported.
    :type scheduled: bool
    :param history: When &#39;true&#39;, returns all past meetings within date range
    :type history: bool
    :param start_date: If history is &#39;true&#39;, required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    :type start_date: str
    :param end_date: If history is &#39;true&#39;, required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    :type end_date: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def organizers_organizer_key_put(request: web.Request, authorization, organizer_key, body) -> web.Response:
    """Update organizer

    Updates the products of the specified organizer. To add a product (G2M, G2W, G2T, OPENVOICE) for the organizer, the call must be sent once for each product you want to add. To remove all products for the organizer, set status to &#39;suspended&#39;. The call is limited to users with the admin role.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param body: The organizer&#39;s status
    :type body: dict | bytes

    """
    body = OrganizerStatus.from_dict(body)
    return web.Response(status=200)


async def organizers_organizer_key_upcoming_meetings_get(request: web.Request, authorization, organizer_key) -> web.Response:
    """Get upcoming meetings by organizer

    Get upcoming meetings for a specified organizer. This API call is only available to users with the admin role.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int

    """
    return web.Response(status=200)


async def organizers_post(request: web.Request, authorization, body) -> web.Response:
    """Create organizer

    Creates a new organizer and sends an email to the email address defined in the request. This API call is only available to users with the admin role. You may also pass &#39;G2W&#39; or &#39;G2T&#39; or &#39;OPENVOICE&#39; as productType variables, creating organizers for those products. A G2W or G2T organizer will also have access to G2M.

    :param authorization: Access token
    :type authorization: str
    :param body: The details of the organizer to be created
    :type body: dict | bytes

    """
    body = OrganizerReq.from_dict(body)
    return web.Response(status=200)
