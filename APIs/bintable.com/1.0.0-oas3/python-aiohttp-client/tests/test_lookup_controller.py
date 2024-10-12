# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.response_item import ResponseItem


pytestmark = pytest.mark.asyncio

async def test_bin_lookup(client):
    """Test case for bin_lookup

    Lookup for bin
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/{bin}'.format(bin='bin_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

