# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.prediction import Prediction


pytestmark = pytest.mark.asyncio

async def test_get_trip_purpose_prediction(client):
    """Test case for get_trip_purpose_prediction

    Returns the forecast purpose of a trip
    """
    params = [('originLocationCode', 'NYC'),
                    ('destinationLocationCode', 'MAD'),
                    ('departureDate', '2023-12-01'),
                    ('returnDate', '2023-12-12'),
                    ('searchDate', 'search_date_example')]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/travel/predictions/trip-purpose',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

