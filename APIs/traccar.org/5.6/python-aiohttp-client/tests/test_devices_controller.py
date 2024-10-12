# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server.models.device_accumulators import DeviceAccumulators


pytestmark = pytest.mark.asyncio

async def test_devices_get(client):
    """Test case for devices_get

    Fetch a list of Devices
    """
    params = [('all', True),
                    ('userId', 56),
                    ('id', 56),
                    ('uniqueId', 'unique_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/devices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_id_accumulators_put(client):
    """Test case for devices_id_accumulators_put

    Update total distance and hours of the Device
    """
    body = {"hours":6.027456183070403,"totalDistance":1.4658129805029452,"deviceId":0}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/devices/{id}/accumulators'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_id_delete(client):
    """Test case for devices_id_delete

    Delete a Device
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/devices/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_id_put(client):
    """Test case for devices_id_put

    Update a Device
    """
    body = {"groupId":6,"positionId":5,"phone":"phone","geofenceIds":[0,0],"contact":"contact","lastUpdate":"2000-01-23T04:56:07.000+00:00","name":"name","attributes":"{}","disabled":True,"model":"model","id":1,"category":"category","uniqueId":"uniqueId","status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/devices/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_post(client):
    """Test case for devices_post

    Create a Device
    """
    body = {"groupId":6,"positionId":5,"phone":"phone","geofenceIds":[0,0],"contact":"contact","lastUpdate":"2000-01-23T04:56:07.000+00:00","name":"name","attributes":"{}","disabled":True,"model":"model","id":1,"category":"category","uniqueId":"uniqueId","status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/devices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

