# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credentials import Credentials
from openapi_server.models.login_apinf_request import LoginApinfRequest
from openapi_server.models.login_apinf_token_request import LoginApinfTokenRequest
from openapi_server.models.login_token import LoginToken
from openapi_server.models.registration import Registration


pytestmark = pytest.mark.asyncio

async def test_login(client):
    """Test case for login

    Log in to OpenAPI space
    """
    body = {"password":"password","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login_apinf(client):
    """Test case for login_apinf

    Log in to OpenAPI space using an APInf account
    """
    body = openapi_server.LoginApinfRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/login/apinf',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login_apinf_token(client):
    """Test case for login_apinf_token

    Log in to OpenAPI space using an APInf authentication token
    """
    body = openapi_server.LoginApinfTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/login/apinf_token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout(client):
    """Test case for logout

    Log out from OpenAPI space
    """
    headers = { 
        'AuthToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/logout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ping(client):
    """Test case for ping

    Check whether or not you are authenticated
    """
    headers = { 
        'Accept': 'application/json',
        'AuthToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register(client):
    """Test case for register

    Register to OpenAPI space
    """
    body = {"password":"password","email":"email","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/register',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

