# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Returns details of a specific fire.com user.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/user/{user_id}'.format(user_id=14059),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users(client):
    """Test case for get_users

    Returns list of all users on your fire.com account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

