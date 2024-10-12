# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.management_policies_rules_set_parameter import ManagementPoliciesRulesSetParameter
from openapi_server.models.storage_account_management_policies import StorageAccountManagementPolicies


pytestmark = pytest.mark.asyncio

async def test_management_policies_create_or_update(client):
    """Test case for management_policies_create_or_update

    
    """
    properties = {"properties":{"policy":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/managementPolicies/{management_policy_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', management_policy_name='management_policy_name_example'),
        headers=headers,
        json=properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_management_policies_delete(client):
    """Test case for management_policies_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/managementPolicies/{management_policy_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', management_policy_name='management_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_management_policies_get(client):
    """Test case for management_policies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/managementPolicies/{management_policy_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', management_policy_name='management_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

