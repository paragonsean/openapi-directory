# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.request import Request
from openapi_server.models.response import Response


pytestmark = pytest.mark.asyncio

async def test_root_post(client):
    """Test case for root_post

    Geolocate a given IP address
    """
    body = {"ip":"ip"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

