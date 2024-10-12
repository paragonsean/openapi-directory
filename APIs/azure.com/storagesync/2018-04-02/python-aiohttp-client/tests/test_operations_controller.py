# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation_entity_list_result import OperationEntityListResult
from openapi_server.models.storage_sync_error import StorageSyncError


pytestmark = pytest.mark.asyncio

async def test_operations_list_0(client):
    """Test case for operations_list_0

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.StorageSync/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

