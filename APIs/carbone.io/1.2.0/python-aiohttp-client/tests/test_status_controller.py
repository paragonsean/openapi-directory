# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.status_get200_response import StatusGet200Response


pytestmark = pytest.mark.asyncio

async def test_status_get(client):
    """Test case for status_get

    Fetch the API status and version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

