# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.cost_estimate_response import CostEstimateResponse
from openapi_server.models.eta_estimate_response import EtaEstimateResponse
from openapi_server.models.nearby_drivers_response import NearbyDriversResponse
from openapi_server.models.ride_types_response import RideTypesResponse


pytestmark = pytest.mark.asyncio

async def test_get_cost(client):
    """Test case for get_cost

    Cost estimates
    """
    params = [('ride_type', 'ride_type_example'),
                    ('start_lat', 3.4),
                    ('start_lng', 3.4),
                    ('end_lat', 3.4),
                    ('end_lng', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/cost',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_drivers(client):
    """Test case for get_drivers

    Available drivers nearby
    """
    params = [('lat', 3.4),
                    ('lng', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/drivers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_eta(client):
    """Test case for get_eta

    Pickup ETAs
    """
    params = [('lat', 3.4),
                    ('lng', 3.4),
                    ('destination_lat', 3.4),
                    ('destination_lng', 3.4),
                    ('ride_type', 'ride_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/eta',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ride_types(client):
    """Test case for get_ride_types

    Types of rides
    """
    params = [('lat', 3.4),
                    ('lng', 3.4),
                    ('ride_type', 'ride_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/ridetypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

