# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_user_store_purchases(client):
    """Test case for get_user_store_purchases

    Get user store purchases
    """
    params = [('identity_cookie', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/user/purchases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_store_recommendations(client):
    """Test case for get_user_store_recommendations

    Get user store recommendations
    """
    params = [('identity_cookie', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/user/recommendations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_watching(client):
    """Test case for get_user_watching

    Get user watching
    """
    params = [('identity_cookie', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/user/watching',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

