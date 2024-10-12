# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server.models.trigger_change_detection_parameters import TriggerChangeDetectionParameters


pytestmark = pytest.mark.asyncio

async def test_cloud_endpoints_trigger_change_detection_1(client):
    """Test case for cloud_endpoints_trigger_change_detection_1

    
    """
    parameters = {"directoryPath":"directoryPath","paths":["paths","paths"],"changeDetectionMode":"Default"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/cloudEndpoints/{cloud_endpoint_name}/triggerChangeDetection'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', cloud_endpoint_name='cloud_endpoint_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

