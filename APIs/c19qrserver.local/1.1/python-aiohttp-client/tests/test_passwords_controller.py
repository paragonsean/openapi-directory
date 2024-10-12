# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.invalid_token import InvalidToken
from openapi_server.models.request_password_reset_response import RequestPasswordResetResponse
from openapi_server.models.sample import Sample
from openapi_server.models.sample2 import Sample2
from openapi_server.models.sample4 import Sample4


pytestmark = pytest.mark.asyncio

async def test_change_password_post(client):
    """Test case for change_password_post

    Used for changing your password
    """
    body = {"old_password":"hunter3","password":"hunter4"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/changePassword',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_password_reset_post(client):
    """Test case for request_password_reset_post

    Used for requesting a password reset code
    """
    body = openapi_server.Sample2()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/requestPasswordReset',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_password_change_post(client):
    """Test case for verify_password_change_post

    Used for resetting your password when you forgot it
    """
    body = openapi_server.Sample4()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/verifyPasswordChange',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

