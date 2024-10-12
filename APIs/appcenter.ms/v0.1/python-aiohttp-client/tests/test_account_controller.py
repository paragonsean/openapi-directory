# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.app_invitations_create_by_email_request import AppInvitationsCreateByEmailRequest
from openapi_server.models.app_invitations_create_request import AppInvitationsCreateRequest
from openapi_server.models.app_invitations_list200_response import AppInvitationsList200Response
from openapi_server.models.app_invitations_list200_response_invited_by import AppInvitationsList200ResponseInvitedBy
from openapi_server.models.app_invitations_update_permissions_request import AppInvitationsUpdatePermissionsRequest
from openapi_server.models.apps_create_request import AppsCreateRequest
from openapi_server.models.apps_get_teams200_response_inner import AppsGetTeams200ResponseInner
from openapi_server.models.apps_list200_response_inner import AppsList200ResponseInner
from openapi_server.models.apps_list200_response_inner_all_of_azure_subscription import AppsList200ResponseInnerAllOfAzureSubscription
from openapi_server.models.apps_update_request import AppsUpdateRequest
from openapi_server.models.apps_update_user_permissions_request import AppsUpdateUserPermissionsRequest
from openapi_server.models.azure_subscription_link_for_app_request import AzureSubscriptionLinkForAppRequest
from openapi_server.models.distribution_groups_add_apps_request import DistributionGroupsAddAppsRequest
from openapi_server.models.distribution_groups_add_apps_request_apps_inner import DistributionGroupsAddAppsRequestAppsInner
from openapi_server.models.distribution_groups_add_user200_response_inner import DistributionGroupsAddUser200ResponseInner
from openapi_server.models.distribution_groups_add_user_request import DistributionGroupsAddUserRequest
from openapi_server.models.distribution_groups_bulk_delete_apps_request import DistributionGroupsBulkDeleteAppsRequest
from openapi_server.models.distribution_groups_create_request import DistributionGroupsCreateRequest
from openapi_server.models.distribution_groups_details_for_org200_response_inner import DistributionGroupsDetailsForOrg200ResponseInner
from openapi_server.models.distribution_groups_get_apps200_response_inner import DistributionGroupsGetApps200ResponseInner
from openapi_server.models.distribution_groups_list200_response_inner import DistributionGroupsList200ResponseInner
from openapi_server.models.distribution_groups_list_all_testers_for_org200_response_inner import DistributionGroupsListAllTestersForOrg200ResponseInner
from openapi_server.models.distribution_groups_list_users200_response_inner import DistributionGroupsListUsers200ResponseInner
from openapi_server.models.distribution_groups_remove_user200_response_inner import DistributionGroupsRemoveUser200ResponseInner
from openapi_server.models.distribution_groups_update_request import DistributionGroupsUpdateRequest
from openapi_server.models.invitations_sent200_response_inner import InvitationsSent200ResponseInner
from openapi_server.models.org_invitations_delete_request import OrgInvitationsDeleteRequest
from openapi_server.models.org_invitations_list_pending200_response_inner import OrgInvitationsListPending200ResponseInner
from openapi_server.models.org_invitations_update_request import OrgInvitationsUpdateRequest
from openapi_server.models.organizations_create_or_update_request import OrganizationsCreateOrUpdateRequest
from openapi_server.models.organizations_list200_response_inner import OrganizationsList200ResponseInner
from openapi_server.models.organizations_list_administered200_response import OrganizationsListAdministered200Response
from openapi_server.models.organizations_list_administered200_response_organizations import OrganizationsListAdministered200ResponseOrganizations
from openapi_server.models.organizations_list_administered_default_response import OrganizationsListAdministeredDefaultResponse
from openapi_server.models.organizations_list_administered_default_response_error import OrganizationsListAdministeredDefaultResponseError
from openapi_server.models.organizations_update_request import OrganizationsUpdateRequest
from openapi_server.models.sharedconnection_connections200_response_inner import SharedconnectionConnections200ResponseInner
from openapi_server.models.teams_create_team_request import TeamsCreateTeamRequest
from openapi_server.models.teams_get_users200_response import TeamsGetUsers200Response
from openapi_server.models.teams_list_all200_response_inner import TeamsListAll200ResponseInner
from openapi_server.models.teams_list_apps200_response_inner import TeamsListApps200ResponseInner
from openapi_server.models.teams_update_permissions_request import TeamsUpdatePermissionsRequest
from openapi_server.models.teams_update_request import TeamsUpdateRequest
from openapi_server.models.user_api_tokens_list200_response_inner import UserApiTokensList200ResponseInner
from openapi_server.models.user_api_tokens_new201_response import UserApiTokensNew201Response
from openapi_server.models.user_api_tokens_new_request import UserApiTokensNewRequest
from openapi_server.models.users_get_user_metadata200_response import UsersGetUserMetadata200Response
from openapi_server.models.users_get_user_metadata_default_response import UsersGetUserMetadataDefaultResponse
from openapi_server.models.users_list_for_org200_response_inner import UsersListForOrg200ResponseInner
from openapi_server.models.users_update_request import UsersUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_app_api_tokens_delete(client):
    """Test case for app_api_tokens_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/api_tokens/{api_token_id}'.format(owner_name='owner_name_example', app_name='app_name_example', api_token_id='api_token_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_api_tokens_list(client):
    """Test case for app_api_tokens_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/api_tokens'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_api_tokens_new(client):
    """Test case for app_api_tokens_new

    
    """
    body = openapi_server.UserApiTokensNewRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/api_tokens'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_invitations_accept(client):
    """Test case for app_invitations_accept

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/user/invitations/apps/{invitation_token}/accept'.format(invitation_token='invitation_token_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_invitations_create(client):
    """Test case for app_invitations_create

    
    """
    body = openapi_server.AppInvitationsCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/invitations'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_invitations_create_by_email(client):
    """Test case for app_invitations_create_by_email

    
    """
    body = openapi_server.AppInvitationsCreateByEmailRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/invitations/{user_email}'.format(owner_name='owner_name_example', app_name='app_name_example', user_email='user_email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_invitations_delete(client):
    """Test case for app_invitations_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/invitations/{user_email}'.format(owner_name='owner_name_example', app_name='app_name_example', user_email='user_email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_invitations_list(client):
    """Test case for app_invitations_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/invitations'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_invitations_reject(client):
    """Test case for app_invitations_reject

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/user/invitations/apps/{invitation_token}/reject'.format(invitation_token='invitation_token_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_invitations_update_permissions(client):
    """Test case for app_invitations_update_permissions

    
    """
    body = openapi_server.AppInvitationsUpdatePermissionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/invitations/{user_email}'.format(owner_name='owner_name_example', app_name='app_name_example', user_email='user_email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_create(client):
    """Test case for apps_create

    
    """
    body = openapi_server.AppsCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_create_for_org(client):
    """Test case for apps_create_for_org

    
    """
    body = openapi_server.AppsCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/apps'.format(org_name='org_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_delete(client):
    """Test case for apps_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}'.format(app_name='app_name_example', owner_name='owner_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_delete_avatar(client):
    """Test case for apps_delete_avatar

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/avatar'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get(client):
    """Test case for apps_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_for_org_user(client):
    """Test case for apps_get_for_org_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/users/{user_name}/apps'.format(org_name='org_name_example', user_name='user_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_teams(client):
    """Test case for apps_get_teams

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/teams'.format(app_name='app_name_example', owner_name='owner_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list(client):
    """Test case for apps_list

    
    """
    params = [('$orderBy', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_for_org(client):
    """Test case for apps_list_for_org

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/apps'.format(org_name='org_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_testers(client):
    """Test case for apps_list_testers

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/testers'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_remove_user(client):
    """Test case for apps_remove_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/users/{user_email}'.format(owner_name='owner_name_example', app_name='app_name_example', user_email='user_email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_apps_transfer_ownership(client):
    """Test case for apps_transfer_ownership

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/transfer/{destination_owner_name}'.format(owner_name='owner_name_example', app_name='app_name_example', destination_owner_name='destination_owner_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_transfer_to_org(client):
    """Test case for apps_transfer_to_org

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/transfer_to_org'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_update(client):
    """Test case for apps_update

    
    """
    body = openapi_server.AppsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}'.format(app_name='app_name_example', owner_name='owner_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_apps_update_avatar(client):
    """Test case for apps_update_avatar

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'APIToken': 'special-key',
    }
    data = FormData()
    data.add_field('avatar', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/avatar'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_update_user_permissions(client):
    """Test case for apps_update_user_permissions

    
    """
    body = openapi_server.AppsUpdateUserPermissionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/users/{user_email}'.format(owner_name='owner_name_example', app_name='app_name_example', user_email='user_email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_subscription_delete_for_app(client):
    """Test case for azure_subscription_delete_for_app

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/azure_subscriptions/{azure_subscription_id}'.format(azure_subscription_id='azure_subscription_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_subscription_link_for_app(client):
    """Test case for azure_subscription_link_for_app

    
    """
    body = openapi_server.AzureSubscriptionLinkForAppRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/azure_subscriptions'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_subscription_list_for_app(client):
    """Test case for azure_subscription_list_for_app

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/azure_subscriptions'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_subscription_list_for_org(client):
    """Test case for azure_subscription_list_for_org

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/azure_subscriptions'.format(org_name='org_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_subscription_list_for_user(client):
    """Test case for azure_subscription_list_for_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/azure_subscriptions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_group_invitations_accept_all(client):
    """Test case for distribution_group_invitations_accept_all

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/user/invitations/distribution_groups/accept',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_add_apps(client):
    """Test case for distribution_groups_add_apps

    
    """
    body = openapi_server.DistributionGroupsAddAppsRequest()
    headers = { 
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/apps'.format(org_name='org_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_add_user(client):
    """Test case for distribution_groups_add_user

    
    """
    body = openapi_server.DistributionGroupsAddUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/members'.format(owner_name='owner_name_example', app_name='app_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_add_users_for_org(client):
    """Test case for distribution_groups_add_users_for_org

    
    """
    body = openapi_server.DistributionGroupsAddUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/members'.format(org_name='org_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_bulk_delete_apps(client):
    """Test case for distribution_groups_bulk_delete_apps

    
    """
    body = openapi_server.DistributionGroupsBulkDeleteAppsRequest()
    headers = { 
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/apps/bulk_delete'.format(org_name='org_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_bulk_delete_users(client):
    """Test case for distribution_groups_bulk_delete_users

    
    """
    body = openapi_server.DistributionGroupsAddUserRequest()
    headers = { 
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/members/bulk_delete'.format(org_name='org_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_create(client):
    """Test case for distribution_groups_create

    
    """
    body = openapi_server.DistributionGroupsCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_create_for_org(client):
    """Test case for distribution_groups_create_for_org

    
    """
    body = openapi_server.DistributionGroupsCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/distribution_groups'.format(org_name='org_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_delete(client):
    """Test case for distribution_groups_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}'.format(app_name='app_name_example', owner_name='owner_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_delete_for_org(client):
    """Test case for distribution_groups_delete_for_org

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}'.format(org_name='org_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_details_for_org(client):
    """Test case for distribution_groups_details_for_org

    
    """
    params = [('apps_limit', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/distribution_groups_details'.format(org_name='org_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_get(client):
    """Test case for distribution_groups_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}'.format(owner_name='owner_name_example', app_name='app_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_get_apps(client):
    """Test case for distribution_groups_get_apps

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/apps'.format(org_name='org_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_get_for_org(client):
    """Test case for distribution_groups_get_for_org

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}'.format(org_name='org_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_list(client):
    """Test case for distribution_groups_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_list_all_testers_for_org(client):
    """Test case for distribution_groups_list_all_testers_for_org

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/testers'.format(org_name='org_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_list_for_org(client):
    """Test case for distribution_groups_list_for_org

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/distribution_groups'.format(org_name='org_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_list_users(client):
    """Test case for distribution_groups_list_users

    
    """
    params = [('exclude_pending_invitations', True)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/members'.format(owner_name='owner_name_example', app_name='app_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_list_users_for_org(client):
    """Test case for distribution_groups_list_users_for_org

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/members'.format(org_name='org_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_patch_for_org(client):
    """Test case for distribution_groups_patch_for_org

    
    """
    body = openapi_server.DistributionGroupsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}'.format(org_name='org_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_remove_user(client):
    """Test case for distribution_groups_remove_user

    
    """
    body = openapi_server.DistributionGroupsAddUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/members/bulk_delete'.format(owner_name='owner_name_example', app_name='app_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_resend_invite(client):
    """Test case for distribution_groups_resend_invite

    
    """
    body = openapi_server.DistributionGroupsAddUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/resend_invite'.format(owner_name='owner_name_example', app_name='app_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_resend_shared_invite(client):
    """Test case for distribution_groups_resend_shared_invite

    
    """
    body = openapi_server.DistributionGroupsAddUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/resend_invite'.format(org_name='org_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distribution_groups_update(client):
    """Test case for distribution_groups_update

    
    """
    body = openapi_server.DistributionGroupsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}'.format(owner_name='owner_name_example', app_name='app_name_example', distribution_group_name='distribution_group_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invitations_sent(client):
    """Test case for invitations_sent

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/invitations/sent',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_invitations(client):
    """Test case for org_invitations

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/invitations/{email}/revoke'.format(org_name='org_name_example', email='email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_invitations_accept(client):
    """Test case for org_invitations_accept

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/user/invitations/orgs/{invitation_token}/accept'.format(invitation_token='invitation_token_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_invitations_create(client):
    """Test case for org_invitations_create

    
    """
    body = openapi_server.AppInvitationsCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/invitations'.format(org_name='org_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_invitations_delete(client):
    """Test case for org_invitations_delete

    
    """
    body = openapi_server.OrgInvitationsDeleteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/orgs/{org_name}/invitations'.format(org_name='org_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_invitations_list_pending(client):
    """Test case for org_invitations_list_pending

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/invitations'.format(org_name='org_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_invitations_reject(client):
    """Test case for org_invitations_reject

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/user/invitations/orgs/{invitation_token}/reject'.format(invitation_token='invitation_token_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_invitations_send_new_invitation(client):
    """Test case for org_invitations_send_new_invitation

    
    """
    body = openapi_server.AppInvitationsCreateByEmailRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/invitations/{email}/resend'.format(org_name='org_name_example', email='email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_org_invitations_update(client):
    """Test case for org_invitations_update

    
    """
    body = openapi_server.OrgInvitationsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/orgs/{org_name}/invitations/{email}'.format(org_name='org_name_example', email='email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organization_delete_avatar(client):
    """Test case for organization_delete_avatar

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/orgs/{org_name}/avatar'.format(org_name='org_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_organization_update_avatar(client):
    """Test case for organization_update_avatar

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'APIToken': 'special-key',
    }
    data = FormData()
    data.add_field('avatar', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/avatar'.format(org_name='org_name_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_create_or_update(client):
    """Test case for organizations_create_or_update

    
    """
    body = openapi_server.OrganizationsCreateOrUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_delete(client):
    """Test case for organizations_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/orgs/{org_name}'.format(org_name='org_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_get(client):
    """Test case for organizations_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}'.format(org_name='org_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_list(client):
    """Test case for organizations_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_list_administered(client):
    """Test case for organizations_list_administered

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/administeredOrgs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_update(client):
    """Test case for organizations_update

    
    """
    body = openapi_server.OrganizationsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/orgs/{org_name}'.format(org_name='org_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sharedconnection_connections(client):
    """Test case for sharedconnection_connections

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/user/export/serviceConnections',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_add_app(client):
    """Test case for teams_add_app

    
    """
    body = openapi_server.DistributionGroupsAddAppsRequestAppsInner()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/teams/{team_name}/apps'.format(org_name='org_name_example', team_name='team_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_add_user(client):
    """Test case for teams_add_user

    
    """
    body = openapi_server.OrgInvitationsDeleteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/teams/{team_name}/users'.format(org_name='org_name_example', team_name='team_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_create_team(client):
    """Test case for teams_create_team

    
    """
    body = openapi_server.TeamsCreateTeamRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/orgs/{org_name}/teams'.format(org_name='org_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete(client):
    """Test case for teams_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/orgs/{org_name}/teams/{team_name}'.format(org_name='org_name_example', team_name='team_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_team(client):
    """Test case for teams_get_team

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/teams/{team_name}'.format(org_name='org_name_example', team_name='team_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get_users(client):
    """Test case for teams_get_users

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/teams/{team_name}/users'.format(org_name='org_name_example', team_name='team_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_all(client):
    """Test case for teams_list_all

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/teams'.format(org_name='org_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list_apps(client):
    """Test case for teams_list_apps

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/teams/{team_name}/apps'.format(org_name='org_name_example', team_name='team_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_remove_app(client):
    """Test case for teams_remove_app

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/orgs/{org_name}/teams/{team_name}/apps/{app_name}'.format(org_name='org_name_example', team_name='team_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_remove_user(client):
    """Test case for teams_remove_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/orgs/{org_name}/teams/{team_name}/users/{user_name}'.format(org_name='org_name_example', team_name='team_name_example', user_name='user_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update(client):
    """Test case for teams_update

    
    """
    body = openapi_server.TeamsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/orgs/{org_name}/teams/{team_name}'.format(org_name='org_name_example', team_name='team_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update_permissions(client):
    """Test case for teams_update_permissions

    
    """
    body = openapi_server.TeamsUpdatePermissionsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/orgs/{org_name}/teams/{team_name}/apps/{app_name}'.format(org_name='org_name_example', team_name='team_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_api_tokens_delete(client):
    """Test case for user_api_tokens_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/api_tokens/{api_token_id}'.format(api_token_id='api_token_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_api_tokens_list(client):
    """Test case for user_api_tokens_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/api_tokens',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_api_tokens_new(client):
    """Test case for user_api_tokens_new

    
    """
    body = openapi_server.UserApiTokensNewRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/api_tokens',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_for_org(client):
    """Test case for users_get_for_org

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/users/{user_name}'.format(org_name='org_name_example', user_name='user_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_user_metadata(client):
    """Test case for users_get_user_metadata

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/user/metadata/optimizely',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list(client):
    """Test case for users_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/users'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_for_org(client):
    """Test case for users_list_for_org

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/orgs/{org_name}/users'.format(org_name='org_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_remove_from_org(client):
    """Test case for users_remove_from_org

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/orgs/{org_name}/users/{user_name}'.format(org_name='org_name_example', user_name='user_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_update(client):
    """Test case for users_update

    
    """
    body = openapi_server.UsersUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_update_org_role(client):
    """Test case for users_update_org_role

    
    """
    body = openapi_server.OrgInvitationsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/orgs/{org_name}/users/{user_name}'.format(org_name='org_name_example', user_name='user_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

