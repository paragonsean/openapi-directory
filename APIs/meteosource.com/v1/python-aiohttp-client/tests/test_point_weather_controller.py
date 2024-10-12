# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.air_quality_point_data import AirQualityPointData
from openapi_server.models.general_request_error import GeneralRequestError
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.language import Language
from openapi_server.models.point_point_data import PointPointData
from openapi_server.models.units import Units


pytestmark = pytest.mark.asyncio

async def test_air_quality_air_quality_get(client):
    """Test case for air_quality_air_quality_get

    Returns air quality data for a single point (geographic name or GPS)
    """
    params = [('place_id', 'place_id_example'),
                    ('lat', 'lat_example'),
                    ('lon', 'lon_example'),
                    ('timezone', 'timezone_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
        'APIKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/premium/air_quality',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_point_point_get(client):
    """Test case for point_point_get

    Returns weather data for a single point (geographic name or GPS)
    """
    params = [('place_id', 'place_id_example'),
                    ('lat', 'lat_example'),
                    ('lon', 'lon_example'),
                    ('sections', 'current,hourly'),
                    ('timezone', 'timezone_example'),
                    ('language', openapi_server.Language()),
                    ('units', openapi_server.Units()),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
        'APIKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/premium/point',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

