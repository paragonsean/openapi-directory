from typing import List, Dict
from aiohttp import web

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
from openapi_server.models.enterprise_admin_list_org_access_to_self_hosted_runner_group_in_enterprise200_response import EnterpriseAdminListOrgAccessToSelfHostedRunnerGroupInEnterprise200Response
from openapi_server.models.enterprise_admin_list_self_hosted_runner_groups_for_enterprise200_response import EnterpriseAdminListSelfHostedRunnerGroupsForEnterprise200Response
from openapi_server.models.enterprise_admin_list_self_hosted_runners_for_enterprise200_response import EnterpriseAdminListSelfHostedRunnersForEnterprise200Response
from openapi_server.models.enterprise_admin_list_self_hosted_runners_in_group_for_enterprise200_response import EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response
from openapi_server.models.enterprise_admin_set_org_access_to_self_hosted_runner_group_in_enterprise_request import EnterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest
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
from openapi_server.models.runner_application import RunnerApplication
from openapi_server.models.runner_groups_enterprise import RunnerGroupsEnterprise
from openapi_server.models.runner_no_labels import RunnerNoLabels
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.ssh_key import SshKey
from openapi_server import util


async def enterprise_admin_add_authorized_ssh_key(request: web.Request, authorized_key) -> web.Response:
    """Add an authorized SSH key

    **Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

    :param authorized_key: The public SSH key.
    :type authorized_key: str

    """
    return web.Response(status=200)


async def enterprise_admin_add_org_access_to_self_hosted_runner_group_in_enterprise(request: web.Request, enterprise, runner_group_id, org_id) -> web.Response:
    """Add organization access to a self-hosted runner group in an enterprise

    Adds an organization to the list of selected organizations that can access a self-hosted runner group. The runner group must have &#x60;visibility&#x60; set to &#x60;selected&#x60;. For more information, see \&quot;[Create a self-hosted runner group for an enterprise](#create-a-self-hosted-runner-group-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param org_id: Unique identifier of an organization.
    :type org_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_add_self_hosted_runner_to_group_for_enterprise(request: web.Request, enterprise, runner_group_id, runner_id) -> web.Response:
    """Add a self-hosted runner to a group for an enterprise

    Adds a self-hosted runner to a runner group configured in an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param runner_id: Unique identifier of the self-hosted runner.
    :type runner_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_create_enterprise_server_license(request: web.Request, license, password=None, settings=None) -> web.Response:
    """Create a GitHub license

    When you boot a GitHub instance for the first time, you can use the following endpoint to upload a license.  Note that you need to &#x60;POST&#x60; to [&#x60;/setup/api/configure&#x60;](https://docs.github.com/enterprise-server@2.22/rest/reference/enterprise-admin#start-a-configuration-process) to start the actual configuration process.  When using this endpoint, your GitHub instance must have a password set. This can be accomplished two ways:  1.  If you&#39;re working directly with the API before accessing the web interface, you must pass in the password parameter to set your password. 2.  If you set up your instance via the web interface before accessing the API, your calls to this endpoint do not need the password parameter.  **Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

    :param license: The content of your _.ghl_ license file.
    :type license: str
    :param password: You **must** provide a password _only if_ you are uploading your license for the first time. If you previously set a password through the web interface, you don&#39;t need this parameter.
    :type password: str
    :param settings: An optional JSON string containing the installation settings. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@2.22/rest/reference/enterprise-admin#get-settings).
    :type settings: str

    """
    return web.Response(status=200)


