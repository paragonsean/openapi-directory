# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.trips_trip_details200_response import TripsTripDetails200Response


pytestmark = pytest.mark.asyncio

async def test_trips_trip_details_0(client):
    """Test case for trips_trip_details_0

    Trips - trip details
    """
    params = [('trackToken', '')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/mobilesdk/stage/track/get_track/v1',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

