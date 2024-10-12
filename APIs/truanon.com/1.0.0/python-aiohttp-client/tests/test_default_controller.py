# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_profile(client):
    """Test case for get_profile

    Get Profile
    """
    params = [('id', '{{your-member-id}}'),
                    ('service', '{{service-identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/get_profile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_token(client):
    """Test case for get_token

    Get Token
    """
    params = [('id', '{{your-member-id}}'),
                    ('service', '{{service-identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/request_token',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

