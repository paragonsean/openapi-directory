# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.airports_api_controllers_airport_iata_controller_response import AirportsAPIControllersAirportIATAControllerResponse


pytestmark = pytest.mark.asyncio

async def test_airport_iata_airport_iata_search(client):
    """Test case for airport_iata_airport_iata_search

    Search for airport by IATA code
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/airport/iata/{airport_iata}'.format(airport_iata='airport_iata_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

