# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.prediction import Prediction


pytestmark = pytest.mark.asyncio

async def test_get_airport_on_time_prediction(client):
    """Test case for get_airport_on_time_prediction

    Returns a percentage of on-time flight departures from a given airport.
    """
    params = [('airportCode', 'JFK'),
                    ('date', '2023-11-12')]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/airport/predictions/on-time',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

