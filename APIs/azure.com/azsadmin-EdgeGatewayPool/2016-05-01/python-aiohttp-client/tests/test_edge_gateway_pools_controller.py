# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edge_gateway_pool import EdgeGatewayPool
from openapi_server.models.edge_gateway_pool_list import EdgeGatewayPoolList


pytestmark = pytest.mark.asyncio

async def test_edge_gateway_pools_get(client):
    """Test case for edge_gateway_pools_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/edgeGatewayPools/{edge_gateway_pool}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', edge_gateway_pool='edge_gateway_pool_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edge_gateway_pools_list(client):
    """Test case for edge_gateway_pools_list

    
    """
    params = [('api-version', '2016-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/edgeGatewayPools'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

