# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.publisher import Publisher


pytestmark = pytest.mark.asyncio

async def test_publisher_name_get(client):
    """Test case for publisher_name_get

    Gets publisher details
    """
    params = [('page', 'page_example'),
                    ('pageSize', 'page_size_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/publisher/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publishers_query_get(client):
    """Test case for publishers_query_get

    Search publishers
    """
    params = [('pageSize', 'page_size_example'),
                    ('page', 'page_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/publishers/{query}'.format(query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

