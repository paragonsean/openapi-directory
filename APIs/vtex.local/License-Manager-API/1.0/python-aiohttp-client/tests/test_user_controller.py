# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_user200_response import CreateUser200Response
from openapi_server.models.create_user400_response import CreateUser400Response
from openapi_server.models.create_user_request import CreateUserRequest
from openapi_server.models.get_user400_response import GetUser400Response
from openapi_server.models.list_users_response import ListUsersResponse


pytestmark = pytest.mark.asyncio

async def test_create_user(client):
    """Test case for create_user

    Create User
    """
    body = {"name":"name","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/license-manager/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_users(client):
    """Test case for get_list_users

    Get List of Users
    """
    params = [('numItems', 10),
                    ('pageNumber', 1),
                    ('sort', 'name'),
                    ('sortType', 'ASC')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/license-manager/site/pvt/logins/list/paged',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Get User
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/license-manager/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

