# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.health_info import HealthInfo
from openapi_server.models.version_info import VersionInfo


pytestmark = pytest.mark.asyncio

async def test_get_health(client):
    """Test case for get_health

    Get instance status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_version(client):
    """Test case for get_version

    Get version information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

