# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.the_root_schema import TheRootSchema


pytestmark = pytest.mark.asyncio

async def test_auto_complete(client):
    """Test case for auto_complete

    Product Search Autocomplete
    """
    params = [('productNameContains', 'jeans')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/buscaautocomplete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