async def enterprise_admin_create_global_webhook(request: web.Request, accept, body) -> web.Response:
    """Create a global webhook

    

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminCreateGlobalWebhookRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_create_impersonation_o_auth_token(request: web.Request, username, body) -> web.Response:
    """Create an impersonation OAuth token

    

    :param username: 
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminCreateImpersonationOAuthTokenRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_create_org(request: web.Request, body) -> web.Response:
    """Create an organization

    

    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminCreateOrgRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_create_pre_receive_environment(request: web.Request, body) -> web.Response:
    """Create a pre-receive environment

    

    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminCreatePreReceiveEnvironmentRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_create_pre_receive_hook(request: web.Request, body) -> web.Response:
    """Create a pre-receive hook

    

    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminCreatePreReceiveHookRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_create_registration_token_for_enterprise(request: web.Request, enterprise) -> web.Response:
    """Create a registration token for an enterprise

    Returns a token that you can pass to the &#x60;config&#x60; script. The token expires after one hour.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.  #### Example using registration token  Configure your self-hosted runner, replacing &#x60;TOKEN&#x60; with the registration token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh --url https://github.com/enterprises/octo-enterprise --token TOKEN &#x60;&#x60;&#x60;

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str

    """
    return web.Response(status=200)


async def enterprise_admin_create_remove_token_for_enterprise(request: web.Request, enterprise) -> web.Response:
    """Create a remove token for an enterprise

    Returns a token that you can pass to the &#x60;config&#x60; script to remove a self-hosted runner from an enterprise. The token expires after one hour.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.  #### Example using remove token  To remove your self-hosted runner from an enterprise, replace &#x60;TOKEN&#x60; with the remove token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh remove --token TOKEN &#x60;&#x60;&#x60;

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str

    """
    return web.Response(status=200)


async def enterprise_admin_create_self_hosted_runner_group_for_enterprise(request: web.Request, enterprise, body) -> web.Response:
    """Create a self-hosted runner group for an enterprise

    Creates a new self-hosted runner group for an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminCreateSelfHostedRunnerGroupForEnterpriseRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_create_user(request: web.Request, body) -> web.Response:
    """Create a user

    If an external authentication mechanism is used, the login name should match the login name in the external system. If you are using LDAP authentication, you should also [update the LDAP mapping](https://docs.github.com/enterprise-server@2.22/rest/reference/enterprise-admin#update-ldap-mapping-for-a-user) for the user.  The login name will be normalized to only contain alphanumeric characters or single hyphens. For example, if you send &#x60;\&quot;octo_cat\&quot;&#x60; as the login, a user named &#x60;\&quot;octo-cat\&quot;&#x60; will be created.  If the login name or email address is already associated with an account, the server will return a &#x60;422&#x60; response.

    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminCreateUserRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_delete_global_webhook(request: web.Request, accept, hook_id) -> web.Response:
    """Delete a global webhook

    

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param hook_id: 
    :type hook_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_delete_impersonation_o_auth_token(request: web.Request, username) -> web.Response:
    """Delete an impersonation OAuth token

    

    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def enterprise_admin_delete_personal_access_token(request: web.Request, token_id) -> web.Response:
    """Delete a personal access token

    Deletes a personal access token. Returns a &#x60;403 - Forbidden&#x60; status when a personal access token is in use. For example, if you access this endpoint with the same personal access token that you are trying to delete, you will receive this error.

    :param token_id: 
    :type token_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_delete_pre_receive_environment(request: web.Request, pre_receive_environment_id) -> web.Response:
    """Delete a pre-receive environment

    If you attempt to delete an environment that cannot be deleted, you will receive a &#x60;422 Unprocessable Entity&#x60; response.  The possible error messages are:  *   _Cannot modify or delete the default environment_ *   _Cannot delete environment that has hooks_ *   _Cannot delete environment when download is in progress_

    :param pre_receive_environment_id: 
    :type pre_receive_environment_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_delete_pre_receive_hook(request: web.Request, pre_receive_hook_id) -> web.Response:
    """Delete a pre-receive hook

    

    :param pre_receive_hook_id: pre_receive_hook_id parameter
    :type pre_receive_hook_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_delete_public_key(request: web.Request, key_ids) -> web.Response:
    """Delete a public key

    

    :param key_ids: 
    :type key_ids: str

    """
    return web.Response(status=200)


