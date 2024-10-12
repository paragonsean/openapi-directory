# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.change_password200_response import ChangePassword200Response
from openapi_server.models.change_password_request import ChangePasswordRequest
from openapi_server.models.login import Login
from openapi_server.models.login200_response import Login200Response
from openapi_server.models.logout_request import LogoutRequest
from openapi_server.models.register200_response import Register200Response
from openapi_server.models.registration import Registration
from openapi_server.models.reset_password_request_request import ResetPasswordRequestRequest


pytestmark = pytest.mark.asyncio

async def test_change_password(client):
    """Test case for change_password

    changes a user's password
    """
    body = openapi_server.ChangePasswordRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/auth/changePassword',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login(client):
    """Test case for login

    Logs in to an existing account
    """
    body = {"password":"8yfqwiuy@!$","login":"john@jjf.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/auth/authorization',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout(client):
    """Test case for logout

    logs out a session uid
    """
    body = openapi_server.LogoutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/auth/logout',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register(client):
    """Test case for register

    Registers a new account
    """
    body = {"fname":"John","lname":"Smith","password":"8yfqwiuy@!$","discount_code":"discount_code","login":"john@jjf.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/auth/register',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_password_request(client):
    """Test case for reset_password_request

    resets a user's password
    """
    body = openapi_server.ResetPasswordRequestRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/auth/resetPasswordRequest',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

