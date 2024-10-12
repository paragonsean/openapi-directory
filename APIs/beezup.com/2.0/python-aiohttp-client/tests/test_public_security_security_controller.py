# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_credentials import ApiCredentials
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.login_request import LoginRequest
from openapi_server.models.register_request import RegisterRequest


pytestmark = pytest.mark.asyncio

async def test_login(client):
    """Test case for login

    Login
    """
    body = openapi_server.LoginRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/public/security/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lost_password(client):
    """Test case for lost_password

    Lost password
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/public/security/lostpassword',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register(client):
    """Test case for register

    User Registration
    """
    body = openapi_server.RegisterRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/public/security/register',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

