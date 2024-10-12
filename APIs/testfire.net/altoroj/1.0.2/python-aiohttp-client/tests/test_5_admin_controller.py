# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.change_password import ChangePassword
from openapi_server.models.new_user import NewUser


pytestmark = pytest.mark.asyncio

async def test_add_user(client):
    """Test case for add_user

    
    """
    body = openapi_server.NewUser()
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/api/admin/addUser',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_password(client):
    """Test case for change_password

    
    """
    body = openapi_server.ChangePassword()
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/api/admin/changePassword',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

