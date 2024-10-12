from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_input import EventInput
from openapi_server.models.eventcreateresponse import Eventcreateresponse
from openapi_server.models.eventresponse import Eventresponse
from openapi_server.models.events import Events
from openapi_server import util


async def create_event(request: web.Request, vestorly_auth, event, access_token=None) -> web.Response:
    """create_event

    Creates a new event in the system

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param event: Event
    :type event: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    event = EventInput.from_dict(event)
    return web.Response(status=200)


async def find_event_by_id(request: web.Request, id, vestorly_auth, access_token=None) -> web.Response:
    """find_event_by_id

    Returns a single event if the user has access

    :param id: Mongo ID of event to fetch
    :type id: str
    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def find_events(request: web.Request, vestorly_auth, access_token=None) -> web.Response:
    """find_events

    Returns all events

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)
