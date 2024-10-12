# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_health_status import ApiHealthStatus
from openapi_server.models.api_version import ApiVersion


pytestmark = pytest.mark.asyncio

async def test_get_api_version(client):
    """Test case for get_api_version

    API version
    """
    headers = { 
        'Accept': 'application/json',
        'APIKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_health(client):
    """Test case for get_health

    Service health
    """
    headers = { 
        'Accept': 'application/json',
        'APIKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

