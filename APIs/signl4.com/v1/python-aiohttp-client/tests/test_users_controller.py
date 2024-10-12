# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.string_items_wrapper import StringItemsWrapper
from openapi_server.models.update_password_info import UpdatePasswordInfo
from openapi_server.models.user_duty_info import UserDutyInfo
from openapi_server.models.user_image import UserImage
from openapi_server.models.user_info import UserInfo
from openapi_server.models.user_profile import UserProfile
from openapi_server.models.user_setup_progress import UserSetupProgress


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    Get all Users
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_users_user_id_change_password_put(client):
    """Test case for users_user_id_change_password_put

    Updates the password of a user
    """
    body = {"newPassword":"newPassword","currentPassword":"currentPassword"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/users/{user_id}/changePassword'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_users_user_id_check_permissions_post(client):
    """Test case for users_user_id_check_permissions_post

    Checks if a user has the provided permission.
    """
    body = {"items":["items","items"]}
    params = [('teamId', 'team_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users/{user_id}/checkPermissions'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_duty_status_get(client):
    """Test case for users_user_id_duty_status_get

    Get duty status by user Id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{user_id}/dutyStatus'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_get(client):
    """Test case for users_user_id_get

    Get User by Id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_image_get(client):
    """Test case for users_user_id_image_get

    
    """
    params = [('height', 56),
                    ('width', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{user_id}/image'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_image_post(client):
    """Test case for users_user_id_image_post

    Uploaded a profile image for a specified user.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users/{user_id}/image'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_users_user_id_profile_put(client):
    """Test case for users_user_id_profile_put

    Updates user profile of an user
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/users/{user_id}/profile'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_punch_in_as_manager_post(client):
    """Test case for users_user_id_punch_in_as_manager_post

    Punch User in as Manager
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users/{user_id}/punchInAsManager'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_punch_in_post(client):
    """Test case for users_user_id_punch_in_post

    Punch User in
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users/{user_id}/punchIn'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_punch_out_post(client):
    """Test case for users_user_id_punch_out_post

    Punch User out
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users/{user_id}/punchOut'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_setup_progress_get(client):
    """Test case for users_user_id_setup_progress_get

    Gets setup progress of a specific user.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{user_id}/setupProgress'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

