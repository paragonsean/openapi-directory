# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.provider_operation_result import ProviderOperationResult


pytestmark = pytest.mark.asyncio

async def test_provider_operations_list(client):
    """Test case for provider_operations_list

    
    """
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.DevTestLab/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

