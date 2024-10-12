# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flux import Flux


pytestmark = pytest.mark.asyncio

async def test_app_api_endpoints_trapped_radiation_calculate_flux_mean(client):
    """Test case for app_api_endpoints_trapped_radiation_calculate_flux_mean

    Calculate mean particle flux 
    """
    params = [('model', 'AE9'),
                    ('coord_sys', 'GEI'),
                    ('coord_units', 'KM'),
                    ('coord1', 3216.6),
                    ('coord2', 35426),
                    ('coord3', 603.4),
                    ('year', 2017),
                    ('month', 1),
                    ('day', 1),
                    ('hour', 0),
                    ('minute', 0),
                    ('second', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/trapped/flux_mean',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_api_endpoints_trapped_radiation_calculate_flux_percentile(client):
    """Test case for app_api_endpoints_trapped_radiation_calculate_flux_percentile

    Calculate percentile particle flux 
    """
    params = [('model', 'AE9'),
                    ('coord_sys', 'GEI'),
                    ('coord_units', 'KM'),
                    ('coord1', 3216.6),
                    ('coord2', 35426),
                    ('coord3', 603.4),
                    ('year', 2017),
                    ('month', 1),
                    ('day', 1),
                    ('hour', 0),
                    ('minute', 0),
                    ('second', 0),
                    ('percentile', 50)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/trapped/flux_percentile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

