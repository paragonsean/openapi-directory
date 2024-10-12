# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.response_item import ResponseItem


pytestmark = pytest.mark.asyncio

async def test_balance_lookup(client):
    """Test case for balance_lookup

    Check Balance
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v1/balance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

