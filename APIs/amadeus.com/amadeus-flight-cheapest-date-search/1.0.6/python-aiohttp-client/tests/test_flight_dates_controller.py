# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.flight_dates import FlightDates


pytestmark = pytest.mark.asyncio

async def test_get_flight_dates(client):
    """Test case for get_flight_dates

    Find the cheapest flight dates from an origin to a destination.
    """
    params = [('origin', 'MAD'),
                    ('destination', 'MUC'),
                    ('departureDate', 'departure_date_example'),
                    ('oneWay', False),
                    ('duration', 'duration_example'),
                    ('nonStop', False),
                    ('maxPrice', 56),
                    ('viewBy', 'view_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/shopping/flight-dates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

