# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.pool import Pool
from openapi_server.models.pool_collection import PoolCollection


pytestmark = pytest.mark.asyncio

async def test_delete_pool(client):
    """Test case for delete_pool

    Delete a pool
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/pools/{pool_name}'.format(pool_name='pool_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pool(client):
    """Test case for get_pool

    Get a pool
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/pools/{pool_name}'.format(pool_name='pool_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pools(client):
    """Test case for get_pools

    List pools
    """
    params = [('limit', 100),
                    ('offset', 56),
                    ('order_by', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/pools',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_pool(client):
    """Test case for patch_pool

    Update a pool
    """
    body = {"open_slots":6,"queued_slots":1,"slots":5,"name":"name","description":"description","used_slots":5,"occupied_slots":0}
    params = [('update_mask', ['update_mask_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/pools/{pool_name}'.format(pool_name='pool_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_pool(client):
    """Test case for post_pool

    Create a pool
    """
    body = {"open_slots":6,"queued_slots":1,"slots":5,"name":"name","description":"description","used_slots":5,"occupied_slots":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/pools',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

