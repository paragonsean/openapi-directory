# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.session import Session
from openapi_server.models.session_logout_response import SessionLogoutResponse


pytestmark = pytest.mark.asyncio

async def test_login(client):
    """Test case for login

    
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/sessions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout(client):
    """Test case for logout

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/sessions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

