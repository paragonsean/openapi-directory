from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_handshake_request import AcceptHandshakeRequest
from openapi_server.models.accept_handshake_response import AcceptHandshakeResponse
from openapi_server.models.attach_policy_request import AttachPolicyRequest
from openapi_server.models.cancel_handshake_request import CancelHandshakeRequest
from openapi_server.models.cancel_handshake_response import CancelHandshakeResponse
from openapi_server.models.close_account_request import CloseAccountRequest
from openapi_server.models.create_account_request import CreateAccountRequest
from openapi_server.models.create_account_response import CreateAccountResponse
from openapi_server.models.create_gov_cloud_account_request import CreateGovCloudAccountRequest
from openapi_server.models.create_gov_cloud_account_response import CreateGovCloudAccountResponse
from openapi_server.models.create_organization_request import CreateOrganizationRequest
from openapi_server.models.create_organization_response import CreateOrganizationResponse
from openapi_server.models.create_organizational_unit_request import CreateOrganizationalUnitRequest
from openapi_server.models.create_organizational_unit_response import CreateOrganizationalUnitResponse
from openapi_server.models.create_policy_request import CreatePolicyRequest
from openapi_server.models.create_policy_response import CreatePolicyResponse
from openapi_server.models.decline_handshake_request import DeclineHandshakeRequest
from openapi_server.models.decline_handshake_response import DeclineHandshakeResponse
from openapi_server.models.delete_organizational_unit_request import DeleteOrganizationalUnitRequest
from openapi_server.models.delete_policy_request import DeletePolicyRequest
from openapi_server.models.deregister_delegated_administrator_request import DeregisterDelegatedAdministratorRequest
from openapi_server.models.describe_account_request import DescribeAccountRequest
from openapi_server.models.describe_account_response import DescribeAccountResponse
from openapi_server.models.describe_create_account_status_request import DescribeCreateAccountStatusRequest
from openapi_server.models.describe_create_account_status_response import DescribeCreateAccountStatusResponse
from openapi_server.models.describe_effective_policy_request import DescribeEffectivePolicyRequest
from openapi_server.models.describe_effective_policy_response import DescribeEffectivePolicyResponse
from openapi_server.models.describe_handshake_request import DescribeHandshakeRequest
from openapi_server.models.describe_handshake_response import DescribeHandshakeResponse
from openapi_server.models.describe_organization_response import DescribeOrganizationResponse
from openapi_server.models.describe_organizational_unit_request import DescribeOrganizationalUnitRequest
from openapi_server.models.describe_organizational_unit_response import DescribeOrganizationalUnitResponse
from openapi_server.models.describe_policy_request import DescribePolicyRequest
from openapi_server.models.describe_policy_response import DescribePolicyResponse
from openapi_server.models.describe_resource_policy_response import DescribeResourcePolicyResponse
from openapi_server.models.detach_policy_request import DetachPolicyRequest
from openapi_server.models.disable_aws_service_access_request import DisableAWSServiceAccessRequest
from openapi_server.models.disable_policy_type_request import DisablePolicyTypeRequest
from openapi_server.models.disable_policy_type_response import DisablePolicyTypeResponse
from openapi_server.models.enable_aws_service_access_request import EnableAWSServiceAccessRequest
from openapi_server.models.enable_all_features_response import EnableAllFeaturesResponse
from openapi_server.models.enable_policy_type_request import EnablePolicyTypeRequest
from openapi_server.models.enable_policy_type_response import EnablePolicyTypeResponse
from openapi_server.models.invite_account_to_organization_request import InviteAccountToOrganizationRequest
from openapi_server.models.invite_account_to_organization_response import InviteAccountToOrganizationResponse
from openapi_server.models.list_aws_service_access_for_organization_request import ListAWSServiceAccessForOrganizationRequest
from openapi_server.models.list_aws_service_access_for_organization_response import ListAWSServiceAccessForOrganizationResponse
from openapi_server.models.list_accounts_for_parent_request import ListAccountsForParentRequest
from openapi_server.models.list_accounts_for_parent_response import ListAccountsForParentResponse
from openapi_server.models.list_accounts_request import ListAccountsRequest
from openapi_server.models.list_accounts_response import ListAccountsResponse
from openapi_server.models.list_children_request import ListChildrenRequest
from openapi_server.models.list_children_response import ListChildrenResponse
from openapi_server.models.list_create_account_status_request import ListCreateAccountStatusRequest
from openapi_server.models.list_create_account_status_response import ListCreateAccountStatusResponse
from openapi_server.models.list_delegated_administrators_request import ListDelegatedAdministratorsRequest
from openapi_server.models.list_delegated_administrators_response import ListDelegatedAdministratorsResponse
from openapi_server.models.list_delegated_services_for_account_request import ListDelegatedServicesForAccountRequest
from openapi_server.models.list_delegated_services_for_account_response import ListDelegatedServicesForAccountResponse
from openapi_server.models.list_handshakes_for_account_request import ListHandshakesForAccountRequest
from openapi_server.models.list_handshakes_for_account_response import ListHandshakesForAccountResponse
from openapi_server.models.list_handshakes_for_organization_request import ListHandshakesForOrganizationRequest
from openapi_server.models.list_handshakes_for_organization_response import ListHandshakesForOrganizationResponse
from openapi_server.models.list_organizational_units_for_parent_request import ListOrganizationalUnitsForParentRequest
from openapi_server.models.list_organizational_units_for_parent_response import ListOrganizationalUnitsForParentResponse
from openapi_server.models.list_parents_request import ListParentsRequest
from openapi_server.models.list_parents_response import ListParentsResponse
from openapi_server.models.list_policies_for_target_request import ListPoliciesForTargetRequest
from openapi_server.models.list_policies_for_target_response import ListPoliciesForTargetResponse
from openapi_server.models.list_policies_request import ListPoliciesRequest
from openapi_server.models.list_policies_response import ListPoliciesResponse
from openapi_server.models.list_roots_request import ListRootsRequest
from openapi_server.models.list_roots_response import ListRootsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_targets_for_policy_request import ListTargetsForPolicyRequest
from openapi_server.models.list_targets_for_policy_response import ListTargetsForPolicyResponse
from openapi_server.models.move_account_request import MoveAccountRequest
from openapi_server.models.put_resource_policy_request import PutResourcePolicyRequest
from openapi_server.models.put_resource_policy_response import PutResourcePolicyResponse
from openapi_server.models.register_delegated_administrator_request import RegisterDelegatedAdministratorRequest
from openapi_server.models.remove_account_from_organization_request import RemoveAccountFromOrganizationRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_organizational_unit_request import UpdateOrganizationalUnitRequest
from openapi_server.models.update_organizational_unit_response import UpdateOrganizationalUnitResponse
from openapi_server.models.update_policy_request import UpdatePolicyRequest
from openapi_server.models.update_policy_response import UpdatePolicyResponse
from openapi_server import util


