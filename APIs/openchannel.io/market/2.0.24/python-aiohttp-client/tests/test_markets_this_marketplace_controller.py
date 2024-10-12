# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.market import Market


pytestmark = pytest.mark.asyncio

async def test_markets_this_get(client):
    """Test case for markets_this_get

    Returns the current marketplace
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/markets/this',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

