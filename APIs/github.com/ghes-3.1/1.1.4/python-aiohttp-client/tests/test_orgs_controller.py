# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apps_update_webhook_config_for_app_request import AppsUpdateWebhookConfigForAppRequest
from openapi_server.models.basic_error import BasicError
from openapi_server.models.org_hook import OrgHook
from openapi_server.models.org_membership import OrgMembership
from openapi_server.models.organization_full import OrganizationFull
from openapi_server.models.organization_simple import OrganizationSimple
from openapi_server.models.orgs_convert_member_to_outside_collaborator_request import OrgsConvertMemberToOutsideCollaboratorRequest
from openapi_server.models.orgs_create_webhook_request import OrgsCreateWebhookRequest
from openapi_server.models.orgs_list_app_installations200_response import OrgsListAppInstallations200Response
from openapi_server.models.orgs_remove_outside_collaborator422_response import OrgsRemoveOutsideCollaborator422Response
from openapi_server.models.orgs_set_membership_for_user_request import OrgsSetMembershipForUserRequest
from openapi_server.models.orgs_update422_response import OrgsUpdate422Response
from openapi_server.models.orgs_update_membership_for_authenticated_user_request import OrgsUpdateMembershipForAuthenticatedUserRequest
from openapi_server.models.orgs_update_request import OrgsUpdateRequest
from openapi_server.models.orgs_update_webhook_request import OrgsUpdateWebhookRequest
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.validation_error import ValidationError
from openapi_server.models.webhook_config import WebhookConfig


pytestmark = pytest.mark.asyncio

async def test_orgs_check_membership_for_user(client):
    """Test case for orgs_check_membership_for_user

    Check organization membership for a user
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/members/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_check_public_membership_for_user(client):
    """Test case for orgs_check_public_membership_for_user

    Check public organization membership for a user
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/public_members/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_convert_member_to_outside_collaborator(client):
    """Test case for orgs_convert_member_to_outside_collaborator

    Convert an organization member to outside collaborator
    """
    body = {"async":true}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/outside_collaborators/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_create_webhook(client):
    """Test case for orgs_create_webhook

    Create an organization webhook
    """
    body = {"active":true,"config":{"content_type":"json","url":"http://example.com/webhook"},"events":["push","pull_request"],"name":"web"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/orgs/{org}/hooks'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_delete_webhook(client):
    """Test case for orgs_delete_webhook

    Delete an organization webhook
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/hooks/{hook_id}'.format(org='org_example', hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_get(client):
    """Test case for orgs_get

    Get an organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}'.format(org='org_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_get_membership_for_authenticated_user(client):
    """Test case for orgs_get_membership_for_authenticated_user

    Get an organization membership for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/memberships/orgs/{org}'.format(org='org_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_get_membership_for_user(client):
    """Test case for orgs_get_membership_for_user

    Get organization membership for a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/memberships/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_get_webhook(client):
    """Test case for orgs_get_webhook

    Get an organization webhook
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/hooks/{hook_id}'.format(org='org_example', hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_get_webhook_config_for_org(client):
    """Test case for orgs_get_webhook_config_for_org

    Get a webhook configuration for an organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/hooks/{hook_id}/config'.format(org='org_example', hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_list(client):
    """Test case for orgs_list

    List organizations
    """
    params = [('since', 56),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/organizations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_list_app_installations(client):
    """Test case for orgs_list_app_installations

    List app installations for an organization
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/installations'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_list_for_authenticated_user(client):
    """Test case for orgs_list_for_authenticated_user

    List organizations for the authenticated user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/orgs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_list_for_user(client):
    """Test case for orgs_list_for_user

    List organizations for a user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/orgs'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_list_members(client):
    """Test case for orgs_list_members

    List organization members
    """
    params = [('filter', all),
                    ('role', all),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/members'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_list_memberships_for_authenticated_user(client):
    """Test case for orgs_list_memberships_for_authenticated_user

    List organization memberships for the authenticated user
    """
    params = [('state', 'state_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/memberships/orgs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_list_outside_collaborators(client):
    """Test case for orgs_list_outside_collaborators

    List outside collaborators for an organization
    """
    params = [('filter', all),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/outside_collaborators'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_list_public_members(client):
    """Test case for orgs_list_public_members

    List public organization members
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/public_members'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_list_webhooks(client):
    """Test case for orgs_list_webhooks

    List organization webhooks
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/hooks'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_ping_webhook(client):
    """Test case for orgs_ping_webhook

    Ping an organization webhook
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/orgs/{org}/hooks/{hook_id}/pings'.format(org='org_example', hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_remove_member(client):
    """Test case for orgs_remove_member

    Remove an organization member
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/members/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_remove_membership_for_user(client):
    """Test case for orgs_remove_membership_for_user

    Remove organization membership for a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/memberships/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_remove_outside_collaborator(client):
    """Test case for orgs_remove_outside_collaborator

    Remove outside collaborator from an organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/outside_collaborators/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_remove_public_membership_for_authenticated_user(client):
    """Test case for orgs_remove_public_membership_for_authenticated_user

    Remove public organization membership for the authenticated user
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/public_members/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_set_membership_for_user(client):
    """Test case for orgs_set_membership_for_user

    Set organization membership for a user
    """
    body = {"role":"member"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/memberships/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_set_public_membership_for_authenticated_user(client):
    """Test case for orgs_set_public_membership_for_authenticated_user

    Set public organization membership for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/public_members/{username}'.format(org='org_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_update(client):
    """Test case for orgs_update

    Update an organization
    """
    body = {"billing_email":"mona@github.com","company":"GitHub","default_repository_permission":"read","description":"GitHub, the company.","email":"mona@github.com","location":"San Francisco","members_allowed_repository_creation_type":"all","members_can_create_repositories":true,"name":"github","twitter_username":"github"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/orgs/{org}'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_update_membership_for_authenticated_user(client):
    """Test case for orgs_update_membership_for_authenticated_user

    Update an organization membership for the authenticated user
    """
    body = {"state":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/user/memberships/orgs/{org}'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_update_webhook(client):
    """Test case for orgs_update_webhook

    Update an organization webhook
    """
    body = {"active":true,"events":["pull_request"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/orgs/{org}/hooks/{hook_id}'.format(org='org_example', hook_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgs_update_webhook_config_for_org(client):
    """Test case for orgs_update_webhook_config_for_org

    Update a webhook configuration for an organization
    """
    body = {"content_type":"json","insecure_ssl":"0","secret":"********","url":"http://example.com/webhook"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/orgs/{org}/hooks/{hook_id}/config'.format(org='org_example', hook_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

