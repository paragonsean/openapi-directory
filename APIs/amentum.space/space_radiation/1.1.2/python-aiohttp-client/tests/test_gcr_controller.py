# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flux_at_energy import FluxAtEnergy


pytestmark = pytest.mark.asyncio

async def test_app_api_endpoints_gcr_calculate_dlr_flux(client):
    """Test case for app_api_endpoints_gcr_calculate_dlr_flux

    Calculate particle flux  
    """
    params = [('year', 2017),
                    ('month', 1),
                    ('day', 1),
                    ('z', 6),
                    ('energy', 100)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/gcr/flux_dlr',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

