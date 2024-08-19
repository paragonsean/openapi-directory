# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_api_endpoints_jb2008_sample_atmosphere200_response import AppApiEndpointsJB2008SampleAtmosphere200Response


pytestmark = pytest.mark.asyncio

async def test_app_api_endpoints_jb2008_sample_atmosphere(client):
    """Test case for app_api_endpoints_jb2008_sample_atmosphere

    Compute atmospheric density and temperatures 
    """
    params = [('year', 2020),
                    ('month', 5),
                    ('day', 23),
                    ('altitude', 300),
                    ('geodetic_latitude', 42),
                    ('geodetic_longitude', 42),
                    ('utc', 2)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/jb2008',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

