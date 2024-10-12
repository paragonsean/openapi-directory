# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.membership import Membership
from openapi_server.models.membership_list import MembershipList
from openapi_server.models.team import Team
from openapi_server.models.team_list import TeamList
from openapi_server.models.teams_create_membership_request import TeamsCreateMembershipRequest
from openapi_server.models.teams_create_request import TeamsCreateRequest
from openapi_server.models.teams_update_membership_roles_request import TeamsUpdateMembershipRolesRequest
from openapi_server.models.teams_update_membership_status_request import TeamsUpdateMembershipStatusRequest
from openapi_server.models.teams_update_request import TeamsUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_teams_create(client):
    """Test case for teams_create

    Create Team
    """
    body = openapi_server.TeamsCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/teams',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_create_membership(client):
    """Test case for teams_create_membership

    Create Team Membership
    """
    body = openapi_server.TeamsCreateMembershipRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/teams/{team_id}/memberships'.format(team_id='team_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete(client):
    """Test case for teams_delete

    Delete Team
    """
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/teams/{team_id}'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete_membership(client):
    """Test case for teams_delete_membership

    Delete Team Membership
    """
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/teams/{team_id}/memberships/{membership_id}'.format(team_id='team_id_example', membership_id='membership_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get(client):
    """Test case for teams_get

    Get Team
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams/{team_id}'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_memberships(client):
    """Test case for teams_get_memberships

    Get Team Memberships
    """
    params = [('search', ''),
                    ('limit', 25),
                    ('offset', 0),
                    ('orderType', 'ASC')]
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams/{team_id}/memberships'.format(team_id='team_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list(client):
    """Test case for teams_list

    List Teams
    """
    params = [('search', ''),
                    ('limit', 25),
                    ('offset', 0),
                    ('orderType', 'ASC')]
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update(client):
    """Test case for teams_update

    Update Team
    """
    body = openapi_server.TeamsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/teams/{team_id}'.format(team_id='team_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update_membership_roles(client):
    """Test case for teams_update_membership_roles

    Update Membership Roles
    """
    body = openapi_server.TeamsUpdateMembershipRolesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/teams/{team_id}/memberships/{membership_id}'.format(team_id='team_id_example', membership_id='membership_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update_membership_status(client):
    """Test case for teams_update_membership_status

    Update Team Membership Status
    """
    body = openapi_server.TeamsUpdateMembershipStatusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/teams/{team_id}/memberships/{membership_id}/status'.format(team_id='team_id_example', membership_id='membership_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

