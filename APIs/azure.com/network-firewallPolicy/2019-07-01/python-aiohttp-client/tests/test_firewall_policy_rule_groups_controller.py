# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.firewall_policy_rule_group import FirewallPolicyRuleGroup
from openapi_server.models.firewall_policy_rule_group_list_result import FirewallPolicyRuleGroupListResult


pytestmark = pytest.mark.asyncio

async def test_firewall_policy_rule_groups_create_or_update(client):
    """Test case for firewall_policy_rule_groups_create_or_update

    
    """
    parameters = {"name":"name","etag":"etag","type":"type","properties":{"rules":[{"ruleType":"FirewallPolicyNatRule","name":"name","priority":39218},{"ruleType":"FirewallPolicyNatRule","name":"name","priority":39218}],"provisioningState":"Succeeded","priority":5297}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/firewallPolicies/{firewall_policy_name}/ruleGroups/{rule_group_name}'.format(resource_group_name='resource_group_name_example', firewall_policy_name='firewall_policy_name_example', rule_group_name='rule_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewall_policy_rule_groups_delete(client):
    """Test case for firewall_policy_rule_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/firewallPolicies/{firewall_policy_name}/ruleGroups/{rule_group_name}'.format(resource_group_name='resource_group_name_example', firewall_policy_name='firewall_policy_name_example', rule_group_name='rule_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewall_policy_rule_groups_get(client):
    """Test case for firewall_policy_rule_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/firewallPolicies/{firewall_policy_name}/ruleGroups/{rule_group_name}'.format(resource_group_name='resource_group_name_example', firewall_policy_name='firewall_policy_name_example', rule_group_name='rule_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewall_policy_rule_groups_list(client):
    """Test case for firewall_policy_rule_groups_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/firewallPolicies/{firewall_policy_name}/ruleGroups'.format(resource_group_name='resource_group_name_example', firewall_policy_name='firewall_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

