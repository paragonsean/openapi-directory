# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_data_metrics_0(client):
    """Test case for get_data_metrics_0

    Get metrics about the current data release
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/utils/metrics',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_data_stats_0(client):
    """Test case for get_data_stats_0

    Get statistics about the current data release
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/utils/stats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ping_0(client):
    """Test case for get_ping_0

    Ping service
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/utils/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_therapeutic_areas_0(client):
    """Test case for get_therapeutic_areas_0

    Get the list of therapeutic areas about the current data release
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/utils/therapeuticareas',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_version_0(client):
    """Test case for get_version_0

    Get API version
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/utils/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

