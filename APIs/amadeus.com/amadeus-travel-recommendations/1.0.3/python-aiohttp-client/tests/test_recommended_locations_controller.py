# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_recommended_location200_response import GetRecommendedLocation200Response


pytestmark = pytest.mark.asyncio

async def test_get_recommended_location(client):
    """Test case for get_recommended_location

    GET recommended destinations
    """
    params = [('cityCodes', 'PAR'),
                    ('travelerCountryCode', 'FR'),
                    ('destinationCountryCodes', 'destination_country_codes_example')]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference-data/recommended-locations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

