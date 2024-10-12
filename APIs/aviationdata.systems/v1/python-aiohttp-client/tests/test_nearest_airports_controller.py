# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.airports_api_controllers_nearest_airports_controller_response import AirportsAPIControllersNearestAirportsControllerResponse


pytestmark = pytest.mark.asyncio

async def test_nearest_airports_nearest_airport_list(client):
    """Test case for nearest_airports_nearest_airport_list

    Search for airports by location
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/airport/nearest/{result_count}/{latitude}/{longitude}'.format(result_count=56, latitude=3.4, longitude=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

