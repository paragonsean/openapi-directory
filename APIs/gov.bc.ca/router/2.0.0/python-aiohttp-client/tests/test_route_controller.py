# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_optimal_route_output_format_get(client):
    """Test case for optimal_route_output_format_get

    Get the optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time.
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
        path='/optimalRoute.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_optimal_route_output_format_post(client):
    """Test case for optimal_route_output_format_post

    Get the path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time.
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
        path='/optimalRoute.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_output_format_get(client):
    """Test case for route_output_format_get

    Get the path, distance and travel time between a series of geographic points
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
        path='/route.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_output_format_post(client):
    """Test case for route_output_format_post

    Get the path, distance and travel time between a series of geographic points
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
        path='/route.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truck_optimal_route_output_format_get(client):
    """Test case for truck_optimal_route_output_format_get

    Get the optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time for a commercial vehicle
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
        path='/truck/optimalRoute.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truck_optimal_route_output_format_post(client):
    """Test case for truck_optimal_route_output_format_post

    Get the path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time.
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
        path='/truck/optimalRoute.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truck_route_output_format_get(client):
    """Test case for truck_route_output_format_get

    Get the path, distance and travel time between a series of geographic points for a commercial vehicle
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
        path='/truck/route.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truck_route_output_format_post(client):
    """Test case for truck_route_output_format_post

    Get the path, distance and travel time between a series of geographic points
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
        path='/truck/route.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

