# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_agents_research200_ok import GetCharactersCharacterIdAgentsResearch200Ok
from openapi_server.models.get_characters_character_id_blueprints200_ok import GetCharactersCharacterIdBlueprints200Ok
from openapi_server.models.get_characters_character_id_corporationhistory200_ok import GetCharactersCharacterIdCorporationhistory200Ok
from openapi_server.models.get_characters_character_id_fatigue_ok import GetCharactersCharacterIdFatigueOk
from openapi_server.models.get_characters_character_id_medals200_ok import GetCharactersCharacterIdMedals200Ok
from openapi_server.models.get_characters_character_id_not_found import GetCharactersCharacterIdNotFound
from openapi_server.models.get_characters_character_id_notifications200_ok import GetCharactersCharacterIdNotifications200Ok
from openapi_server.models.get_characters_character_id_notifications_contacts200_ok import GetCharactersCharacterIdNotificationsContacts200Ok
from openapi_server.models.get_characters_character_id_ok import GetCharactersCharacterIdOk
from openapi_server.models.get_characters_character_id_portrait_not_found import GetCharactersCharacterIdPortraitNotFound
from openapi_server.models.get_characters_character_id_portrait_ok import GetCharactersCharacterIdPortraitOk
from openapi_server.models.get_characters_character_id_roles_ok import GetCharactersCharacterIdRolesOk
from openapi_server.models.get_characters_character_id_standings200_ok import GetCharactersCharacterIdStandings200Ok
from openapi_server.models.get_characters_character_id_stats200_ok import GetCharactersCharacterIdStats200Ok
from openapi_server.models.get_characters_character_id_titles200_ok import GetCharactersCharacterIdTitles200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_characters_affiliation200_ok import PostCharactersAffiliation200Ok
from openapi_server.models.post_characters_affiliation_not_found import PostCharactersAffiliationNotFound
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id(client):
    """Test case for get_characters_character_id

    Get character's public information
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_agents_research(client):
    """Test case for get_characters_character_id_agents_research

    Get agents research
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
        path='/latest/characters/{character_id}/agents_research'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_blueprints(client):
    """Test case for get_characters_character_id_blueprints

    Get blueprints
    """
    params = [('datasource', tranquility),
                    ('page', 1),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/blueprints'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_corporationhistory(client):
    """Test case for get_characters_character_id_corporationhistory

    Get corporation history
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/corporationhistory'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_fatigue(client):
    """Test case for get_characters_character_id_fatigue

    Get jump fatigue
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
        path='/latest/characters/{character_id}/fatigue'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_medals(client):
    """Test case for get_characters_character_id_medals

    Get medals
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
        path='/latest/characters/{character_id}/medals'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_notifications(client):
    """Test case for get_characters_character_id_notifications

    Get character notifications
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
        path='/latest/characters/{character_id}/notifications'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_notifications_contacts(client):
    """Test case for get_characters_character_id_notifications_contacts

    Get new contact notifications
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
        path='/latest/characters/{character_id}/notifications/contacts'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_portrait(client):
    """Test case for get_characters_character_id_portrait

    Get character portraits
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/portrait'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_roles(client):
    """Test case for get_characters_character_id_roles

    Get character corporation roles
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
        path='/latest/characters/{character_id}/roles'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_standings(client):
    """Test case for get_characters_character_id_standings

    Get standings
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
        path='/latest/characters/{character_id}/standings'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_stats(client):
    """Test case for get_characters_character_id_stats

    Yearly aggregate stats
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
        path='/latest/characters/{character_id}/stats'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_titles(client):
    """Test case for get_characters_character_id_titles

    Get character corporation titles
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
        path='/latest/characters/{character_id}/titles'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_characters_affiliation(client):
    """Test case for post_characters_affiliation

    Character affiliation
    """
    characters = [56]
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/latest/characters/affiliation/',
        headers=headers,
        json=characters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_characters_character_id_cspa(client):
    """Test case for post_characters_character_id_cspa

    Calculate a CSPA charge cost
    """
    characters = [56]
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/characters/{character_id}/cspa'.format(character_id=56),
        headers=headers,
        json=characters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

