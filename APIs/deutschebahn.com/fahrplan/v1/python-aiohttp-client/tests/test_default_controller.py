# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.board_response import BoardResponse
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.journey_response import JourneyResponse
from openapi_server.models.location_response import LocationResponse


pytestmark = pytest.mark.asyncio

async def test_arrival_board_id_get(client):
    """Test case for arrival_board_id_get

    Get arrival board of a location
    """
    params = [('date', '_date_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/freeplan/v1/arrivalBoard/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_departure_board_id_get(client):
    """Test case for departure_board_id_get

    Get departure board of a location
    """
    params = [('date', '_date_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/freeplan/v1/departureBoard/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_journey_details_id_get(client):
    """Test case for journey_details_id_get

    Get details about a single journey
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/freeplan/v1/journeyDetails/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_location_name_get(client):
    """Test case for location_name_get

    Get location information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/freeplan/v1/location/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

