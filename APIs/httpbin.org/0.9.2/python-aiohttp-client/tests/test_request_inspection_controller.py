# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_headers_get(client):
    """Test case for headers_get

    Return the incoming request's HTTP headers.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/headers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ip_get(client):
    """Test case for ip_get

    Returns the requester's IP Address.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/ip',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_agent_get(client):
    """Test case for user_agent_get

    Return the incoming requests's User-Agent header.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/user-agent',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

