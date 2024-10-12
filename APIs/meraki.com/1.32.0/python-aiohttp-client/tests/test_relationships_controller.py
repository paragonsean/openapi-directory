# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_device_sensor_relationships200_response_inner import GetDeviceSensorRelationships200ResponseInner
from openapi_server.models.get_network_sensor_relationships200_response_inner import GetNetworkSensorRelationships200ResponseInner
from openapi_server.models.update_device_sensor_relationships_request import UpdateDeviceSensorRelationshipsRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_sensor_relationships_1(client):
    """Test case for get_device_sensor_relationships_1

    List the sensor roles for a given sensor or camera device.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/sensor/relationships'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sensor_relationships_1(client):
    """Test case for get_network_sensor_relationships_1

    List the sensor roles for devices in a given network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sensor/relationships'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_sensor_relationships_1(client):
    """Test case for update_device_sensor_relationships_1

    Assign one or more sensor roles to a given sensor or camera device.
    """
    body = openapi_server.UpdateDeviceSensorRelationshipsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/sensor/relationships'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