async def enterprise_admin_delete_self_hosted_runner_from_enterprise(request: web.Request, enterprise, runner_id) -> web.Response:
    """Delete a self-hosted runner from an enterprise

    Forces the removal of a self-hosted runner from an enterprise. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_id: Unique identifier of the self-hosted runner.
    :type runner_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_delete_self_hosted_runner_group_from_enterprise(request: web.Request, enterprise, runner_group_id) -> web.Response:
    """Delete a self-hosted runner group from an enterprise

    Deletes a self-hosted runner group for an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_delete_user(request: web.Request, username) -> web.Response:
    """Delete a user

    Deleting a user will delete all their repositories, gists, applications, and personal settings. [Suspending a user](https://docs.github.com/enterprise-server@2.22/rest/reference/enterprise-admin#suspend-a-user) is often a better option.  You can delete any user account except your own.

    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def enterprise_admin_demote_site_administrator(request: web.Request, username) -> web.Response:
    """Demote a site administrator

    You can demote any user account except your own.

    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def enterprise_admin_enable_or_disable_maintenance_mode(request: web.Request, maintenance) -> web.Response:
    """Enable or disable maintenance mode

    **Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

    :param maintenance: A JSON string with the attributes &#x60;enabled&#x60; and &#x60;when&#x60;.  The possible values for &#x60;enabled&#x60; are &#x60;true&#x60; and &#x60;false&#x60;. When it&#39;s &#x60;false&#x60;, the attribute &#x60;when&#x60; is ignored and the maintenance mode is turned off. &#x60;when&#x60; defines the time period when the maintenance was enabled.  The possible values for &#x60;when&#x60; are &#x60;now&#x60; or any date parseable by [mojombo/chronic](https://github.com/mojombo/chronic).
    :type maintenance: str

    """
    return web.Response(status=200)


async def enterprise_admin_get_all_authorized_ssh_keys(request: web.Request, ) -> web.Response:
    """Get all authorized SSH keys

    


    """
    return web.Response(status=200)


async def enterprise_admin_get_all_stats(request: web.Request, ) -> web.Response:
    """Get all statistics

    


    """
    return web.Response(status=200)


async def enterprise_admin_get_comment_stats(request: web.Request, ) -> web.Response:
    """Get comment statistics

    


    """
    return web.Response(status=200)


async def enterprise_admin_get_configuration_status(request: web.Request, ) -> web.Response:
    """Get the configuration status

    This endpoint allows you to check the status of the most recent configuration process:  Note that you may need to wait several seconds after you start a process before you can check its status.  The different statuses are:  | Status        | Description                       | | ------------- | --------------------------------- | | &#x60;PENDING&#x60;     | The job has not started yet       | | &#x60;CONFIGURING&#x60; | The job is running                | | &#x60;DONE&#x60;        | The job has finished correctly    | | &#x60;FAILED&#x60;      | The job has finished unexpectedly |


    """
    return web.Response(status=200)


async def enterprise_admin_get_download_status_for_pre_receive_environment(request: web.Request, pre_receive_environment_id) -> web.Response:
    """Get the download status for a pre-receive environment

    In addition to seeing the download status at the \&quot;[Get a pre-receive environment](#get-a-pre-receive-environment)\&quot; endpoint, there is also this separate endpoint for just the download status.

    :param pre_receive_environment_id: 
    :type pre_receive_environment_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_get_global_webhook(request: web.Request, accept, hook_id) -> web.Response:
    """Get a global webhook

    

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param hook_id: 
    :type hook_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_get_hooks_stats(request: web.Request, ) -> web.Response:
    """Get hooks statistics

    


    """
    return web.Response(status=200)


async def enterprise_admin_get_issue_stats(request: web.Request, ) -> web.Response:
    """Get issue statistics

    


    """
    return web.Response(status=200)


async def enterprise_admin_get_license_information(request: web.Request, ) -> web.Response:
    """Get license information

    


    """
    return web.Response(status=200)


async def enterprise_admin_get_maintenance_status(request: web.Request, ) -> web.Response:
    """Get the maintenance status

    Check your installation&#39;s maintenance status:


    """
    return web.Response(status=200)


async def enterprise_admin_get_milestone_stats(request: web.Request, ) -> web.Response:
    """Get milestone statistics

    


    """
    return web.Response(status=200)


async def enterprise_admin_get_org_stats(request: web.Request, ) -> web.Response:
    """Get organization statistics

    


    """
    return web.Response(status=200)


