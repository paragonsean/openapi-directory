# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.storage_account_credential import StorageAccountCredential
from openapi_server.models.storage_account_credential_list import StorageAccountCredentialList


pytestmark = pytest.mark.asyncio

async def test_storage_account_credentials_create_or_update(client):
    """Test case for storage_account_credentials_create_or_update

    
    """
    parameters = {"properties":{"endPoint":"endPoint","volumesCount":0,"accessKey":{"encryptionAlgorithm":"None","encryptionCertThumbprint":"encryptionCertThumbprint","value":"value"},"sslStatus":"Enabled"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/storageAccountCredentials/{storage_account_credential_name}'.format(storage_account_credential_name='storage_account_credential_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_account_credentials_delete(client):
    """Test case for storage_account_credentials_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/storageAccountCredentials/{storage_account_credential_name}'.format(storage_account_credential_name='storage_account_credential_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/storageAccountCredentials/{storage_account_credential_name}'.format(storage_account_credential_name='storage_account_credential_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_account_credentials_list_by_manager(client):
    """Test case for storage_account_credentials_list_by_manager

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/storageAccountCredentials'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

