from typing import List, Dict
from aiohttp import web

from openapi_server.models.attendee import Attendee
from openapi_server.models.attendee_question import AttendeeQuestion
from openapi_server.models.poll import Poll
from openapi_server.models.session import Session
from openapi_server.models.session_performance import SessionPerformance
from openapi_server import util


async def get_all_sessions(request: web.Request, authorization, organizer_key, webinar_key) -> web.Response:
    """Get webinar sessions

    Retrieves details for all past sessions of a specific webinar.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int

    """
    return web.Response(status=200)


async def get_organizer_sessions(request: web.Request, authorization, organizer_key, from_time, to_time) -> web.Response:
    """Get organizer sessions

    Retrieve all completed sessions of all the webinars of a given organizer.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param from_time: A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z
    :type from_time: str
    :param to_time: A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z
    :type to_time: str

    """
    from_time = util.deserialize_datetime(from_time)
    to_time = util.deserialize_datetime(to_time)
    return web.Response(status=200)


async def get_performance(request: web.Request, authorization, organizer_key, webinar_key, session_key) -> web.Response:
    """Get session performance

    Get performance details for a session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param session_key: The key of the webinar session
    :type session_key: int

    """
    return web.Response(status=200)


async def get_polls(request: web.Request, authorization, organizer_key, webinar_key, session_key) -> web.Response:
    """Get session polls

    Retrieve all collated attendee questions and answers for polls from a specific webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param session_key: The key of the webinar session
    :type session_key: int

    """
    return web.Response(status=200)


async def get_questions(request: web.Request, authorization, organizer_key, webinar_key, session_key) -> web.Response:
    """Get session questions

    Retrieve questions and answers for a past webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param session_key: The key of the webinar session
    :type session_key: int

    """
    return web.Response(status=200)


async def get_surveys(request: web.Request, authorization, organizer_key, webinar_key, session_key) -> web.Response:
    """Get session surveys

    Retrieve surveys for a past webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param session_key: The key of the webinar session
    :type session_key: int

    """
    return web.Response(status=200)


async def get_webinar_session(request: web.Request, authorization, organizer_key, webinar_key, session_key) -> web.Response:
    """Get webinar session

    Retrieves attendance details for a specific webinar session that has ended. If attendees attended the session (&#39;registrantsAttended&#39;), specific attendance details, such as attendenceTime for a registrant, will also be retrieved. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param session_key: The key of the webinar session
    :type session_key: int

    """
    return web.Response(status=200)
