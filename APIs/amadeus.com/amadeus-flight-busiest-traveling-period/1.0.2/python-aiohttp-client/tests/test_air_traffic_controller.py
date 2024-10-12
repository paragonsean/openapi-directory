# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.success import Success


pytestmark = pytest.mark.asyncio

async def test_get_air_traffic(client):
    """Test case for get_air_traffic

    Returns a list of air traffic reports.
    """
    params = [('cityCode', 'MAD'),
                    ('period', '2017'),
                    ('direction', ARRIVING)]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/travel/analytics/air-traffic/busiest-period',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

