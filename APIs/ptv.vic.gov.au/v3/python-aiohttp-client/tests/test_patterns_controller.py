# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_stopping_pattern import V3StoppingPattern


pytestmark = pytest.mark.asyncio

async def test_patterns_get_pattern_by_run(client):
    """Test case for patterns_get_pattern_by_run

    View the stopping pattern for a specific trip/service run
    """
    params = [('expand', ['expand_example']),
                    ('stop_id', 56),
                    ('date_utc', '2013-10-20T19:20:30+01:00'),
                    ('include_skipped_stops', True),
                    ('include_geopath', True),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/pattern/run/{run_ref}/route_type/{route_type}'.format(run_ref='run_ref_example', route_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

