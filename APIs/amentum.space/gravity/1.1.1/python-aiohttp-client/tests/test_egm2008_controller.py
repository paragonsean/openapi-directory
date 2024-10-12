# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.anomaly import Anomaly
from openapi_server.models.height import Height


pytestmark = pytest.mark.asyncio

async def test_app_api_egm2008_endpoints_egm2008_calculate_anomaly(client):
    """Test case for app_api_egm2008_endpoints_egm2008_calculate_anomaly

    Calculate gravity anomaly values 
    """
    params = [('latitude', -45),
                    ('longitude', 45)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/egm2008/gravity_anomaly',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_api_egm2008_endpoints_egm2008_calculate_height(client):
    """Test case for app_api_egm2008_endpoints_egm2008_calculate_height

    Calculate the geoid height 
    """
    params = [('latitude', -45),
                    ('longitude', 45)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/egm2008/geoid_height',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

