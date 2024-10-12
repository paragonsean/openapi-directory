# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.maps_list_operations_default_response import MapsListOperationsDefaultResponse
from openapi_server.models.maps_operations import MapsOperations


pytestmark = pytest.mark.asyncio

async def test_maps_list_operations(client):
    """Test case for maps_list_operations

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Maps/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

