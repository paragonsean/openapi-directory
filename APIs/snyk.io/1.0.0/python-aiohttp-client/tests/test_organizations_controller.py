# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_a_new_organization400_response import CreateANewOrganization400Response
from openapi_server.models.create_a_new_organization_request import CreateANewOrganizationRequest
from openapi_server.models.delete_pending_user_provision200_response import DeletePendingUserProvision200Response
from openapi_server.models.invite_users_request import InviteUsersRequest
from openapi_server.models.org_org_id_notification_settings_get200_response import OrgOrgIdNotificationSettingsGet200Response
from openapi_server.models.provision_a_user_to_the_organization200_response import ProvisionAUserToTheOrganization200Response
from openapi_server.models.provision_a_user_to_the_organization_request import ProvisionAUserToTheOrganizationRequest
from openapi_server.models.set_notification_settings_request import SetNotificationSettingsRequest
from openapi_server.models.update_a_member_in_the_organization_request import UpdateAMemberInTheOrganizationRequest
from openapi_server.models.update_a_member_s_role_in_the_organization_request import UpdateAMemberSRoleInTheOrganizationRequest
from openapi_server.models.update_organization_settings_request import UpdateOrganizationSettingsRequest
from openapi_server.models.view_organization_settings200_response import ViewOrganizationSettings200Response


pytestmark = pytest.mark.asyncio

async def test_create_a_new_organization(client):
    """Test case for create_a_new_organization

    Create a new organization
    """
    body = openapi_server.CreateANewOrganizationRequest()
    headers = { 
        'Accept': 'application/json, charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_pending_user_provision(client):
    """Test case for delete_pending_user_provision

    Delete pending user provision
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/org/{org_id}/provision'.format(org_id='25065eb1-109c-4c3e-9503-68fc56ef6f44'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invite_users(client):
    """Test case for invite_users

    Invite users
    """
    body = openapi_server.InviteUsersRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/invite'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_the_organizations_a_user_belongs_to(client):
    """Test case for list_all_the_organizations_a_user_belongs_to

    List all the organizations a user belongs to
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/orgs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_members(client):
    """Test case for list_members

    List Members
    """
    params = [('includeGroupAdmins', False)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/members'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_pending_user_provisions(client):
    """Test case for list_pending_user_provisions

    List pending user provisions
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/provision'.format(org_id='25065eb1-109c-4c3e-9503-68fc56ef6f44'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_org_id_notification_settings_get(client):
    """Test case for org_org_id_notification_settings_get

    Get organization notification settings
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/notification-settings'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provision_a_user_to_the_organization(client):
    """Test case for provision_a_user_to_the_organization

    Provision a user to the organization
    """
    body = openapi_server.ProvisionAUserToTheOrganizationRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/provision'.format(org_id='25065eb1-109c-4c3e-9503-68fc56ef6f44'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_a_member_from_the_organization(client):
    """Test case for remove_a_member_from_the_organization

    Remove a member from the organization
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/org/{org_id}/members/{user_id}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', user_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_organization(client):
    """Test case for remove_organization

    Remove organization
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/org/{org_id}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_notification_settings(client):
    """Test case for set_notification_settings

    Set notification settings
    """
    body = openapi_server.SetNotificationSettingsRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/org/{org_id}/notification-settings'.format(org_id='org_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_a_member_in_the_organization(client):
    """Test case for update_a_member_in_the_organization

    Update a member in the organization
    """
    body = openapi_server.UpdateAMemberInTheOrganizationRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/org/{org_id}/members/{user_id}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', user_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_a_members_role_in_the_organization(client):
    """Test case for update_a_members_role_in_the_organization

    Update a member's role in the organization
    """
    body = openapi_server.UpdateAMemberSRoleInTheOrganizationRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/org/{org_id}/members/update/{user_id}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', user_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_settings(client):
    """Test case for update_organization_settings

    Update organization settings
    """
    body = openapi_server.UpdateOrganizationSettingsRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/org/{org_id}/settings'.format(org_id='25065eb1-109c-4c3e-9503-68fc56ef6f44'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_view_organization_settings(client):
    """Test case for view_organization_settings

    View organization settings
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/settings'.format(org_id='25065eb1-109c-4c3e-9503-68fc56ef6f44'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

