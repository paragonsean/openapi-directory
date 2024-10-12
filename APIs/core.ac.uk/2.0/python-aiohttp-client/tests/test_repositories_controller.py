# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.repository_response import RepositoryResponse
from openapi_server.models.repository_search_response import RepositorySearchResponse
from openapi_server.models.search_request import SearchRequest


pytestmark = pytest.mark.asyncio

async def test_get_repository_by_id(client):
    """Test case for get_repository_by_id

    Get repository by CORE repository ID
    """
    params = [('stats', False),
                    ('depositHistory', False),
                    ('depositHistoryCumulative', False)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api-v2/repositories/get/{repository_id}'.format(repository_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_repository_by_id_batch(client):
    """Test case for get_repository_by_id_batch

    Batch operation for retrieving repositories by CORE repository ID
    """
    body = [56]
    params = [('stats', False),
                    ('depositHistory', False),
                    ('depositHistoryCumulative', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api-v2/repositories/get',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_repositories_search_post(client):
    """Test case for repositories_search_post

    Batch operation for searching through repositories
    """
    body = [openapi_server.SearchRequest()]
    params = [('stats', False),
                    ('depositHistory', False),
                    ('depositHistoryCumulative', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api-v2/repositories/search',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repositories_search_query_get(client):
    """Test case for repositories_search_query_get

    Search through all repositories
    """
    params = [('page', 1),
                    ('pageSize', 10),
                    ('stats', False),
                    ('depositHistory', False),
                    ('depositHistoryCumulative', False)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api-v2/repositories/search/{query}'.format(query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

