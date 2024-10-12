# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.redis_firewall_rule import RedisFirewallRule
from openapi_server.models.redis_firewall_rule_list_result import RedisFirewallRuleListResult


pytestmark = pytest.mark.asyncio

async def test_firewall_rules_list_0(client):
    """Test case for firewall_rules_list_0

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cache/Redis/{cache_name}/firewallRules'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cache_name='cache_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_firewall_rule_create_or_update_0(client):
    """Test case for redis_firewall_rule_create_or_update_0

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"endIP":"endIP","startIP":"startIP"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cache/Redis/{cache_name}/firewallRules/{rule_name}'.format(resource_group_name='resource_group_name_example', cache_name='cache_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_firewall_rule_delete_0(client):
    """Test case for redis_firewall_rule_delete_0

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cache/Redis/{cache_name}/firewallRules/{rule_name}'.format(resource_group_name='resource_group_name_example', cache_name='cache_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_firewall_rule_get_0(client):
    """Test case for redis_firewall_rule_get_0

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cache/Redis/{cache_name}/firewallRules/{rule_name}'.format(resource_group_name='resource_group_name_example', cache_name='cache_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

