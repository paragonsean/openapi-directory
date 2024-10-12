# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token_details import AccessTokenDetails
from openapi_server.models.subscription_data_list import SubscriptionDataList
from openapi_server.models.user_details import UserDetails


pytestmark = pytest.mark.asyncio

async def test_get_access_token(client):
    """Test case for get_access_token

    Get access token details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/access_token',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Get user details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_subscription_list(client):
    """Test case for get_user_subscription_list

    List user subscriptions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/subscriptions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

