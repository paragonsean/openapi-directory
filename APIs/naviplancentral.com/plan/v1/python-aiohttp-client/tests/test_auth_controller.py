# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.login_model import LoginModel
from openapi_server.models.public_session_info_model import PublicSessionInfoModel


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_auth_login_by_model(client):
    """Test case for auth_login_by_model

    Start a session with the DomainProviders user store
    """
    model = {"password":"password","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/plan/api/auth/Login',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_logout(client):
    """Test case for auth_logout

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/plan/api/auth/Logout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_password_requirements(client):
    """Test case for auth_password_requirements

    Gets the login rules
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/plan/api/auth/LoginConfiguration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_resume_session(client):
    """Test case for auth_resume_session

    Validate and extend the duration of a session
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/plan/api/auth/ResumeSession',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

