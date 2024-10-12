# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_alliances_alliance_id_contacts200_ok import GetAlliancesAllianceIdContacts200Ok
from openapi_server.models.get_alliances_alliance_id_contacts_labels200_ok import GetAlliancesAllianceIdContactsLabels200Ok
from openapi_server.models.get_characters_character_id_contacts200_ok import GetCharactersCharacterIdContacts200Ok
from openapi_server.models.get_characters_character_id_contacts_labels200_ok import GetCharactersCharacterIdContactsLabels200Ok
from openapi_server.models.get_corporations_corporation_id_contacts200_ok import GetCorporationsCorporationIdContacts200Ok
from openapi_server.models.get_corporations_corporation_id_contacts_labels200_ok import GetCorporationsCorporationIdContactsLabels200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_characters_character_id_contacts_error520 import PostCharactersCharacterIdContactsError520
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_delete_characters_character_id_contacts(client):
    """Test case for delete_characters_character_id_contacts

    Delete contacts
    """
    params = [('contact_ids', [56]),
                    ('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/latest/characters/{character_id}/contacts'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_alliances_alliance_id_contacts(client):
    """Test case for get_alliances_alliance_id_contacts

    Get alliance contacts
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
        path='/latest/alliances/{alliance_id}/contacts'.format(alliance_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_alliances_alliance_id_contacts_labels(client):
    """Test case for get_alliances_alliance_id_contacts_labels

    Get alliance contact labels
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
        path='/latest/alliances/{alliance_id}/contacts/labels'.format(alliance_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_contacts(client):
    """Test case for get_characters_character_id_contacts

    Get contacts
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
        path='/latest/characters/{character_id}/contacts'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_contacts_labels(client):
    """Test case for get_characters_character_id_contacts_labels

    Get contact labels
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
        path='/latest/characters/{character_id}/contacts/labels'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporations_corporation_id_contacts(client):
    """Test case for get_corporations_corporation_id_contacts

    Get corporation contacts
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
        path='/latest/corporations/{corporation_id}/contacts'.format(corporation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporations_corporation_id_contacts_labels(client):
    """Test case for get_corporations_corporation_id_contacts_labels

    Get corporation contact labels
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
        path='/latest/corporations/{corporation_id}/contacts/labels'.format(corporation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_characters_character_id_contacts(client):
    """Test case for post_characters_character_id_contacts

    Add contacts
    """
    contact_ids = [56]
    params = [('datasource', tranquility),
                    ('label_ids', [56]),
                    ('standing', 3.4),
                    ('token', 'token_example'),
                    ('watched', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/characters/{character_id}/contacts'.format(character_id=56),
        headers=headers,
        json=contact_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_characters_character_id_contacts(client):
    """Test case for put_characters_character_id_contacts

    Edit contacts
    """
    contact_ids = [56]
    params = [('datasource', tranquility),
                    ('label_ids', [56]),
                    ('standing', 3.4),
                    ('token', 'token_example'),
                    ('watched', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/latest/characters/{character_id}/contacts'.format(character_id=56),
        headers=headers,
        json=contact_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

