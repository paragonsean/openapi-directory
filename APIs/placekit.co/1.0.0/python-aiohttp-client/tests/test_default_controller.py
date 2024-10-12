# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.results import Results
from openapi_server.models.reverse_request import ReverseRequest
from openapi_server.models.search_request import SearchRequest


pytestmark = pytest.mark.asyncio

async def test_reverse(client):
    """Test case for reverse

    Reverse geocoding
    """
    payload = openapi_server.ReverseRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/reverse',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Search for addresses
    """
    payload = openapi_server.SearchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/search',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

