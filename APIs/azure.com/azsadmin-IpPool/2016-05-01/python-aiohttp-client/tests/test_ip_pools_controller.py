# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ip_pool import IpPool
from openapi_server.models.ip_pool_list import IpPoolList


pytestmark = pytest.mark.asyncio

async def test_ip_pools_create_or_update(client):
    """Test case for ip_pools_create_or_update

    
    """
    pool = {"properties":{"endIpAddress":"endIpAddress","numberOfAllocatedIpAddresses":0,"addressPrefix":"addressPrefix","numberOfIpAddresses":6,"numberOfIpAddressesInTransition":1,"startIpAddress":"startIpAddress"}}
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/ipPools/{ip_pool}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', ip_pool='ip_pool_example'),
        headers=headers,
        json=pool,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ip_pools_get(client):
    """Test case for ip_pools_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/ipPools/{ip_pool}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', ip_pool='ip_pool_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ip_pools_list(client):
    """Test case for ip_pools_list

    
    """
    params = [('api-version', '2016-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/ipPools'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

