# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.capacity_pool import CapacityPool
from openapi_server.models.capacity_pool_list import CapacityPoolList
from openapi_server.models.capacity_pool_patch import CapacityPoolPatch


pytestmark = pytest.mark.asyncio

async def test_pools_create_or_update(client):
    """Test case for pools_create_or_update

    Create or Update the specified capacity pool within the resource group
    """
    body = openapi_server.CapacityPool()
    params = [('api-version', '2019-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pools_delete(client):
    """Test case for pools_delete

    Delete a capacity pool
    """
    params = [('api-version', '2019-11-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pools_get(client):
    """Test case for pools_get

    Describe a Capacity Pool
    """
    params = [('api-version', '2019-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pools_list(client):
    """Test case for pools_list

    Describe all Capacity Pools
    """
    params = [('api-version', '2019-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pools_update(client):
    """Test case for pools_update

    Update a capacity pool
    """
    body = openapi_server.CapacityPoolPatch()
    params = [('api-version', '2019-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

