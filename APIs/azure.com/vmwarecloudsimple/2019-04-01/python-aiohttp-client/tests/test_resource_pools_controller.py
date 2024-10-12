# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.resource_pool import ResourcePool
from openapi_server.models.resource_pools_list_response import ResourcePoolsListResponse


pytestmark = pytest.mark.asyncio

async def test_resource_pools_get(client):
    """Test case for resource_pools_get

    Implements get of resource pool
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/privateClouds/{pc_name}/resourcePools/{resource_pool_name}'.format(subscription_id='subscription_id_example', region_id='region_id_example', pc_name='pc_name_example', resource_pool_name='resource_pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_pools_list(client):
    """Test case for resource_pools_list

    Implements get of resource pools list
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/privateClouds/{pc_name}/resourcePools'.format(subscription_id='subscription_id_example', region_id='region_id_example', pc_name='pc_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

