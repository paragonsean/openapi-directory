# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.login import Login


pytestmark = pytest.mark.asyncio

async def test_check_login(client):
    """Test case for check_login

    Check if any user is logged in
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/api/login',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login(client):
    """Test case for login

    Login method
    """
    body = openapi_server.Login()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

