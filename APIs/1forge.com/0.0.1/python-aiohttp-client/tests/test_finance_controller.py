# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_quotes_get_0(client):
    """Test case for quotes_get_0

    Get quotes for all symbols
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/forex-quotes/quotes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_symbols_get_0(client):
    """Test case for symbols_get_0

    Get a list of symbols for which we provide real-time quotes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/forex-quotes/symbols',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