async def accept_handshake(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """accept_handshake

    &lt;p&gt;Sends a response to the originator of a handshake agreeing to the action proposed by the handshake request.&lt;/p&gt; &lt;p&gt;You can only call this operation by the following principals when they also have the relevant IAM permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Invitation to join&lt;/b&gt; or &lt;b&gt;Approve all features request&lt;/b&gt; handshakes: only a principal from the member account.&lt;/p&gt; &lt;p&gt;The user who calls the API for an invitation to join must have the &lt;code&gt;organizations:AcceptHandshake&lt;/code&gt; permission. If you enabled all features in the organization, the user must also have the &lt;code&gt;iam:CreateServiceLinkedRole&lt;/code&gt; permission so that Organizations can create the required service-linked role named &lt;code&gt;AWSServiceRoleForOrganizations&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integration_services.html#orgs_integration_service-linked-roles\&quot;&gt;Organizations and Service-Linked Roles&lt;/a&gt; in the &lt;i&gt;Organizations User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Enable all features final confirmation&lt;/b&gt; handshake: only a principal from the management account.&lt;/p&gt; &lt;p&gt;For more information about invitations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html\&quot;&gt;Inviting an Amazon Web Services account to join your organization&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; For more information about requests to enable all features in the organization, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\&quot;&gt;Enabling all features in your organization&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;After you accept a handshake, it continues to appear in the results of relevant APIs for only 30 days. After that, it&#39;s deleted.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = AcceptHandshakeRequest.from_dict(body)
    return web.Response(status=200)


async def attach_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """attach_policy

    &lt;p&gt;Attaches a policy to a root, an organizational unit (OU), or an individual account. How the policy affects accounts depends on the type of policy. Refer to the &lt;i&gt;Organizations User Guide&lt;/i&gt; for information about each policy type:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html\&quot;&gt;AISERVICES_OPT_OUT_POLICY&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html\&quot;&gt;BACKUP_POLICY&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html\&quot;&gt;SERVICE_CONTROL_POLICY&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html\&quot;&gt;TAG_POLICY&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = AttachPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_handshake(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_handshake

    &lt;p&gt;Cancels a handshake. Canceling a handshake sets the handshake state to &lt;code&gt;CANCELED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation can be called only from the account that originated the handshake. The recipient of the handshake can&#39;t cancel it, but can use &lt;a&gt;DeclineHandshake&lt;/a&gt; instead. After a handshake is canceled, the recipient can no longer respond to that handshake.&lt;/p&gt; &lt;p&gt;After you cancel a handshake, it continues to appear in the results of relevant APIs for only 30 days. After that, it&#39;s deleted.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CancelHandshakeRequest.from_dict(body)
    return web.Response(status=200)


async def close_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """close_account

    &lt;p&gt;Closes an Amazon Web Services member account within an organization. You can close an account when &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\&quot;&gt;all features are enabled &lt;/a&gt;. You can&#39;t close the management account with this API. This is an asynchronous request that Amazon Web Services performs in the background. Because &lt;code&gt;CloseAccount&lt;/code&gt; operates asynchronously, it can return a successful completion message even though account closure might still be in progress. You need to wait a few minutes before the account is fully closed. To check the status of the request, do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;AccountId&lt;/code&gt; that you sent in the &lt;code&gt;CloseAccount&lt;/code&gt; request to provide as a parameter to the &lt;a&gt;DescribeAccount&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;While the close account request is in progress, Account status will indicate PENDING_CLOSURE. When the close account request completes, the status will change to SUSPENDED. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Check the CloudTrail log for the &lt;code&gt;CloseAccountResult&lt;/code&gt; event that gets published after the account closes successfully. For information on using CloudTrail with Organizations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_incident-response.html#orgs_cloudtrail-integration\&quot;&gt;Logging and monitoring in Organizations&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can close only 10% of member accounts, between 10 and 200, within a rolling 30 day period. This quota is not bound by a calendar month, but starts when you close an account.&lt;/p&gt; &lt;p&gt;After you reach this limit, you can close additional accounts in the Billing console. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/close-account.html\&quot;&gt;Closing an account&lt;/a&gt; in the Amazon Web Services Billing and Cost Management User Guide.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To reinstate a closed account, contact Amazon Web Services Support within the 90-day grace period while the account is in SUSPENDED status. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the Amazon Web Services account you attempt to close is linked to an Amazon Web Services GovCloud (US) account, the &lt;code&gt;CloseAccount&lt;/code&gt; request will close both accounts. To learn important pre-closure details, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/Closing-govcloud-account.html\&quot;&gt; Closing an Amazon Web Services GovCloud (US) account&lt;/a&gt; in the &lt;i&gt; Amazon Web Services GovCloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;For more information about closing accounts, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close.html\&quot;&gt;Closing an Amazon Web Services account&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CloseAccountRequest.from_dict(body)
    return web.Response(status=200)


async def create_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_account

    &lt;p&gt;Creates an Amazon Web Services account that is automatically a member of the organization whose credentials made the request. This is an asynchronous request that Amazon Web Services performs in the background. Because &lt;code&gt;CreateAccount&lt;/code&gt; operates asynchronously, it can return a successful completion message even though account initialization might still be in progress. You might need to wait a few minutes before you can successfully access the account. To check the status of the request, do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;Id&lt;/code&gt; value of the &lt;code&gt;CreateAccountStatus&lt;/code&gt; response element from this operation to provide as a parameter to the &lt;a&gt;DescribeCreateAccountStatus&lt;/a&gt; operation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Check the CloudTrail log for the &lt;code&gt;CreateAccountResult&lt;/code&gt; event. For information on using CloudTrail with Organizations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_incident-response.html#orgs_cloudtrail-integration\&quot;&gt;Logging and monitoring in Organizations&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The user who calls the API to create an account must have the &lt;code&gt;organizations:CreateAccount&lt;/code&gt; permission. If you enabled all features in the organization, Organizations creates the required service-linked role named &lt;code&gt;AWSServiceRoleForOrganizations&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_integrate_services-using_slrs\&quot;&gt;Organizations and Service-Linked Roles&lt;/a&gt; in the &lt;i&gt;Organizations User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If the request includes tags, then the requester must have the &lt;code&gt;organizations:TagResource&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;Organizations preconfigures the new member account with a role (named &lt;code&gt;OrganizationAccountAccessRole&lt;/code&gt; by default) that grants users in the management account administrator permissions in the new member account. Principals in the management account can assume the role. Organizations clones the company name and address information for the new account from the organization&#39;s management account.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt; &lt;p&gt;For more information about creating accounts, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html\&quot;&gt;Creating an Amazon Web Services account in Your Organization&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;important&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;When you create an account in an organization using the Organizations console, API, or CLI commands, the information required for the account to operate as a standalone account, such as a payment method and signing the end user license agreement (EULA) is &lt;i&gt;not&lt;/i&gt; automatically collected. If you must remove an account from your organization later, you can do so only after you provide the missing information. Follow the steps at &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info\&quot;&gt; To leave an organization as a member account&lt;/a&gt; in the &lt;i&gt;Organizations User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you get an exception that indicates that you exceeded your account limits for the organization, contact &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you get an exception that indicates that the operation failed because your organization is still initializing, wait one hour and then try again. If the error persists, contact &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Using &lt;code&gt;CreateAccount&lt;/code&gt; to create multiple temporary accounts isn&#39;t recommended. You can only close an account from the Billing and Cost Management console, and you must be signed in as the root user. For information on the requirements and process for closing an account, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close.html\&quot;&gt;Closing an Amazon Web Services account&lt;/a&gt; in the &lt;i&gt;Organizations User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;When you create a member account with this operation, you can choose whether to create the account with the &lt;b&gt;IAM User and Role Access to Billing Information&lt;/b&gt; switch enabled. If you enable it, IAM users and roles that have appropriate permissions can view billing information for the account. If you disable it, only the account root user can access billing information. For information about how to disable this switch for an account, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html\&quot;&gt;Granting Access to Your Billing Information and Tools&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateAccountRequest.from_dict(body)
    return web.Response(status=200)


async def create_gov_cloud_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_gov_cloud_account

    &lt;p&gt;This action is available if all of the following are true:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You&#39;re authorized to create accounts in the Amazon Web Services GovCloud (US) Region. For more information on the Amazon Web Services GovCloud (US) Region, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/welcome.html\&quot;&gt; &lt;i&gt;Amazon Web Services GovCloud User Guide&lt;/i&gt;.&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You already have an account in the Amazon Web Services GovCloud (US) Region that is paired with a management account of an organization in the commercial Region.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You call this action from the management account of your organization in the commercial Region.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You have the &lt;code&gt;organizations:CreateGovCloudAccount&lt;/code&gt; permission. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Organizations automatically creates the required service-linked role named &lt;code&gt;AWSServiceRoleForOrganizations&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_integrate_services-using_slrs\&quot;&gt;Organizations and Service-Linked Roles&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;Amazon Web Services automatically enables CloudTrail for Amazon Web Services GovCloud (US) accounts, but you should also do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Verify that CloudTrail is enabled to store logs.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create an Amazon S3 bucket for CloudTrail log storage.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/verifying-cloudtrail.html\&quot;&gt;Verifying CloudTrail Is Enabled&lt;/a&gt; in the &lt;i&gt;Amazon Web Services GovCloud User Guide&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the request includes tags, then the requester must have the &lt;code&gt;organizations:TagResource&lt;/code&gt; permission. The tags are attached to the commercial account associated with the GovCloud account, rather than the GovCloud account itself. To add tags to the GovCloud account, call the &lt;a&gt;TagResource&lt;/a&gt; operation in the GovCloud Region after the new GovCloud account exists.&lt;/p&gt; &lt;p&gt;You call this action from the management account of your organization in the commercial Region to create a standalone Amazon Web Services account in the Amazon Web Services GovCloud (US) Region. After the account is created, the management account of an organization in the Amazon Web Services GovCloud (US) Region can invite it to that organization. For more information on inviting standalone accounts in the Amazon Web Services GovCloud (US) to join an organization, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-organizations.html\&quot;&gt;Organizations&lt;/a&gt; in the &lt;i&gt;Amazon Web Services GovCloud User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;Calling &lt;code&gt;CreateGovCloudAccount&lt;/code&gt; is an asynchronous request that Amazon Web Services performs in the background. Because &lt;code&gt;CreateGovCloudAccount&lt;/code&gt; operates asynchronously, it can return a successful completion message even though account initialization might still be in progress. You might need to wait a few minutes before you can successfully access the account. To check the status of the request, do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;OperationId&lt;/code&gt; response element from this operation to provide as a parameter to the &lt;a&gt;DescribeCreateAccountStatus&lt;/a&gt; operation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Check the CloudTrail log for the &lt;code&gt;CreateAccountResult&lt;/code&gt; event. For information on using CloudTrail with Organizations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_monitoring.html\&quot;&gt;Monitoring the Activity in Your Organization&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;p&gt;When you call the &lt;code&gt;CreateGovCloudAccount&lt;/code&gt; action, you create two accounts: a standalone account in the Amazon Web Services GovCloud (US) Region and an associated account in the commercial Region for billing and support purposes. The account in the commercial Region is automatically a member of the organization whose credentials made the request. Both accounts are associated with the same email address.&lt;/p&gt; &lt;p&gt;A role is created in the new account in the commercial Region that allows the management account in the organization in the commercial Region to assume it. An Amazon Web Services GovCloud (US) account is then created and associated with the commercial account that you just created. A role is also created in the new Amazon Web Services GovCloud (US) account that can be assumed by the Amazon Web Services GovCloud (US) account that is associated with the management account of the commercial organization. For more information and to view a diagram that explains how account access works, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-organizations.html\&quot;&gt;Organizations&lt;/a&gt; in the &lt;i&gt;Amazon Web Services GovCloud User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;For more information about creating accounts, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html\&quot;&gt;Creating an Amazon Web Services account in Your Organization&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;important&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;When you create an account in an organization using the Organizations console, API, or CLI commands, the information required for the account to operate as a standalone account is &lt;i&gt;not&lt;/i&gt; automatically collected. This includes a payment method and signing the end user license agreement (EULA). If you must remove an account from your organization later, you can do so only after you provide the missing information. Follow the steps at &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info\&quot;&gt; To leave an organization as a member account&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you get an exception that indicates that you exceeded your account limits for the organization, contact &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you get an exception that indicates that the operation failed because your organization is still initializing, wait one hour and then try again. If the error persists, contact &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Using &lt;code&gt;CreateGovCloudAccount&lt;/code&gt; to create multiple temporary accounts isn&#39;t recommended. You can only close an account from the Amazon Web Services Billing and Cost Management console, and you must be signed in as the root user. For information on the requirements and process for closing an account, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close.html\&quot;&gt;Closing an Amazon Web Services account&lt;/a&gt; in the &lt;i&gt;Organizations User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;When you create a member account with this operation, you can choose whether to create the account with the &lt;b&gt;IAM User and Role Access to Billing Information&lt;/b&gt; switch enabled. If you enable it, IAM users and roles that have appropriate permissions can view billing information for the account. If you disable it, only the account root user can access billing information. For information about how to disable this switch for an account, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html\&quot;&gt;Granting Access to Your Billing Information and Tools&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateGovCloudAccountRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_organization

    &lt;p&gt;Creates an Amazon Web Services organization. The account whose user is calling the &lt;code&gt;CreateOrganization&lt;/code&gt; operation automatically becomes the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\&quot;&gt;management account&lt;/a&gt; of the new organization.&lt;/p&gt; &lt;p&gt;This operation must be called using credentials from the account that is to become the new organization&#39;s management account. The principal must also have the relevant IAM permissions.&lt;/p&gt; &lt;p&gt;By default (or if you set the &lt;code&gt;FeatureSet&lt;/code&gt; parameter to &lt;code&gt;ALL&lt;/code&gt;), the new organization is created with all features enabled and service control policies automatically enabled in the root. If you instead choose to create the organization supporting only the consolidated billing features by setting the &lt;code&gt;FeatureSet&lt;/code&gt; parameter to &lt;code&gt;CONSOLIDATED_BILLING\&quot;&lt;/code&gt;, no policy types are enabled by default, and you can&#39;t use organization policies&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def create_organizational_unit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_organizational_unit

    &lt;p&gt;Creates an organizational unit (OU) within a root or parent OU. An OU is a container for accounts that enables you to organize your accounts to apply policies according to your business requirements. The number of levels deep that you can nest OUs is dependent upon the policy types enabled for that root. For service control policies, the limit is five.&lt;/p&gt; &lt;p&gt;For more information about OUs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html\&quot;&gt;Managing Organizational Units&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;If the request includes tags, then the requester must have the &lt;code&gt;organizations:TagResource&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateOrganizationalUnitRequest.from_dict(body)
    return web.Response(status=200)


async def create_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_policy

    &lt;p&gt;Creates a policy of a specified type that you can attach to a root, an organizational unit (OU), or an individual Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For more information about policies and their use, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html\&quot;&gt;Managing Organization Policies&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If the request includes tags, then the requester must have the &lt;code&gt;organizations:TagResource&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreatePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def decline_handshake(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """decline_handshake

    &lt;p&gt;Declines a handshake request. This sets the handshake state to &lt;code&gt;DECLINED&lt;/code&gt; and effectively deactivates the request.&lt;/p&gt; &lt;p&gt;This operation can be called only from the account that received the handshake. The originator of the handshake can use &lt;a&gt;CancelHandshake&lt;/a&gt; instead. The originator can&#39;t reactivate a declined request, but can reinitiate the process with a new handshake request.&lt;/p&gt; &lt;p&gt;After you decline a handshake, it continues to appear in the results of relevant APIs for only 30 days. After that, it&#39;s deleted.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeclineHandshakeRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization(request: web.Request, x_amz_target, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_organization

    Deletes the organization. You can delete an organization only by using credentials from the management account. The organization must be empty of member accounts.

    :param x_amz_target: 
    :type x_amz_target: str
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


async def delete_organizational_unit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_organizational_unit

    &lt;p&gt;Deletes an organizational unit (OU) from a root or another OU. You must first remove all accounts and child OUs from the OU that you want to delete.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteOrganizationalUnitRequest.from_dict(body)
    return web.Response(status=200)


async def delete_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_policy

    &lt;p&gt;Deletes the specified policy from your organization. Before you perform this operation, you must first detach the policy from all organizational units (OUs), roots, and accounts.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeletePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_resource_policy(request: web.Request, x_amz_target, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resource_policy

    &lt;p&gt;Deletes the resource policy from your organization.&lt;/p&gt; &lt;p&gt;You can only call this operation from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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


async def deregister_delegated_administrator(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_delegated_administrator

    &lt;p&gt;Removes the specified member Amazon Web Services account as a delegated administrator for the specified Amazon Web Services service.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Deregistering a delegated administrator can have unintended impacts on the functionality of the enabled Amazon Web Services service. See the documentation for the enabled service before you deregister a delegated administrator so that you understand any potential impacts.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;You can run this action only for Amazon Web Services services that support this feature. For a current list of services that support it, see the column &lt;i&gt;Supports Delegated Administrator&lt;/i&gt; in the table at &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html\&quot;&gt;Amazon Web Services Services that you can use with Organizations&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeregisterDelegatedAdministratorRequest.from_dict(body)
    return web.Response(status=200)


async def describe_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_account

    &lt;p&gt;Retrieves Organizations-related information about the specified account.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeAccountRequest.from_dict(body)
    return web.Response(status=200)


async def describe_create_account_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_create_account_status

    &lt;p&gt;Retrieves the current status of an asynchronous request to create an account.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeCreateAccountStatusRequest.from_dict(body)
    return web.Response(status=200)


async def describe_effective_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_effective_policy

    &lt;p&gt;Returns the contents of the effective policy for specified policy type and account. The effective policy is the aggregation of any policies of the specified type that the account inherits, plus any policy of that type that is directly attached to the account.&lt;/p&gt; &lt;p&gt;This operation applies only to policy types &lt;i&gt;other&lt;/i&gt; than service control policies (SCPs).&lt;/p&gt; &lt;p&gt;For more information about policy inheritance, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies-inheritance.html\&quot;&gt;How Policy Inheritance Works&lt;/a&gt; in the &lt;i&gt;Organizations User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeEffectivePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def describe_handshake(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_handshake

    &lt;p&gt;Retrieves information about a previously requested handshake. The handshake ID comes from the response to the original &lt;a&gt;InviteAccountToOrganization&lt;/a&gt; operation that generated the handshake.&lt;/p&gt; &lt;p&gt;You can access handshakes that are &lt;code&gt;ACCEPTED&lt;/code&gt;, &lt;code&gt;DECLINED&lt;/code&gt;, or &lt;code&gt;CANCELED&lt;/code&gt; for only 30 days after they change to that state. They&#39;re then deleted and no longer accessible.&lt;/p&gt; &lt;p&gt;This operation can be called from any account in the organization.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeHandshakeRequest.from_dict(body)
    return web.Response(status=200)


async def describe_organization(request: web.Request, x_amz_target, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_organization

    &lt;p&gt;Retrieves information about the organization that the user&#39;s account belongs to.&lt;/p&gt; &lt;p&gt;This operation can be called from any account in the organization.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Even if a policy type is shown as available in the organization, you can disable it separately at the root level with &lt;a&gt;DisablePolicyType&lt;/a&gt;. Use &lt;a&gt;ListRoots&lt;/a&gt; to see the status of policy types for a specified root.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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


async def describe_organizational_unit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_organizational_unit

    &lt;p&gt;Retrieves information about an organizational unit (OU).&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeOrganizationalUnitRequest.from_dict(body)
    return web.Response(status=200)


async def describe_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_policy

    &lt;p&gt;Retrieves information about a policy.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def describe_resource_policy(request: web.Request, x_amz_target, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_resource_policy

    &lt;p&gt;Retrieves information about a resource policy.&lt;/p&gt; &lt;p&gt;You can only call this operation from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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


async def detach_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """detach_policy

    &lt;p&gt;Detaches a policy from a target root, organizational unit (OU), or account.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the policy being detached is a service control policy (SCP), the changes to permissions for Identity and Access Management (IAM) users and roles in affected accounts are immediate.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Every root, OU, and account must have at least one SCP attached. If you want to replace the default &lt;code&gt;FullAWSAccess&lt;/code&gt; policy with an SCP that limits the permissions that can be delegated, you must attach the replacement SCP before you can remove the default SCP. This is the authorization strategy of an \&quot;&lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/SCP_strategies.html#orgs_policies_allowlist\&quot;&gt;allow list&lt;/a&gt;\&quot;. If you instead attach a second SCP and leave the &lt;code&gt;FullAWSAccess&lt;/code&gt; SCP still attached, and specify &lt;code&gt;\&quot;Effect\&quot;: \&quot;Deny\&quot;&lt;/code&gt; in the second SCP to override the &lt;code&gt;\&quot;Effect\&quot;: \&quot;Allow\&quot;&lt;/code&gt; in the &lt;code&gt;FullAWSAccess&lt;/code&gt; policy (or any other attached SCP), you&#39;re using the authorization strategy of a \&quot;&lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/SCP_strategies.html#orgs_policies_denylist\&quot;&gt;deny list&lt;/a&gt;\&quot;.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DetachPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def disable_aws_service_access(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disable_aws_service_access

    &lt;p&gt;Disables the integration of an Amazon Web Services service (the service that is specified by &lt;code&gt;ServicePrincipal&lt;/code&gt;) with Organizations. When you disable integration, the specified service no longer can create a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html\&quot;&gt;service-linked role&lt;/a&gt; in &lt;i&gt;new&lt;/i&gt; accounts in your organization. This means the service can&#39;t perform operations on your behalf on any new accounts in your organization. The service can still perform operations in older accounts until the service completes its clean-up from Organizations.&lt;/p&gt; &lt;important&gt; &lt;p&gt;We &lt;b&gt; &lt;i&gt;strongly recommend&lt;/i&gt; &lt;/b&gt; that you don&#39;t use this command to disable integration between Organizations and the specified Amazon Web Services service. Instead, use the console or commands that are provided by the specified service. This lets the trusted service perform any required initialization when enabling trusted access, such as creating any required resources and any required clean up of resources when disabling trusted access. &lt;/p&gt; &lt;p&gt;For information about how to disable trusted service access to your organization using the trusted service, see the &lt;b&gt;Learn more&lt;/b&gt; link under the &lt;b&gt;Supports Trusted Access&lt;/b&gt; column at &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html\&quot;&gt;Amazon Web Services services that you can use with Organizations&lt;/a&gt;. on this page.&lt;/p&gt; &lt;p&gt;If you disable access by using this command, it causes the following actions to occur:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The service can no longer create a service-linked role in the accounts in your organization. This means that the service can&#39;t perform operations on your behalf on any new accounts in your organization. The service can still perform operations in older accounts until the service completes its clean-up from Organizations. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The service can no longer perform tasks in the member accounts in the organization, unless those operations are explicitly permitted by the IAM policies that are attached to your roles. This includes any data aggregation from the member accounts to the management account, or to a delegated administrator account, where relevant.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Some services detect this and clean up any remaining data or resources related to the integration, while other services stop accessing the organization but leave any historical data and configuration in place to support a possible re-enabling of the integration.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Using the other service&#39;s console or commands to disable the integration ensures that the other service is aware that it can clean up any resources that are required only for the integration. How the service cleans up its resources in the organization&#39;s accounts depends on that service. For more information, see the documentation for the other Amazon Web Services service. &lt;/p&gt; &lt;/important&gt; &lt;p&gt;After you perform the &lt;code&gt;DisableAWSServiceAccess&lt;/code&gt; operation, the specified service can no longer perform operations in your organization&#39;s accounts &lt;/p&gt; &lt;p&gt;For more information about integrating other services with Organizations, including the list of services that work with Organizations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html\&quot;&gt;Integrating Organizations with Other Amazon Web Services Services&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DisableAWSServiceAccessRequest.from_dict(body)
    return web.Response(status=200)


async def disable_policy_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disable_policy_type

    &lt;p&gt;Disables an organizational policy type in a root. A policy of a certain type can be attached to entities in a root only if that type is enabled in the root. After you perform this operation, you no longer can attach policies of the specified type to that root or to any organizational unit (OU) or account in that root. You can undo this by using the &lt;a&gt;EnablePolicyType&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;This is an asynchronous request that Amazon Web Services performs in the background. If you disable a policy type for a root, it still appears enabled for the organization if &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\&quot;&gt;all features&lt;/a&gt; are enabled for the organization. Amazon Web Services recommends that you first use &lt;a&gt;ListRoots&lt;/a&gt; to see the status of policy types for a specified root, and then use this operation.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt; &lt;p&gt; To view the status of available policy types in the organization, use &lt;a&gt;DescribeOrganization&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DisablePolicyTypeRequest.from_dict(body)
    return web.Response(status=200)


async def enable_all_features(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """enable_all_features

    &lt;p&gt;Enables all features in an organization. This enables the use of organization policies that can restrict the services and actions that can be called in each account. Until you enable all features, you have access only to consolidated billing, and you can&#39;t use any of the advanced account administration features that Organizations supports. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\&quot;&gt;Enabling All Features in Your Organization&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;important&gt; &lt;p&gt;This operation is required only for organizations that were created explicitly with only the consolidated billing features enabled. Calling this operation sends a handshake to every invited account in the organization. The feature set change can be finalized and the additional features enabled only after all administrators in the invited accounts approve the change by accepting the handshake.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;After you enable all features, you can separately enable or disable individual policy types in a root using &lt;a&gt;EnablePolicyType&lt;/a&gt; and &lt;a&gt;DisablePolicyType&lt;/a&gt;. To see the status of policy types in a root, use &lt;a&gt;ListRoots&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;After all invited member accounts accept the handshake, you finalize the feature set change by accepting the handshake that contains &lt;code&gt;\&quot;Action\&quot;: \&quot;ENABLE_ALL_FEATURES\&quot;&lt;/code&gt;. This completes the change.&lt;/p&gt; &lt;p&gt;After you enable all features in your organization, the management account in the organization can apply policies on all member accounts. These policies can restrict what users and even administrators in those accounts can do. The management account can apply policies that prevent accounts from leaving the organization. Ensure that your account administrators are aware of this.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
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


async def enable_aws_service_access(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """enable_aws_service_access

    &lt;p&gt;Enables the integration of an Amazon Web Services service (the service that is specified by &lt;code&gt;ServicePrincipal&lt;/code&gt;) with Organizations. When you enable integration, you allow the specified service to create a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html\&quot;&gt;service-linked role&lt;/a&gt; in all the accounts in your organization. This allows the service to perform operations on your behalf in your organization and its accounts.&lt;/p&gt; &lt;important&gt; &lt;p&gt;We recommend that you enable integration between Organizations and the specified Amazon Web Services service by using the console or commands that are provided by the specified service. Doing so ensures that the service is aware that it can create the resources that are required for the integration. How the service creates those resources in the organization&#39;s accounts depends on that service. For more information, see the documentation for the other Amazon Web Services service.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about enabling services to integrate with Organizations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html\&quot;&gt;Integrating Organizations with Other Amazon Web Services Services&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;You can only call this operation from the organization&#39;s management account and only if the organization has &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\&quot;&gt;enabled all features&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = EnableAWSServiceAccessRequest.from_dict(body)
    return web.Response(status=200)


async def enable_policy_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """enable_policy_type

    &lt;p&gt;Enables a policy type in a root. After you enable a policy type in a root, you can attach policies of that type to the root, any organizational unit (OU), or account in that root. You can undo this by using the &lt;a&gt;DisablePolicyType&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;This is an asynchronous request that Amazon Web Services performs in the background. Amazon Web Services recommends that you first use &lt;a&gt;ListRoots&lt;/a&gt; to see the status of policy types for a specified root, and then use this operation.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt; &lt;p&gt;You can enable a policy type in a root only if that policy type is available in the organization. To view the status of available policy types in the organization, use &lt;a&gt;DescribeOrganization&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = EnablePolicyTypeRequest.from_dict(body)
    return web.Response(status=200)


async def invite_account_to_organization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """invite_account_to_organization

    &lt;p&gt;Sends an invitation to another account to join your organization as a member account. Organizations sends email on your behalf to the email address that is associated with the other account&#39;s owner. The invitation is implemented as a &lt;a&gt;Handshake&lt;/a&gt; whose details are in the response.&lt;/p&gt; &lt;important&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can invite Amazon Web Services accounts only from the same seller as the management account. For example, if your organization&#39;s management account was created by Amazon Internet Services Pvt. Ltd (AISPL), an Amazon Web Services seller in India, you can invite only other AISPL accounts to your organization. You can&#39;t combine accounts from AISPL and Amazon Web Services or from any other Amazon Web Services seller. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/useconsolidatedbilliing-India.html\&quot;&gt;Consolidated Billing in India&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you receive an exception that indicates that you exceeded your account limits for the organization or that the operation failed because your organization is still initializing, wait one hour and then try again. If the error persists after an hour, contact &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt; &lt;p&gt;If the request includes tags, then the requester must have the &lt;code&gt;organizations:TagResource&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = InviteAccountToOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def leave_organization(request: web.Request, x_amz_target, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """leave_organization

    &lt;p&gt;Removes a member account from its parent organization. This version of the operation is performed by the account that wants to leave. To remove a member account as a user in the management account, use &lt;a&gt;RemoveAccountFromOrganization&lt;/a&gt; instead.&lt;/p&gt; &lt;p&gt;This operation can be called only from a member account in the organization.&lt;/p&gt; &lt;important&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The management account in an organization with all features enabled can set service control policies (SCPs) that can restrict what administrators of member accounts can do. This includes preventing them from successfully calling &lt;code&gt;LeaveOrganization&lt;/code&gt; and leaving the organization.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can leave an organization as a member account only if the account is configured with the information required to operate as a standalone account. When you create an account in an organization using the Organizations console, API, or CLI commands, the information required of standalone accounts is &lt;i&gt;not&lt;/i&gt; automatically collected. For each account that you want to make standalone, you must perform the following steps. If any of the steps are already completed for this account, that step doesn&#39;t appear.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Choose a support plan&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Provide and verify the required contact information&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Provide a current payment method&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Amazon Web Services uses the payment method to charge for any billable (not free tier) Amazon Web Services activity that occurs while the account isn&#39;t attached to an organization. Follow the steps at &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info\&quot;&gt; To leave an organization when all required account information has not yet been provided&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The account that you want to leave must not be a delegated administrator account for any Amazon Web Services service enabled for your organization. If the account is a delegated administrator, you must first change the delegated administrator account to another account that is remaining in the organization.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can leave an organization only after you enable IAM user access to billing in your account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html#ControllingAccessWebsite-Activate\&quot;&gt;Activating Access to the Billing and Cost Management Console&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Billing and Cost Management User Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;After the account leaves the organization, all tags that were attached to the account object in the organization are deleted. Amazon Web Services accounts outside of an organization do not support tags.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A newly created account has a waiting period before it can be removed from its organization. If you get an error that indicates that a wait period is required, then try again in a few days.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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


async def list_accounts(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_accounts

    &lt;p&gt;Lists all the accounts in the organization. To request only the accounts in a specified root or organizational unit (OU), use the &lt;a&gt;ListAccountsForParent&lt;/a&gt; operation instead.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a &lt;code&gt;List*&lt;/code&gt; operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListAccountsRequest.from_dict(body)
    return web.Response(status=200)


async def list_accounts_for_parent(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_accounts_for_parent

    &lt;p&gt;Lists the accounts in an organization that are contained by the specified target root or organizational unit (OU). If you specify the root, you get a list of all the accounts that aren&#39;t in any OU. If you specify an OU, you get a list of all the accounts in only that OU and not in any child OUs. To get a list of all accounts in the organization, use the &lt;a&gt;ListAccounts&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a &lt;code&gt;List*&lt;/code&gt; operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListAccountsForParentRequest.from_dict(body)
    return web.Response(status=200)


async def list_aws_service_access_for_organization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_aws_service_access_for_organization

    &lt;p&gt;Returns a list of the Amazon Web Services services that you enabled to integrate with your organization. After a service on this list creates the resources that it requires for the integration, it can perform operations on your organization and its accounts.&lt;/p&gt; &lt;p&gt;For more information about integrating other services with Organizations, including the list of services that currently work with Organizations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html\&quot;&gt;Integrating Organizations with Other Amazon Web Services Services&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListAWSServiceAccessForOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def list_children(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_children

    &lt;p&gt;Lists all of the organizational units (OUs) or accounts that are contained in the specified parent OU or root. This operation, along with &lt;a&gt;ListParents&lt;/a&gt; enables you to traverse the tree structure that makes up this root.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a &lt;code&gt;List*&lt;/code&gt; operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListChildrenRequest.from_dict(body)
    return web.Response(status=200)


async def list_create_account_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_create_account_status

    &lt;p&gt;Lists the account creation requests that match the specified status that is currently being tracked for the organization.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a &lt;code&gt;List*&lt;/code&gt; operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListCreateAccountStatusRequest.from_dict(body)
    return web.Response(status=200)


async def list_delegated_administrators(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_delegated_administrators

    &lt;p&gt;Lists the Amazon Web Services accounts that are designated as delegated administrators in this organization.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListDelegatedAdministratorsRequest.from_dict(body)
    return web.Response(status=200)


async def list_delegated_services_for_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_delegated_services_for_account

    &lt;p&gt;List the Amazon Web Services services for which the specified account is a delegated administrator.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListDelegatedServicesForAccountRequest.from_dict(body)
    return web.Response(status=200)


async def list_handshakes_for_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_handshakes_for_account

    &lt;p&gt;Lists the current handshakes that are associated with the account of the requesting user.&lt;/p&gt; &lt;p&gt;Handshakes that are &lt;code&gt;ACCEPTED&lt;/code&gt;, &lt;code&gt;DECLINED&lt;/code&gt;, &lt;code&gt;CANCELED&lt;/code&gt;, or &lt;code&gt;EXPIRED&lt;/code&gt; appear in the results of this API for only 30 days after changing to that state. After that, they&#39;re deleted and no longer accessible.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a &lt;code&gt;List*&lt;/code&gt; operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation can be called from any account in the organization.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListHandshakesForAccountRequest.from_dict(body)
    return web.Response(status=200)


async def list_handshakes_for_organization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_handshakes_for_organization

    &lt;p&gt;Lists the handshakes that are associated with the organization that the requesting user is part of. The &lt;code&gt;ListHandshakesForOrganization&lt;/code&gt; operation returns a list of handshake structures. Each structure contains details and status about a handshake.&lt;/p&gt; &lt;p&gt;Handshakes that are &lt;code&gt;ACCEPTED&lt;/code&gt;, &lt;code&gt;DECLINED&lt;/code&gt;, &lt;code&gt;CANCELED&lt;/code&gt;, or &lt;code&gt;EXPIRED&lt;/code&gt; appear in the results of this API for only 30 days after changing to that state. After that, they&#39;re deleted and no longer accessible.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a &lt;code&gt;List*&lt;/code&gt; operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListHandshakesForOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def list_organizational_units_for_parent(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_organizational_units_for_parent

    &lt;p&gt;Lists the organizational units (OUs) in a parent organizational unit or root.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a &lt;code&gt;List*&lt;/code&gt; operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListOrganizationalUnitsForParentRequest.from_dict(body)
    return web.Response(status=200)


async def list_parents(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_parents

    &lt;p&gt;Lists the root or organizational units (OUs) that serve as the immediate parent of the specified child OU or account. This operation, along with &lt;a&gt;ListChildren&lt;/a&gt; enables you to traverse the tree structure that makes up this root.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a &lt;code&gt;List*&lt;/code&gt; operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt; &lt;note&gt; &lt;p&gt;In the current release, a child can have only a single parent.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListParentsRequest.from_dict(body)
    return web.Response(status=200)


async def list_policies(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_policies

    &lt;p&gt;Retrieves the list of all policies in an organization of a specified type.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a &lt;code&gt;List*&lt;/code&gt; operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def list_policies_for_target(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_policies_for_target

    &lt;p&gt;Lists the policies that are directly attached to the specified target root, organizational unit (OU), or account. You must specify the policy type that you want included in the returned list.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a &lt;code&gt;List*&lt;/code&gt; operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListPoliciesForTargetRequest.from_dict(body)
    return web.Response(status=200)


async def list_roots(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_roots

    &lt;p&gt;Lists the roots that are defined in the current organization.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a &lt;code&gt;List*&lt;/code&gt; operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Policy types can be enabled and disabled in roots. This is distinct from whether they&#39;re available in the organization. When you enable all features, you make policy types available for use in that organization. Individual policy types can then be enabled and disabled in a root. To see the availability of a policy type in an organization, use &lt;a&gt;DescribeOrganization&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListRootsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Lists tags that are attached to the specified resource.&lt;/p&gt; &lt;p&gt;You can attach tags to the following resources in Organizations.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services account&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Organization root&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Organizational unit (OU)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Policy (any type)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def list_targets_for_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_targets_for_policy

    &lt;p&gt;Lists all the roots, organizational units (OUs), and accounts that the specified policy is attached to.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a &lt;code&gt;List*&lt;/code&gt; operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account or by a member account that is a delegated administrator for an Amazon Web Services service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListTargetsForPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def move_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """move_account

    &lt;p&gt;Moves an account from its current source parent root or organizational unit (OU) to the specified destination parent root or OU.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = MoveAccountRequest.from_dict(body)
    return web.Response(status=200)


async def put_resource_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_resource_policy

    &lt;p&gt;Creates or updates a resource policy.&lt;/p&gt; &lt;p&gt;You can only call this operation from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = PutResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def register_delegated_administrator(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_delegated_administrator

    &lt;p&gt;Enables the specified member account to administer the Organizations features of the specified Amazon Web Services service. It grants read-only access to Organizations service data. The account still requires IAM permissions to access and administer the Amazon Web Services service.&lt;/p&gt; &lt;p&gt;You can run this action only for Amazon Web Services services that support this feature. For a current list of services that support it, see the column &lt;i&gt;Supports Delegated Administrator&lt;/i&gt; in the table at &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html\&quot;&gt;Amazon Web Services Services that you can use with Organizations&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = RegisterDelegatedAdministratorRequest.from_dict(body)
    return web.Response(status=200)


async def remove_account_from_organization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_account_from_organization

    &lt;p&gt;Removes the specified account from the organization.&lt;/p&gt; &lt;p&gt;The removed account becomes a standalone account that isn&#39;t a member of any organization. It&#39;s no longer subject to any policies and is responsible for its own bill payments. The organization&#39;s management account is no longer charged for any expenses accrued by the member account after it&#39;s removed from the organization.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account. Member accounts can remove themselves with &lt;a&gt;LeaveOrganization&lt;/a&gt; instead.&lt;/p&gt; &lt;important&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can remove an account from your organization only if the account is configured with the information required to operate as a standalone account. When you create an account in an organization using the Organizations console, API, or CLI commands, the information required of standalone accounts is &lt;i&gt;not&lt;/i&gt; automatically collected. For an account that you want to make standalone, you must choose a support plan, provide and verify the required contact information, and provide a current payment method. Amazon Web Services uses the payment method to charge for any billable (not free tier) Amazon Web Services activity that occurs while the account isn&#39;t attached to an organization. To remove an account that doesn&#39;t yet have this information, you must sign in as the member account and follow the steps at &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info\&quot;&gt; To leave an organization when all required account information has not yet been provided&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The account that you want to leave must not be a delegated administrator account for any Amazon Web Services service enabled for your organization. If the account is a delegated administrator, you must first change the delegated administrator account to another account that is remaining in the organization.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;After the account leaves the organization, all tags that were attached to the account object in the organization are deleted. Amazon Web Services accounts outside of an organization do not support tags.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = RemoveAccountFromOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Adds one or more tags to the specified resource.&lt;/p&gt; &lt;p&gt;Currently, you can attach tags to the following resources in Organizations.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services account&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Organization root&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Organizational unit (OU)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Policy (any type)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    &lt;p&gt;Removes any tags with the specified keys from the specified resource.&lt;/p&gt; &lt;p&gt;You can attach tags to the following resources in Organizations.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services account&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Organization root&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Organizational unit (OU)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Policy (any type)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_organizational_unit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_organizational_unit

    &lt;p&gt;Renames the specified organizational unit (OU). The ID and ARN don&#39;t change. The child OUs and accounts remain in place, and any attached policies of the OU remain attached.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateOrganizationalUnitRequest.from_dict(body)
    return web.Response(status=200)


async def update_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_policy

    &lt;p&gt;Updates an existing policy with a new name, description, or content. If you don&#39;t supply any parameter, that value remains unchanged. You can&#39;t change a policy&#39;s type.&lt;/p&gt; &lt;p&gt;This operation can be called only from the organization&#39;s management account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdatePolicyRequest.from_dict(body)
    return web.Response(status=200)
