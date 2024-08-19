# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.minimal_repository import MinimalRepository
from openapi_server.models.orgs_remove_outside_collaborator422_response import OrgsRemoveOutsideCollaborator422Response
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.team import Team
from openapi_server.models.team_discussion import TeamDiscussion
from openapi_server.models.team_discussion_comment import TeamDiscussionComment
from openapi_server.models.team_full import TeamFull
from openapi_server.models.team_membership import TeamMembership
from openapi_server.models.team_project import TeamProject
from openapi_server.models.team_repository import TeamRepository
from openapi_server.models.teams_add_or_update_membership_for_user_in_org_request import TeamsAddOrUpdateMembershipForUserInOrgRequest
from openapi_server.models.teams_add_or_update_project_permissions_in_org_request import TeamsAddOrUpdateProjectPermissionsInOrgRequest
from openapi_server.models.teams_add_or_update_project_permissions_legacy_request import TeamsAddOrUpdateProjectPermissionsLegacyRequest
from openapi_server.models.teams_add_or_update_repo_permissions_in_org_request import TeamsAddOrUpdateRepoPermissionsInOrgRequest
from openapi_server.models.teams_add_or_update_repo_permissions_legacy_request import TeamsAddOrUpdateRepoPermissionsLegacyRequest
from openapi_server.models.teams_create_discussion_comment_in_org_request import TeamsCreateDiscussionCommentInOrgRequest
from openapi_server.models.teams_create_discussion_in_org_request import TeamsCreateDiscussionInOrgRequest
from openapi_server.models.teams_create_request import TeamsCreateRequest
from openapi_server.models.teams_update_discussion_in_org_request import TeamsUpdateDiscussionInOrgRequest
from openapi_server.models.teams_update_in_org_request import TeamsUpdateInOrgRequest
from openapi_server.models.teams_update_legacy_request import TeamsUpdateLegacyRequest
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

