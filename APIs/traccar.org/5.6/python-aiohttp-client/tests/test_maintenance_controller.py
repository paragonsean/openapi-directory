# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.maintenance import Maintenance


pytestmark = pytest.mark.asyncio

async def test_maintenance_get(client):
    """Test case for maintenance_get

    Fetch a list of Maintenance
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
        path='/api/maintenance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maintenance_id_delete(client):
    """Test case for maintenance_id_delete

    Delete a Maintenance
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/maintenance/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maintenance_id_put(client):
    """Test case for maintenance_id_put

    Update a Maintenance
    """
    body = {"period":6.027456183070403,"name":"name","start":1.4658129805029452,"attributes":"{}","id":0,"type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/maintenance/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maintenance_post(client):
    """Test case for maintenance_post

    Create a Maintenance
    """
    body = {"period":6.027456183070403,"name":"name","start":1.4658129805029452,"attributes":"{}","id":0,"type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/maintenance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

