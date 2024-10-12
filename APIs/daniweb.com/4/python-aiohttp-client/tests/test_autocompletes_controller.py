# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.endpoint_get_autocompletes import EndpointGetAutocompletes


pytestmark = pytest.mark.asyncio

async def test_autocompletes_get(client):
    """Test case for autocompletes_get

    
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/autocompletes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

