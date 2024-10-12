# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_request import BackupRequest
from openapi_server.models.cloud_endpoint import CloudEndpoint
from openapi_server.models.cloud_endpoint_array import CloudEndpointArray
from openapi_server.models.post_backup_response import PostBackupResponse
from openapi_server.models.post_restore_request import PostRestoreRequest
from openapi_server.models.pre_restore_request import PreRestoreRequest
from openapi_server.models.storage_sync_error import StorageSyncError


pytestmark = pytest.mark.asyncio

async def test_cloud_endpoints_create(client):
    """Test case for cloud_endpoints_create

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"backupEnabled":True,"partnershipId":"partnershipId","storageAccountTenantId":"storageAccountTenantId","storageAccountKey":"storageAccountKey","storageAccountShareName":"storageAccountShareName","lastWorkflowId":"lastWorkflowId","provisioningState":"provisioningState","storageAccount":"storageAccount","storageAccountResourceId":"storageAccountResourceId","friendlyName":"friendlyName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/cloudEndpoints/{cloud_endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', cloud_endpoint_name='cloud_endpoint_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_endpoints_delete(client):
    """Test case for cloud_endpoints_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/cloudEndpoints/{cloud_endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', cloud_endpoint_name='cloud_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_endpoints_get(client):
    """Test case for cloud_endpoints_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/cloudEndpoints/{cloud_endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', cloud_endpoint_name='cloud_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_endpoints_list_by_sync_group(client):
    """Test case for cloud_endpoints_list_by_sync_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/cloudEndpoints'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_endpoints_post_backup(client):
    """Test case for cloud_endpoints_post_backup

    
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

async def test_cloud_endpoints_post_restore(client):
    """Test case for cloud_endpoints_post_restore

    
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

async def test_cloud_endpoints_pre_backup(client):
    """Test case for cloud_endpoints_pre_backup

    
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

async def test_cloud_endpoints_pre_restore(client):
    """Test case for cloud_endpoints_pre_restore

    
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

async def test_cloud_endpoints_restore_heatbeat(client):
    """Test case for cloud_endpoints_restore_heatbeat

    
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

