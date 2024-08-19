# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invite_user_request import InviteUserRequest
from openapi_server.models.join_account_request import JoinAccountRequest
from openapi_server.models.session_model import SessionModel
from openapi_server.models.user_account import UserAccount
from openapi_server.models.user_account_roles_results import UserAccountRolesResults
from openapi_server.models.user_invitation_model import UserInvitationModel


pytestmark = pytest.mark.asyncio

async def test_cancel_user_invitation(client):
    """Test case for cancel_user_invitation

    Cancel user invitation
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/invitations/{user_invitation_id}'.format(user_invitation_id='user_invitation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user(client):
    """Test case for delete_user

    Delete user
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/{user_id}'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Get user
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{user_id}'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_invitations(client):
    """Test case for get_user_invitations

    Get user invitations
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/invitations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users(client):
    """Test case for get_users

    Get users
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invite_user(client):
    """Test case for invite_user

    Invite user
    """
    body = {"roleId":0,"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users/invitations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_join_account(client):
    """Test case for join_account

    Join Account
    """
    body = {"invitationId":"invitationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/user/join-account',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user(client):
    """Test case for update_user

    Update user
    """
    body = {"accountName":"accountName","created":"2000-01-23T04:56:07.000+00:00","roleId":0,"fullName":"fullName","pageSize":0,"userId":0,"accountId":0,"password":"password","twoFactorAuthEnabled":True,"isOwner":True,"isCollaborator":True,"roleName":"roleName","updated":"2000-01-23T04:56:07.000+00:00","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