async def enterprise_admin_get_pages_stats(request: web.Request, ) -> web.Response:
    """Get pages statistics

    


    """
    return web.Response(status=200)


async def enterprise_admin_get_pre_receive_environment(request: web.Request, pre_receive_environment_id) -> web.Response:
    """Get a pre-receive environment

    

    :param pre_receive_environment_id: 
    :type pre_receive_environment_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_get_pre_receive_hook(request: web.Request, pre_receive_hook_id) -> web.Response:
    """Get a pre-receive hook

    

    :param pre_receive_hook_id: pre_receive_hook_id parameter
    :type pre_receive_hook_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_get_pre_receive_hook_for_org(request: web.Request, org, pre_receive_hook_id) -> web.Response:
    """Get a pre-receive hook for an organization

    

    :param org: 
    :type org: str
    :param pre_receive_hook_id: pre_receive_hook_id parameter
    :type pre_receive_hook_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_get_pre_receive_hook_for_repo(request: web.Request, owner, repo, pre_receive_hook_id) -> web.Response:
    """Get a pre-receive hook for a repository

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pre_receive_hook_id: pre_receive_hook_id parameter
    :type pre_receive_hook_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_get_pull_request_stats(request: web.Request, ) -> web.Response:
    """Get pull request statistics

    


    """
    return web.Response(status=200)


async def enterprise_admin_get_repo_stats(request: web.Request, ) -> web.Response:
    """Get repository statistics

    


    """
    return web.Response(status=200)


async def enterprise_admin_get_self_hosted_runner_for_enterprise(request: web.Request, enterprise, runner_id) -> web.Response:
    """Get a self-hosted runner for an enterprise

    Gets a specific self-hosted runner configured in an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_id: Unique identifier of the self-hosted runner.
    :type runner_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_get_self_hosted_runner_group_for_enterprise(request: web.Request, enterprise, runner_group_id) -> web.Response:
    """Get a self-hosted runner group for an enterprise

    Gets a specific self-hosted runner group for an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_get_settings(request: web.Request, ) -> web.Response:
    """Get settings

    


    """
    return web.Response(status=200)


async def enterprise_admin_get_user_stats(request: web.Request, ) -> web.Response:
    """Get users statistics

    


    """
    return web.Response(status=200)


