# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v3_directions_response import V3DirectionsResponse
from openapi_server.models.v3_error_response import V3ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_directions_for_direction(client):
    """Test case for directions_for_direction

    View all routes for a direction of travel
    """
    params = [('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/directions/{direction_id}'.format(direction_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_directions_for_direction_and_type(client):
    """Test case for directions_for_direction_and_type

    View all routes of a particular type for a direction of travel
    """
    params = [('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/directions/{direction_id}/route_type/{route_type}'.format(direction_id=56, route_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_directions_for_route(client):
    """Test case for directions_for_route

    View directions that a route travels in
    """
    params = [('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/directions/route/{route_id}'.format(route_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

