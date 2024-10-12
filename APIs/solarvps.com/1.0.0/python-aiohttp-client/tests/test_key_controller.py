# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_key_generate_get(client):
    """Test case for key_generate_get

    Generate API Key
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example')]
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/key/generate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_key_get_get(client):
    """Test case for key_get_get

    Get API Key
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example')]
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/key/get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

