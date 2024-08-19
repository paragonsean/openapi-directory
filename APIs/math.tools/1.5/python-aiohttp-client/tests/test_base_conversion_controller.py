# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_numbers_base_binary_get(client):
    """Test case for numbers_base_binary_get

    
    """
    params = [('number', 56),
                    ('from', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/base/binary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_base_get(client):
    """Test case for numbers_base_get

    
    """
    params = [('number', 56),
                    ('from', 56),
                    ('to', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/base',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_base_hex_get(client):
    """Test case for numbers_base_hex_get

    
    """
    params = [('number', 56),
                    ('from', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/base/hex',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_base_octal_get(client):
    """Test case for numbers_base_octal_get

    
    """
    params = [('number', 56),
                    ('from', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/base/octal',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

