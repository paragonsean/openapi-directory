# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_outlet_geolocation_response import V3OutletGeolocationResponse
from openapi_server.models.v3_outlet_response import V3OutletResponse


pytestmark = pytest.mark.asyncio

async def test_outlets_get_all_outlets(client):
    """Test case for outlets_get_all_outlets

    List all ticket outlets
    """
    params = [('max_results', 56),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/outlets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outlets_get_outlets_by_geolocation(client):
    """Test case for outlets_get_outlets_by_geolocation

    List ticket outlets near a specific location
    """
    params = [('max_distance', 3.4),
                    ('max_results', 56),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/outlets/location/{latitudelongitude}'.format(latitude=3.4, longitude=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

