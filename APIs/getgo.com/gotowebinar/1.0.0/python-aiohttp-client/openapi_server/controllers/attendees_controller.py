from typing import List, Dict
from aiohttp import web

from openapi_server.models.attendee import Attendee
from openapi_server.models.attendee_question import AttendeeQuestion
from openapi_server.models.poll_answer import PollAnswer
from openapi_server.models.registrant import Registrant
from openapi_server import util


async def get_attendee(request: web.Request, authorization, organizer_key, webinar_key, session_key, registrant_key) -> web.Response:
    """Get attendee

    Retrieve registration details for a particular attendee of a specific webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param session_key: The key of the webinar session
    :type session_key: int
    :param registrant_key: The key of the registrant
    :type registrant_key: int

    """
    return web.Response(status=200)


async def get_attendee_poll_answers(request: web.Request, authorization, organizer_key, webinar_key, session_key, registrant_key) -> web.Response:
    """Get attendee poll answers

    Get poll answers from a particular attendee of a specific webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param session_key: The key of the webinar session
    :type session_key: int
    :param registrant_key: The key of the registrant
    :type registrant_key: int

    """
    return web.Response(status=200)


async def get_attendee_questions(request: web.Request, authorization, organizer_key, webinar_key, session_key, registrant_key) -> web.Response:
    """Get attendee questions

    Get questions asked by an attendee during a webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param session_key: The key of the webinar session
    :type session_key: int
    :param registrant_key: The key of the registrant
    :type registrant_key: int

    """
    return web.Response(status=200)


async def get_attendee_survey_answers(request: web.Request, authorization, organizer_key, webinar_key, session_key, registrant_key) -> web.Response:
    """Get attendee survey answers

    Retrieve survey answers from a particular attendee during a webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param session_key: The key of the webinar session
    :type session_key: int
    :param registrant_key: The key of the registrant
    :type registrant_key: int

    """
    return web.Response(status=200)


async def get_attendees(request: web.Request, authorization, organizer_key, webinar_key, session_key) -> web.Response:
    """Get session attendees

    Retrieve details for all attendees of a specific webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

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
