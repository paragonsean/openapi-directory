# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.mac_address_pool import MacAddressPool
from openapi_server.models.mac_address_pool_list import MacAddressPoolList


pytestmark = pytest.mark.asyncio

async def test_mac_address_pools_get(client):
    """Test case for mac_address_pools_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/macAddressPools/{mac_address_pool}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', mac_address_pool='mac_address_pool_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mac_address_pools_list(client):
    """Test case for mac_address_pools_list

    
    """
    params = [('api-version', '2016-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/macAddressPools'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

