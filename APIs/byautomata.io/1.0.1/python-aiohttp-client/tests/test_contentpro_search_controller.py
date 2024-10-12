# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contentpro_search_get200_response import ContentproSearchGet200Response


pytestmark = pytest.mark.asyncio

async def test_contentpro_search_get(client):
    """Test case for contentpro_search_get

    Send search terms to receive the most relevant articles and companies.
    """
    params = [('terms', 'terms_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/contentpro-search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

