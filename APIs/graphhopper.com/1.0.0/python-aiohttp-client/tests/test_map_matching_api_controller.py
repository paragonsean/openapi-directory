# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.gh_error import GHError
from openapi_server.models.route_response import RouteResponse


pytestmark = pytest.mark.asyncio

async def test_post_gpx(client):
    """Test case for post_gpx

    Map-match a GPX file
    """
    params = [('gps_accuracy', 56),
                    ('vehicle', 'vehicle_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1/match',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

