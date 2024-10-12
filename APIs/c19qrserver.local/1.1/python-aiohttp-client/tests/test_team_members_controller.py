# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_user_response import CreateUserResponse
from openapi_server.models.invalid_token import InvalidToken
from openapi_server.models.sample3 import Sample3
from openapi_server.models.user_record import UserRecord


pytestmark = pytest.mark.asyncio

async def test_user_post(client):
    """Test case for user_post

    Create a user
    """
    body = openapi_server.Sample3()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_user_id_delete(client):
    """Test case for user_user_id_delete

    Delete a team member's user record
    """
    headers = { 
        'Accept': 'application/json',
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/user/{user_id}'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_user_id_get(client):
    """Test case for user_user_id_get

    Retrieve the information associated with a team member's user record
    """
    headers = { 
        'Accept': 'application/json',
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/user/{user_id}'.format(user_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    Retrieve the information associated with all team members' user records
    """
    headers = { 
        'Accept': 'application/json',
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

