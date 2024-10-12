# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_sas_parameters import AccountSasParameters
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server.models.list_account_sas_response import ListAccountSasResponse
from openapi_server.models.list_service_sas_response import ListServiceSasResponse
from openapi_server.models.service_sas_parameters import ServiceSasParameters
from openapi_server.models.storage_account import StorageAccount
from openapi_server.models.storage_account_check_name_availability_parameters import StorageAccountCheckNameAvailabilityParameters
from openapi_server.models.storage_account_create_parameters import StorageAccountCreateParameters
from openapi_server.models.storage_account_list_keys_result import StorageAccountListKeysResult
from openapi_server.models.storage_account_list_result import StorageAccountListResult
from openapi_server.models.storage_account_regenerate_key_parameters import StorageAccountRegenerateKeyParameters
from openapi_server.models.storage_account_update_parameters import StorageAccountUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_check_name_availability(client):
    """Test case for storage_accounts_check_name_availability

    
    """
    account_name = {"name":"name","type":"Microsoft.Storage/storageAccounts"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Storage/checkNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=account_name,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_create(client):
    """Test case for storage_accounts_create

    
    """
    parameters = {"kind":"Storage","location":"location","sku":{"tier":"Standard","name":"Standard_LRS"},"properties":{"encryption":{"keySource":"Microsoft.Storage","services":{"blob":{"lastEnabledTime":"2000-01-23T04:56:07.000+00:00","enabled":True}}},"accessTier":"Hot","customDomain":{"useSubDomainName":True,"name":"name"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_delete(client):
    """Test case for storage_accounts_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_get_properties(client):
    """Test case for storage_accounts_get_properties

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_list(client):
    """Test case for storage_accounts_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Storage/storageAccounts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_list_account_sas(client):
    """Test case for storage_accounts_list_account_sas

    
    """
    parameters = {"signedStart":"2000-01-23T04:56:07.000+00:00","signedProtocol":"https,http","signedIp":"signedIp","signedServices":"b","keyToSign":"keyToSign","signedPermission":"r","signedResourceTypes":"s","signedExpiry":"2000-01-23T04:56:07.000+00:00"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/ListAccountSas'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_list_by_resource_group(client):
    """Test case for storage_accounts_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_list_keys(client):
    """Test case for storage_accounts_list_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/listKeys'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_list_service_sas(client):
    """Test case for storage_accounts_list_service_sas

    
    """
    parameters = {"signedStart":"2000-01-23T04:56:07.000+00:00","signedProtocol":"https,http","rsct":"rsct","keyToSign":"keyToSign","signedExpiry":"2000-01-23T04:56:07.000+00:00","startRk":"startRk","signedIdentifier":"signedIdentifier","signedResource":"b","canonicalizedResource":"canonicalizedResource","endPk":"endPk","rscc":"rscc","signedIp":"signedIp","endRk":"endRk","rsce":"rsce","startPk":"startPk","rscd":"rscd","signedPermission":"r","rscl":"rscl"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/ListServiceSas'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_regenerate_key(client):
    """Test case for storage_accounts_regenerate_key

    
    """
    regenerate_key = {"keyName":"keyName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/regenerateKey'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=regenerate_key,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_accounts_update(client):
    """Test case for storage_accounts_update

    
    """
    parameters = {"sku":{"tier":"Standard","name":"Standard_LRS"},"properties":{"encryption":{"keySource":"Microsoft.Storage","services":{"blob":{"lastEnabledTime":"2000-01-23T04:56:07.000+00:00","enabled":True}}},"accessTier":"Hot","customDomain":{"useSubDomainName":True,"name":"name"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

