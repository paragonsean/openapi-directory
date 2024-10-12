# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.body import Body


pytestmark = pytest.mark.asyncio

async def test_json_search_get(client):
    """Test case for json_search_get

    
    """
    params = [('text', ['text_example']),
                    ('lang', 'lang_example'),
                    ('type', stimulus),
                    ('limit', 50),
                    ('pos', ["noun","adjective","verb","adverb"]),
                    ('indent', true)]
    headers = { 
        'Accept': 'application/json',
        'internalApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/associations/v1.0/json/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_json_search_post(client):
    """Test case for json_search_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'internalApiKey': 'special-key',
    }
    data = {
        'text': ['text_example'],
        'lang': 'lang_example',
        'type': stimulus,
        'limit': 50,
        'pos': ['pos_example'],
        'indent': true
        }
    response = await client.request(
        method='POST',
        path='/associations/v1.0/json/search',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

