# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_shipping_providers_get(client):
    """Test case for shipping_providers_get

    List of supported shipping providers
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/shipping/providers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shipping_regions_get(client):
    """Test case for shipping_regions_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/shipping/regions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

