# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_lake_store_account import DataLakeStoreAccount
from openapi_server.models.data_lake_store_account_list_result import DataLakeStoreAccountListResult
from openapi_server.models.data_lake_store_firewall_rule_list_result import DataLakeStoreFirewallRuleListResult
from openapi_server.models.firewall_rule import FirewallRule


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_account_create(client):
    """Test case for account_create

    
    """
    parameters = {"identity":{"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","principalId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"SystemAssigned"},"name":"name","location":"location","id":"id","type":"type","properties":{"encryptionConfig":{"keyVaultMetaInfo":{"encryptionKeyName":"encryptionKeyName","encryptionKeyVersion":"encryptionKeyVersion","keyVaultResourceId":"keyVaultResourceId"},"type":"UserManaged"},"encryptionProvisioningState":"Creating","encryptionState":"Enabled","endpoint":"endpoint","lastModifiedTime":"2000-01-23T04:56:07.000+00:00","creationTime":"2000-01-23T04:56:07.000+00:00","defaultGroup":"defaultGroup","provisioningState":"Failed","state":"active"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_account_create_or_update_firewall_rule(client):
    """Test case for account_create_or_update_firewall_rule

    
    """
    parameters = {"name":"name","location":"location","id":"id","type":"type","properties":{"endIpAddress":"endIpAddress","startIpAddress":"startIpAddress"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/firewallRules/{name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_delete(client):
    """Test case for account_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_delete_firewall_rule(client):
    """Test case for account_delete_firewall_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/firewallRules/{firewall_rule_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', firewall_rule_name='firewall_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_enable_key_vault(client):
    """Test case for account_enable_key_vault

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/enableKeyVault'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get(client):
    """Test case for account_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_firewall_rule(client):
    """Test case for account_get_firewall_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/firewallRules/{firewall_rule_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', firewall_rule_name='firewall_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_list(client):
    """Test case for account_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('$search', 'search_example'),
                    ('$format', 'format_example'),
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

async def test_account_list_by_resource_group(client):
    """Test case for account_list_by_resource_group

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('$search', 'search_example'),
                    ('$format', 'format_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_list_firewall_rules(client):
    """Test case for account_list_firewall_rules

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/firewallRules'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_account_update(client):
    """Test case for account_update

    
    """
    parameters = {"identity":{"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","principalId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"SystemAssigned"},"name":"name","location":"location","id":"id","type":"type","properties":{"encryptionConfig":{"keyVaultMetaInfo":{"encryptionKeyName":"encryptionKeyName","encryptionKeyVersion":"encryptionKeyVersion","keyVaultResourceId":"keyVaultResourceId"},"type":"UserManaged"},"encryptionProvisioningState":"Creating","encryptionState":"Enabled","endpoint":"endpoint","lastModifiedTime":"2000-01-23T04:56:07.000+00:00","creationTime":"2000-01-23T04:56:07.000+00:00","defaultGroup":"defaultGroup","provisioningState":"Failed","state":"active"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

