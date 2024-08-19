# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_api_parma_endpoints_parma_ambient_dose200_response import AppApiParmaEndpointsPARMAAmbientDose200Response
from openapi_server.models.app_api_parma_endpoints_parma_differential_intensity200_response import AppApiParmaEndpointsPARMADifferentialIntensity200Response
from openapi_server.models.app_api_parma_endpoints_parma_effective_dose200_response import AppApiParmaEndpointsPARMAEffectiveDose200Response


pytestmark = pytest.mark.asyncio

async def test_app_api_parma_endpoints_parma_ambient_dose(client):
    """Test case for app_api_parma_endpoints_parma_ambient_dose

    The ambient dose equivalent rate calculated for a single particle type, or accumulated over all particle types. 
    """
    params = [('altitude', 11),
                    ('atmospheric_depth', 0.92),
                    ('latitude', 30),
                    ('longitude', 30),
                    ('year', 2019),
                    ('month', 12),
                    ('day', 1),
                    ('particle', 'proton')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/parma/ambient_dose',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_api_parma_endpoints_parma_differential_intensity(client):
    """Test case for app_api_parma_endpoints_parma_differential_intensity

    The energy differential intensity of a particle at a given zenith angle.
    """
    params = [('altitude', 11),
                    ('atmospheric_depth', 0.92),
                    ('latitude', 30),
                    ('longitude', 30),
                    ('year', 2019),
                    ('month', 12),
                    ('day', 1),
                    ('particle', 'proton'),
                    ('angle', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/parma/differential_intensity',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_api_parma_endpoints_parma_effective_dose(client):
    """Test case for app_api_parma_endpoints_parma_effective_dose

    The effective dose rate calculated for a single particle type, or accumulated over all particle types. 
    """
    params = [('altitude', 11),
                    ('atmospheric_depth', 0.92),
                    ('latitude', 30),
                    ('longitude', 30),
                    ('year', 2019),
                    ('month', 12),
                    ('day', 1),
                    ('particle', 'proton')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/parma/effective_dose',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

