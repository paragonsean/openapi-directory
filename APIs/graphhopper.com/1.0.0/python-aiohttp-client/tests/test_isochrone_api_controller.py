# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.gh_error import GHError
from openapi_server.models.isochrone_response import IsochroneResponse
from openapi_server.models.vehicle_profile_id import VehicleProfileId


pytestmark = pytest.mark.asyncio

async def test_get_isochrone(client):
    """Test case for get_isochrone

    Isochrone Endpoint
    """
    params = [('point', 'point_example'),
                    ('time_limit', 600),
                    ('distance_limit', 56),
                    ('vehicle', car),
                    ('buckets', 1),
                    ('reverse_flow', False),
                    ('weighting', fastest)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1/isochrone',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

