# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.offering_metadata_response import OfferingMetadataResponse
from openapi_server.models.suspended_request import SuspendedRequest
from openapi_server.models.user import User
from openapi_server.models.user_response import UserResponse


pytestmark = pytest.mark.asyncio

async def test_users_post(client):
    """Test case for users_post

    Add new user
    """
    body = {"firstName":"firstName","lastName":"lastName","metadata":{"tags":["tags","tags"]},"sendInvite":True,"profile":{"displayName":"displayName"},"personId":"personId","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_email_get(client):
    """Test case for users_user_email_get

    Find user by email
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_email}'.format(user_email='user_email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_email_invite_email_post(client):
    """Test case for users_user_email_invite_email_post

    Resend invitation email
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users/{user_email}/invite-email'.format(user_email='user_email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_email_offerings_get(client):
    """Test case for users_user_email_offerings_get

    Find user's offerings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_email}/offerings'.format(user_email='user_email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_email_offerings_post(client):
    """Test case for users_user_email_offerings_post

    Adds the user to the specified offerings as a learner
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users/{user_email}/offerings'.format(user_email='user_email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_email_patch(client):
    """Test case for users_user_email_patch

    Update user
    """
    body = {"firstName":"firstName","lastName":"lastName","metadata":{"tags":["tags","tags"]},"sendInvite":True,"profile":{"displayName":"displayName"},"personId":"personId","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/users/{user_email}'.format(user_email='user_email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_email_permissions_permission_name_post(client):
    """Test case for users_user_email_permissions_permission_name_post

    Add permission to user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users/{user_email}/permissions/{permission_name}'.format(user_email='user_email_example', permission_name='permission_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_email_suspend_put(client):
    """Test case for users_user_email_suspend_put

    Suspend user
    """
    body = {"suspended":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/users/{user_email}/suspend'.format(user_email='user_email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

