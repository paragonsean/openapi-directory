# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_search_ok import GetCharactersCharacterIdSearchOk
from openapi_server.models.get_search_ok import GetSearchOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_search(client):
    """Test case for get_characters_character_id_search

    Search on a string
    """
    params = [('categories', ['categories_example']),
                    ('datasource', tranquility),
                    ('language', en-us),
                    ('search', 'search_example'),
                    ('strict', False),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/search'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_search(client):
    """Test case for get_search

    Search on a string
    """
    params = [('categories', ['categories_example']),
                    ('datasource', tranquility),
                    ('language', en-us),
                    ('search', 'search_example'),
                    ('strict', False)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/search/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

