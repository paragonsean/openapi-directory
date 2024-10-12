# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.availability_day_view_model import AvailabilityDayViewModel
from openapi_server.models.availability_view_model import AvailabilityViewModel
from openapi_server.models.unavailable_time_list_view_model import UnavailableTimeListViewModel


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_availability_service_id_start_date_end_date_days_get(client):
    """Test case for consumer_v1_availability_service_id_start_date_end_date_days_get

    Get Available Days
    """
    params = [('locationId', 'location_id_example'),
                    ('resourceId', 'resource_id_example'),
                    ('tzOffset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/availability/{service_id}/{start_date}/{end_date}/days'.format(service_id='service_id_example', start_date='2013-10-20T19:20:30+01:00', end_date='2013-10-20T19:20:30+01:00'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_availability_service_id_start_date_end_date_get(client):
    """Test case for consumer_v1_availability_service_id_start_date_end_date_get

    Get Available Times
    """
    params = [('startTime', 56),
                    ('endTime', 56),
                    ('locationId', 'location_id_example'),
                    ('resourceId', 'resource_id_example'),
                    ('resourceGroupId', 'resource_group_id_example'),
                    ('resourceIds', 'resource_ids_example'),
                    ('roundRobin', 'round_robin_example'),
                    ('duration', 56),
                    ('interval', 56),
                    ('timezoneName', 'timezone_name_example'),
                    ('tzOffset', 56),
                    ('destination', 'destination_example'),
                    ('dayAvailabilityStartDate', '2013-10-20T19:20:30+01:00'),
                    ('dayAvailability', 56),
                    ('firstDayAvailable', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/availability/{service_id}/{start_date}/{end_date}'.format(service_id='service_id_example', start_date='2013-10-20T19:20:30+01:00', end_date='2013-10-20T19:20:30+01:00'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_availability_service_id_start_date_end_date_unavailable_get(client):
    """Test case for consumer_v1_availability_service_id_start_date_end_date_unavailable_get

    Get Unavailable Times
    """
    params = [('locationId', 'location_id_example'),
                    ('resourceId', 'resource_id_example'),
                    ('duration', 56),
                    ('tzOffset', 56),
                    ('skipTimePastUnavailability', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/availability/{service_id}/{start_date}/{end_date}/unavailable'.format(service_id='service_id_example', start_date='2013-10-20T19:20:30+01:00', end_date='2013-10-20T19:20:30+01:00'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

