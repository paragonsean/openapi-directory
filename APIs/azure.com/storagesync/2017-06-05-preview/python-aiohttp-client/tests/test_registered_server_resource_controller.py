# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.registered_server import RegisteredServer
from openapi_server.models.registered_server_array import RegisteredServerArray
from openapi_server.models.storage_sync_error import StorageSyncError


pytestmark = pytest.mark.asyncio

async def test_registered_servers_create(client):
    """Test case for registered_servers_create

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"lastHeartBeat":"lastHeartBeat","serverRole":"serverRole","storageSyncServiceUid":"storageSyncServiceUid","serverManagementtErrorCode":0,"serverCertificate":"serverCertificate","clusterName":"clusterName","agentVersion":"agentVersion","serverOSVersion":"serverOSVersion","clusterId":"clusterId","lastWorkflowId":"lastWorkflowId","provisioningState":"provisioningState","serverId":"serverId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/registeredServers/{server_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', server_id='server_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registered_servers_delete(client):
    """Test case for registered_servers_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/registeredServers/{server_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', server_id='server_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registered_servers_get(client):
    """Test case for registered_servers_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/registeredServers/{server_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example', server_id='server_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registered_servers_list_by_storage_sync_service(client):
    """Test case for registered_servers_list_by_storage_sync_service

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}/registeredServers'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

