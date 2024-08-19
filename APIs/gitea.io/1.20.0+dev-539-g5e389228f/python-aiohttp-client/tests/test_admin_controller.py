# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_hook_option import CreateHookOption
from openapi_server.models.create_key_option import CreateKeyOption
from openapi_server.models.create_org_option import CreateOrgOption
from openapi_server.models.create_repo_option import CreateRepoOption
from openapi_server.models.create_user_option import CreateUserOption
from openapi_server.models.cron import Cron
from openapi_server.models.edit_hook_option import EditHookOption
from openapi_server.models.edit_user_option import EditUserOption
from openapi_server.models.email import Email
from openapi_server.models.hook import Hook
from openapi_server.models.organization import Organization
from openapi_server.models.public_key import PublicKey
from openapi_server.models.rename_user_option import RenameUserOption
from openapi_server.models.repository import Repository
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_admin_adopt_repository(client):
    """Test case for admin_adopt_repository

    Adopt unadopted files as a repository
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
        method='POST',
        path='/api/v1/admin/unadopted/{owner}/{repo}'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_create_hook(client):
    """Test case for admin_create_hook

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
        path='/api/v1/admin/hooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_create_org(client):
    """Test case for admin_create_org

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
        path='/api/v1/admin/users/{username}/orgs'.format(username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_create_public_key(client):
    """Test case for admin_create_public_key

    Add a public key on behalf of a user
    """
    body = {"read_only":True,"title":"title","key":"key"}
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
        path='/api/v1/admin/users/{username}/keys'.format(username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_create_repo(client):
    """Test case for admin_create_repo

    Create a repository on behalf of a user
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
        path='/api/v1/admin/users/{username}/repos'.format(username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_create_user(client):
    """Test case for admin_create_user

    Create a user
    """
    body = {"must_change_password":True,"password":"password","full_name":"full_name","login_name":"login_name","visibility":"visibility","restricted":True,"created_at":"2000-01-23T04:56:07.000+00:00","send_notify":True,"source_id":0,"email":"email","username":"username"}
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
        path='/api/v1/admin/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_cron_list(client):
    """Test case for admin_cron_list

    List cron tasks
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
        path='/api/v1/admin/cron',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_cron_run(client):
    """Test case for admin_cron_run

    Run cron task
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
        method='POST',
        path='/api/v1/admin/cron/{task}'.format(task='task_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_delete_hook(client):
    """Test case for admin_delete_hook

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
        path='/api/v1/amdin/hooks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_delete_unadopted_repository(client):
    """Test case for admin_delete_unadopted_repository

    Delete unadopted files
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
        path='/api/v1/admin/unadopted/{owner}/{repo}'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_delete_user(client):
    """Test case for admin_delete_user

    Delete a user
    """
    params = [('purge', True)]
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
        path='/api/v1/admin/users/{username}'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_delete_user_public_key(client):
    """Test case for admin_delete_user_public_key

    Delete a user's public key
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
        path='/api/v1/admin/users/{username}/keys/{id}'.format(username='username_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_edit_hook(client):
    """Test case for admin_edit_hook

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
        path='/api/v1/admin/hooks/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_edit_user(client):
    """Test case for admin_edit_user

    Edit an existing user
    """
    body = {"website":"website","visibility":"visibility","active":True,"admin":True,"description":"description","max_repo_creation":0,"must_change_password":True,"password":"password","full_name":"full_name","login_name":"login_name","restricted":True,"location":"location","allow_create_organization":True,"prohibit_login":True,"source_id":6,"allow_import_local":True,"email":"email","allow_git_hook":True}
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
        path='/api/v1/admin/users/{username}'.format(username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_get_all_emails(client):
    """Test case for admin_get_all_emails

    List all emails
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
        path='/api/v1/admin/emails',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_get_all_orgs(client):
    """Test case for admin_get_all_orgs

    List all organizations
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
        path='/api/v1/admin/orgs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_get_hook(client):
    """Test case for admin_get_hook

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
        path='/api/v1/admin/hooks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_list_hooks(client):
    """Test case for admin_list_hooks

    List system's webhooks
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
        path='/api/v1/admin/hooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_admin_rename_user(client):
    """Test case for admin_rename_user

    Rename a user
    """
    body = {"new_username":"new_username"}
    headers = { 
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
        path='/api/v1/admin/users/{username}/rename'.format(username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_search_emails(client):
    """Test case for admin_search_emails

    Search all emails
    """
    params = [('q', 'q_example'),
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
        path='/api/v1/admin/emails/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_search_users(client):
    """Test case for admin_search_users

    Search users according filter conditions
    """
    params = [('source_id', 56),
                    ('login_name', 'login_name_example'),
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
        path='/api/v1/admin/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_unadopted_list(client):
    """Test case for admin_unadopted_list

    List unadopted repositories
    """
    params = [('page', 56),
                    ('limit', 56),
                    ('pattern', 'pattern_example')]
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
        path='/api/v1/admin/unadopted',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

