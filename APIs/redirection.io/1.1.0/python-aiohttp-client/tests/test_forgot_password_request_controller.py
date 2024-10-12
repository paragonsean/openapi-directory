# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.forgot_password_request import ForgotPasswordRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_forgot_password_request_collection(client):
    """Test case for post_forgot_password_request_collection

    Creates a ForgotPasswordRequest resource.
    """
    forgot_password_request = {"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/forgot-password-request',
        headers=headers,
        json=forgot_password_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

