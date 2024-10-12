# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_parameters import CheckNameAvailabilityParameters
from openapi_server.models.create_data_lake_store_account_parameters import CreateDataLakeStoreAccountParameters
from openapi_server.models.data_lake_store_account import DataLakeStoreAccount
from openapi_server.models.data_lake_store_account_list_result import DataLakeStoreAccountListResult
from openapi_server.models.name_availability_information import NameAvailabilityInformation
from openapi_server.models.update_data_lake_store_account_parameters import UpdateDataLakeStoreAccountParameters


pytestmark = pytest.mark.asyncio

async def test_accounts_check_name_availability(client):
    """Test case for accounts_check_name_availability

    
    """
    parameters = {"name":"name","type":"Microsoft.DataLakeStore/accounts"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataLakeStore/locations/{location}/checkNameAvailability'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_create(client):
    """Test case for accounts_create

    
    """
    parameters = {"identity":{"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","principalId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"SystemAssigned"},"location":"location","properties":{"encryptionConfig":{"keyVaultMetaInfo":{"encryptionKeyName":"encryptionKeyName","encryptionKeyVersion":"encryptionKeyVersion","keyVaultResourceId":"keyVaultResourceId"},"type":"UserManaged"},"encryptionState":"Enabled","defaultGroup":"defaultGroup","trustedIdProviders":[{"name":"name","properties":{"idProvider":"idProvider"}},{"name":"name","properties":{"idProvider":"idProvider"}}],"firewallState":"Enabled","newTier":"Consumption","virtualNetworkRules":[{"name":"name","properties":{"subnetId":"subnetId"}},{"name":"name","properties":{"subnetId":"subnetId"}}],"trustedIdProviderState":"Enabled","firewallRules":[{"name":"name","properties":{"endIpAddress":"endIpAddress","startIpAddress":"startIpAddress"}},{"name":"name","properties":{"endIpAddress":"endIpAddress","startIpAddress":"startIpAddress"}}],"firewallAllowAzureIps":"Enabled"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_delete(client):
    """Test case for accounts_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_enable_key_vault(client):
    """Test case for accounts_enable_key_vault

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/enableKeyVault'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_get(client):
    """Test case for accounts_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_list(client):
    """Test case for accounts_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataLakeStore/accounts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_list_by_resource_group(client):
    """Test case for accounts_list_by_resource_group

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_update(client):
    """Test case for accounts_update

    
    """
    parameters = {"properties":{"encryptionConfig":{"keyVaultMetaInfo":{"encryptionKeyVersion":"encryptionKeyVersion"}},"defaultGroup":"defaultGroup","trustedIdProviders":[{"name":"name","properties":{"idProvider":"idProvider"}},{"name":"name","properties":{"idProvider":"idProvider"}}],"firewallState":"Enabled","newTier":"Consumption","virtualNetworkRules":[{"name":"name","properties":{"subnetId":"subnetId"}},{"name":"name","properties":{"subnetId":"subnetId"}}],"trustedIdProviderState":"Enabled","firewallRules":[{"name":"name","properties":{"endIpAddress":"endIpAddress","startIpAddress":"startIpAddress"}},{"name":"name","properties":{"endIpAddress":"endIpAddress","startIpAddress":"startIpAddress"}}],"firewallAllowAzureIps":"Enabled"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

