# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.nat_gateway import NatGateway
from openapi_server.models.nat_gateway_list_result import NatGatewayListResult
from openapi_server.models.nat_gateways_update_tags_request import NatGatewaysUpdateTagsRequest


pytestmark = pytest.mark.asyncio

async def test_nat_gateways_create_or_update(client):
    """Test case for nat_gateways_create_or_update

    
    """
    parameters = {"etag":"etag","sku":{"name":"Standard"},"zones":["zones","zones"],"properties":{"publicIpPrefixes":[{"id":"id"},{"id":"id"}],"publicIpAddresses":[{"id":"id"},{"id":"id"}],"resourceGuid":"resourceGuid","idleTimeoutInMinutes":0,"subnets":[{"id":"id"},{"id":"id"}],"provisioningState":"Succeeded"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/natGateways/{nat_gateway_name}'.format(resource_group_name='resource_group_name_example', nat_gateway_name='nat_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nat_gateways_delete(client):
    """Test case for nat_gateways_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/natGateways/{nat_gateway_name}'.format(resource_group_name='resource_group_name_example', nat_gateway_name='nat_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nat_gateways_get(client):
    """Test case for nat_gateways_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/natGateways/{nat_gateway_name}'.format(resource_group_name='resource_group_name_example', nat_gateway_name='nat_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nat_gateways_list(client):
    """Test case for nat_gateways_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/natGateways'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nat_gateways_list_all(client):
    """Test case for nat_gateways_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/natGateways'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nat_gateways_update_tags(client):
    """Test case for nat_gateways_update_tags

    
    """
    parameters = openapi_server.NatGatewaysUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/natGateways/{nat_gateway_name}'.format(resource_group_name='resource_group_name_example', nat_gateway_name='nat_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

