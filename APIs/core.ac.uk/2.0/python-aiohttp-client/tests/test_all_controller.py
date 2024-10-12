# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_all_response import SearchAllResponse
from openapi_server.models.search_request import SearchRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_search_post(client):
    """Test case for search_post

    Batch operation for search through all resources
    """
    body = [openapi_server.SearchRequest()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api-v2/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_query_get(client):
    """Test case for search_query_get

    Search through all resources
    """
    params = [('page', 1),
                    ('pageSize', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api-v2/search/{query}'.format(query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