async def enterprise_admin_list_global_webhooks(request: web.Request, accept, per_page=None, page=None) -> web.Response:
    """List global webhooks

    

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def enterprise_admin_list_org_access_to_self_hosted_runner_group_in_enterprise(request: web.Request, enterprise, runner_group_id, per_page=None, page=None) -> web.Response:
    """List organization access to a self-hosted runner group in an enterprise

    Lists the organizations with access to a self-hosted runner group.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def enterprise_admin_list_personal_access_tokens(request: web.Request, per_page=None, page=None) -> web.Response:
    """List personal access tokens

    Lists personal access tokens for all users, including admin users.

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def enterprise_admin_list_pre_receive_environments(request: web.Request, per_page=None, page=None, direction=None, sort=None) -> web.Response:
    """List pre-receive environments

    

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param sort: 
    :type sort: str

    """
    return web.Response(status=200)


async def enterprise_admin_list_pre_receive_hooks(request: web.Request, per_page=None, page=None, direction=None, sort=None) -> web.Response:
    """List pre-receive hooks

    

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param sort: One of &#x60;created&#x60; (when the repository was starred) or &#x60;updated&#x60; (when it was last pushed to) or &#x60;name&#x60;.
    :type sort: str

    """
    return web.Response(status=200)


async def enterprise_admin_list_pre_receive_hooks_for_org(request: web.Request, org, per_page=None, page=None, direction=None, sort=None) -> web.Response:
    """List pre-receive hooks for an organization

    List all pre-receive hooks that are enabled or testing for this organization as well as any disabled hooks that can be configured at the organization level. Globally disabled pre-receive hooks that do not allow downstream configuration are not listed.

    :param org: 
    :type org: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param sort: The sort order for the response collection.
    :type sort: str

    """
    return web.Response(status=200)


async def enterprise_admin_list_pre_receive_hooks_for_repo(request: web.Request, owner, repo, per_page=None, page=None, direction=None, sort=None) -> web.Response:
    """List pre-receive hooks for a repository

    List all pre-receive hooks that are enabled or testing for this repository as well as any disabled hooks that are allowed to be enabled at the repository level. Pre-receive hooks that are disabled at a higher level and are not configurable will not be listed.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param sort: 
    :type sort: str

    """
    return web.Response(status=200)


async def enterprise_admin_list_public_keys(request: web.Request, per_page=None, page=None, direction=None, sort=None, since=None) -> web.Response:
    """List public keys

    

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param sort: 
    :type sort: str
    :param since: Only show public keys accessed after the given time.
    :type since: str

    """
    return web.Response(status=200)


async def enterprise_admin_list_runner_applications_for_enterprise(request: web.Request, enterprise) -> web.Response:
    """List runner applications for an enterprise

    Lists binaries for the runner application that you can download and run.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str

    """
    return web.Response(status=200)


async def enterprise_admin_list_self_hosted_runner_groups_for_enterprise(request: web.Request, enterprise, per_page=None, page=None) -> web.Response:
    """List self-hosted runner groups for an enterprise

    Lists all self-hosted runner groups for an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def enterprise_admin_list_self_hosted_runners_for_enterprise(request: web.Request, enterprise, per_page=None, page=None) -> web.Response:
    """List self-hosted runners for an enterprise

    Lists all self-hosted runners configured for an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def enterprise_admin_list_self_hosted_runners_in_group_for_enterprise(request: web.Request, enterprise, runner_group_id, per_page=None, page=None) -> web.Response:
    """List self-hosted runners in a group for an enterprise

    Lists the self-hosted runners that are in a specific enterprise group.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def enterprise_admin_ping_global_webhook(request: web.Request, accept, hook_id) -> web.Response:
    """Ping a global webhook

    This will trigger a [ping event](https://docs.github.com/enterprise-server@2.22/webhooks/#ping-event) to be sent to the webhook.

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param hook_id: 
    :type hook_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_promote_user_to_be_site_administrator(request: web.Request, username) -> web.Response:
    """Promote a user to be a site administrator

    Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def enterprise_admin_remove_authorized_ssh_key(request: web.Request, authorized_key) -> web.Response:
    """Remove an authorized SSH key

    **Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

    :param authorized_key: The public SSH key.
    :type authorized_key: str

    """
    return web.Response(status=200)


async def enterprise_admin_remove_org_access_to_self_hosted_runner_group_in_enterprise(request: web.Request, enterprise, runner_group_id, org_id) -> web.Response:
    """Remove organization access to a self-hosted runner group in an enterprise

    Removes an organization from the list of selected organizations that can access a self-hosted runner group. The runner group must have &#x60;visibility&#x60; set to &#x60;selected&#x60;. For more information, see \&quot;[Create a self-hosted runner group for an enterprise](#create-a-self-hosted-runner-group-for-an-enterprise).\&quot;  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param org_id: Unique identifier of an organization.
    :type org_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_remove_pre_receive_hook_enforcement_for_org(request: web.Request, org, pre_receive_hook_id) -> web.Response:
    """Remove pre-receive hook enforcement for an organization

    Removes any overrides for this hook at the org level for this org.

    :param org: 
    :type org: str
    :param pre_receive_hook_id: pre_receive_hook_id parameter
    :type pre_receive_hook_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_remove_pre_receive_hook_enforcement_for_repo(request: web.Request, owner, repo, pre_receive_hook_id) -> web.Response:
    """Remove pre-receive hook enforcement for a repository

    Deletes any overridden enforcement on this repository for the specified hook.  Responds with effective values inherited from owner and/or global level.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pre_receive_hook_id: pre_receive_hook_id parameter
    :type pre_receive_hook_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_remove_self_hosted_runner_from_group_for_enterprise(request: web.Request, enterprise, runner_group_id, runner_id) -> web.Response:
    """Remove a self-hosted runner from a group for an enterprise

    Removes a self-hosted runner from a group configured in an enterprise. The runner is then returned to the default group.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param runner_id: Unique identifier of the self-hosted runner.
    :type runner_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_set_org_access_to_self_hosted_runner_group_in_enterprise(request: web.Request, enterprise, runner_group_id, body) -> web.Response:
    """Set organization access for a self-hosted runner group in an enterprise

    Replaces the list of organizations that have access to a self-hosted runner configured in an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminSetOrgAccessToSelfHostedRunnerGroupInEnterpriseRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_set_self_hosted_runners_in_group_for_enterprise(request: web.Request, enterprise, runner_group_id, body) -> web.Response:
    """Set self-hosted runners in a group for an enterprise

    Replaces the list of self-hosted runners that are part of an enterprise runner group.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_set_settings(request: web.Request, settings) -> web.Response:
    """Set settings

    For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@2.22/rest/reference/enterprise-admin#get-settings).  **Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

    :param settings: A JSON string with the new settings. Note that you only need to pass the specific settings you want to modify. For a list of the available settings, see the [Get settings endpoint](https://docs.github.com/enterprise-server@2.22/rest/reference/enterprise-admin#get-settings).
    :type settings: str

    """
    return web.Response(status=200)


