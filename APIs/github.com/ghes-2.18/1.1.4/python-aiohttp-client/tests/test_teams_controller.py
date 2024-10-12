# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.full_repository import FullRepository
from openapi_server.models.minimal_repository import MinimalRepository
from openapi_server.models.orgs_remove_outside_collaborator422_response import OrgsRemoveOutsideCollaborator422Response
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.team import Team
from openapi_server.models.team2 import Team2
from openapi_server.models.team_discussion import TeamDiscussion
from openapi_server.models.team_discussion_comment import TeamDiscussionComment
from openapi_server.models.team_full import TeamFull
from openapi_server.models.team_membership import TeamMembership
from openapi_server.models.team_project import TeamProject
from openapi_server.models.teams_add_or_update_membership_for_user_request import TeamsAddOrUpdateMembershipForUserRequest
from openapi_server.models.teams_add_or_update_project_permissions_request import TeamsAddOrUpdateProjectPermissionsRequest
from openapi_server.models.teams_add_or_update_repo_permissions_request import TeamsAddOrUpdateRepoPermissionsRequest
from openapi_server.models.teams_create_discussion_comment_request import TeamsCreateDiscussionCommentRequest
from openapi_server.models.teams_create_discussion_request import TeamsCreateDiscussionRequest
from openapi_server.models.teams_create_request import TeamsCreateRequest
from openapi_server.models.teams_update_discussion_request import TeamsUpdateDiscussionRequest
from openapi_server.models.teams_update_request import TeamsUpdateRequest
from openapi_server.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_teams_add_member_legacy(client):
    """Test case for teams_add_member_legacy

    Add team member (Legacy)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/teams/{team_id}/members/{username}'.format(team_id=56, username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_add_or_update_membership_for_user(client):
    """Test case for teams_add_or_update_membership_for_user

    Add or update team membership for a user
    """
    body = openapi_server.TeamsAddOrUpdateMembershipForUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/teams/{team_id}/memberships/{username}'.format(team_id=56, username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_add_or_update_project_permissions(client):
    """Test case for teams_add_or_update_project_permissions

    Add or update team project permissions
    """
    body = openapi_server.TeamsAddOrUpdateProjectPermissionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/vnd.github.inertia-preview+json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/teams/{team_id}/projects/{project_id}'.format(team_id=56, project_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_add_or_update_repo_permissions(client):
    """Test case for teams_add_or_update_repo_permissions

    Add or update team repository permissions
    """
    body = openapi_server.TeamsAddOrUpdateRepoPermissionsRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/teams/{team_id}/repos/{owner}/{repo}'.format(team_id=56, owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_check_permissions_for_project(client):
    """Test case for teams_check_permissions_for_project

    Check team permissions for a project
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.inertia-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/projects/{project_id}'.format(team_id=56, project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_check_permissions_for_repo(client):
    """Test case for teams_check_permissions_for_repo

    Check team permissions for a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/repos/{owner}/{repo}'.format(team_id=56, owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_create(client):
    """Test case for teams_create

    Create a team
    """
    body = {"description":"A great team","name":"Justice League","permission":"admin","privacy":"closed"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/orgs/{org}/teams'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_create_discussion(client):
    """Test case for teams_create_discussion

    Create a discussion
    """
    body = {"body":"Hi! This is an area for us to collaborate as a team.","title":"Our first team post"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/vnd.github.echo-preview+json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/teams/{team_id}/discussions'.format(team_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_create_discussion_comment(client):
    """Test case for teams_create_discussion_comment

    Create a discussion comment
    """
    body = {"body":"Do you like apples?"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/vnd.github.echo-preview+json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments'.format(team_id=56, discussion_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete(client):
    """Test case for teams_delete

    Delete a team
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/teams/{team_id}'.format(team_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete_discussion(client):
    """Test case for teams_delete_discussion

    Delete a discussion
    """
    headers = { 
        'accept': 'application/vnd.github.echo-preview+json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}'.format(team_id=56, discussion_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete_discussion_comment(client):
    """Test case for teams_delete_discussion_comment

    Delete a discussion comment
    """
    headers = { 
        'accept': 'application/vnd.github.echo-preview+json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}'.format(team_id=56, discussion_number=56, comment_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get(client):
    """Test case for teams_get

    Get a team
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}'.format(team_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_by_name(client):
    """Test case for teams_get_by_name

    Get a team by name
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}'.format(org='org_example', team_slug='team_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_discussion(client):
    """Test case for teams_get_discussion

    Get a discussion
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.echo-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}'.format(team_id=56, discussion_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_discussion_comment(client):
    """Test case for teams_get_discussion_comment

    Get a discussion comment
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.echo-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}'.format(team_id=56, discussion_number=56, comment_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_member_legacy(client):
    """Test case for teams_get_member_legacy

    Get team member (Legacy)
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/members/{username}'.format(team_id=56, username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_membership_for_user(client):
    """Test case for teams_get_membership_for_user

    Get team membership for a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/memberships/{username}'.format(team_id=56, username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list(client):
    """Test case for teams_list

    List teams
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_child(client):
    """Test case for teams_list_child

    List child teams
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/teams'.format(team_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_discussion_comments(client):
    """Test case for teams_list_discussion_comments

    List discussion comments
    """
    params = [('direction', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.echo-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments'.format(team_id=56, discussion_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_discussions(client):
    """Test case for teams_list_discussions

    List discussions
    """
    params = [('direction', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.echo-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/discussions'.format(team_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_for_authenticated_user(client):
    """Test case for teams_list_for_authenticated_user

    List teams for the authenticated user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/teams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_members(client):
    """Test case for teams_list_members

    List team members
    """
    params = [('role', all),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/members'.format(team_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_projects(client):
    """Test case for teams_list_projects

    List team projects
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.inertia-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/projects'.format(team_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_repos(client):
    """Test case for teams_list_repos

    List team repositories
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/repos'.format(team_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_remove_member_legacy(client):
    """Test case for teams_remove_member_legacy

    Remove team member (Legacy)
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/teams/{team_id}/members/{username}'.format(team_id=56, username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_remove_membership_for_user(client):
    """Test case for teams_remove_membership_for_user

    Remove team membership for a user
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/teams/{team_id}/memberships/{username}'.format(team_id=56, username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_remove_project(client):
    """Test case for teams_remove_project

    Remove a project from a team
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/teams/{team_id}/projects/{project_id}'.format(team_id=56, project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_remove_repo(client):
    """Test case for teams_remove_repo

    Remove a repository from a team
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/teams/{team_id}/repos/{owner}/{repo}'.format(team_id=56, owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update(client):
    """Test case for teams_update

    Update a team
    """
    body = {"description":"new team description","name":"new team name","privacy":"closed"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/teams/{team_id}'.format(team_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update_discussion(client):
    """Test case for teams_update_discussion

    Update a discussion
    """
    body = {"title":"Welcome to our first team post"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/vnd.github.echo-preview+json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}'.format(team_id=56, discussion_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update_discussion_comment(client):
    """Test case for teams_update_discussion_comment

    Update a discussion comment
    """
    body = {"body":"Do you like pineapples?"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/vnd.github.echo-preview+json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}'.format(team_id=56, discussion_number=56, comment_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

