# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_calendar(client):
    """Test case for get_characters_character_id_calendar

    List calendar event summaries
    """
    params = [('datasource', tranquility),
                    ('from_event', 56),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/calendar'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_calendar_event_id(client):
    """Test case for get_characters_character_id_calendar_event_id

    Get an event
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/calendar/{event_id}'.format(character_id=56, event_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_calendar_event_id_attendees(client):
    """Test case for get_characters_character_id_calendar_event_id_attendees

    Get attendees
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/calendar/{event_id}/attendees'.format(character_id=56, event_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_characters_character_id_calendar_event_id(client):
    """Test case for put_characters_character_id_calendar_event_id

    Respond to an event
    """
    response = openapi_server.PutCharactersCharacterIdCalendarEventIdResponse()
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/latest/characters/{character_id}/calendar/{event_id}'.format(character_id=56, event_id=56),
        headers=headers,
        json=response,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

