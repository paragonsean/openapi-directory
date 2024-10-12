# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_endpoints_airport_response import ApiEndpointsAirportResponse


pytestmark = pytest.mark.asyncio

async def test_airport_api_get_airport(client):
    """Test case for airport_api_get_airport

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/_ah/api/airportsapi/v1/airports/{icao_code}'.format(icao_code='icao_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

