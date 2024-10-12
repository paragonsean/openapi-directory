# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_user200_response import AddUser200Response
from openapi_server.models.delete_user200_response import DeleteUser200Response
from openapi_server.models.get_role200_response import GetRole200Response
from openapi_server.models.get_user_info200_response import GetUserInfo200Response
from openapi_server.models.reload_user_conf200_response import ReloadUserConf200Response
from openapi_server.models.update_user200_response import UpdateUser200Response
from openapi_server.models.users import Users


pytestmark = pytest.mark.asyncio

async def test_add_user(client):
    """Test case for add_user

    Add user
    """
    body = openapi_server.Users()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/usermanagement',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user(client):
    """Test case for delete_user

    Delete an user
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/usermanagement/{username}'.format(username='JaneDoe'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_role(client):
    """Test case for get_role

    List all roles
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/usermanagement/roles',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_info(client):
    """Test case for get_user_info

    List all users
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/usermanagement/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_user_conf(client):
    """Test case for reload_user_conf

    Reload user
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/usermanagement/users/reload',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user(client):
    """Test case for update_user

    Update user's infos
    """
    body = openapi_server.Users()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/usermanagement/update/{username}'.format(username='JaneDoe'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

