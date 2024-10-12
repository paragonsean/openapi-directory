# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.gh_error import GHError
from openapi_server.models.geocoding_response import GeocodingResponse


pytestmark = pytest.mark.asyncio

async def test_get_geocode(client):
    """Test case for get_geocode

    Geocoding Endpoint
    """
    params = [('q', 'q_example'),
                    ('locale', 'en'),
                    ('limit', 10),
                    ('reverse', False),
                    ('debug', False),
                    ('point', 'point_example'),
                    ('provider', 'default')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1/geocode',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

