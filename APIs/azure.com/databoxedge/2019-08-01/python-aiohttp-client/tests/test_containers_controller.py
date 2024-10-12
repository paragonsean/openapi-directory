# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.container import Container
from openapi_server.models.container_list import ContainerList


pytestmark = pytest.mark.asyncio

async def test_containers_create_or_update(client):
    """Test case for containers_create_or_update

    Creates a new container or updates an existing container on the device.
    """
    container = {"properties":{"dataFormat":"BlockBlob","createdDateTime":"2000-01-23T04:56:07.000+00:00","containerStatus":"OK","refreshDetails":{"errorManifestFile":"errorManifestFile","lastJob":"lastJob","inProgressRefreshJobId":"inProgressRefreshJobId","lastCompletedRefreshJobTimeInUTC":"2000-01-23T04:56:07.000+00:00"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccounts/{storage_account_name}/containers/{container_name}'.format(device_name='device_name_example', storage_account_name='storage_account_name_example', container_name='container_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=container,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_delete(client):
    """Test case for containers_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccounts/{storage_account_name}/containers/{container_name}'.format(device_name='device_name_example', storage_account_name='storage_account_name_example', container_name='container_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_get(client):
    """Test case for containers_get

    Gets a container by name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccounts/{storage_account_name}/containers/{container_name}'.format(device_name='device_name_example', storage_account_name='storage_account_name_example', container_name='container_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_list_by_storage_account(client):
    """Test case for containers_list_by_storage_account

    Lists all the containers of a storage Account in a Data Box Edge/Data Box Gateway device.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccounts/{storage_account_name}/containers'.format(device_name='device_name_example', storage_account_name='storage_account_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_refresh(client):
    """Test case for containers_refresh

    Refreshes the container metadata with the data from the cloud.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccounts/{storage_account_name}/containers/{container_name}/refresh'.format(device_name='device_name_example', storage_account_name='storage_account_name_example', container_name='container_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

