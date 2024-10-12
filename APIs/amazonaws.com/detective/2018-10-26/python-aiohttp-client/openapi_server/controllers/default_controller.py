from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_invitation_request import AcceptInvitationRequest
from openapi_server.models.batch_get_graph_member_datasources_request import BatchGetGraphMemberDatasourcesRequest
from openapi_server.models.batch_get_graph_member_datasources_response import BatchGetGraphMemberDatasourcesResponse
from openapi_server.models.batch_get_membership_datasources_request import BatchGetMembershipDatasourcesRequest
from openapi_server.models.batch_get_membership_datasources_response import BatchGetMembershipDatasourcesResponse
from openapi_server.models.create_graph_request import CreateGraphRequest
from openapi_server.models.create_graph_response import CreateGraphResponse
from openapi_server.models.create_members_request import CreateMembersRequest
from openapi_server.models.create_members_response import CreateMembersResponse
from openapi_server.models.delete_graph_request import DeleteGraphRequest
from openapi_server.models.delete_members_request import DeleteMembersRequest
from openapi_server.models.delete_members_response import DeleteMembersResponse
from openapi_server.models.describe_organization_configuration_request import DescribeOrganizationConfigurationRequest
from openapi_server.models.describe_organization_configuration_response import DescribeOrganizationConfigurationResponse
from openapi_server.models.disassociate_membership_request import DisassociateMembershipRequest
from openapi_server.models.enable_organization_admin_account_request import EnableOrganizationAdminAccountRequest
from openapi_server.models.get_members_request import GetMembersRequest
from openapi_server.models.get_members_response import GetMembersResponse
from openapi_server.models.list_datasource_packages_request import ListDatasourcePackagesRequest
from openapi_server.models.list_datasource_packages_response import ListDatasourcePackagesResponse
from openapi_server.models.list_graphs_request import ListGraphsRequest
from openapi_server.models.list_graphs_response import ListGraphsResponse
from openapi_server.models.list_invitations_request import ListInvitationsRequest
from openapi_server.models.list_invitations_response import ListInvitationsResponse
from openapi_server.models.list_members_request import ListMembersRequest
from openapi_server.models.list_members_response import ListMembersResponse
from openapi_server.models.list_organization_admin_accounts_request import ListOrganizationAdminAccountsRequest
from openapi_server.models.list_organization_admin_accounts_response import ListOrganizationAdminAccountsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.reject_invitation_request import RejectInvitationRequest
from openapi_server.models.start_monitoring_member_request import StartMonitoringMemberRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_datasource_packages_request import UpdateDatasourcePackagesRequest
from openapi_server.models.update_organization_configuration_request import UpdateOrganizationConfigurationRequest
from openapi_server import util


