# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subnet import Subnet
from openapi_server.models.subnet_list_result import SubnetListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_subnets_create_or_update(client):
    """Test case for subnets_create_or_update

    
    """
    subnet_parameters = {"name":"name","etag":"etag","properties":{"ipConfigurations":[{"id":"id"},{"id":"id"}],"routeTable":{"id":"id"},"addressPrefix":"addressPrefix","provisioningState":"provisioningState","networkSecurityGroup":{"id":"id"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualnetworks/{virtual_network_name}/subnets/{subnet_name}'.format(resource_group_name='resource_group_name_example', virtual_network_name='virtual_network_name_example', subnet_name='subnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=subnet_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subnets_delete(client):
    """Test case for subnets_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualnetworks/{virtual_network_name}/subnets/{subnet_name}'.format(resource_group_name='resource_group_name_example', virtual_network_name='virtual_network_name_example', subnet_name='subnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subnets_get(client):
    """Test case for subnets_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualnetworks/{virtual_network_name}/subnets/{subnet_name}'.format(resource_group_name='resource_group_name_example', virtual_network_name='virtual_network_name_example', subnet_name='subnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subnets_list(client):
    """Test case for subnets_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualnetworks/{virtual_network_name}/subnets'.format(resource_group_name='resource_group_name_example', virtual_network_name='virtual_network_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

