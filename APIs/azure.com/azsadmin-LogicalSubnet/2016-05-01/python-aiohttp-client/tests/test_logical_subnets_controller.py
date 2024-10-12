# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.logical_subnet import LogicalSubnet
from openapi_server.models.logical_subnet_list import LogicalSubnetList


pytestmark = pytest.mark.asyncio

async def test_logical_subnets_get(client):
    """Test case for logical_subnets_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/logicalNetworks/{logical_network}/logicalSubnets/{logical_subnet}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', logical_network='logical_network_example', logical_subnet='logical_subnet_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logical_subnets_list(client):
    """Test case for logical_subnets_list

    
    """
    params = [('api-version', '2016-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/logicalNetworks/{logical_network}/logicalSubnets'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', logical_network='logical_network_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

