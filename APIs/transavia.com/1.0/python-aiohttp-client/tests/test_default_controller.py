# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.airport_details_dto import AirportDetailsDto
from openapi_server.models.airport_dto import AirportDto
from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.internal_server_error_response import InternalServerErrorResponse
from openapi_server.models.nearest_airport_dto import NearestAirportDto


pytestmark = pytest.mark.asyncio

async def test_call58d8bcb7a9e6240e200cff24(client):
    """Test case for call58d8bcb7a9e6240e200cff24

    All airports
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/airports/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call58d8bcb7a9e6240e200cff25(client):
    """Test case for call58d8bcb7a9e6240e200cff25

    Airport by id.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/airports/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call58d8bcb8a9e6240e200cff26(client):
    """Test case for call58d8bcb8a9e6240e200cff26

    Airport(s) by country code.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/airports/countrycode/{country_code}'.format(country_code='country_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call58d8bcb8a9e6240e200cff27(client):
    """Test case for call58d8bcb8a9e6240e200cff27

    Nearest airport(s) by geo coordinates.
    """
    params = [('latitude', 'latitude_example'),
                    ('longitude', 'longitude_example'),
                    ('maxDistanceInKm', 'max_distance_in_km_example'),
                    ('limit', 'limit_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/airports/nearest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call58d8bcb8a9e6240e200cff28(client):
    """Test case for call58d8bcb8a9e6240e200cff28

    Nearest airport(s) by airport id.
    """
    params = [('maxDistanceInKm', 'max_distance_in_km_example'),
                    ('limit', 'limit_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/airports/nearest/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

