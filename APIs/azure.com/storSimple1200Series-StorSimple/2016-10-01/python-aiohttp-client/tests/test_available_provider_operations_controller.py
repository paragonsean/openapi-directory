# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.available_provider_operations import AvailableProviderOperations
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_available_provider_operations_list(client):
    """Test case for available_provider_operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.StorSimple/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

