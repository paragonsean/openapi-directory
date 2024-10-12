# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_api_wmm_endpoints_wmm_magnetic_field200_response import AppApiWmmEndpointsWMMMagneticField200Response


pytestmark = pytest.mark.asyncio

async def test_app_api_wmm_endpoints_wmm_magnetic_field(client):
    """Test case for app_api_wmm_endpoints_wmm_magnetic_field

    Calculate magnetic declination, inclination, total field intensity, and grid variation 
    """
    params = [('altitude', 10),
                    ('latitude', 80),
                    ('longitude', 100),
                    ('year', 2020.5)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/wmm/magnetic_field',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

