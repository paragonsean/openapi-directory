# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_killmails_recent200_ok import GetCharactersCharacterIdKillmailsRecent200Ok
from openapi_server.models.get_corporations_corporation_id_killmails_recent200_ok import GetCorporationsCorporationIdKillmailsRecent200Ok
from openapi_server.models.get_killmails_killmail_id_killmail_hash_ok import GetKillmailsKillmailIdKillmailHashOk
from openapi_server.models.get_killmails_killmail_id_killmail_hash_unprocessable_entity import GetKillmailsKillmailIdKillmailHashUnprocessableEntity
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_killmails_recent(client):
    """Test case for get_characters_character_id_killmails_recent

    Get a character's recent kills and losses
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
        path='/latest/characters/{character_id}/killmails/recent'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporations_corporation_id_killmails_recent(client):
    """Test case for get_corporations_corporation_id_killmails_recent

    Get a corporation's recent kills and losses
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
        path='/latest/corporations/{corporation_id}/killmails/recent'.format(corporation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_killmails_killmail_id_killmail_hash(client):
    """Test case for get_killmails_killmail_id_killmail_hash

    Get a single killmail
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/killmails/{killmail_id}/{killmail_hash}'.format(killmail_hash='killmail_hash_example', killmail_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

