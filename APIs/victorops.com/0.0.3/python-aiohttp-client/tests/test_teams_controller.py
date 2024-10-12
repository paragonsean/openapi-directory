# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_team_member_payload import AddTeamMemberPayload
from openapi_server.models.add_team_payload import AddTeamPayload
from openapi_server.models.escalation_policy_list import EscalationPolicyList
from openapi_server.models.list_team_members_response import ListTeamMembersResponse
from openapi_server.models.remove_team_member_payload import RemoveTeamMemberPayload
from openapi_server.models.team_admins_response import TeamAdminsResponse
from openapi_server.models.team_detail import TeamDetail


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_team_get(client):
    """Test case for api_public_v1_team_get

    List teams
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/team',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_team_post(client):
    """Test case for api_public_v1_team_post

    Add a team
    """
    body = openapi_server.AddTeamPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api-public/v1/team',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_team_team_admins_get(client):
    """Test case for api_public_v1_team_team_admins_get

    Retrieve a list of team admins for a team
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/team/{team}/admins'.format(team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_team_team_delete(client):
    """Test case for api_public_v1_team_team_delete

    Remove a team
    """
    headers = { 
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api-public/v1/team/{team}'.format(team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_team_team_get(client):
    """Test case for api_public_v1_team_team_get

    Retrieve information for a team
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/team/{team}'.format(team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_team_team_members_get(client):
    """Test case for api_public_v1_team_team_members_get

    Retrieve a list of members for a team
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/team/{team}/members'.format(team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_team_team_members_post(client):
    """Test case for api_public_v1_team_team_members_post

    Add a team member
    """
    body = openapi_server.AddTeamMemberPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api-public/v1/team/{team}/members'.format(team='team_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_team_team_members_user_delete(client):
    """Test case for api_public_v1_team_team_members_user_delete

    Remove a team member
    """
    body = openapi_server.RemoveTeamMemberPayload()
    headers = { 
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api-public/v1/team/{team}/members/{user}'.format(team='team_example', user='user_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_team_team_policies_get_0(client):
    """Test case for api_public_v1_team_team_policies_get_0

    Retrieve a list of escalation policies for a team
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/team/{team}/policies'.format(team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_team_team_put(client):
    """Test case for api_public_v1_team_team_put

    Update a team
    """
    body = openapi_server.AddTeamPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/api-public/v1/team/{team}'.format(team='team_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

