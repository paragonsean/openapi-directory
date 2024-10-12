# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_get200_response import SearchGet200Response


pytestmark = pytest.mark.asyncio

async def test_search_get(client):
    """Test case for search_get

    Send search terms to receive the most relevant companies along with text snippets.
    """
    params = [('terms', 'terms_example'),
                    ('page', '0')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

