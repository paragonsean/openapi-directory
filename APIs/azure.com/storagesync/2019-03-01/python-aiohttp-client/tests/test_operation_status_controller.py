# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.storage_sync_error import StorageSyncError


pytestmark = pytest.mark.asyncio

async def test_operation_status_get(client):
    """Test case for operation_status_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/locations/{location_name}/workflows/{workflow_id}/operations/{operation_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location_name='location_name_example', workflow_id='workflow_id_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

