# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_root200_response import GetRoot200Response


pytestmark = pytest.mark.asyncio

async def test_get_root(client):
    """Test case for get_root

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

