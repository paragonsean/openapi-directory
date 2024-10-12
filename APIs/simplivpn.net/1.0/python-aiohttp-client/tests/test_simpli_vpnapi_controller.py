# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.disable_user import DisableUser
from openapi_server.models.enable_user import EnableUser
from openapi_server.models.register import Register
from openapi_server.models.user_login import UserLogin


pytestmark = pytest.mark.asyncio

async def test_disable_user(client):
    """Test case for disable_user

    DisableUser
    """
    body = {"username":"username"}
    headers = { 
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/disable-user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_user(client):
    """Test case for enable_user

    EnableUser
    """
    body = {"username":"username"}
    headers = { 
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/enable-user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_server_summaries(client):
    """Test case for get_server_summaries

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/server-summaries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_servers(client):
    """Test case for get_servers

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login(client):
    """Test case for login

    Login
    """
    body = {"password":"password","username":"username"}
    headers = { 
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register(client):
    """Test case for register

    Register
    """
    body = {"password":"password","await":True,"username":"username"}
    headers = { 
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/register',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_username_available(client):
    """Test case for username_available

    UsernameAvailable
    """
    body = {"username":"username"}
    headers = { 
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/username-available',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

