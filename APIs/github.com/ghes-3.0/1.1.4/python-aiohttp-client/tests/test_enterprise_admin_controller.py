# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.actions_enterprise_permissions import ActionsEnterprisePermissions
from openapi_server.models.announcement import Announcement
from openapi_server.models.authentication_token import AuthenticationToken
from openapi_server.models.authorization import Authorization
from openapi_server.models.configuration_status import ConfigurationStatus
from openapi_server.models.enterprise_admin_create_global_webhook_request import EnterpriseAdminCreateGlobalWebhookRequest
from openapi_server.models.enterprise_admin_create_impersonation_o_auth_token_request import EnterpriseAdminCreateImpersonationOAuthTokenRequest
from openapi_server.models.enterprise_admin_create_org_request import EnterpriseAdminCreateOrgRequest
from openapi_server.models.enterprise_admin_create_pre_receive_environment_request import EnterpriseAdminCreatePreReceiveEnvironmentRequest
from openapi_server.models.enterprise_admin_create_pre_receive_hook_request import EnterpriseAdminCreatePreReceiveHookRequest
from openapi_server.models.enterprise_admin_create_self_hosted_runner_group_for_enterprise_request import EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest
from openapi_server.models.enterprise_admin_create_user_request import EnterpriseAdminCreateUserRequest
from openapi_server.models.enterprise_admin_delete_pre_receive_environment422_response import EnterpriseAdminDeletePreReceiveEnvironment422Response
from openapi_server.models.enterprise_admin_list_selected_organizations_enabled_github_actions_enterprise200_response import EnterpriseAdminListSelectedOrganizationsEnabledGithubActionsEnterprise200Response
from openapi_server.models.enterprise_admin_list_self_hosted_runner_groups_for_enterprise200_response import EnterpriseAdminListSelfHostedRunnerGroupsForEnterprise200Response
from openapi_server.models.enterprise_admin_list_self_hosted_runners_for_enterprise200_response import EnterpriseAdminListSelfHostedRunnersForEnterprise200Response
from openapi_server.models.enterprise_admin_list_self_hosted_runners_in_group_for_enterprise200_response import EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response
from openapi_server.models.enterprise_admin_set_github_actions_permissions_enterprise_request import EnterpriseAdminSetGithubActionsPermissionsEnterpriseRequest
from openapi_server.models.enterprise_admin_set_org_access_to_self_hosted_runner_group_in_enterprise_request import EnterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest
from openapi_server.models.enterprise_admin_set_selected_organizations_enabled_github_actions_enterprise_request import EnterpriseAdminSetSelectedOrganizationsEnabledGithubActionsEnterpriseRequest
from openapi_server.models.enterprise_admin_set_self_hosted_runners_in_group_for_enterprise_request import EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest
from openapi_server.models.enterprise_admin_suspend_user_request import EnterpriseAdminSuspendUserRequest
from openapi_server.models.enterprise_admin_sync_ldap_mapping_for_team201_response import EnterpriseAdminSyncLdapMappingForTeam201Response
from openapi_server.models.enterprise_admin_unsuspend_user_request import EnterpriseAdminUnsuspendUserRequest
from openapi_server.models.enterprise_admin_update_global_webhook_request import EnterpriseAdminUpdateGlobalWebhookRequest
from openapi_server.models.enterprise_admin_update_ldap_mapping_for_team_request import EnterpriseAdminUpdateLdapMappingForTeamRequest
from openapi_server.models.enterprise_admin_update_org_name202_response import EnterpriseAdminUpdateOrgName202Response
from openapi_server.models.enterprise_admin_update_org_name_request import EnterpriseAdminUpdateOrgNameRequest
from openapi_server.models.enterprise_admin_update_pre_receive_environment_request import EnterpriseAdminUpdatePreReceiveEnvironmentRequest
from openapi_server.models.enterprise_admin_update_pre_receive_hook_enforcement_for_org_request import EnterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest
from openapi_server.models.enterprise_admin_update_pre_receive_hook_enforcement_for_repo_request import EnterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest
from openapi_server.models.enterprise_admin_update_pre_receive_hook_request import EnterpriseAdminUpdatePreReceiveHookRequest
from openapi_server.models.enterprise_admin_update_self_hosted_runner_group_for_enterprise_request import EnterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest
from openapi_server.models.enterprise_admin_update_username_for_user_request import EnterpriseAdminUpdateUsernameForUserRequest
from openapi_server.models.enterprise_comment_overview import EnterpriseCommentOverview
from openapi_server.models.enterprise_gist_overview import EnterpriseGistOverview
from openapi_server.models.enterprise_hook_overview import EnterpriseHookOverview
from openapi_server.models.enterprise_issue_overview import EnterpriseIssueOverview
from openapi_server.models.enterprise_milestone_overview import EnterpriseMilestoneOverview
from openapi_server.models.enterprise_organization_overview import EnterpriseOrganizationOverview
from openapi_server.models.enterprise_overview import EnterpriseOverview
from openapi_server.models.enterprise_page_overview import EnterprisePageOverview
from openapi_server.models.enterprise_pull_request_overview import EnterprisePullRequestOverview
from openapi_server.models.enterprise_repository_overview import EnterpriseRepositoryOverview
from openapi_server.models.enterprise_settings import EnterpriseSettings
from openapi_server.models.enterprise_user_overview import EnterpriseUserOverview
from openapi_server.models.global_hook import GlobalHook
from openapi_server.models.global_hook2 import GlobalHook2
from openapi_server.models.ldap_mapping_team import LdapMappingTeam
from openapi_server.models.ldap_mapping_user import LdapMappingUser
from openapi_server.models.license_info import LicenseInfo
from openapi_server.models.maintenance_status import MaintenanceStatus
from openapi_server.models.org_pre_receive_hook import OrgPreReceiveHook
from openapi_server.models.organization_simple import OrganizationSimple
from openapi_server.models.pre_receive_environment import PreReceiveEnvironment
from openapi_server.models.pre_receive_environment_download_status import PreReceiveEnvironmentDownloadStatus
from openapi_server.models.pre_receive_hook import PreReceiveHook
from openapi_server.models.public_key_full import PublicKeyFull
from openapi_server.models.repository_pre_receive_hook import RepositoryPreReceiveHook
from openapi_server.models.runner import Runner
from openapi_server.models.runner_application import RunnerApplication
from openapi_server.models.runner_groups_enterprise import RunnerGroupsEnterprise
from openapi_server.models.selected_actions import SelectedActions
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.ssh_key import SshKey


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_enterprise_admin_add_authorized_ssh_key(client):
    """Test case for enterprise_admin_add_authorized_ssh_key

    Add an authorized SSH key
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'authorized_key': 'authorized_key_example'
        }
    response = await client.request(
        method='POST',
        path='/api/v3/setup/api/settings/authorized-keys',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_add_org_access_to_self_hosted_runner_group_in_enterprise(client):
    """Test case for enterprise_admin_add_org_access_to_self_hosted_runner_group_in_enterprise

    Add organization access to a self-hosted runner group in an enterprise
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}'.format(enterprise='enterprise_example', runner_group_id=56, org_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_add_self_hosted_runner_to_group_for_enterprise(client):
    """Test case for enterprise_admin_add_self_hosted_runner_to_group_for_enterprise

    Add a self-hosted runner to a group for an enterprise
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}'.format(enterprise='enterprise_example', runner_group_id=56, runner_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_enterprise_admin_create_enterprise_server_license(client):
    """Test case for enterprise_admin_create_enterprise_server_license

    Create a GitHub license
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'license': 'license_example',
        'password': 'password_example',
        'settings': 'settings_example'
        }
    response = await client.request(
        method='POST',
        path='/api/v3/setup/api/start',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_create_global_webhook(client):
    """Test case for enterprise_admin_create_global_webhook

    Create a global webhook
    """
    body = {"config":{"content_type":"json","secret":"secret","url":"https://example.com/webhook"},"events":["organization","user"],"name":"web"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/vnd.github.superpro-preview+json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/admin/hooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_create_impersonation_o_auth_token(client):
    """Test case for enterprise_admin_create_impersonation_o_auth_token

    Create an impersonation OAuth token
    """
    body = openapi_server.EnterpriseAdminCreateImpersonationOAuthTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/admin/users/{username}/authorizations'.format(username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_create_org(client):
    """Test case for enterprise_admin_create_org

    Create an organization
    """
    body = {"admin":"monalisaoctocat","login":"github","profile_name":"GitHub, Inc."}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/admin/organizations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_create_pre_receive_environment(client):
    """Test case for enterprise_admin_create_pre_receive_environment

    Create a pre-receive environment
    """
    body = {"image_url":"https://my_file_server/path/to/devtools_env.tar.gz","name":"DevTools Hook Env"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/admin/pre-receive-environments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_create_pre_receive_hook(client):
    """Test case for enterprise_admin_create_pre_receive_hook

    Create a pre-receive hook
    """
    body = {"allow_downstream_configuration":false,"enforcement":"disabled","environment":{"id":2},"name":"Check Commits","script":"scripts/commit_check.sh","script_repository":{"full_name":"DevIT/hooks"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/admin/pre-receive-hooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_create_registration_token_for_enterprise(client):
    """Test case for enterprise_admin_create_registration_token_for_enterprise

    Create a registration token for an enterprise
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/enterprises/{enterprise}/actions/runners/registration-token'.format(enterprise='enterprise_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_create_remove_token_for_enterprise(client):
    """Test case for enterprise_admin_create_remove_token_for_enterprise

    Create a remove token for an enterprise
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/enterprises/{enterprise}/actions/runners/remove-token'.format(enterprise='enterprise_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_create_self_hosted_runner_group_for_enterprise(client):
    """Test case for enterprise_admin_create_self_hosted_runner_group_for_enterprise

    Create a self-hosted runner group for an enterprise
    """
    body = {"name":"Expensive hardware runners","runners":[9,2],"selected_organization_ids":[32,91],"visibility":"selected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups'.format(enterprise='enterprise_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_create_user(client):
    """Test case for enterprise_admin_create_user

    Create a user
    """
    body = {"email":"octocat@github.com","login":"monalisa"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/admin/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_delete_global_webhook(client):
    """Test case for enterprise_admin_delete_global_webhook

    Delete a global webhook
    """
    headers = { 
        'accept': 'application/vnd.github.superpro-preview+json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/admin/hooks/{hook_id}'.format(hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_delete_impersonation_o_auth_token(client):
    """Test case for enterprise_admin_delete_impersonation_o_auth_token

    Delete an impersonation OAuth token
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/admin/users/{username}/authorizations'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_delete_personal_access_token(client):
    """Test case for enterprise_admin_delete_personal_access_token

    Delete a personal access token
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/admin/tokens/{token_id}'.format(token_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_delete_pre_receive_environment(client):
    """Test case for enterprise_admin_delete_pre_receive_environment

    Delete a pre-receive environment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/admin/pre-receive-environments/{pre_receive_environment_id}'.format(pre_receive_environment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_delete_pre_receive_hook(client):
    """Test case for enterprise_admin_delete_pre_receive_hook

    Delete a pre-receive hook
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/admin/pre-receive-hooks/{pre_receive_hook_id}'.format(pre_receive_hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_delete_public_key(client):
    """Test case for enterprise_admin_delete_public_key

    Delete a public key
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/admin/keys/{key_ids}'.format(key_ids='key_ids_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_delete_self_hosted_runner_from_enterprise(client):
    """Test case for enterprise_admin_delete_self_hosted_runner_from_enterprise

    Delete a self-hosted runner from an enterprise
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/enterprises/{enterprise}/actions/runners/{runner_id}'.format(enterprise='enterprise_example', runner_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_delete_self_hosted_runner_group_from_enterprise(client):
    """Test case for enterprise_admin_delete_self_hosted_runner_group_from_enterprise

    Delete a self-hosted runner group from an enterprise
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}'.format(enterprise='enterprise_example', runner_group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_delete_user(client):
    """Test case for enterprise_admin_delete_user

    Delete a user
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/admin/users/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_demote_site_administrator(client):
    """Test case for enterprise_admin_demote_site_administrator

    Demote a site administrator
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/users/{username}/site_admin'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_disable_selected_organization_github_actions_enterprise(client):
    """Test case for enterprise_admin_disable_selected_organization_github_actions_enterprise

    Disable a selected organization for GitHub Actions in an enterprise
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/enterprises/{enterprise}/actions/permissions/organizations/{org_id}'.format(enterprise='enterprise_example', org_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_enterprise_admin_enable_or_disable_maintenance_mode(client):
    """Test case for enterprise_admin_enable_or_disable_maintenance_mode

    Enable or disable maintenance mode
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'maintenance': 'maintenance_example'
        }
    response = await client.request(
        method='POST',
        path='/api/v3/setup/api/maintenance',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_enable_selected_organization_github_actions_enterprise(client):
    """Test case for enterprise_admin_enable_selected_organization_github_actions_enterprise

    Enable a selected organization for GitHub Actions in an enterprise
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/enterprises/{enterprise}/actions/permissions/organizations/{org_id}'.format(enterprise='enterprise_example', org_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_all_authorized_ssh_keys(client):
    """Test case for enterprise_admin_get_all_authorized_ssh_keys

    Get all authorized SSH keys
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/setup/api/settings/authorized-keys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_all_stats(client):
    """Test case for enterprise_admin_get_all_stats

    Get all statistics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/stats/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_allowed_actions_enterprise(client):
    """Test case for enterprise_admin_get_allowed_actions_enterprise

    Get allowed actions for an enterprise
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprises/{enterprise}/actions/permissions/selected-actions'.format(enterprise='enterprise_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_announcement(client):
    """Test case for enterprise_admin_get_announcement

    Get the global announcement banner
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/announcement',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_comment_stats(client):
    """Test case for enterprise_admin_get_comment_stats

    Get comment statistics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/stats/comments',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_configuration_status(client):
    """Test case for enterprise_admin_get_configuration_status

    Get the configuration status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/setup/api/configcheck',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_download_status_for_pre_receive_environment(client):
    """Test case for enterprise_admin_get_download_status_for_pre_receive_environment

    Get the download status for a pre-receive environment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/pre-receive-environments/{pre_receive_environment_id}/downloads/latest'.format(pre_receive_environment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_gist_stats(client):
    """Test case for enterprise_admin_get_gist_stats

    Get gist statistics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/stats/gists',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_github_actions_permissions_enterprise(client):
    """Test case for enterprise_admin_get_github_actions_permissions_enterprise

    Get GitHub Actions permissions for an enterprise
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprises/{enterprise}/actions/permissions'.format(enterprise='enterprise_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_global_webhook(client):
    """Test case for enterprise_admin_get_global_webhook

    Get a global webhook
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.superpro-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/hooks/{hook_id}'.format(hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_hooks_stats(client):
    """Test case for enterprise_admin_get_hooks_stats

    Get hooks statistics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/stats/hooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_issue_stats(client):
    """Test case for enterprise_admin_get_issue_stats

    Get issue statistics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/stats/issues',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_license_information(client):
    """Test case for enterprise_admin_get_license_information

    Get license information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/settings/license',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_maintenance_status(client):
    """Test case for enterprise_admin_get_maintenance_status

    Get the maintenance status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/setup/api/maintenance',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_milestone_stats(client):
    """Test case for enterprise_admin_get_milestone_stats

    Get milestone statistics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/stats/milestones',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_org_stats(client):
    """Test case for enterprise_admin_get_org_stats

    Get organization statistics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/stats/orgs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_pages_stats(client):
    """Test case for enterprise_admin_get_pages_stats

    Get pages statistics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/stats/pages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_pre_receive_environment(client):
    """Test case for enterprise_admin_get_pre_receive_environment

    Get a pre-receive environment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/pre-receive-environments/{pre_receive_environment_id}'.format(pre_receive_environment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_pre_receive_hook(client):
    """Test case for enterprise_admin_get_pre_receive_hook

    Get a pre-receive hook
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/pre-receive-hooks/{pre_receive_hook_id}'.format(pre_receive_hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_pre_receive_hook_for_org(client):
    """Test case for enterprise_admin_get_pre_receive_hook_for_org

    Get a pre-receive hook for an organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}'.format(org='org_example', pre_receive_hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_pre_receive_hook_for_repo(client):
    """Test case for enterprise_admin_get_pre_receive_hook_for_repo

    Get a pre-receive hook for a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}'.format(owner='owner_example', repo='repo_example', pre_receive_hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_pull_request_stats(client):
    """Test case for enterprise_admin_get_pull_request_stats

    Get pull request statistics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/stats/pulls',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_repo_stats(client):
    """Test case for enterprise_admin_get_repo_stats

    Get repository statistics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/stats/repos',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_self_hosted_runner_for_enterprise(client):
    """Test case for enterprise_admin_get_self_hosted_runner_for_enterprise

    Get a self-hosted runner for an enterprise
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprises/{enterprise}/actions/runners/{runner_id}'.format(enterprise='enterprise_example', runner_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_self_hosted_runner_group_for_enterprise(client):
    """Test case for enterprise_admin_get_self_hosted_runner_group_for_enterprise

    Get a self-hosted runner group for an enterprise
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}'.format(enterprise='enterprise_example', runner_group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_settings(client):
    """Test case for enterprise_admin_get_settings

    Get settings
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/setup/api/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_get_user_stats(client):
    """Test case for enterprise_admin_get_user_stats

    Get users statistics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/stats/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_global_webhooks(client):
    """Test case for enterprise_admin_list_global_webhooks

    List global webhooks
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.superpro-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/hooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_org_access_to_self_hosted_runner_group_in_enterprise(client):
    """Test case for enterprise_admin_list_org_access_to_self_hosted_runner_group_in_enterprise

    List organization access to a self-hosted runner group in an enterprise
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations'.format(enterprise='enterprise_example', runner_group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_personal_access_tokens(client):
    """Test case for enterprise_admin_list_personal_access_tokens

    List personal access tokens
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/tokens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_pre_receive_environments(client):
    """Test case for enterprise_admin_list_pre_receive_environments

    List pre-receive environments
    """
    params = [('per_page', 30),
                    ('page', 1),
                    ('direction', desc),
                    ('sort', created)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/pre-receive-environments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_pre_receive_hooks(client):
    """Test case for enterprise_admin_list_pre_receive_hooks

    List pre-receive hooks
    """
    params = [('per_page', 30),
                    ('page', 1),
                    ('direction', desc),
                    ('sort', created)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/pre-receive-hooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_pre_receive_hooks_for_org(client):
    """Test case for enterprise_admin_list_pre_receive_hooks_for_org

    List pre-receive hooks for an organization
    """
    params = [('per_page', 30),
                    ('page', 1),
                    ('direction', desc),
                    ('sort', created)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/pre-receive-hooks'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_pre_receive_hooks_for_repo(client):
    """Test case for enterprise_admin_list_pre_receive_hooks_for_repo

    List pre-receive hooks for a repository
    """
    params = [('per_page', 30),
                    ('page', 1),
                    ('direction', desc),
                    ('sort', created)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/pre-receive-hooks'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_public_keys(client):
    """Test case for enterprise_admin_list_public_keys

    List public keys
    """
    params = [('per_page', 30),
                    ('page', 1),
                    ('direction', desc),
                    ('sort', created),
                    ('since', 'since_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_runner_applications_for_enterprise(client):
    """Test case for enterprise_admin_list_runner_applications_for_enterprise

    List runner applications for an enterprise
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprises/{enterprise}/actions/runners/downloads'.format(enterprise='enterprise_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_selected_organizations_enabled_github_actions_enterprise(client):
    """Test case for enterprise_admin_list_selected_organizations_enabled_github_actions_enterprise

    List selected organizations enabled for GitHub Actions in an enterprise
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprises/{enterprise}/actions/permissions/organizations'.format(enterprise='enterprise_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_self_hosted_runner_groups_for_enterprise(client):
    """Test case for enterprise_admin_list_self_hosted_runner_groups_for_enterprise

    List self-hosted runner groups for an enterprise
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups'.format(enterprise='enterprise_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_self_hosted_runners_for_enterprise(client):
    """Test case for enterprise_admin_list_self_hosted_runners_for_enterprise

    List self-hosted runners for an enterprise
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprises/{enterprise}/actions/runners'.format(enterprise='enterprise_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_list_self_hosted_runners_in_group_for_enterprise(client):
    """Test case for enterprise_admin_list_self_hosted_runners_in_group_for_enterprise

    List self-hosted runners in a group for an enterprise
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners'.format(enterprise='enterprise_example', runner_group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_ping_global_webhook(client):
    """Test case for enterprise_admin_ping_global_webhook

    Ping a global webhook
    """
    headers = { 
        'accept': 'application/vnd.github.superpro-preview+json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/admin/hooks/{hook_id}/pings'.format(hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_promote_user_to_be_site_administrator(client):
    """Test case for enterprise_admin_promote_user_to_be_site_administrator

    Promote a user to be a site administrator
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/users/{username}/site_admin'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_remove_announcement(client):
    """Test case for enterprise_admin_remove_announcement

    Remove the global announcement banner
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/enterprise/announcement',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_enterprise_admin_remove_authorized_ssh_key(client):
    """Test case for enterprise_admin_remove_authorized_ssh_key

    Remove an authorized SSH key
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'authorized_key': 'authorized_key_example'
        }
    response = await client.request(
        method='DELETE',
        path='/api/v3/setup/api/settings/authorized-keys',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_remove_org_access_to_self_hosted_runner_group_in_enterprise(client):
    """Test case for enterprise_admin_remove_org_access_to_self_hosted_runner_group_in_enterprise

    Remove organization access to a self-hosted runner group in an enterprise
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}'.format(enterprise='enterprise_example', runner_group_id=56, org_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_remove_pre_receive_hook_enforcement_for_org(client):
    """Test case for enterprise_admin_remove_pre_receive_hook_enforcement_for_org

    Remove pre-receive hook enforcement for an organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}'.format(org='org_example', pre_receive_hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_remove_pre_receive_hook_enforcement_for_repo(client):
    """Test case for enterprise_admin_remove_pre_receive_hook_enforcement_for_repo

    Remove pre-receive hook enforcement for a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}'.format(owner='owner_example', repo='repo_example', pre_receive_hook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_remove_self_hosted_runner_from_group_for_enterprise(client):
    """Test case for enterprise_admin_remove_self_hosted_runner_from_group_for_enterprise

    Remove a self-hosted runner from a group for an enterprise
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}'.format(enterprise='enterprise_example', runner_group_id=56, runner_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_set_allowed_actions_enterprise(client):
    """Test case for enterprise_admin_set_allowed_actions_enterprise

    Set allowed actions for an enterprise
    """
    body = openapi_server.SelectedActions()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/enterprises/{enterprise}/actions/permissions/selected-actions'.format(enterprise='enterprise_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_set_announcement(client):
    """Test case for enterprise_admin_set_announcement

    Set the global announcement banner
    """
    body = openapi_server.Announcement()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/enterprise/announcement',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_set_github_actions_permissions_enterprise(client):
    """Test case for enterprise_admin_set_github_actions_permissions_enterprise

    Set GitHub Actions permissions for an enterprise
    """
    body = {"allowed_actions":"selected","enabled_organizations":"all"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/enterprises/{enterprise}/actions/permissions'.format(enterprise='enterprise_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_set_org_access_to_self_hosted_runner_group_in_enterprise(client):
    """Test case for enterprise_admin_set_org_access_to_self_hosted_runner_group_in_enterprise

    Set organization access for a self-hosted runner group in an enterprise
    """
    body = {"selected_organization_ids":[32,91]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations'.format(enterprise='enterprise_example', runner_group_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_set_selected_organizations_enabled_github_actions_enterprise(client):
    """Test case for enterprise_admin_set_selected_organizations_enabled_github_actions_enterprise

    Set selected organizations enabled for GitHub Actions in an enterprise
    """
    body = {"selected_organization_ids":[32,91]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/enterprises/{enterprise}/actions/permissions/organizations'.format(enterprise='enterprise_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_set_self_hosted_runners_in_group_for_enterprise(client):
    """Test case for enterprise_admin_set_self_hosted_runners_in_group_for_enterprise

    Set self-hosted runners in a group for an enterprise
    """
    body = {"runners":[9,2]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners'.format(enterprise='enterprise_example', runner_group_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_enterprise_admin_set_settings(client):
    """Test case for enterprise_admin_set_settings

    Set settings
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'settings': 'settings_example'
        }
    response = await client.request(
        method='PUT',
        path='/api/v3/setup/api/settings',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_start_configuration_process(client):
    """Test case for enterprise_admin_start_configuration_process

    Start a configuration process
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/v3/setup/api/configure',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_start_pre_receive_environment_download(client):
    """Test case for enterprise_admin_start_pre_receive_environment_download

    Start a pre-receive environment download
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/admin/pre-receive-environments/{pre_receive_environment_id}/downloads'.format(pre_receive_environment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_suspend_user(client):
    """Test case for enterprise_admin_suspend_user

    Suspend a user
    """
    body = openapi_server.EnterpriseAdminSuspendUserRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/users/{username}/suspended'.format(username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_sync_ldap_mapping_for_team(client):
    """Test case for enterprise_admin_sync_ldap_mapping_for_team

    Sync LDAP mapping for a team
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/admin/ldap/teams/{team_id}/sync'.format(team_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_sync_ldap_mapping_for_user(client):
    """Test case for enterprise_admin_sync_ldap_mapping_for_user

    Sync LDAP mapping for a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/admin/ldap/users/{username}/sync'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_unsuspend_user(client):
    """Test case for enterprise_admin_unsuspend_user

    Unsuspend a user
    """
    body = openapi_server.EnterpriseAdminUnsuspendUserRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/users/{username}/suspended'.format(username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_update_global_webhook(client):
    """Test case for enterprise_admin_update_global_webhook

    Update a global webhook
    """
    body = {"config":{"url":"https://example.com/webhook"},"events":["organization"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/vnd.github.superpro-preview+json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/admin/hooks/{hook_id}'.format(hook_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_update_ldap_mapping_for_team(client):
    """Test case for enterprise_admin_update_ldap_mapping_for_team

    Update LDAP mapping for a team
    """
    body = {"ldap_dn":"cn=Enterprise Ops,ou=teams,dc=github,dc=com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/admin/ldap/teams/{team_id}/mapping'.format(team_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_update_ldap_mapping_for_user(client):
    """Test case for enterprise_admin_update_ldap_mapping_for_user

    Update LDAP mapping for a user
    """
    body = {"ldap_dn":"uid=asdf,ou=users,dc=github,dc=com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/admin/ldap/users/{username}/mapping'.format(username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_update_org_name(client):
    """Test case for enterprise_admin_update_org_name

    Update an organization name
    """
    body = {"login":"the-new-octocats"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/admin/organizations/{org}'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_update_pre_receive_environment(client):
    """Test case for enterprise_admin_update_pre_receive_environment

    Update a pre-receive environment
    """
    body = openapi_server.EnterpriseAdminUpdatePreReceiveEnvironmentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/admin/pre-receive-environments/{pre_receive_environment_id}'.format(pre_receive_environment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_update_pre_receive_hook(client):
    """Test case for enterprise_admin_update_pre_receive_hook

    Update a pre-receive hook
    """
    body = {"allow_downstream_configuration":true,"environment":{"id":1},"name":"Check Commits"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/admin/pre-receive-hooks/{pre_receive_hook_id}'.format(pre_receive_hook_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_update_pre_receive_hook_enforcement_for_org(client):
    """Test case for enterprise_admin_update_pre_receive_hook_enforcement_for_org

    Update pre-receive hook enforcement for an organization
    """
    body = {"allow_downstream_configuration":false,"enforcement":"enabled"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}'.format(org='org_example', pre_receive_hook_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_update_pre_receive_hook_enforcement_for_repo(client):
    """Test case for enterprise_admin_update_pre_receive_hook_enforcement_for_repo

    Update pre-receive hook enforcement for a repository
    """
    body = {"enforcement":"enabled"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}'.format(owner='owner_example', repo='repo_example', pre_receive_hook_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_update_self_hosted_runner_group_for_enterprise(client):
    """Test case for enterprise_admin_update_self_hosted_runner_group_for_enterprise

    Update a self-hosted runner group for an enterprise
    """
    body = {"name":"Expensive hardware runners","visibility":"selected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}'.format(enterprise='enterprise_example', runner_group_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_admin_update_username_for_user(client):
    """Test case for enterprise_admin_update_username_for_user

    Update the username for a user
    """
    body = {"login":"thenewmonalisa"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/admin/users/{username}'.format(username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_enterprise_admin_upgrade_license(client):
    """Test case for enterprise_admin_upgrade_license

    Upgrade a license
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'license': 'license_example'
        }
    response = await client.request(
        method='POST',
        path='/api/v3/setup/api/upgrade',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

