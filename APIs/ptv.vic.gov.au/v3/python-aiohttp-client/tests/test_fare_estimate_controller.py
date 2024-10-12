# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_fare_estimate_get_fare_estimate_by_zone(client):
    """Test case for fare_estimate_get_fare_estimate_by_zone

    Estimate a fare by zone
    """
    params = [('journey_touch_on_utc', '2013-10-20T19:20:30+01:00'),
                    ('journey_touch_off_utc', '2013-10-20T19:20:30+01:00'),
                    ('is_journey_in_free_tram_zone', True),
                    ('travelled_route_types', [56]),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/fare_estimate/min_zone/{min_zone}/max_zone/{max_zone}'.format(min_zone=56, max_zone=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

