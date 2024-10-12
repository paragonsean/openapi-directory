# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.countries_response import CountriesResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_atms_v1_country_get(client):
    """Test case for atms_v1_country_get

    Returns countries with valid ATM locations.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/atms/v1/country',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

