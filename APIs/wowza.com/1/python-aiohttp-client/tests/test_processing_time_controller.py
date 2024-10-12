# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error422_invalid_time_format import Error422InvalidTimeFormat
from openapi_server.models.usage_time_transcoders import UsageTimeTranscoders


pytestmark = pytest.mark.asyncio

async def test_usage_time_transcoders_index(client):
    """Test case for usage_time_transcoders_index

    Fetch stream processing time
    """
    params = [('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('transcoder_type', 'transcoder_type_example'),
                    ('billing_mode', 'billing_mode_example')]
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/usage/time/transcoders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

