# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.server_endpoint import ServerEndpoint
from openapi_server.models.server_endpoint_array import ServerEndpointArray
from openapi_server.models.storage_sync_error import StorageSyncError


pytestmark = pytest.mark.asyncio

async def test_server_endpoints_create(client):
    """Test case for server_endpoints_create

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"syncErrorState":"syncErrorState","syncErrorContext":"syncErrorContext","serverResourceId":"serverResourceId","syncErrorStateTimestamp":"2000-01-23T04:56:07.000+00:00","itemProgressCount":5,"lastSyncSuccess":"2000-01-23T04:56:07.000+00:00","lastWorkflowId":"lastWorkflowId","provisioningState":"provisioningState","itemUploadErrorCount":2,"cloudTiering":"on","volumeFreeSpacePercent":93,"currentProgressType":"none","itemTotalCount":5,"serverLocalPath":"serverLocalPath","totalProgress":7,"byteProgress":0,"byteTotal":6,"friendlyName":"friendlyName","itemDownloadErrorCount":1}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/serverEndpoints/{server_endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', server_endpoint_name='server_endpoint_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_endpoints_delete(client):
    """Test case for server_endpoints_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/serverEndpoints/{server_endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', server_endpoint_name='server_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_endpoints_get(client):
    """Test case for server_endpoints_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/serverEndpoints/{server_endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', server_endpoint_name='server_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_endpoints_list_by_sync_group(client):
    """Test case for server_endpoints_list_by_sync_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/serverEndpoints'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_endpoints_recall(client):
    """Test case for server_endpoints_recall

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/serverEndpoints/{server_endpoint_name}/recallAction'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', server_endpoint_name='server_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_endpoints_update(client):
    """Test case for server_endpoints_update

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"syncErrorState":"syncErrorState","syncErrorContext":"syncErrorContext","serverResourceId":"serverResourceId","syncErrorStateTimestamp":"2000-01-23T04:56:07.000+00:00","itemProgressCount":5,"lastSyncSuccess":"2000-01-23T04:56:07.000+00:00","lastWorkflowId":"lastWorkflowId","provisioningState":"provisioningState","itemUploadErrorCount":2,"cloudTiering":"on","volumeFreeSpacePercent":93,"currentProgressType":"none","itemTotalCount":5,"serverLocalPath":"serverLocalPath","totalProgress":7,"byteProgress":0,"byteTotal":6,"friendlyName":"friendlyName","itemDownloadErrorCount":1}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/syncGroups/{sync_group_name}/serverEndpoints/{server_endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', sync_group_name='sync_group_name_example', server_endpoint_name='server_endpoint_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

