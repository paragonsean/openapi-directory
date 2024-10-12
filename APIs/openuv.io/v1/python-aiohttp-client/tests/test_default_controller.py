# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.forecast import Forecast
from openapi_server.models.protection_result import ProtectionResult
from openapi_server.models.uv_index_result import UvIndexResult


pytestmark = pytest.mark.asyncio

async def test_forecast_get(client):
    """Test case for forecast_get

    
    """
    params = [('lat', 78.67),
                    ('lng', 115.67),
                    ('alt', 1050),
                    ('ozone', 304.5),
                    ('dt', '2018-02-04T04:39:06.467Z')]
    headers = { 
        'Accept': 'application/json',
        'x_access_token': 'x_access_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/forecast',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protection_get(client):
    """Test case for protection_get

    
    """
    params = [('lat', 78.67),
                    ('lng', 115.67),
                    ('from', 2.5),
                    ('to', 3.6),
                    ('alt', 1050),
                    ('ozone', 304.5)]
    headers = { 
        'Accept': 'application/json',
        'x_access_token': 'x_access_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/protection',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_uv_get(client):
    """Test case for uv_get

    
    """
    params = [('lat', 78.67),
                    ('lng', 115.67),
                    ('alt', 1050),
                    ('ozone', 304.5),
                    ('dt', '2018-02-04T04:39:06.467Z')]
    headers = { 
        'Accept': 'application/json',
        'x_access_token': 'x_access_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/uv',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

