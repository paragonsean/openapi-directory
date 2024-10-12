# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_virtual_network_rule_parameters import CreateOrUpdateVirtualNetworkRuleParameters
from openapi_server.models.update_virtual_network_rule_parameters import UpdateVirtualNetworkRuleParameters
from openapi_server.models.virtual_network_rule import VirtualNetworkRule
from openapi_server.models.virtual_network_rule_list_result import VirtualNetworkRuleListResult


pytestmark = pytest.mark.asyncio

async def test_virtual_network_rules_create_or_update(client):
    """Test case for virtual_network_rules_create_or_update

    
    """
    parameters = {"properties":{"subnetId":"subnetId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/virtualNetworkRules/{virtual_network_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', virtual_network_rule_name='virtual_network_rule_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_rules_delete(client):
    """Test case for virtual_network_rules_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/virtualNetworkRules/{virtual_network_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', virtual_network_rule_name='virtual_network_rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_rules_get(client):
    """Test case for virtual_network_rules_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/virtualNetworkRules/{virtual_network_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', virtual_network_rule_name='virtual_network_rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_rules_list_by_account(client):
    """Test case for virtual_network_rules_list_by_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/virtualNetworkRules'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_rules_update(client):
    """Test case for virtual_network_rules_update

    
    """
    parameters = {"properties":{"subnetId":"subnetId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/virtualNetworkRules/{virtual_network_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', virtual_network_rule_name='virtual_network_rule_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