async def accept_invitation(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """accept_invitation

    &lt;p&gt;Accepts an invitation for the member account to contribute data to a behavior graph. This operation can only be called by an invited member account. &lt;/p&gt; &lt;p&gt;The request provides the ARN of behavior graph.&lt;/p&gt; &lt;p&gt;The member account status in the graph must be &lt;code&gt;INVITED&lt;/code&gt;.&lt;/p&gt;

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
    body = AcceptInvitationRequest.from_dict(body)
    return web.Response(status=200)


async def batch_get_graph_member_datasources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_get_graph_member_datasources

    Gets data source package information for the behavior graph.

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
    body = BatchGetGraphMemberDatasourcesRequest.from_dict(body)
    return web.Response(status=200)


async def batch_get_membership_datasources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_get_membership_datasources

    Gets information on the data source package history for an account.

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
    body = BatchGetMembershipDatasourcesRequest.from_dict(body)
    return web.Response(status=200)


async def create_graph(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_graph

    &lt;p&gt;Creates a new behavior graph for the calling account, and sets that account as the administrator account. This operation is called by the account that is enabling Detective.&lt;/p&gt; &lt;p&gt;Before you try to enable Detective, make sure that your account has been enrolled in Amazon GuardDuty for at least 48 hours. If you do not meet this requirement, you cannot enable Detective. If you do meet the GuardDuty prerequisite, then when you make the request to enable Detective, it checks whether your data volume is within the Detective quota. If it exceeds the quota, then you cannot enable Detective. &lt;/p&gt; &lt;p&gt;The operation also enables Detective for the calling account in the currently selected Region. It returns the ARN of the new behavior graph.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateGraph&lt;/code&gt; triggers a process to create the corresponding data tables for the new behavior graph.&lt;/p&gt; &lt;p&gt;An account can only be the administrator account for one behavior graph within a Region. If the same account calls &lt;code&gt;CreateGraph&lt;/code&gt; with the same administrator account, it always returns the same behavior graph ARN. It does not create a new behavior graph.&lt;/p&gt;

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
    body = CreateGraphRequest.from_dict(body)
    return web.Response(status=200)


async def create_members(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_members

    &lt;p&gt; &lt;code&gt;CreateMembers&lt;/code&gt; is used to send invitations to accounts. For the organization behavior graph, the Detective administrator account uses &lt;code&gt;CreateMembers&lt;/code&gt; to enable organization accounts as member accounts.&lt;/p&gt; &lt;p&gt;For invited accounts, &lt;code&gt;CreateMembers&lt;/code&gt; sends a request to invite the specified Amazon Web Services accounts to be member accounts in the behavior graph. This operation can only be called by the administrator account for a behavior graph. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateMembers&lt;/code&gt; verifies the accounts and then invites the verified accounts. The administrator can optionally specify to not send invitation emails to the member accounts. This would be used when the administrator manages their member accounts centrally.&lt;/p&gt; &lt;p&gt;For organization accounts in the organization behavior graph, &lt;code&gt;CreateMembers&lt;/code&gt; attempts to enable the accounts. The organization accounts do not receive invitations.&lt;/p&gt; &lt;p&gt;The request provides the behavior graph ARN and the list of accounts to invite or to enable.&lt;/p&gt; &lt;p&gt;The response separates the requested accounts into two lists:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The accounts that &lt;code&gt;CreateMembers&lt;/code&gt; was able to process. For invited accounts, includes member accounts that are being verified, that have passed verification and are to be invited, and that have failed verification. For organization accounts in the organization behavior graph, includes accounts that can be enabled and that cannot be enabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The accounts that &lt;code&gt;CreateMembers&lt;/code&gt; was unable to process. This list includes accounts that were already invited to be member accounts in the behavior graph.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateMembersRequest.from_dict(body)
    return web.Response(status=200)


async def delete_graph(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_graph

    &lt;p&gt;Disables the specified behavior graph and queues it to be deleted. This operation removes the behavior graph from each member account&#39;s list of behavior graphs.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DeleteGraph&lt;/code&gt; can only be called by the administrator account for a behavior graph.&lt;/p&gt;

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
    body = DeleteGraphRequest.from_dict(body)
    return web.Response(status=200)


async def delete_members(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_members

    &lt;p&gt;Removes the specified member accounts from the behavior graph. The removed accounts no longer contribute data to the behavior graph. This operation can only be called by the administrator account for the behavior graph.&lt;/p&gt; &lt;p&gt;For invited accounts, the removed accounts are deleted from the list of accounts in the behavior graph. To restore the account, the administrator account must send another invitation.&lt;/p&gt; &lt;p&gt;For organization accounts in the organization behavior graph, the Detective administrator account can always enable the organization account again. Organization accounts that are not enabled as member accounts are not included in the &lt;code&gt;ListMembers&lt;/code&gt; results for the organization behavior graph.&lt;/p&gt; &lt;p&gt;An administrator account cannot use &lt;code&gt;DeleteMembers&lt;/code&gt; to remove their own account from the behavior graph. To disable a behavior graph, the administrator account uses the &lt;code&gt;DeleteGraph&lt;/code&gt; API method.&lt;/p&gt;

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
    body = DeleteMembersRequest.from_dict(body)
    return web.Response(status=200)


async def describe_organization_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_organization_configuration

    &lt;p&gt;Returns information about the configuration for the organization behavior graph. Currently indicates whether to automatically enable new organization accounts as member accounts.&lt;/p&gt; &lt;p&gt;Can only be called by the Detective administrator account for the organization. &lt;/p&gt;

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
    body = DescribeOrganizationConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def disable_organization_admin_account(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disable_organization_admin_account

    &lt;p&gt;Removes the Detective administrator account in the current Region. Deletes the organization behavior graph.&lt;/p&gt; &lt;p&gt;Can only be called by the organization management account.&lt;/p&gt; &lt;p&gt;Removing the Detective administrator account does not affect the delegated administrator account for Detective in Organizations.&lt;/p&gt; &lt;p&gt;To remove the delegated administrator account in Organizations, use the Organizations API. Removing the delegated administrator account also removes the Detective administrator account in all Regions, except for Regions where the Detective administrator account is the organization management account.&lt;/p&gt;

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


async def disassociate_membership(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_membership

    &lt;p&gt;Removes the member account from the specified behavior graph. This operation can only be called by an invited member account that has the &lt;code&gt;ENABLED&lt;/code&gt; status.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DisassociateMembership&lt;/code&gt; cannot be called by an organization account in the organization behavior graph. For the organization behavior graph, the Detective administrator account determines which organization accounts to enable or disable as member accounts.&lt;/p&gt;

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
    body = DisassociateMembershipRequest.from_dict(body)
    return web.Response(status=200)


async def enable_organization_admin_account(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """enable_organization_admin_account

    &lt;p&gt;Designates the Detective administrator account for the organization in the current Region.&lt;/p&gt; &lt;p&gt;If the account does not have Detective enabled, then enables Detective for that account and creates a new behavior graph.&lt;/p&gt; &lt;p&gt;Can only be called by the organization management account.&lt;/p&gt; &lt;p&gt;If the organization has a delegated administrator account in Organizations, then the Detective administrator account must be either the delegated administrator account or the organization management account.&lt;/p&gt; &lt;p&gt;If the organization does not have a delegated administrator account in Organizations, then you can choose any account in the organization. If you choose an account other than the organization management account, Detective calls Organizations to make that account the delegated administrator account for Detective. The organization management account cannot be the delegated administrator account.&lt;/p&gt;

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
    body = EnableOrganizationAdminAccountRequest.from_dict(body)
    return web.Response(status=200)


async def get_members(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_members

    Returns the membership details for specified member accounts for a behavior graph.

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
    body = GetMembersRequest.from_dict(body)
    return web.Response(status=200)


async def list_datasource_packages(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_datasource_packages

    Lists data source packages in the behavior graph.

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListDatasourcePackagesRequest.from_dict(body)
    return web.Response(status=200)


async def list_graphs(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_graphs

    &lt;p&gt;Returns the list of behavior graphs that the calling account is an administrator account of. This operation can only be called by an administrator account.&lt;/p&gt; &lt;p&gt;Because an account can currently only be the administrator of one behavior graph within a Region, the results always contain a single behavior graph.&lt;/p&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListGraphsRequest.from_dict(body)
    return web.Response(status=200)


async def list_invitations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_invitations

    &lt;p&gt;Retrieves the list of open and accepted behavior graph invitations for the member account. This operation can only be called by an invited member account.&lt;/p&gt; &lt;p&gt;Open invitations are invitations that the member account has not responded to.&lt;/p&gt; &lt;p&gt;The results do not include behavior graphs for which the member account declined the invitation. The results also do not include behavior graphs that the member account resigned from or was removed from.&lt;/p&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListInvitationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_members(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_members

    &lt;p&gt;Retrieves the list of member accounts for a behavior graph.&lt;/p&gt; &lt;p&gt;For invited accounts, the results do not include member accounts that were removed from the behavior graph.&lt;/p&gt; &lt;p&gt;For the organization behavior graph, the results do not include organization accounts that the Detective administrator account has not enabled as member accounts.&lt;/p&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListMembersRequest.from_dict(body)
    return web.Response(status=200)


async def list_organization_admin_accounts(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_organization_admin_accounts

    Returns information about the Detective administrator account for an organization. Can only be called by the organization management account.

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListOrganizationAdminAccountsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Returns the tag values that are assigned to a behavior graph.

    :param resource_arn: The ARN of the behavior graph for which to retrieve the tag values.
    :type resource_arn: str
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


async def reject_invitation(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reject_invitation

    &lt;p&gt;Rejects an invitation to contribute the account data to a behavior graph. This operation must be called by an invited member account that has the &lt;code&gt;INVITED&lt;/code&gt; status.&lt;/p&gt; &lt;p&gt; &lt;code&gt;RejectInvitation&lt;/code&gt; cannot be called by an organization account in the organization behavior graph. In the organization behavior graph, organization accounts do not receive an invitation.&lt;/p&gt;

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
    body = RejectInvitationRequest.from_dict(body)
    return web.Response(status=200)


async def start_monitoring_member(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_monitoring_member

    &lt;p&gt;Sends a request to enable data ingest for a member account that has a status of &lt;code&gt;ACCEPTED_BUT_DISABLED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For valid member accounts, the status is updated as follows.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If Detective enabled the member account, then the new status is &lt;code&gt;ENABLED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If Detective cannot enable the member account, the status remains &lt;code&gt;ACCEPTED_BUT_DISABLED&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = StartMonitoringMemberRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Applies tag values to a behavior graph.

    :param resource_arn: The ARN of the behavior graph to assign the tags to.
    :type resource_arn: str
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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes tags from a behavior graph.

    :param resource_arn: The ARN of the behavior graph to remove the tags from.
    :type resource_arn: str
    :param tag_keys: The tag keys of the tags to remove from the behavior graph. You can remove up to 50 tags at a time.
    :type tag_keys: List[str]
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


async def update_datasource_packages(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_datasource_packages

    Starts a data source packages for the behavior graph.

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
    body = UpdateDatasourcePackagesRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_organization_configuration

    Updates the configuration for the Organizations integration in the current Region. Can only be called by the Detective administrator account for the organization.

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
    body = UpdateOrganizationConfigurationRequest.from_dict(body)
    return web.Response(status=200)
