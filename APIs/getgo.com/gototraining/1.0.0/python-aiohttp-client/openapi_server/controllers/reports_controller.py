from typing import List, Dict
from aiohttp import web

from openapi_server.models.attendee import Attendee
from openapi_server.models.date_time_range import DateTimeRange
from openapi_server.models.session import Session
from openapi_server import util


async def get_attendance_details(request: web.Request, authorization, organizer_key, session_key) -> web.Response:
    """Get Attendance Details

    This call retrieves a list of registrants from a specific completed training session. The response includes the registrants&#39; email addresses, and if they attended, it includes the duration of each period of their attendance in minutes, and the times at which they joined and left. If a registrant does not attend, they appear at the bottom of the listing with timeInSession &#x3D; 0.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param session_key: The key of the training session
    :type session_key: int

    """
    return web.Response(status=200)


async def get_session_details_for_date_range(request: web.Request, authorization, organizer_key, body) -> web.Response:
    """Get Sessions by Date Range

    This call returns all session details over a given date range for a given organizer. A session is a completed training event.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param body: The start and end times for the time range over which to retrieve training sessions
    :type body: dict | bytes

    """
    body = DateTimeRange.from_dict(body)
    return web.Response(status=200)


async def get_session_details_for_training(request: web.Request, authorization, organizer_key, training_key) -> web.Response:
    """Get Sessions By Training

    This call returns session details for a given training. A session is a completed training event. Each training may contain one or more sessions.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int

    """
    return web.Response(status=200)