async def enterprise_admin_start_configuration_process(request: web.Request, ) -> web.Response:
    """Start a configuration process

    This endpoint allows you to start a configuration process at any time for your updated settings to take effect:


    """
    return web.Response(status=200)


async def enterprise_admin_start_pre_receive_environment_download(request: web.Request, pre_receive_environment_id) -> web.Response:
    """Start a pre-receive environment download

    Triggers a new download of the environment tarball from the environment&#39;s &#x60;image_url&#x60;. When the download is finished, the newly downloaded tarball will overwrite the existing environment.  If a download cannot be triggered, you will receive a &#x60;422 Unprocessable Entity&#x60; response.  The possible error messages are:  * _Cannot modify or delete the default environment_ * _Can not start a new download when a download is in progress_

    :param pre_receive_environment_id: 
    :type pre_receive_environment_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_suspend_user(request: web.Request, username, body=None) -> web.Response:
    """Suspend a user

    If your GitHub instance uses [LDAP Sync with Active Directory LDAP servers](https://help.github.com/enterprise/admin/guides/user-management/using-ldap), Active Directory LDAP-authenticated users cannot be suspended through this API. If you attempt to suspend an Active Directory LDAP-authenticated user through this API, it will return a &#x60;403&#x60; response.  You can suspend any user account except your own.  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

    :param username: 
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminSuspendUserRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_sync_ldap_mapping_for_team(request: web.Request, team_id) -> web.Response:
    """Sync LDAP mapping for a team

    Note that this API call does not automatically initiate an LDAP sync. Rather, if a &#x60;201&#x60; is returned, the sync job is queued successfully, and is performed when the instance is ready.

    :param team_id: 
    :type team_id: int

    """
    return web.Response(status=200)


async def enterprise_admin_sync_ldap_mapping_for_user(request: web.Request, username) -> web.Response:
    """Sync LDAP mapping for a user

    Note that this API call does not automatically initiate an LDAP sync. Rather, if a &#x60;201&#x60; is returned, the sync job is queued successfully, and is performed when the instance is ready.

    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def enterprise_admin_unsuspend_user(request: web.Request, username, body=None) -> web.Response:
    """Unsuspend a user

    If your GitHub instance uses [LDAP Sync with Active Directory LDAP servers](https://help.github.com/enterprise/admin/guides/user-management/using-ldap), this API is disabled and will return a &#x60;403&#x60; response. Active Directory LDAP-authenticated users cannot be unsuspended using the API.

    :param username: 
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminUnsuspendUserRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_update_global_webhook(request: web.Request, accept, hook_id, body=None) -> web.Response:
    """Update a global webhook

    Parameters that are not provided will be overwritten with the default value or removed if no default exists.

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param hook_id: 
    :type hook_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminUpdateGlobalWebhookRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_update_ldap_mapping_for_team(request: web.Request, team_id, body) -> web.Response:
    """Update LDAP mapping for a team

    Updates the [distinguished name](https://www.ldap.com/ldap-dns-and-rdns) (DN) of the LDAP entry to map to a team. [LDAP synchronization](https://help.github.com/enterprise/admin/guides/user-management/using-ldap/#enabling-ldap-sync) must be enabled to map LDAP entries to a team. Use the [Create a team](https://docs.github.com/enterprise-server@2.22/rest/reference/teams/#create-a-team) endpoint to create a team with LDAP mapping.  If you pass the &#x60;hellcat-preview&#x60; media type, you can also update the LDAP mapping of a child team.

    :param team_id: 
    :type team_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminUpdateLdapMappingForTeamRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_update_ldap_mapping_for_user(request: web.Request, username, body) -> web.Response:
    """Update LDAP mapping for a user

    

    :param username: 
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminUpdateLdapMappingForTeamRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_update_org_name(request: web.Request, org, body) -> web.Response:
    """Update an organization name

    

    :param org: 
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminUpdateOrgNameRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_update_pre_receive_environment(request: web.Request, pre_receive_environment_id, body=None) -> web.Response:
    """Update a pre-receive environment

    You cannot modify the default environment. If you attempt to modify the default environment, you will receive a &#x60;422 Unprocessable Entity&#x60; response.

    :param pre_receive_environment_id: 
    :type pre_receive_environment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminUpdatePreReceiveEnvironmentRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_update_pre_receive_hook(request: web.Request, pre_receive_hook_id, body=None) -> web.Response:
    """Update a pre-receive hook

    

    :param pre_receive_hook_id: pre_receive_hook_id parameter
    :type pre_receive_hook_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminUpdatePreReceiveHookRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_update_pre_receive_hook_enforcement_for_org(request: web.Request, org, pre_receive_hook_id, body=None) -> web.Response:
    """Update pre-receive hook enforcement for an organization

    For pre-receive hooks which are allowed to be configured at the org level, you can set &#x60;enforcement&#x60; and &#x60;allow_downstream_configuration&#x60;

    :param org: 
    :type org: str
    :param pre_receive_hook_id: pre_receive_hook_id parameter
    :type pre_receive_hook_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminUpdatePreReceiveHookEnforcementForOrgRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_update_pre_receive_hook_enforcement_for_repo(request: web.Request, owner, repo, pre_receive_hook_id, body=None) -> web.Response:
    """Update pre-receive hook enforcement for a repository

    For pre-receive hooks which are allowed to be configured at the repo level, you can set &#x60;enforcement&#x60;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param pre_receive_hook_id: pre_receive_hook_id parameter
    :type pre_receive_hook_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminUpdatePreReceiveHookEnforcementForRepoRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_update_self_hosted_runner_group_for_enterprise(request: web.Request, enterprise, runner_group_id, body=None) -> web.Response:
    """Update a self-hosted runner group for an enterprise

    Updates the &#x60;name&#x60; and &#x60;visibility&#x60; of a self-hosted runner group in an enterprise.  You must authenticate using an access token with the &#x60;admin:enterprise&#x60; scope to use this endpoint.

    :param enterprise: The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    :type enterprise: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminUpdateSelfHostedRunnerGroupForEnterpriseRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_update_username_for_user(request: web.Request, username, body) -> web.Response:
    """Update the username for a user

    

    :param username: 
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminUpdateUsernameForUserRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_admin_upgrade_license(request: web.Request, license=None) -> web.Response:
    """Upgrade a license

    This API upgrades your license and also triggers the configuration process.  **Note:** The request body for this operation must be submitted as &#x60;application/x-www-form-urlencoded&#x60; data. You can submit a parameter value as a string, or you can use a tool such as &#x60;curl&#x60; to submit a parameter value as the contents of a text file. For more information, see the [&#x60;curl&#x60; documentation](https://curl.se/docs/manpage.html#--data-urlencode).

    :param license: The content of your new _.ghl_ license file.
    :type license: str

    """
    return web.Response(status=200)


async def enterprise_stats_gists_get(request: web.Request, ) -> web.Response:
    """Get gist statistics

    


    """
    return web.Response(status=200)
