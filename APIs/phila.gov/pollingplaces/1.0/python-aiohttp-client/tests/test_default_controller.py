# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.features import Features


pytestmark = pytest.mark.asyncio

async def test_root_get(client):
    """Test case for root_get

    Get Polling Places Data
    """
    params = [('ward', 56),
                    ('division', 56),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/polling-places/v1/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

