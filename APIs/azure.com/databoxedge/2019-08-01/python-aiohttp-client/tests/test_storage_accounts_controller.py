# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.storage_account import StorageAccount
from openapi_server.models.storage_account_list import StorageAccountList


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_create_or_update(client):
    """Test case for storage_accounts_create_or_update

    Creates a new StorageAccount or updates an existing StorageAccount on the device.
    """
    storage_account = {"properties":{"dataPolicy":"Cloud","description":"description","storageAccountCredentialId":"storageAccountCredentialId","blobEndpoint":"blobEndpoint","containerCount":0,"storageAccountStatus":"OK"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccounts/{storage_account_name}'.format(device_name='device_name_example', storage_account_name='storage_account_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=storage_account,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_delete(client):
    """Test case for storage_accounts_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccounts/{storage_account_name}'.format(device_name='device_name_example', storage_account_name='storage_account_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_get(client):
    """Test case for storage_accounts_get

    Gets a StorageAccount by name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccounts/{storage_account_name}'.format(device_name='device_name_example', storage_account_name='storage_account_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_list_by_data_box_edge_device(client):
    """Test case for storage_accounts_list_by_data_box_edge_device

    Lists all the storage accounts in a Data Box Edge/Data Box Gateway device.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccounts'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

