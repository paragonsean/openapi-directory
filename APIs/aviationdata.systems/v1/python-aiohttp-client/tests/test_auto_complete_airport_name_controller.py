# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.airports_api_controllers_auto_complete_airport_name_controller_response import AirportsAPIControllersAutoCompleteAirportNameControllerResponse


pytestmark = pytest.mark.asyncio

async def test_auto_complete_airport_name_airport_name_search(client):
    """Test case for auto_complete_airport_name_airport_name_search

    Autocomplete airport names. Returns a maximum of 10 airport names.
    """
    params = [('airport_service_type', 'airport_service_type_example'),
                    ('optional_country_code', 'optional_country_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/airport/autocomplete/{airport_name}'.format(airport_name='airport_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

