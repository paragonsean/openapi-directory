# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.package_search_result import PackageSearchResult
from openapi_server.models.search_result import SearchResult


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Searches through source code
    """
    params = [('query', 'query_example'),
                    ('match_mode', regexp)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_searchperpackage(client):
    """Test case for searchperpackage

    Like /search, but aggregates per package
    """
    params = [('query', 'query_example'),
                    ('match_mode', regexp)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/searchperpackage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

