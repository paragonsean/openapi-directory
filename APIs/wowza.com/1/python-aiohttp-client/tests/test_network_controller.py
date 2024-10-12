# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.usage_network_stream_sources import UsageNetworkStreamSources
from openapi_server.models.usage_network_stream_targets import UsageNetworkStreamTargets
from openapi_server.models.usage_network_transcoders import UsageNetworkTranscoders


pytestmark = pytest.mark.asyncio

async def test_usage_network_stream_sources_index(client):
    """Test case for usage_network_stream_sources_index

    Fetch network usage for all stream sources
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
        path='/api/v1/usage/network/stream_sources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_usage_network_stream_targets_index(client):
    """Test case for usage_network_stream_targets_index

    Fetch network usage for all stream targets
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
        path='/api/v1/usage/network/stream_targets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_usage_network_transcoders_index(client):
    """Test case for usage_network_transcoders_index

    Fetch network usage for all transcoders
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
        path='/api/v1/usage/network/transcoders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

