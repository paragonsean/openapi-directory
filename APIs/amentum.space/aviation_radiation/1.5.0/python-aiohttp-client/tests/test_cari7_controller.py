# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_api_cari7_endpoints_cari7_ambient_dose200_response import AppApiCari7EndpointsCARI7AmbientDose200Response
from openapi_server.models.app_api_cari7_endpoints_cari7_effective_dose200_response import AppApiCari7EndpointsCARI7EffectiveDose200Response


pytestmark = pytest.mark.asyncio

async def test_app_api_cari7_endpoints_cari7_ambient_dose(client):
    """Test case for app_api_cari7_endpoints_cari7_ambient_dose

    The ambient dose equivalent rate calculated for a single particle type, or accumulated over all particle types. 
    """
    params = [('altitude', 11),
                    ('latitude', 30),
                    ('longitude', 30),
                    ('year', 2019),
                    ('month', 12),
                    ('day', 1),
                    ('utc', 3),
                    ('particle', 'total')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/cari7/ambient_dose',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_api_cari7_endpoints_cari7_effective_dose(client):
    """Test case for app_api_cari7_endpoints_cari7_effective_dose

    The effective dose rate calculated for a single particle type, or accumulated over all particle types. 
    """
    params = [('altitude', 11),
                    ('latitude', 30),
                    ('longitude', 30),
                    ('year', 2019),
                    ('month', 12),
                    ('day', 1),
                    ('utc', 3),
                    ('particle', 'total')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/cari7/effective_dose',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

