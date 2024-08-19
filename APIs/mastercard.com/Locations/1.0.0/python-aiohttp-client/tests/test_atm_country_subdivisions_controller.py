# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.country_subdivision_response import CountrySubdivisionResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_atms_v1_countrysubdivision_get(client):
    """Test case for atms_v1_countrysubdivision_get

    Returns country subdivisions that have ATM locations.  A country subdivision is a segment within a country (ex  state or province). Country subdivisions are only available for the US and Canada.
    """
    params = [('Country', 'USA')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/atms/v1/countrysubdivision',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

