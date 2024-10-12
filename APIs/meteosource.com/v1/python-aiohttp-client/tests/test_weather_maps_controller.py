# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.general_request_error import GeneralRequestError
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_map_map_get(client):
    """Test case for map_map_get

    Returns PNG weather map for given area and variable
    """
    params = [('tile_x', 56),
                    ('tile_y', 56),
                    ('tile_zoom', 56),
                    ('min_lat', 'min_lat_example'),
                    ('min_lon', 'min_lon_example'),
                    ('max_lat', 'max_lat_example'),
                    ('max_lon', 'max_lon_example'),
                    ('variable', 'variable_example'),
                    ('datetime', 'datetime_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
        'APIKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/premium/map',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

