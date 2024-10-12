# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_global_stats(client):
    """Test case for global_stats

    Global stats
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health(client):
    """Test case for health

    Health
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stats_of_an_index(client):
    """Test case for stats_of_an_index

    Stats of an index
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/stats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_version(client):
    """Test case for version

    Version
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

