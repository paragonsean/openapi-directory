from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_slack_channel_configuration_request import CreateSlackChannelConfigurationRequest
from openapi_server.models.delete_slack_channel_configuration_request import DeleteSlackChannelConfigurationRequest
from openapi_server.models.delete_slack_workspace_configuration_request import DeleteSlackWorkspaceConfigurationRequest
from openapi_server.models.get_account_alias_result import GetAccountAliasResult
from openapi_server.models.list_slack_channel_configurations_request import ListSlackChannelConfigurationsRequest
from openapi_server.models.list_slack_channel_configurations_result import ListSlackChannelConfigurationsResult
from openapi_server.models.list_slack_workspace_configurations_result import ListSlackWorkspaceConfigurationsResult
from openapi_server.models.put_account_alias_request import PutAccountAliasRequest
from openapi_server.models.register_slack_workspace_for_organization_request import RegisterSlackWorkspaceForOrganizationRequest
from openapi_server.models.register_slack_workspace_for_organization_result import RegisterSlackWorkspaceForOrganizationResult
from openapi_server.models.update_slack_channel_configuration_request import UpdateSlackChannelConfigurationRequest
from openapi_server.models.update_slack_channel_configuration_result import UpdateSlackChannelConfigurationResult
from openapi_server import util


async def create_slack_channel_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_slack_channel_configuration

    &lt;p&gt;Creates a Slack channel configuration for your Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can add up to 5 Slack workspaces for your account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can add up to 20 Slack channels for your account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;A Slack channel can have up to 100 Amazon Web Services accounts. This means that only 100 accounts can add the same Slack channel to the Amazon Web Services Support App. We recommend that you only add the accounts that you need to manage support cases for your organization. This can reduce the notifications about case updates that you receive in the Slack channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;We recommend that you choose a private Slack channel so that only members in that channel have read and write access to your support cases. Anyone in your Slack channel can create, update, or resolve support cases for your account. Users require an invitation to join private channels. &lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSlackChannelConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_account_alias(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_account_alias

    Deletes an alias for an Amazon Web Services account ID. The alias appears in the Amazon Web Services Support App page of the Amazon Web Services Support Center. The alias also appears in Slack messages from the Amazon Web Services Support App.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_slack_channel_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_slack_channel_configuration

    Deletes a Slack channel configuration from your Amazon Web Services account. This operation doesn&#39;t delete your Slack channel.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteSlackChannelConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_slack_workspace_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_slack_workspace_configuration

    Deletes a Slack workspace configuration from your Amazon Web Services account. This operation doesn&#39;t delete your Slack workspace.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteSlackWorkspaceConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def get_account_alias(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account_alias

    Retrieves the alias from an Amazon Web Services account ID. The alias appears in the Amazon Web Services Support App page of the Amazon Web Services Support Center. The alias also appears in Slack messages from the Amazon Web Services Support App.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_slack_channel_configurations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_slack_channel_configurations

    Lists the Slack channel configurations for an Amazon Web Services account.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListSlackChannelConfigurationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_slack_workspace_configurations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_slack_workspace_configurations

    Lists the Slack workspace configurations for an Amazon Web Services account.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListSlackChannelConfigurationsRequest.from_dict(body)
    return web.Response(status=200)


async def put_account_alias(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_account_alias

    Creates or updates an individual alias for each Amazon Web Services account ID. The alias appears in the Amazon Web Services Support App page of the Amazon Web Services Support Center. The alias also appears in Slack messages from the Amazon Web Services Support App.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAccountAliasRequest.from_dict(body)
    return web.Response(status=200)


async def register_slack_workspace_for_organization(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_slack_workspace_for_organization

    &lt;p&gt;Registers a Slack workspace for your Amazon Web Services account. To call this API, your account must be part of an organization in Organizations.&lt;/p&gt; &lt;p&gt;If you&#39;re the &lt;i&gt;management account&lt;/i&gt; and you want to register Slack workspaces for your organization, you must complete the following tasks:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Sign in to the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/app\&quot;&gt;Amazon Web Services Support Center&lt;/a&gt; and authorize the Slack workspaces where you want your organization to have access to. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/authorize-slack-workspace.html\&quot;&gt;Authorize a Slack workspace&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call the &lt;code&gt;RegisterSlackWorkspaceForOrganization&lt;/code&gt; API to authorize each Slack workspace for the organization.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;After the management account authorizes the Slack workspace, member accounts can call this API to authorize the same Slack workspace for their individual accounts. Member accounts don&#39;t need to authorize the Slack workspace manually through the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/app\&quot;&gt;Amazon Web Services Support Center&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To use the Amazon Web Services Support App, each account must then complete the following tasks:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Create an Identity and Access Management (IAM) role with the required permission. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html\&quot;&gt;Managing access to the Amazon Web Services Support App&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Configure a Slack channel to use the Amazon Web Services Support App for support cases for that account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/add-your-slack-channel.html\&quot;&gt;Configuring a Slack channel&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RegisterSlackWorkspaceForOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def update_slack_channel_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_slack_channel_configuration

    Updates the configuration for a Slack channel, such as case update notifications.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateSlackChannelConfigurationRequest.from_dict(body)
    return web.Response(status=200)
