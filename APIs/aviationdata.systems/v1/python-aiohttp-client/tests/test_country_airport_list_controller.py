# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.airports_api_controllers_country_airport_list_controller_airport_list_response import AirportsAPIControllersCountryAirportListControllerAirportListResponse


pytestmark = pytest.mark.asyncio

async def test_country_airport_list_country_airport_list(client):
    """Test case for country_airport_list_country_airport_list

    Country airports. Returns a list of airports for a country code(ISO 3166-1 alpha-2 code)
    """
    params = [('airport_service_type', 'airport_service_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/country/code/{country_code}'.format(country_code='country_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

