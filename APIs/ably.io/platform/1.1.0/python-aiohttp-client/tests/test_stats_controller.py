# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_stats(client):
    """Test case for get_stats

    Retrieve usage statistics for an application
    """
    params = [('format', 'format_example'),
                    ('start', 'start_example'),
                    ('limit', 56),
                    ('end', 'now'),
                    ('direction', backwards),
                    ('unit', minute)]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_time(client):
    """Test case for get_time

    Get the service time
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
    }
    response = await client.request(
        method='GET',
        path='/time',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

