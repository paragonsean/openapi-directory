# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.content_json_get200_response import ContentJsonGet200Response


pytestmark = pytest.mark.asyncio

async def test_content_json_get(client):
    """Test case for content_json_get

    
    """
    params = [('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/news/v3/content.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_source_section_json_get(client):
    """Test case for content_source_section_json_get

    
    """
    params = [('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/news/v3/content/{source}/{section_jso}'.format(source='source_example', section='section_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_source_section_time_period_json_get(client):
    """Test case for content_source_section_time_period_json_get

    
    """
    params = [('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/news/v3/content/{source}/{section}/{time_period_jso}'.format(source='source_example', section='section_example', time_period=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

