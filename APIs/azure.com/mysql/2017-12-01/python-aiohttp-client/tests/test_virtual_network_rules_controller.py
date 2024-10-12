# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_network_rule import VirtualNetworkRule
from openapi_server.models.virtual_network_rule_list_result import VirtualNetworkRuleListResult


pytestmark = pytest.mark.asyncio

async def test_virtual_network_rules_create_or_update(client):
    """Test case for virtual_network_rules_create_or_update

    
    """
    parameters = {"properties":{"ignoreMissingVnetServiceEndpoint":True,"virtualNetworkSubnetId":"virtualNetworkSubnetId","state":"Initializing"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DBforMySQL/servers/{server_name}/virtualNetworkRules/{virtual_network_rule_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', subscription_id='subscription_id_example', virtual_network_rule_name='virtual_network_rule_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DBforMySQL/servers/{server_name}/virtualNetworkRules/{virtual_network_rule_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', virtual_network_rule_name='virtual_network_rule_name_example', subscription_id='subscription_id_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DBforMySQL/servers/{server_name}/virtualNetworkRules/{virtual_network_rule_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', subscription_id='subscription_id_example', virtual_network_rule_name='virtual_network_rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_rules_list_by_server(client):
    """Test case for virtual_network_rules_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DBforMySQL/servers/{server_name}/virtualNetworkRules'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

