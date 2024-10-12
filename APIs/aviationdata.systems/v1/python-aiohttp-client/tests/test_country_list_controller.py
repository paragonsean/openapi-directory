# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.airports_api_controllers_country_list_controller_country_list_response import AirportsAPIControllersCountryListControllerCountryListResponse


pytestmark = pytest.mark.asyncio

async def test_country_list_country_airport_list(client):
    """Test case for country_list_country_airport_list

    Country list. Returns a list of countries where airport data is available
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/country_list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

