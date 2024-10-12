# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.storage_account_credential import StorageAccountCredential
from openapi_server.models.storage_account_credential_list import StorageAccountCredentialList


pytestmark = pytest.mark.asyncio

async def test_storage_account_credentials_create_or_update(client):
    """Test case for storage_account_credentials_create_or_update

    
    """
    storage_account_credential = {"properties":{"connectionString":"connectionString","sslStatus":"Enabled","accountType":"GeneralPurposeStorage","blobDomainName":"blobDomainName","alias":"alias","userName":"userName","accountKey":{"encryptionAlgorithm":"None","encryptionCertThumbprint":"encryptionCertThumbprint","value":"value"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccountCredentials/{name}'.format(device_name='device_name_example', name='name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=storage_account_credential,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_account_credentials_delete(client):
    """Test case for storage_account_credentials_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccountCredentials/{name}'.format(device_name='device_name_example', name='name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_account_credentials_get(client):
    """Test case for storage_account_credentials_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccountCredentials/{name}'.format(device_name='device_name_example', name='name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_account_credentials_list_by_data_box_edge_device(client):
    """Test case for storage_account_credentials_list_by_data_box_edge_device

    Gets all the storage account credentials in a data box edge/gateway device.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/storageAccountCredentials'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

