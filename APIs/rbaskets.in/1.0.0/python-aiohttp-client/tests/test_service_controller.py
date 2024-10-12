# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.version import Version


pytestmark = pytest.mark.asyncio

async def test_api_version_get(client):
    """Test case for api_version_get

    Get service version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

