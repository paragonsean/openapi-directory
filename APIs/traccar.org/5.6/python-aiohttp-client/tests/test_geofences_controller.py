# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.geofence import Geofence


pytestmark = pytest.mark.asyncio

async def test_geofences_get(client):
    """Test case for geofences_get

    Fetch a list of Geofences
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
        path='/api/geofences',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geofences_id_delete(client):
    """Test case for geofences_id_delete

    Delete a Geofence
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/geofences/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geofences_id_put(client):
    """Test case for geofences_id_put

    Update a Geofence
    """
    body = {"area":"area","calendarId":0,"name":"name","description":"description","attributes":"{}","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/geofences/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geofences_post(client):
    """Test case for geofences_post

    Create a Geofence
    """
    body = {"area":"area","calendarId":0,"name":"name","description":"description","attributes":"{}","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/geofences',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

