# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.reset_password_model import ResetPasswordModel
from openapi_server.models.set_password_model import SetPasswordModel


pytestmark = pytest.mark.asyncio

async def test_password_has_user_set_password(client):
    """Test case for password_has_user_set_password

    Determines if the currently logged in user has set their own password
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/plan/api/Password/HasUserSetPassword',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_password_password_requirements(client):
    """Test case for password_password_requirements

    Gets the password complexity requirements
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/plan/api/Password/PasswordRequirements',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_password_reset_by_model(client):
    """Test case for password_reset_by_model

    Resets the password for the supplied user name
    """
    model = {"locale":"locale","userName":"userName"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/plan/api/Password/Reset',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_password_set_by_model(client):
    """Test case for password_set_by_model

    Sets the password for the currently logged in user
    """
    model = {"oldPassword":"oldPassword","newPassword":"newPassword"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/plan/api/Password/Set',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

