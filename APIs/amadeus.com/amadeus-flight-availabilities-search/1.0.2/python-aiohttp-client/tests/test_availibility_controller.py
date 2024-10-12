# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_flight_availabilities_query import GetFlightAvailabilitiesQuery
from openapi_server.models.success_availability import SuccessAvailability


pytestmark = pytest.mark.asyncio

async def test_search_flight_availabilities(client):
    """Test case for search_flight_availabilities

    Return list of Flight Availabilities based on posted searching criteria.
    """
    get_flight_availabilities_body = openapi_server.GetFlightAvailabilitiesQuery()
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
        'Content-Type': 'application/vnd.amadeus+json',
        'x_http_method_override': 'GET',
    }
    response = await client.request(
        method='POST',
        path='/v1/shopping/availability/flight-availabilities',
        headers=headers,
        json=get_flight_availabilities_body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

