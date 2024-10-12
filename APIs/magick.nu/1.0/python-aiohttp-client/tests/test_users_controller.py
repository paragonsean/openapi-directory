# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.password_dto import PasswordDTO
from openapi_server.models.user_dto import UserDTO


pytestmark = pytest.mark.asyncio

async def test_get_users_email_email(client):
    """Test case for get_users_email_email

    Check if email is available
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/rest/users/email/{email}'.format(email='email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_username_username(client):
    """Test case for get_users_username_username

    Check if username is available
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/rest/users/username/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_users(client):
    """Test case for post_users

    Create a new Tradeworks User
    """
    body = {"firstName":"firstName","lastName":"lastName","password":"password","subscriptionType":"subscriptionType","affiliateId":"affiliateId","email":"email","username":"username"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_users_password_username(client):
    """Test case for put_users_password_username

    Update user's password
    """
    body = {"oldPassword":"oldPassword","newPassword":"newPassword"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/users/password/{username}'.format(username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

