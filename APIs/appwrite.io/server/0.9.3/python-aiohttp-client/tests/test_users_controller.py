# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_update_prefs_request import AccountUpdatePrefsRequest
from openapi_server.models.log_list import LogList
from openapi_server.models.session_list import SessionList
from openapi_server.models.user import User
from openapi_server.models.user_list import UserList
from openapi_server.models.users_create_request import UsersCreateRequest
from openapi_server.models.users_update_status_request import UsersUpdateStatusRequest
from openapi_server.models.users_update_verification_request import UsersUpdateVerificationRequest


pytestmark = pytest.mark.asyncio

async def test_users_create(client):
    """Test case for users_create

    Create User
    """
    body = openapi_server.UsersCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_delete(client):
    """Test case for users_delete

    Delete User
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_delete_session(client):
    """Test case for users_delete_session

    Delete User Session
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/users/{user_id}/sessions/{session_id}'.format(user_id='user_id_example', session_id='session_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_delete_sessions(client):
    """Test case for users_delete_sessions

    Delete User Sessions
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/users/{user_id}/sessions'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    Get User
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_logs(client):
    """Test case for users_get_logs

    Get User Logs
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_id}/logs'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_prefs(client):
    """Test case for users_get_prefs

    Get User Preferences
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_id}/prefs'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_sessions(client):
    """Test case for users_get_sessions

    Get User Sessions
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_id}/sessions'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list(client):
    """Test case for users_list

    List Users
    """
    params = [('search', ''),
                    ('limit', 25),
                    ('offset', 0),
                    ('orderType', 'ASC')]
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_update_prefs(client):
    """Test case for users_update_prefs

    Update User Preferences
    """
    body = openapi_server.AccountUpdatePrefsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/users/{user_id}/prefs'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_update_status(client):
    """Test case for users_update_status

    Update User Status
    """
    body = openapi_server.UsersUpdateStatusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/users/{user_id}/status'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_update_verification(client):
    """Test case for users_update_verification

    Update Email Verification
    """
    body = openapi_server.UsersUpdateVerificationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/users/{user_id}/verification'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

