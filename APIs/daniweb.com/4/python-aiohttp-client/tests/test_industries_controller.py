# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.endpoint_get_industries import EndpointGetIndustries


pytestmark = pytest.mark.asyncio

async def test_industries_get(client):
    """Test case for industries_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/industries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

