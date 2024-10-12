# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server.models.create_hook_option import CreateHookOption
from openapi_server.models.create_label_option import CreateLabelOption
from openapi_server.models.create_org_option import CreateOrgOption
from openapi_server.models.create_repo_option import CreateRepoOption
from openapi_server.models.create_team_option import CreateTeamOption
from openapi_server.models.edit_hook_option import EditHookOption
from openapi_server.models.edit_label_option import EditLabelOption
from openapi_server.models.edit_org_option import EditOrgOption
from openapi_server.models.edit_team_option import EditTeamOption
from openapi_server.models.hook import Hook
from openapi_server.models.label import Label
from openapi_server.models.organization import Organization
from openapi_server.models.organization_permissions import OrganizationPermissions
from openapi_server.models.repository import Repository
from openapi_server.models.team import Team
from openapi_server.models.team_search200_response import TeamSearch200Response
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_create_org_repo(client):
    """Test case for create_org_repo

    Create a repository in an organization
    """
    body = {"auto_init":True,"template":True,"issue_labels":"issue_labels","license":"license","private":True,"trust_model":"default","gitignores":"gitignores","name":"name","description":"description","default_branch":"default_branch","readme":"readme"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orgs/{org}/repos'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_org_repo_deprecated(client):
    """Test case for create_org_repo_deprecated

    Create a repository in an organization
    """
    body = {"auto_init":True,"template":True,"issue_labels":"issue_labels","license":"license","private":True,"trust_model":"default","gitignores":"gitignores","name":"name","description":"description","default_branch":"default_branch","readme":"readme"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/org/{org}/repos'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_add_team_member(client):
    """Test case for org_add_team_member

    Add a team member
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/teams/{id}/members/{username}'.format(id=56, username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_add_team_repository(client):
    """Test case for org_add_team_repository

    Add a repository to a team
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/teams/{id}/repos/{org}/{repo}'.format(id=56, org='org_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_conceal_member(client):
    """Test case for org_conceal_member

    Conceal a user's membership
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/orgs/{org}/public_members/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_create(client):
    """Test case for org_create

    Create an organization
    """
    body = {"website":"website","full_name":"full_name","repo_admin_change_team_access":True,"visibility":"public","description":"description","location":"location","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orgs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_create_hook(client):
    """Test case for org_create_hook

    Create a hook
    """
    body = {"branch_filter":"branch_filter","active":False,"type":"dingtalk","config":{"key":"config"},"authorization_header":"authorization_header","events":["events","events"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orgs/{org}/hooks'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_create_label(client):
    """Test case for org_create_label

    Create a label for an organization
    """
    body = {"color":"#00aabb","name":"name","description":"description","exclusive":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orgs/{org}/labels'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_create_team(client):
    """Test case for org_create_team

    Create a team
    """
    body = {"can_create_org_repo":True,"units_map":{"repo.code":"read","repo.ext_issues":"none","repo.ext_wiki":"none","repo.issues":"write","repo.projects":"none","repo.pulls":"owner","repo.releases":"none","repo.wiki":"admin"},"name":"name","description":"description","permission":"read","includes_all_repositories":True,"units":["repo.code","repo.issues","repo.ext_issues","repo.wiki","repo.pulls","repo.releases","repo.projects","repo.ext_wiki"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orgs/{org}/teams'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_delete(client):
    """Test case for org_delete

    Delete an organization
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/orgs/{org}'.format(org='org_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_delete_hook(client):
    """Test case for org_delete_hook

    Delete a hook
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/orgs/{org}/hooks/{id}'.format(org='org_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_delete_label(client):
    """Test case for org_delete_label

    Delete a label
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/orgs/{org}/labels/{id}'.format(org='org_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_delete_member(client):
    """Test case for org_delete_member

    Remove a member from an organization
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/orgs/{org}/members/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_delete_team(client):
    """Test case for org_delete_team

    Delete a team
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/teams/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_edit(client):
    """Test case for org_edit

    Edit an organization
    """
    body = {"website":"website","full_name":"full_name","repo_admin_change_team_access":True,"visibility":"public","description":"description","location":"location"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/orgs/{org}'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_edit_hook(client):
    """Test case for org_edit_hook

    Update a hook
    """
    body = {"branch_filter":"branch_filter","active":True,"config":{"key":"config"},"authorization_header":"authorization_header","events":["events","events"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/orgs/{org}/hooks/{id}'.format(org='org_example', id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_edit_label(client):
    """Test case for org_edit_label

    Update a label
    """
    body = {"color":"#00aabb","name":"name","description":"description","exclusive":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/orgs/{org}/labels/{id}'.format(org='org_example', id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_edit_team(client):
    """Test case for org_edit_team

    Edit a team
    """
    body = {"can_create_org_repo":True,"units_map":{"repo.code":"read","repo.ext_issues":"none","repo.ext_wiki":"none","repo.issues":"write","repo.projects":"none","repo.pulls":"owner","repo.releases":"none","repo.wiki":"admin"},"name":"name","description":"description","permission":"read","includes_all_repositories":True,"units":["repo.code","repo.issues","repo.ext_issues","repo.wiki","repo.pulls","repo.releases","repo.projects","repo.ext_wiki"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/teams/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_get(client):
    """Test case for org_get

    Get an organization
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}'.format(org='org_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_get_all(client):
    """Test case for org_get_all

    Get list of organizations
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_get_hook(client):
    """Test case for org_get_hook

    Get a hook
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}/hooks/{id}'.format(org='org_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_get_label(client):
    """Test case for org_get_label

    Get a single label
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}/labels/{id}'.format(org='org_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_get_team(client):
    """Test case for org_get_team

    Get a team
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/teams/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_get_user_permissions(client):
    """Test case for org_get_user_permissions

    Get user permissions in organization
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/{username}/orgs/{org}/permissions'.format(username='username_example', org='org_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_is_member(client):
    """Test case for org_is_member

    Check if a user is a member of an organization
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}/members/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_is_public_member(client):
    """Test case for org_is_public_member

    Check if a user is a public member of an organization
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}/public_members/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_activity_feeds(client):
    """Test case for org_list_activity_feeds

    List an organization's activity feeds
    """
    params = [('date', '2013-10-20'),
                    ('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}/activities/feeds'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_current_user_orgs(client):
    """Test case for org_list_current_user_orgs

    List the current user's organizations
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/user/orgs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_hooks(client):
    """Test case for org_list_hooks

    List an organization's webhooks
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}/hooks'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_labels(client):
    """Test case for org_list_labels

    List an organization's labels
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}/labels'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_members(client):
    """Test case for org_list_members

    List an organization's members
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}/members'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_public_members(client):
    """Test case for org_list_public_members

    List an organization's public members
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}/public_members'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_repos(client):
    """Test case for org_list_repos

    List an organization's repos
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}/repos'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_team_activity_feeds(client):
    """Test case for org_list_team_activity_feeds

    List a team's activity feeds
    """
    params = [('date', '2013-10-20'),
                    ('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/teams/{id}/activities/feeds'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_team_member(client):
    """Test case for org_list_team_member

    List a particular member of team
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/teams/{id}/members/{username}'.format(id=56, username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_team_members(client):
    """Test case for org_list_team_members

    List a team's members
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/teams/{id}/members'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_team_repo(client):
    """Test case for org_list_team_repo

    List a particular repo of team
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/teams/{id}/repos/{org}/{repo}'.format(id=56, org='org_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_team_repos(client):
    """Test case for org_list_team_repos

    List a team's repos
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/teams/{id}/repos'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_teams(client):
    """Test case for org_list_teams

    List an organization's teams
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}/teams'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_list_user_orgs(client):
    """Test case for org_list_user_orgs

    List a user's organizations
    """
    params = [('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/{username}/orgs'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_publicize_member(client):
    """Test case for org_publicize_member

    Publicize a user's membership
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/orgs/{org}/public_members/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_remove_team_member(client):
    """Test case for org_remove_team_member

    Remove a team member
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/teams/{id}/members/{username}'.format(id=56, username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_remove_team_repository(client):
    """Test case for org_remove_team_repository

    Remove a repository from a team
    """
    headers = { 
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/teams/{id}/repos/{org}/{repo}'.format(id=56, org='org_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_team_search(client):
    """Test case for team_search

    Search for teams within an organization
    """
    params = [('q', 'q_example'),
                    ('include_desc', True),
                    ('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orgs/{org}/teams/search'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

