# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_request import BackupRequest
from openapi_server.models.post_backup_response import PostBackupResponse
from openapi_server.models.post_restore_request import PostRestoreRequest
from openapi_server.models.pre_restore_request import PreRestoreRequest
from openapi_server.models.recall_action_parameters import RecallActionParameters
from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server.models.trigger_rollover_request import TriggerRolloverRequest


pytestmark = pytest.mark.asyncio

async def test_cloud_endpoints_post_backup_0(client):
    """Test case for cloud_endpoints_post_backup_0

    
    """
    parameters = {"azureFileShare":"azureFileShare"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/cloudEndpoints/{cloud_endpoint_name}/postbackup'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', cloud_endpoint_name='cloud_endpoint_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_endpoints_post_restore_0(client):
    """Test case for cloud_endpoints_post_restore_0

    
    """
    parameters = {"partition":"partition","restoreFileSpec":[{"path":"path","isdir":True},{"path":"path","isdir":True}],"requestId":"requestId","azureFileShareUri":"azureFileShareUri","failedFileList":"failedFileList","replicaGroup":"replicaGroup","sourceAzureFileShareUri":"sourceAzureFileShareUri","status":"status"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/cloudEndpoints/{cloud_endpoint_name}/postrestore'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', cloud_endpoint_name='cloud_endpoint_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_endpoints_pre_backup_0(client):
    """Test case for cloud_endpoints_pre_backup_0

    
    """
    parameters = {"azureFileShare":"azureFileShare"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/cloudEndpoints/{cloud_endpoint_name}/prebackup'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', cloud_endpoint_name='cloud_endpoint_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_endpoints_pre_restore_0(client):
    """Test case for cloud_endpoints_pre_restore_0

    
    """
    parameters = {"partition":"partition","restoreFileSpec":[{"path":"path","isdir":True},{"path":"path","isdir":True}],"requestId":"requestId","azureFileShareUri":"azureFileShareUri","backupMetadataPropertyBag":"backupMetadataPropertyBag","pauseWaitForSyncDrainTimePeriodInSeconds":0,"replicaGroup":"replicaGroup","sourceAzureFileShareUri":"sourceAzureFileShareUri","status":"status"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/cloudEndpoints/{cloud_endpoint_name}/prerestore'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', cloud_endpoint_name='cloud_endpoint_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_endpoints_restoreheartbeat_0(client):
    """Test case for cloud_endpoints_restoreheartbeat_0

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/cloudEndpoints/{cloud_endpoint_name}/restoreheartbeat'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', cloud_endpoint_name='cloud_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registered_servers_trigger_rollover_0(client):
    """Test case for registered_servers_trigger_rollover_0

    
    """
    parameters = {"serverCertificate":"serverCertificate"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/registeredServers/{server_id}/triggerRollover'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', server_id='server_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_endpoints_recall_action_0(client):
    """Test case for server_endpoints_recall_action_0

    
    """
    parameters = {"pattern":"pattern","recallPath":"recallPath"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/serverEndpoints/{server_endpoint_name}/recallAction'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', server_endpoint_name='server_endpoint_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_abort_0(client):
    """Test case for workflows_abort_0

    
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

