# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.auth_response import AuthResponse
from openapi_server.models.model_error import ModelError


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_auth_default_login_post(client):
    """Test case for auth_default_login_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('username', 'username_example')
    data.add_field('password', 'password_example')
    response = await client.request(
        method='POST',
        path='/auth/default/login',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

