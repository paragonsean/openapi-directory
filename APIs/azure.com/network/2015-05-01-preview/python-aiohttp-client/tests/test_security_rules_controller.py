# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.security_rule import SecurityRule
from openapi_server.models.security_rule_list_result import SecurityRuleListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_security_rules_create_or_update(client):
    """Test case for security_rules_create_or_update

    
    """
    security_rule_parameters = {"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":0,"direction":"Inbound"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkSecurityGroups/{network_security_group_name}/securityRules/{security_rule_name}'.format(resource_group_name='resource_group_name_example', network_security_group_name='network_security_group_name_example', security_rule_name='security_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=security_rule_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_rules_delete(client):
    """Test case for security_rules_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkSecurityGroups/{network_security_group_name}/securityRules/{security_rule_name}'.format(resource_group_name='resource_group_name_example', network_security_group_name='network_security_group_name_example', security_rule_name='security_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_rules_get(client):
    """Test case for security_rules_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkSecurityGroups/{network_security_group_name}/securityRules/{security_rule_name}'.format(resource_group_name='resource_group_name_example', network_security_group_name='network_security_group_name_example', security_rule_name='security_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_rules_list(client):
    """Test case for security_rules_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkSecurityGroups/{network_security_group_name}/securityRules'.format(resource_group_name='resource_group_name_example', network_security_group_name='network_security_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

