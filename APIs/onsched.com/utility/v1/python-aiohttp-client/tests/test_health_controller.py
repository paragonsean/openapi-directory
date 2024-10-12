# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.thread_pool_info import ThreadPoolInfo


pytestmark = pytest.mark.asyncio

async def test_utility_v1_health_heartbeat_get(client):
    """Test case for utility_v1_health_heartbeat_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/utility/v1/health/heartbeat',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_utility_v1_health_threadinfo_get(client):
    """Test case for utility_v1_health_threadinfo_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/utility/v1/health/threadinfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

