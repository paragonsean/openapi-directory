# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_get200_response import SearchGet200Response


pytestmark = pytest.mark.asyncio

async def test_search_get(client):
    """Test case for search_get

    List all company ESG Ratings
    """
    params = [('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/prod/authorization/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

