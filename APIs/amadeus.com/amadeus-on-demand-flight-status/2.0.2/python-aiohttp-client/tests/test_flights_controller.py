# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error401 import Error401
from openapi_server.models.error500 import Error500
from openapi_server.models.success_flights import SuccessFlights


pytestmark = pytest.mark.asyncio

async def test_get_flights_status(client):
    """Test case for get_flights_status

    Retrieves a unique flight by search criteria.
    """
    params = [('carrierCode', 'TP'),
                    ('flightNumber', '487'),
                    ('scheduledDepartureDate', '2023-08-01'),
                    ('operationalSuffix', 'operational_suffix_example')]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v2/schedule/flights',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

