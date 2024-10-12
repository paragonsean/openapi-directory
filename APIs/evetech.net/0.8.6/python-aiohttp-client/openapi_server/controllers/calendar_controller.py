from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_calendar200_ok import GetCharactersCharacterIdCalendar200Ok
from openapi_server.models.get_characters_character_id_calendar_event_id_attendees200_ok import GetCharactersCharacterIdCalendarEventIdAttendees200Ok
from openapi_server.models.get_characters_character_id_calendar_event_id_attendees_not_found import GetCharactersCharacterIdCalendarEventIdAttendeesNotFound
from openapi_server.models.get_characters_character_id_calendar_event_id_not_found import GetCharactersCharacterIdCalendarEventIdNotFound
from openapi_server.models.get_characters_character_id_calendar_event_id_ok import GetCharactersCharacterIdCalendarEventIdOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.put_characters_character_id_calendar_event_id_response import PutCharactersCharacterIdCalendarEventIdResponse
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_characters_character_id_calendar(request: web.Request, character_id, datasource=None, from_event=None, if_none_match=None, token=None) -> web.Response:
    """List calendar event summaries

    Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event  --- Alternate route: &#x60;/dev/characters/{character_id}/calendar/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/calendar/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/calendar/&#x60;  --- This route is cached for up to 5 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param from_event: The event ID to retrieve events from
    :type from_event: int
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_calendar_event_id(request: web.Request, character_id, event_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get an event

    Get all the information for a specific event  --- Alternate route: &#x60;/dev/characters/{character_id}/calendar/{event_id}/&#x60;  Alternate route: &#x60;/v3/characters/{character_id}/calendar/{event_id}/&#x60;  --- This route is cached for up to 5 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param event_id: The id of the event requested
    :type event_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_calendar_event_id_attendees(request: web.Request, character_id, event_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get attendees

    Get all invited attendees for a given event  --- Alternate route: &#x60;/dev/characters/{character_id}/calendar/{event_id}/attendees/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/calendar/{event_id}/attendees/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/calendar/{event_id}/attendees/&#x60;  --- This route is cached for up to 600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param event_id: The id of the event requested
    :type event_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def put_characters_character_id_calendar_event_id(request: web.Request, character_id, event_id, response, datasource=None, token=None) -> web.Response:
    """Respond to an event

    Set your response status to an event  --- Alternate route: &#x60;/dev/characters/{character_id}/calendar/{event_id}/&#x60;  Alternate route: &#x60;/v3/characters/{character_id}/calendar/{event_id}/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param event_id: The ID of the event requested
    :type event_id: int
    :param response: The response value to set, overriding current value
    :type response: dict | bytes
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    response = PutCharactersCharacterIdCalendarEventIdResponse.from_dict(response)
    return web.Response(status=200)
