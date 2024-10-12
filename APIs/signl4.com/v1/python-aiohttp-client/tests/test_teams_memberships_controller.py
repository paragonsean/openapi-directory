# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.invited_user_info import InvitedUserInfo
from openapi_server.models.user_info import UserInfo
from openapi_server.models.user_invitation_info import UserInvitationInfo
from openapi_server.models.user_invitation_result import UserInvitationResult
from openapi_server.models.user_membership import UserMembership
from openapi_server.models.users_invitation import UsersInvitation


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_memberships_get(client):
    """Test case for teams_team_id_memberships_get

    Get all invites of a team.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams/{team_id}/memberships'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_teams_team_id_memberships_post(client):
    """Test case for teams_team_id_memberships_post

    Invite users to a team
    """
    body = {"inviterId":"inviterId","invites":[{"roleId":"roleId","email":"email"},{"roleId":"roleId","email":"email"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/teams/{team_id}/memberships'.format(team_id='team_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_teams_team_id_memberships_resend_invite_mail_post(client):
    """Test case for teams_team_id_memberships_resend_invite_mail_post

    Sends invite email again if an invite exists
    """
    body = {"inviterId":"inviterId","userMail":"userMail"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/teams/{team_id}/memberships/resendInviteMail'.format(team_id='team_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_memberships_user_id_delete(client):
    """Test case for teams_team_id_memberships_user_id_delete

    Removes a user or invitation from a team, and may delete the user if he is not in any team.
    """
    params = [('requesterUserId', 'requester_user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/teams/{team_id}/memberships/{user_id}'.format(team_id='team_id_example', user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_teams_team_id_memberships_user_id_put(client):
    """Test case for teams_team_id_memberships_user_id_put

    Update user's team membership.
    """
    body = {"roleId":"roleId","isValid":True,"teamId":"teamId"}
    params = [('requesterUserId', 'requester_user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/teams/{team_id}/memberships/{user_id}'.format(team_id='team_id_example', user_id='user_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

