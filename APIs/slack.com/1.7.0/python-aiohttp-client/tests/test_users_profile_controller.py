# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.users_profile_get_error_schema import UsersProfileGetErrorSchema
from openapi_server.models.users_profile_get_schema import UsersProfileGetSchema
from openapi_server.models.users_profile_set_error_schema import UsersProfileSetErrorSchema
from openapi_server.models.users_profile_set_schema import UsersProfileSetSchema


pytestmark = pytest.mark.asyncio

async def test_users_profile_get(client):
    """Test case for users_profile_get

    
    """
    params = [('token', 'token_example'),
                    ('include_labels', True),
                    ('user', 'user_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users.profile.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_users_profile_set(client):
    """Test case for users_profile_set

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'name': 'name_example',
        'profile': 'profile_example',
        'user': 'user_example',
        'value': 'value_example'
        }
    response = await client.request(
        method='POST',
        path='/api/users.profile.set',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

