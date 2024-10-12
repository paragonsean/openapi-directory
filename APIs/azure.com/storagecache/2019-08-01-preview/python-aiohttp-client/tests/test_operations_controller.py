# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_operation_list_result import ApiOperationListResult
from openapi_server.models.cloud_error import CloudError


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.StorageCache/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

