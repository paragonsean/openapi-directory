# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bastion_host import BastionHost
from openapi_server.models.bastion_host_list_result import BastionHostListResult


pytestmark = pytest.mark.asyncio

async def test_bastion_hosts_create_or_update(client):
    """Test case for bastion_hosts_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"ipConfigurations":[{"name":"name","etag":"etag","type":"type","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","provisioningState":"Succeeded","publicIPAddress":{"id":"id"}}},{"name":"name","etag":"etag","type":"type","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","provisioningState":"Succeeded","publicIPAddress":{"id":"id"}}}],"dnsName":"dnsName","provisioningState":"Succeeded"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/bastionHosts/{bastion_host_name}'.format(resource_group_name='resource_group_name_example', bastion_host_name='bastion_host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bastion_hosts_delete(client):
    """Test case for bastion_hosts_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/bastionHosts/{bastion_host_name}'.format(resource_group_name='resource_group_name_example', bastion_host_name='bastion_host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bastion_hosts_get(client):
    """Test case for bastion_hosts_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/bastionHosts/{bastion_host_name}'.format(resource_group_name='resource_group_name_example', bastion_host_name='bastion_host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bastion_hosts_list(client):
    """Test case for bastion_hosts_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/bastionHosts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bastion_hosts_list_by_resource_group(client):
    """Test case for bastion_hosts_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/bastionHosts'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

