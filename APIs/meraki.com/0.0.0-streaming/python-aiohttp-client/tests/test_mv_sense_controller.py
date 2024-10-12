# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_device_camera_analytics_live(client):
    """Test case for get_device_camera_analytics_live

    Returns live state from camera of analytics zones
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/devices/{serial}/camera/analytics/live'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_analytics_overview(client):
    """Test case for get_device_camera_analytics_overview

    Returns an overview of aggregate analytics data for a timespan
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('objectType', 'object_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/devices/{serial}/camera/analytics/overview'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_analytics_recent(client):
    """Test case for get_device_camera_analytics_recent

    Returns most recent record for analytics zones
    """
    params = [('objectType', 'object_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/devices/{serial}/camera/analytics/recent'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_analytics_zone_history(client):
    """Test case for get_device_camera_analytics_zone_history

    Return historical records for analytic zones
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('resolution', 56),
                    ('objectType', 'object_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/devices/{serial}/camera/analytics/zones/{zone_id}/history'.format(serial='serial_example', zone_id='zone_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_analytics_zones(client):
    """Test case for get_device_camera_analytics_zones

    Returns all configured analytic zones for this camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/devices/{serial}/camera/analytics/zones'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