async def test_teams_add_or_update_membership_for_user_in_org(client):
    """Test case for teams_add_or_update_membership_for_user_in_org

    Add or update team membership for a user
    """
    body = {"role":"maintainer"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/teams/{team_slug}/memberships/{username}'.format(org='org_example', team_slug='team_slug_example', username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_add_or_update_membership_for_user_legacy(client):
    """Test case for teams_add_or_update_membership_for_user_legacy

    Add or update team membership for a user (Legacy)
    """
    body = {"role":"member"}
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

async def test_teams_add_or_update_project_permissions_in_org(client):
    """Test case for teams_add_or_update_project_permissions_in_org

    Add or update team project permissions
    """
    body = {"permission":"write"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/teams/{team_slug}/projects/{project_id}'.format(org='org_example', team_slug='team_slug_example', project_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_add_or_update_project_permissions_legacy(client):
    """Test case for teams_add_or_update_project_permissions_legacy

    Add or update team project permissions (Legacy)
    """
    body = openapi_server.TeamsAddOrUpdateProjectPermissionsLegacyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/teams/{team_id}/projects/{project_id}'.format(team_id=56, project_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_add_or_update_repo_permissions_in_org(client):
    """Test case for teams_add_or_update_repo_permissions_in_org

    Add or update team repository permissions
    """
    body = {"permission":"push"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}'.format(org='org_example', team_slug='team_slug_example', owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_add_or_update_repo_permissions_legacy(client):
    """Test case for teams_add_or_update_repo_permissions_legacy

    Add or update team repository permissions (Legacy)
    """
    body = openapi_server.TeamsAddOrUpdateRepoPermissionsLegacyRequest()
    headers = { 
        'Accept': 'application/json',
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

async def test_teams_check_permissions_for_project_in_org(client):
    """Test case for teams_check_permissions_for_project_in_org

    Check team permissions for a project
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}/projects/{project_id}'.format(org='org_example', team_slug='team_slug_example', project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_check_permissions_for_project_legacy(client):
    """Test case for teams_check_permissions_for_project_legacy

    Check team permissions for a project (Legacy)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/projects/{project_id}'.format(team_id=56, project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_check_permissions_for_repo_in_org(client):
    """Test case for teams_check_permissions_for_repo_in_org

    Check team permissions for a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}'.format(org='org_example', team_slug='team_slug_example', owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_check_permissions_for_repo_legacy(client):
    """Test case for teams_check_permissions_for_repo_legacy

    Check team permissions for a repository (Legacy)
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
    body = {"description":"A great team","name":"Justice League","permission":"push","privacy":"closed"}
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

async def test_teams_create_discussion_comment_in_org(client):
    """Test case for teams_create_discussion_comment_in_org

    Create a discussion comment
    """
    body = {"body":"Do you like apples?"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments'.format(org='org_example', team_slug='team_slug_example', discussion_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_create_discussion_comment_legacy(client):
    """Test case for teams_create_discussion_comment_legacy

    Create a discussion comment (Legacy)
    """
    body = {"body":"Do you like apples?"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments'.format(team_id=56, discussion_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_create_discussion_in_org(client):
    """Test case for teams_create_discussion_in_org

    Create a discussion
    """
    body = {"body":"Hi! This is an area for us to collaborate as a team.","title":"Our first team post"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions'.format(org='org_example', team_slug='team_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_create_discussion_legacy(client):
    """Test case for teams_create_discussion_legacy

    Create a discussion (Legacy)
    """
    body = {"body":"Hi! This is an area for us to collaborate as a team.","title":"Our first team post"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/teams/{team_id}/discussions'.format(team_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete_discussion_comment_in_org(client):
    """Test case for teams_delete_discussion_comment_in_org

    Delete a discussion comment
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}'.format(org='org_example', team_slug='team_slug_example', discussion_number=56, comment_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete_discussion_comment_legacy(client):
    """Test case for teams_delete_discussion_comment_legacy

    Delete a discussion comment (Legacy)
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}'.format(team_id=56, discussion_number=56, comment_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete_discussion_in_org(client):
    """Test case for teams_delete_discussion_in_org

    Delete a discussion
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}'.format(org='org_example', team_slug='team_slug_example', discussion_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete_discussion_legacy(client):
    """Test case for teams_delete_discussion_legacy

    Delete a discussion (Legacy)
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}'.format(team_id=56, discussion_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete_in_org(client):
    """Test case for teams_delete_in_org

    Delete a team
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/teams/{team_slug}'.format(org='org_example', team_slug='team_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete_legacy(client):
    """Test case for teams_delete_legacy

    Delete a team (Legacy)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
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

async def test_teams_get_discussion_comment_in_org(client):
    """Test case for teams_get_discussion_comment_in_org

    Get a discussion comment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}'.format(org='org_example', team_slug='team_slug_example', discussion_number=56, comment_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_discussion_comment_legacy(client):
    """Test case for teams_get_discussion_comment_legacy

    Get a discussion comment (Legacy)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}'.format(team_id=56, discussion_number=56, comment_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_discussion_in_org(client):
    """Test case for teams_get_discussion_in_org

    Get a discussion
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}'.format(org='org_example', team_slug='team_slug_example', discussion_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_discussion_legacy(client):
    """Test case for teams_get_discussion_legacy

    Get a discussion (Legacy)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}'.format(team_id=56, discussion_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_legacy(client):
    """Test case for teams_get_legacy

    Get a team (Legacy)
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

async def test_teams_get_membership_for_user_in_org(client):
    """Test case for teams_get_membership_for_user_in_org

    Get team membership for a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}/memberships/{username}'.format(org='org_example', team_slug='team_slug_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_membership_for_user_legacy(client):
    """Test case for teams_get_membership_for_user_legacy

    Get team membership for a user (Legacy)
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

async def test_teams_list_child_in_org(client):
    """Test case for teams_list_child_in_org

    List child teams
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}/teams'.format(org='org_example', team_slug='team_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_child_legacy(client):
    """Test case for teams_list_child_legacy

    List child teams (Legacy)
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

async def test_teams_list_discussion_comments_in_org(client):
    """Test case for teams_list_discussion_comments_in_org

    List discussion comments
    """
    params = [('direction', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments'.format(org='org_example', team_slug='team_slug_example', discussion_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_discussion_comments_legacy(client):
    """Test case for teams_list_discussion_comments_legacy

    List discussion comments (Legacy)
    """
    params = [('direction', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments'.format(team_id=56, discussion_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_discussions_in_org(client):
    """Test case for teams_list_discussions_in_org

    List discussions
    """
    params = [('direction', desc),
                    ('per_page', 30),
                    ('page', 1),
                    ('pinned', 'pinned_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions'.format(org='org_example', team_slug='team_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_discussions_legacy(client):
    """Test case for teams_list_discussions_legacy

    List discussions (Legacy)
    """
    params = [('direction', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
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

async def test_teams_list_members_in_org(client):
    """Test case for teams_list_members_in_org

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
        path='/api/v3/orgs/{org}/teams/{team_slug}/members'.format(org='org_example', team_slug='team_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_members_legacy(client):
    """Test case for teams_list_members_legacy

    List team members (Legacy)
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

async def test_teams_list_projects_in_org(client):
    """Test case for teams_list_projects_in_org

    List team projects
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}/projects'.format(org='org_example', team_slug='team_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_projects_legacy(client):
    """Test case for teams_list_projects_legacy

    List team projects (Legacy)
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{team_id}/projects'.format(team_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_repos_in_org(client):
    """Test case for teams_list_repos_in_org

    List team repositories
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/teams/{team_slug}/repos'.format(org='org_example', team_slug='team_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_repos_legacy(client):
    """Test case for teams_list_repos_legacy

    List team repositories (Legacy)
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

async def test_teams_remove_membership_for_user_in_org(client):
    """Test case for teams_remove_membership_for_user_in_org

    Remove team membership for a user
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/teams/{team_slug}/memberships/{username}'.format(org='org_example', team_slug='team_slug_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_remove_membership_for_user_legacy(client):
    """Test case for teams_remove_membership_for_user_legacy

    Remove team membership for a user (Legacy)
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

async def test_teams_remove_project_in_org(client):
    """Test case for teams_remove_project_in_org

    Remove a project from a team
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/teams/{team_slug}/projects/{project_id}'.format(org='org_example', team_slug='team_slug_example', project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_remove_project_legacy(client):
    """Test case for teams_remove_project_legacy

    Remove a project from a team (Legacy)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/teams/{team_id}/projects/{project_id}'.format(team_id=56, project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_remove_repo_in_org(client):
    """Test case for teams_remove_repo_in_org

    Remove a repository from a team
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}'.format(org='org_example', team_slug='team_slug_example', owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_remove_repo_legacy(client):
    """Test case for teams_remove_repo_legacy

    Remove a repository from a team (Legacy)
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

async def test_teams_update_discussion_comment_in_org(client):
    """Test case for teams_update_discussion_comment_in_org

    Update a discussion comment
    """
    body = {"body":"Do you like pineapples?"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}'.format(org='org_example', team_slug='team_slug_example', discussion_number=56, comment_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update_discussion_comment_legacy(client):
    """Test case for teams_update_discussion_comment_legacy

    Update a discussion comment (Legacy)
    """
    body = {"body":"Do you like pineapples?"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}'.format(team_id=56, discussion_number=56, comment_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update_discussion_in_org(client):
    """Test case for teams_update_discussion_in_org

    Update a discussion
    """
    body = {"title":"Welcome to our first team post"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}'.format(org='org_example', team_slug='team_slug_example', discussion_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update_discussion_legacy(client):
    """Test case for teams_update_discussion_legacy

    Update a discussion (Legacy)
    """
    body = {"title":"Welcome to our first team post"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/teams/{team_id}/discussions/{discussion_number}'.format(team_id=56, discussion_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update_in_org(client):
    """Test case for teams_update_in_org

    Update a team
    """
    body = {"description":"new team description","name":"new team name","privacy":"closed"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/orgs/{org}/teams/{team_slug}'.format(org='org_example', team_slug='team_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update_legacy(client):
    """Test case for teams_update_legacy

    Update a team (Legacy)
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

