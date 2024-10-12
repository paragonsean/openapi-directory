# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.usage_storage_peak_recording import UsageStoragePeakRecording


pytestmark = pytest.mark.asyncio

async def test_usage_storage_peak_recording_index(client):
    """Test case for usage_storage_peak_recording_index

    Fetch peak recording storage
    """
    params = [('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/usage/storage/peak_recording',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

