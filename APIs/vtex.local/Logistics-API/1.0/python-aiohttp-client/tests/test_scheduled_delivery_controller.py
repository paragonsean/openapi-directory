# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_add_blocked_delivery_windows(client):
    """Test case for add_blocked_delivery_windows

    Add blocked delivery windows
    """
    body = "2016-08-09T08:00:00"
    headers = { 
        'Content-Type': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/configuration/carriers/{carrier_id}/adddayofweekblocked'.format(carrier_id='carrier_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_logistics_capacity_resources_carriercapacity_typeshipping_policy_id_time_frames_get(client):
    """Test case for api_logistics_capacity_resources_carriercapacity_typeshipping_policy_id_time_frames_get

    Search capacity reservations in time range
    """
    params = [('rangeStart', 'yyyy-mm-dd'),
                    ('rangeEnd', 'yyyy-mm-dd')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/vnd.vtex.availability.v1+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics-capacity/resources/carrier@{capacityType}@{shippingPolicyId}/time-frames'.format(capacity_type='{{capacityType}}', shipping_policy_id='{{shippingPolicyId}}'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_logistics_capacity_resources_carriercapacity_typeshipping_policy_id_time_frames_window_day_fwindow_start_time_twindow_end_time_get(client):
    """Test case for api_logistics_capacity_resources_carriercapacity_typeshipping_policy_id_time_frames_window_day_fwindow_start_time_twindow_end_time_get

    Get capacity reservation usage by window
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/vnd.vtex.availability.v1+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics-capacity/resources/carrier@{capacityType}@{shippingPolicyId}/time-frames/{window_day_fwindow_start_time_twindow_end_time}'.format(capacity_type='{{capacityType}}', shipping_policy_id='{{shippingPolicyId}}', window_day='yyyy-mm-dd', window_start_time='hhmm', window_end_time='hhmm'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_remove_blocked_delivery_windows(client):
    """Test case for remove_blocked_delivery_windows

    Remove blocked delivery windows
    """
    body = "2016-08-09T08:00:00"
    headers = { 
        'Content-Type': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/configuration/carriers/{carrier_id}/removedayofweekblocked'.format(carrier_id='carrier_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_blocked_delivery_windows(client):
    """Test case for retrieve_blocked_delivery_windows

    Retrieve blocked delivery windows
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/carriers/{carrier_id}/getdayofweekblocked'.format(carrier_id='carrier_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

