# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_firewall_rule_parameters import CreateOrUpdateFirewallRuleParameters
from openapi_server.models.firewall_rule import FirewallRule
from openapi_server.models.firewall_rule_list_result import FirewallRuleListResult
from openapi_server.models.update_firewall_rule_parameters import UpdateFirewallRuleParameters


pytestmark = pytest.mark.asyncio

async def test_firewall_rules_create_or_update(client):
    """Test case for firewall_rules_create_or_update

    
    """
    parameters = {"properties":{"endIpAddress":"endIpAddress","startIpAddress":"startIpAddress"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/firewallRules/{firewall_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', firewall_rule_name='firewall_rule_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewall_rules_delete(client):
    """Test case for firewall_rules_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/firewallRules/{firewall_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', firewall_rule_name='firewall_rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewall_rules_get(client):
    """Test case for firewall_rules_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/firewallRules/{firewall_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', firewall_rule_name='firewall_rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewall_rules_list_by_account(client):
    """Test case for firewall_rules_list_by_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/firewallRules'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewall_rules_update(client):
    """Test case for firewall_rules_update

    
    """
    parameters = {"properties":{"endIpAddress":"endIpAddress","startIpAddress":"startIpAddress"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataLakeStore/accounts/{account_name}/firewallRules/{firewall_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', firewall_rule_name='firewall_rule_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

