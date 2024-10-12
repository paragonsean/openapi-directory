# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.network_security_group import NetworkSecurityGroup
from openapi_server.models.network_security_group_list_result import NetworkSecurityGroupListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_security_groups_create_or_update(client):
    """Test case for network_security_groups_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"defaultSecurityRules":[{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":0,"direction":"Inbound"}},{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":0,"direction":"Inbound"}}],"networkInterfaces":[{"id":"id"},{"id":"id"}],"resourceGuid":"resourceGuid","securityRules":[{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":0,"direction":"Inbound"}},{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":0,"direction":"Inbound"}}],"subnets":[{"id":"id"},{"id":"id"}],"provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkSecurityGroups/{network_security_group_name}'.format(resource_group_name='resource_group_name_example', network_security_group_name='network_security_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_security_groups_delete(client):
    """Test case for network_security_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkSecurityGroups/{network_security_group_name}'.format(resource_group_name='resource_group_name_example', network_security_group_name='network_security_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_security_groups_get(client):
    """Test case for network_security_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkSecurityGroups/{network_security_group_name}'.format(resource_group_name='resource_group_name_example', network_security_group_name='network_security_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_security_groups_list(client):
    """Test case for network_security_groups_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkSecurityGroups'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_security_groups_list_all(client):
    """Test case for network_security_groups_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/networkSecurityGroups'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

