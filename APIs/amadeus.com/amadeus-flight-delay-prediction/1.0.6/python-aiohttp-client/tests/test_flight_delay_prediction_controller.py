# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.prediction import Prediction


pytestmark = pytest.mark.asyncio

async def test_get_flight_delay_prediction(client):
    """Test case for get_flight_delay_prediction

    Return the delay segment where the flight is likely to lay.
    """
    params = [('originLocationCode', 'NCE'),
                    ('destinationLocationCode', 'IST'),
                    ('departureDate', '2020-08-01'),
                    ('departureTime', '66000'),
                    ('arrivalDate', '2020-08-01'),
                    ('arrivalTime', '80100'),
                    ('aircraftCode', '321'),
                    ('carrierCode', 'TK'),
                    ('flightNumber', '1816'),
                    ('duration', 'PT31H10M')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/travel/predictions/flight-delay',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

