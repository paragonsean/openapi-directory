# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.load_balancer import LoadBalancer
from openapi_server.models.load_balancer_list_result import LoadBalancerListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_load_balancers_create_or_update(client):
    """Test case for load_balancers_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"inboundNatPools":[{"name":"name","etag":"etag","properties":{"protocol":"Udp","backendPort":0,"frontendPortRangeStart":1,"frontendIPConfiguration":{"id":"id"},"provisioningState":"provisioningState","frontendPortRangeEnd":6}},{"name":"name","etag":"etag","properties":{"protocol":"Udp","backendPort":0,"frontendPortRangeStart":1,"frontendIPConfiguration":{"id":"id"},"provisioningState":"provisioningState","frontendPortRangeEnd":6}}],"inboundNatRules":[{"name":"name","etag":"etag","properties":{"enableFloatingIP":True,"protocol":"Udp","backendPort":5,"backendIPConfiguration":{"id":"id"},"frontendIPConfiguration":{"id":"id"},"idleTimeoutInMinutes":2,"frontendPort":5,"provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"enableFloatingIP":True,"protocol":"Udp","backendPort":5,"backendIPConfiguration":{"id":"id"},"frontendIPConfiguration":{"id":"id"},"idleTimeoutInMinutes":2,"frontendPort":5,"provisioningState":"provisioningState"}}],"loadBalancingRules":[{"name":"name","etag":"etag","properties":{"enableFloatingIP":True,"loadDistribution":"Default","protocol":"Udp","backendPort":7,"frontendIPConfiguration":{"id":"id"},"idleTimeoutInMinutes":3,"backendAddressPool":{"id":"id"},"frontendPort":9,"provisioningState":"provisioningState","probe":{"id":"id"}}},{"name":"name","etag":"etag","properties":{"enableFloatingIP":True,"loadDistribution":"Default","protocol":"Udp","backendPort":7,"frontendIPConfiguration":{"id":"id"},"idleTimeoutInMinutes":3,"backendAddressPool":{"id":"id"},"frontendPort":9,"provisioningState":"provisioningState","probe":{"id":"id"}}}],"resourceGuid":"resourceGuid","probes":[{"name":"name","etag":"etag","properties":{"loadBalancingRules":[{"id":"id"},{"id":"id"}],"protocol":"Http","port":1,"intervalInSeconds":4,"numberOfProbes":7,"provisioningState":"provisioningState","requestPath":"requestPath"}},{"name":"name","etag":"etag","properties":{"loadBalancingRules":[{"id":"id"},{"id":"id"}],"protocol":"Http","port":1,"intervalInSeconds":4,"numberOfProbes":7,"provisioningState":"provisioningState","requestPath":"requestPath"}}],"frontendIPConfigurations":[{"name":"name","etag":"etag","properties":{"inboundNatPools":[{"id":"id"},{"id":"id"}],"inboundNatRules":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"loadBalancingRules":[{"id":"id"},{"id":"id"}],"privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","provisioningState":"provisioningState","outboundNatRules":[{"id":"id"},{"id":"id"}],"publicIPAddress":{"id":"id"}}},{"name":"name","etag":"etag","properties":{"inboundNatPools":[{"id":"id"},{"id":"id"}],"inboundNatRules":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"loadBalancingRules":[{"id":"id"},{"id":"id"}],"privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","provisioningState":"provisioningState","outboundNatRules":[{"id":"id"},{"id":"id"}],"publicIPAddress":{"id":"id"}}}],"provisioningState":"provisioningState","backendAddressPools":[{"name":"name","etag":"etag","properties":{"outboundNatRule":{"id":"id"},"loadBalancingRules":[{"id":"id"},{"id":"id"}],"backendIPConfigurations":[{"id":"id"},{"id":"id"}],"provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"outboundNatRule":{"id":"id"},"loadBalancingRules":[{"id":"id"},{"id":"id"}],"backendIPConfigurations":[{"id":"id"},{"id":"id"}],"provisioningState":"provisioningState"}}],"outboundNatRules":[{"name":"name","etag":"etag","properties":{"allocatedOutboundPorts":2,"backendAddressPool":{"id":"id"},"frontendIPConfigurations":[{"id":"id"},{"id":"id"}],"provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"allocatedOutboundPorts":2,"backendAddressPool":{"id":"id"},"frontendIPConfigurations":[{"id":"id"},{"id":"id"}],"provisioningState":"provisioningState"}}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/loadBalancers/{load_balancer_name}'.format(resource_group_name='resource_group_name_example', load_balancer_name='load_balancer_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_delete(client):
    """Test case for load_balancers_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/loadBalancers/{load_balancer_name}'.format(resource_group_name='resource_group_name_example', load_balancer_name='load_balancer_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_get(client):
    """Test case for load_balancers_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/loadBalancers/{load_balancer_name}'.format(resource_group_name='resource_group_name_example', load_balancer_name='load_balancer_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_list(client):
    """Test case for load_balancers_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/loadBalancers'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_list_all(client):
    """Test case for load_balancers_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/loadBalancers'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

