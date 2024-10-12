# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_platform(client):
    """Test case for get_platform

    Platform Detail
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/platform/{platform_id}'.format(platform_id='d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_platform_regions(client):
    """Test case for list_platform_regions

    Platform Region Collection
    """
    params = [('aliases', True)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/platform/{platform_id}/region'.format(platform_id='d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_platforms(client):
    """Test case for list_platforms

    Platform Collection
    """
    params = [('aliases', True)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/platform',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

