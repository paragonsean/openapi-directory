# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_distance_between_pairs_output_format_get(client):
    """Test case for distance_between_pairs_output_format_get

    Get distance and travel time between each pair of geographic points
    """
    params = [('fromPoints', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('toPoints', '-124.972951,49.715181,-123.139464,49.704015'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results'),
                    ('maxPairs', 56)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/distance/betweenPairs.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distance_between_pairs_output_format_post(client):
    """Test case for distance_between_pairs_output_format_post

    Get distance and travel time between each pair of geographic points
    """
    params = [('fromPoints', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('toPoints', '-124.972951,49.715181,-123.139464,49.704015'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results'),
                    ('maxPairs', 56)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/distance/betweenPairs.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distance_output_format_get(client):
    """Test case for distance_output_format_get

    Get distance and travel time between two geographic points
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
        path='/distance.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distance_output_format_post(client):
    """Test case for distance_output_format_post

    Get distance and travel time between two geographic points
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
        path='/distance.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truck_distance_between_pairs_output_format_get(client):
    """Test case for truck_distance_between_pairs_output_format_get

    Get distance and travel time between each pair of geographic points for a commercial vehicle
    """
    params = [('fromPoints', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('toPoints', '-124.972951,49.715181,-123.139464,49.704015'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results'),
                    ('maxPairs', 56)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/truck/distance/betweenPairs.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truck_distance_between_pairs_output_format_post(client):
    """Test case for truck_distance_between_pairs_output_format_post

    Get distance and travel time between each pair of geographic points
    """
    params = [('fromPoints', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('toPoints', '-124.972951,49.715181,-123.139464,49.704015'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results'),
                    ('maxPairs', 56)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/truck/distance/betweenPairs.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truck_distance_output_format_get(client):
    """Test case for truck_distance_output_format_get

    Get distance and travel time between two geographic points for a commercial vehicle
    """
    params = [('points', '-123.70794,48.77869,-123.53785,48.38200'),
                    ('outputSRS', 4326),
                    ('criteria', shortest),
                    ('distanceUnit', km),
                    ('roundTrip', False),
                    ('departure', '2013-10-20T19:20:30+01:00'),
                    ('correctSide', False),
                    ('truckRouteMultiplier', 9),
                    ('disable', 'sc,tf,ev,td'),
                    ('routeDescription', 'Routing results')]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/truck/distance.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_truck_distance_output_format_post(client):
    """Test case for truck_distance_output_format_post

    Get distance and travel time between two geographic points
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
        path='/truck/distance.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

