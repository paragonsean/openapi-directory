# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.destination import Destination
from openapi_server.models.source import Source


pytestmark = pytest.mark.asyncio

async def test_destinations_get(client):
    """Test case for destinations_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/destinations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_get(client):
    """Test case for sources_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/sources',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_system_health_get(client):
    """Test case for system_health_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/system/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_system_stop_post(client):
    """Test case for system_stop_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/system/stop',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

