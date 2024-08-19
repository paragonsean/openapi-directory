# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_directions_output_format_get(client):
    """Test case for directions_output_format_get

    Get the directions, path, distance and travel time between a series of geographic points
    """
    params = [('points', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('roundTrip', False),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results')]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/directions.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_directions_output_format_post(client):
    """Test case for directions_output_format_post

    Get the directions, path, distance and travel time between a series of geographic points
    """
    params = [('points', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('roundTrip', False),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results')]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/directions.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_optimal_directions_output_format_get(client):
    """Test case for optimal_directions_output_format_get

    Get the directions, optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time.
    """
    params = [('points', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('roundTrip', False),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results')]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/optimalDirections.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_optimal_directions_output_format_post(client):
    """Test case for optimal_directions_output_format_post

    Get the directions, optimal path, distance and travel time between a start point and one or more end points which are reordered to minimize total distance or time.
    """
    params = [('points', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('roundTrip', False),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results')]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/optimalDirections.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truck_directions_output_format_get(client):
    """Test case for truck_directions_output_format_get

    Get the directions, path, distance and travel time between a series of geographic points for a commercial vehicle
    """
    params = [('points', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('roundTrip', False),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('truckRouteMultiplier', 9),
                    ('partition', ''),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results')]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/truck/directions.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truck_directions_output_format_post(client):
    """Test case for truck_directions_output_format_post

    Get the directions, path, distance and travel time between a series of geographic points
    """
    params = [('points', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('roundTrip', False),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('truckRouteMultiplier', 9),
                    ('partition', ''),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results')]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/truck/directions.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truck_optimal_directions_output_format_get(client):
    """Test case for truck_optimal_directions_output_format_get

    Get the directions, optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time for a commercial vehicle
    """
    params = [('points', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('roundTrip', False),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('truckRouteMultiplier', 9),
                    ('partition', ''),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results')]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/truck/optimalDirections.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truck_optimal_directions_output_format_post(client):
    """Test case for truck_optimal_directions_output_format_post

    Get the directions, optimal path, distance and travel time between a start point and one or more end points which are reordered to minimize total distance or time.
    """
    params = [('points', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('roundTrip', False),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('truckRouteMultiplier', 9),
                    ('partition', ''),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results')]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/truck/optimalDirections.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

