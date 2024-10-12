# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server.models.workflow import Workflow
from openapi_server.models.workflow_array import WorkflowArray


pytestmark = pytest.mark.asyncio

async def test_workflows_abort(client):
    """Test case for workflows_abort

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/workflows/{workflow_id}/abort'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', workflow_id='workflow_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_get(client):
    """Test case for workflows_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/workflows/{workflow_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', workflow_id='workflow_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_list_by_storage_sync_service(client):
    """Test case for workflows_list_by_storage_sync_service

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/workflows'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

