# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_operations_flightstatus_arrivals_by_airport_code_and_from_date_time_get(client):
    """Test case for operations_flightstatus_arrivals_by_airport_code_and_from_date_time_get

    Flight Status at Arrival Airport
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/operations/flightstatus/arrivals/{airport_code}/{from_date_time}'.format(airport_code='airport_code_example', from_date_time='from_date_time_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_flightstatus_by_flight_number_and_date_get(client):
    """Test case for operations_flightstatus_by_flight_number_and_date_get

    Flight Status
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/operations/flightstatus/{flight_number}/{_date}'.format(flight_number='flight_number_example', _date='_date_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_flightstatus_departures_by_airport_code_and_from_date_time_get(client):
    """Test case for operations_flightstatus_departures_by_airport_code_and_from_date_time_get

    Flight Status at Departure Airport
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/operations/flightstatus/departures/{airport_code}/{from_date_time}'.format(airport_code='airport_code_example', from_date_time='from_date_time_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_flightstatus_route_date_by_origin_and_destination_get(client):
    """Test case for operations_flightstatus_route_date_by_origin_and_destination_get

    Flight Status by Route
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/operations/flightstatus/route/{origin}/{destination}/{_date}'.format(origin='origin_example', destination='destination_example', _date='_date_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_schedules_from_date_time_by_origin_and_destination_get(client):
    """Test case for operations_schedules_from_date_time_by_origin_and_destination_get

    Flight Schedules
    """
    params = [('directFlights', True),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/operations/schedules/{origin}/{destination}/{from_date_time}'.format(origin='origin_example', destination='destination_example', from_date_time='from_date_time_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

