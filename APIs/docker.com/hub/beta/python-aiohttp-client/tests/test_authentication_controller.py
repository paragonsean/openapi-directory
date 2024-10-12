# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.post_users2_fa_login_error_response import PostUsers2FALoginErrorResponse
from openapi_server.models.post_users_login_error_response import PostUsersLoginErrorResponse
from openapi_server.models.post_users_login_success_response import PostUsersLoginSuccessResponse
from openapi_server.models.users2_fa_login_request import Users2FALoginRequest
from openapi_server.models.users_login_request import UsersLoginRequest


pytestmark = pytest.mark.asyncio

async def test_post_users2_fa_login(client):
    """Test case for post_users2_fa_login

    Second factor authentication.
    """
    body = {"code":"123456","login_2fa_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/2fa-login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_users_login(client):
    """Test case for post_users_login

    Create an authentication token
    """
    body = {"password":"hunter2","username":"myusername"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

