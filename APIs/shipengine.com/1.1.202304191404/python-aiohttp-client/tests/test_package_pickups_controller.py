# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_pickup_by_id_response_body import DeletePickupByIdResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_pickup_by_id_response_body import GetPickupByIdResponseBody
from openapi_server.models.get_pickups_response_body import GetPickupsResponseBody
from openapi_server.models.schedule_pickup_request_body import SchedulePickupRequestBody
from openapi_server.models.schedule_pickup_response_body import SchedulePickupResponseBody


pytestmark = pytest.mark.asyncio

async def test_delete_scheduled_pickup(client):
    """Test case for delete_scheduled_pickup

    Delete a Scheduled Pickup
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/pickups/{pickup_id}'.format(pickup_id='pickup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pickup_by_id(client):
    """Test case for get_pickup_by_id

    Get Pickup By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/pickups/{pickup_id}'.format(pickup_id='pickup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_scheduled_pickups(client):
    """Test case for list_scheduled_pickups

    List Scheduled Pickups
    """
    params = [('carrier_id', 'carrier_id_example'),
                    ('warehouse_id', 'warehouse_id_example'),
                    ('created_at_start', '2019-03-12T19:24:13.657Z'),
                    ('created_at_end', '2019-03-12T19:24:13.657Z'),
                    ('page', 1),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/pickups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedule_pickup(client):
    """Test case for schedule_pickup

    Schedule a Pickup
    """
    body = openapi_server.SchedulePickupRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/pickups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

