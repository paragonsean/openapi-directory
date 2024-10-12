# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_fittings200_ok import GetCharactersCharacterIdFittings200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_characters_character_id_fittings_created import PostCharactersCharacterIdFittingsCreated
from openapi_server.models.post_characters_character_id_fittings_fitting import PostCharactersCharacterIdFittingsFitting
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_delete_characters_character_id_fittings_fitting_id(client):
    """Test case for delete_characters_character_id_fittings_fitting_id

    Delete fitting
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/latest/characters/{character_id}/fittings/{fitting_id}'.format(character_id=56, fitting_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_fittings(client):
    """Test case for get_characters_character_id_fittings

    Get fittings
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
        path='/latest/characters/{character_id}/fittings'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_characters_character_id_fittings(client):
    """Test case for post_characters_character_id_fittings

    Create fitting
    """
    fitting = openapi_server.PostCharactersCharacterIdFittingsFitting()
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/characters/{character_id}/fittings'.format(character_id=56),
        headers=headers,
        json=fitting,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

