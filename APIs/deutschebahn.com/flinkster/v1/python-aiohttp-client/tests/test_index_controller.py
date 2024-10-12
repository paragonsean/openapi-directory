# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_collection import JsonCollection


pytestmark = pytest.mark.asyncio

async def test_get_index(client):
    """Test case for get_index

    Show index.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/flinkster-api-ng/v1/index',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

