# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.territories_response import TerritoriesResponse


pytestmark = pytest.mark.asyncio

async def test_territories_get_collection(client):
    """Test case for territories_get_collection

    
    """
    params = [('fields[territories]', ['fields_territories_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/territories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

