# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_currencies_display_get(client):
    """Test case for currencies_display_get

    List of supported display currencies for browsing listings
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/currencies/display',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currencies_listing_get(client):
    """Test case for currencies_listing_get

    List of supported listing currencies for shops
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/currencies/listing',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

