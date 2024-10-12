# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.driver import Driver


pytestmark = pytest.mark.asyncio

async def test_drivers_get(client):
    """Test case for drivers_get

    Fetch a list of Drivers
    """
    params = [('all', True),
                    ('userId', 56),
                    ('deviceId', 56),
                    ('groupId', 56),
                    ('refresh', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/drivers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivers_id_delete(client):
    """Test case for drivers_id_delete

    Delete a Driver
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/drivers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivers_id_put(client):
    """Test case for drivers_id_put

    Update a Driver
    """
    body = {"name":"name","attributes":"{}","id":0,"uniqueId":"uniqueId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/drivers/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivers_post(client):
    """Test case for drivers_post

    Create a Driver
    """
    body = {"name":"name","attributes":"{}","id":0,"uniqueId":"uniqueId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/drivers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

