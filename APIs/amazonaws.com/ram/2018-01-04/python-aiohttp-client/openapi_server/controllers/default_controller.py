from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_resource_share_invitation_request import AcceptResourceShareInvitationRequest
from openapi_server.models.accept_resource_share_invitation_response import AcceptResourceShareInvitationResponse
from openapi_server.models.associate_resource_share_permission_request import AssociateResourceSharePermissionRequest
from openapi_server.models.associate_resource_share_permission_response import AssociateResourceSharePermissionResponse
from openapi_server.models.associate_resource_share_request import AssociateResourceShareRequest
from openapi_server.models.associate_resource_share_response import AssociateResourceShareResponse
from openapi_server.models.create_permission_request import CreatePermissionRequest
from openapi_server.models.create_permission_response import CreatePermissionResponse
from openapi_server.models.create_permission_version_request import CreatePermissionVersionRequest
from openapi_server.models.create_permission_version_response import CreatePermissionVersionResponse
from openapi_server.models.create_resource_share_request import CreateResourceShareRequest
from openapi_server.models.create_resource_share_response import CreateResourceShareResponse
from openapi_server.models.delete_permission_response import DeletePermissionResponse
from openapi_server.models.delete_permission_version_response import DeletePermissionVersionResponse
from openapi_server.models.delete_resource_share_response import DeleteResourceShareResponse
from openapi_server.models.disassociate_resource_share_permission_request import DisassociateResourceSharePermissionRequest
from openapi_server.models.disassociate_resource_share_permission_response import DisassociateResourceSharePermissionResponse
from openapi_server.models.disassociate_resource_share_request import DisassociateResourceShareRequest
from openapi_server.models.disassociate_resource_share_response import DisassociateResourceShareResponse
from openapi_server.models.enable_sharing_with_aws_organization_response import EnableSharingWithAwsOrganizationResponse
from openapi_server.models.get_permission_request import GetPermissionRequest
from openapi_server.models.get_permission_response import GetPermissionResponse
from openapi_server.models.get_resource_policies_request import GetResourcePoliciesRequest
from openapi_server.models.get_resource_policies_response import GetResourcePoliciesResponse
from openapi_server.models.get_resource_share_associations_request import GetResourceShareAssociationsRequest
from openapi_server.models.get_resource_share_associations_response import GetResourceShareAssociationsResponse
from openapi_server.models.get_resource_share_invitations_request import GetResourceShareInvitationsRequest
from openapi_server.models.get_resource_share_invitations_response import GetResourceShareInvitationsResponse
from openapi_server.models.get_resource_shares_request import GetResourceSharesRequest
from openapi_server.models.get_resource_shares_response import GetResourceSharesResponse
from openapi_server.models.list_pending_invitation_resources_request import ListPendingInvitationResourcesRequest
from openapi_server.models.list_pending_invitation_resources_response import ListPendingInvitationResourcesResponse
from openapi_server.models.list_permission_associations_request import ListPermissionAssociationsRequest
from openapi_server.models.list_permission_associations_response import ListPermissionAssociationsResponse
from openapi_server.models.list_permission_versions_request import ListPermissionVersionsRequest
from openapi_server.models.list_permission_versions_response import ListPermissionVersionsResponse
from openapi_server.models.list_permissions_request import ListPermissionsRequest
from openapi_server.models.list_permissions_response import ListPermissionsResponse
from openapi_server.models.list_principals_request import ListPrincipalsRequest
from openapi_server.models.list_principals_response import ListPrincipalsResponse
from openapi_server.models.list_replace_permission_associations_work_request import ListReplacePermissionAssociationsWorkRequest
from openapi_server.models.list_replace_permission_associations_work_response import ListReplacePermissionAssociationsWorkResponse
from openapi_server.models.list_resource_share_permissions_request import ListResourceSharePermissionsRequest
from openapi_server.models.list_resource_share_permissions_response import ListResourceSharePermissionsResponse
from openapi_server.models.list_resource_types_request import ListResourceTypesRequest
from openapi_server.models.list_resource_types_response import ListResourceTypesResponse
from openapi_server.models.list_resources_request import ListResourcesRequest
from openapi_server.models.list_resources_response import ListResourcesResponse
from openapi_server.models.promote_permission_created_from_policy_request import PromotePermissionCreatedFromPolicyRequest
from openapi_server.models.promote_permission_created_from_policy_response import PromotePermissionCreatedFromPolicyResponse
from openapi_server.models.promote_resource_share_created_from_policy_response import PromoteResourceShareCreatedFromPolicyResponse
from openapi_server.models.reject_resource_share_invitation_request import RejectResourceShareInvitationRequest
from openapi_server.models.reject_resource_share_invitation_response import RejectResourceShareInvitationResponse
from openapi_server.models.replace_permission_associations_request import ReplacePermissionAssociationsRequest
from openapi_server.models.replace_permission_associations_response import ReplacePermissionAssociationsResponse
from openapi_server.models.set_default_permission_version_request import SetDefaultPermissionVersionRequest
from openapi_server.models.set_default_permission_version_response import SetDefaultPermissionVersionResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_resource_share_request import UpdateResourceShareRequest
from openapi_server.models.update_resource_share_response import UpdateResourceShareResponse
from openapi_server import util


async def accept_resource_share_invitation(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """accept_resource_share_invitation

    Accepts an invitation to a resource share from another Amazon Web Services account. After you accept the invitation, the resources included in the resource share are available to interact with in the relevant Amazon Web Services Management Consoles and tools.

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
    body = AcceptResourceShareInvitationRequest.from_dict(body)
    return web.Response(status=200)


async def associate_resource_share(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_resource_share

    Adds the specified list of principals and list of resources to a resource share. Principals that already have access to this resource share immediately receive access to the added resources. Newly added principals immediately receive access to the resources shared in this resource share. 

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
    body = AssociateResourceShareRequest.from_dict(body)
    return web.Response(status=200)


async def associate_resource_share_permission(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_resource_share_permission

    Adds or replaces the RAM permission for a resource type included in a resource share. You can have exactly one permission associated with each resource type in the resource share. You can add a new RAM permission only if there are currently no resources of that resource type currently in the resource share.

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
    body = AssociateResourceSharePermissionRequest.from_dict(body)
    return web.Response(status=200)


async def create_permission(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_permission

    Creates a customer managed permission for a specified resource type that you can attach to resource shares. It is created in the Amazon Web Services Region in which you call the operation.

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
    body = CreatePermissionRequest.from_dict(body)
    return web.Response(status=200)


async def create_permission_version(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_permission_version

    &lt;p&gt;Creates a new version of the specified customer managed permission. The new version is automatically set as the default version of the customer managed permission. New resource shares automatically use the default permission. Existing resource shares continue to use their original permission versions, but you can use &lt;a&gt;ReplacePermissionAssociations&lt;/a&gt; to update them.&lt;/p&gt; &lt;p&gt;If the specified customer managed permission already has the maximum of 5 versions, then you must delete one of the existing versions before you can create a new one.&lt;/p&gt;

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
    body = CreatePermissionVersionRequest.from_dict(body)
    return web.Response(status=200)


async def create_resource_share(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_resource_share

    &lt;p&gt;Creates a resource share. You can provide a list of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; for the resources that you want to share, a list of principals you want to share the resources with, and the permissions to grant those principals.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Sharing a resource makes it available for use by principals outside of the Amazon Web Services account that created the resource. Sharing doesn&#39;t change any permissions or quotas that apply to the resource in the account that created it.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateResourceShareRequest.from_dict(body)
    return web.Response(status=200)


async def delete_permission(request: web.Request, permission_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """delete_permission

    Deletes the specified customer managed permission in the Amazon Web Services Region in which you call this operation. You can delete a customer managed permission only if it isn&#39;t attached to any resource share. The operation deletes all versions associated with the customer managed permission.

    :param permission_arn: Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the customer managed permission that you want to delete.
    :type permission_arn: str
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
    :param client_token: &lt;p&gt;Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a &lt;a href&#x3D;\&quot;https://wikipedia.org/wiki/Universally_unique_identifier\&quot;&gt;UUID type of value.&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t provide this value, then Amazon Web Services generates a random one for you.&lt;/p&gt; &lt;p&gt;If you retry the operation with the same &lt;code&gt;ClientToken&lt;/code&gt;, but with different parameters, the retry fails with an &lt;code&gt;IdempotentParameterMismatch&lt;/code&gt; error.&lt;/p&gt;
    :type client_token: str

    """
    return web.Response(status=200)


async def delete_permission_version(request: web.Request, permission_arn, permission_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """delete_permission_version

    &lt;p&gt;Deletes one version of a customer managed permission. The version you specify must not be attached to any resource share and must not be the default version for the permission.&lt;/p&gt; &lt;p&gt;If a customer managed permission has the maximum of 5 versions, then you must delete at least one version before you can create another.&lt;/p&gt;

    :param permission_arn: Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the permission with the version you want to delete.
    :type permission_arn: str
    :param permission_version: &lt;p&gt;Specifies the version number to delete.&lt;/p&gt; &lt;p&gt;You can&#39;t delete the default version for a customer managed permission.&lt;/p&gt; &lt;p&gt;You can&#39;t delete a version if it&#39;s the only version of the permission. You must either first create another version, or delete the permission completely.&lt;/p&gt; &lt;p&gt;You can&#39;t delete a version if it is attached to any resource shares. If the version is the default, you must first use &lt;a&gt;SetDefaultPermissionVersion&lt;/a&gt; to set a different version as the default for the customer managed permission, and then use &lt;a&gt;AssociateResourceSharePermission&lt;/a&gt; to update your resource shares to use the new default version.&lt;/p&gt;
    :type permission_version: int
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
    :param client_token: &lt;p&gt;Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a &lt;a href&#x3D;\&quot;https://wikipedia.org/wiki/Universally_unique_identifier\&quot;&gt;UUID type of value.&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t provide this value, then Amazon Web Services generates a random one for you.&lt;/p&gt; &lt;p&gt;If you retry the operation with the same &lt;code&gt;ClientToken&lt;/code&gt;, but with different parameters, the retry fails with an &lt;code&gt;IdempotentParameterMismatch&lt;/code&gt; error.&lt;/p&gt;
    :type client_token: str

    """
    return web.Response(status=200)


async def delete_resource_share(request: web.Request, resource_share_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """delete_resource_share

    &lt;p&gt;Deletes the specified resource share.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This doesn&#39;t delete any of the resources that were associated with the resource share; it only stops the sharing of those resources through this resource share.&lt;/p&gt; &lt;/important&gt;

    :param resource_share_arn: Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the resource share to delete.
    :type resource_share_arn: str
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
    :param client_token: &lt;p&gt;Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a &lt;a href&#x3D;\&quot;https://wikipedia.org/wiki/Universally_unique_identifier\&quot;&gt;UUID type of value.&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t provide this value, then Amazon Web Services generates a random one for you.&lt;/p&gt; &lt;p&gt;If you retry the operation with the same &lt;code&gt;ClientToken&lt;/code&gt;, but with different parameters, the retry fails with an &lt;code&gt;IdempotentParameterMismatch&lt;/code&gt; error.&lt;/p&gt;
    :type client_token: str

    """
    return web.Response(status=200)


async def disassociate_resource_share(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_resource_share

    Removes the specified principals or resources from participating in the specified resource share.

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
    body = DisassociateResourceShareRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_resource_share_permission(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_resource_share_permission

    Removes a managed permission from a resource share. Permission changes take effect immediately. You can remove a managed permission from a resource share only if there are currently no resources of the relevant resource type currently attached to the resource share.

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
    body = DisassociateResourceSharePermissionRequest.from_dict(body)
    return web.Response(status=200)


async def enable_sharing_with_aws_organization(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """enable_sharing_with_aws_organization

    &lt;p&gt;Enables resource sharing within your organization in Organizations. This operation creates a service-linked role called &lt;code&gt;AWSServiceRoleForResourceAccessManager&lt;/code&gt; that has the IAM managed policy named AWSResourceAccessManagerServiceRolePolicy attached. This role permits RAM to retrieve information about the organization and its structure. This lets you share resources with all of the accounts in the calling account&#39;s organization by specifying the organization ID, or all of the accounts in an organizational unit (OU) by specifying the OU ID. Until you enable sharing within the organization, you can specify only individual Amazon Web Services accounts, or for supported resource types, IAM roles and users.&lt;/p&gt; &lt;p&gt;You must call this operation from an IAM role or user in the organization&#39;s management account.&lt;/p&gt; &lt;p/&gt;

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


async def get_permission(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_permission

    Retrieves the contents of a managed permission in JSON format.

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
    body = GetPermissionRequest.from_dict(body)
    return web.Response(status=200)


async def get_resource_policies(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_resource_policies

    Retrieves the resource policies for the specified resources that you own and have shared.

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
    body = GetResourcePoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def get_resource_share_associations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_resource_share_associations

    Retrieves the lists of resources and principals that associated for resource shares that you own.

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
    body = GetResourceShareAssociationsRequest.from_dict(body)
    return web.Response(status=200)


async def get_resource_share_invitations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_resource_share_invitations

    Retrieves details about invitations that you have received for resource shares.

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
    body = GetResourceShareInvitationsRequest.from_dict(body)
    return web.Response(status=200)


async def get_resource_shares(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_resource_shares

    Retrieves details about the resource shares that you own or that are shared with you.

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
    body = GetResourceSharesRequest.from_dict(body)
    return web.Response(status=200)


async def list_pending_invitation_resources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_pending_invitation_resources

    Lists the resources in a resource share that is shared with you but for which the invitation is still &lt;code&gt;PENDING&lt;/code&gt;. That means that you haven&#39;t accepted or rejected the invitation and the invitation hasn&#39;t expired.

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
    body = ListPendingInvitationResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def list_permission_associations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_permission_associations

    Lists information about the managed permission and its associations to any resource shares that use this managed permission. This lets you see which resource shares use which versions of the specified managed permission.

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
    body = ListPermissionAssociationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_permission_versions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_permission_versions

    Lists the available versions of the specified RAM permission.

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
    body = ListPermissionVersionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_permissions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_permissions

    Retrieves a list of available RAM permissions that you can use for the supported resource types. 

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
    body = ListPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_principals(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_principals

    Lists the principals that you are sharing resources with or that are sharing resources with you.

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
    body = ListPrincipalsRequest.from_dict(body)
    return web.Response(status=200)


async def list_replace_permission_associations_work(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_replace_permission_associations_work

    Retrieves the current status of the asynchronous tasks performed by RAM when you perform the &lt;a&gt;ReplacePermissionAssociationsWork&lt;/a&gt; operation.

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
    body = ListReplacePermissionAssociationsWorkRequest.from_dict(body)
    return web.Response(status=200)


async def list_resource_share_permissions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_resource_share_permissions

    Lists the RAM permissions that are associated with a resource share.

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
    body = ListResourceSharePermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_resource_types(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_resource_types

    Lists the resource types that can be shared by RAM.

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
    body = ListResourceTypesRequest.from_dict(body)
    return web.Response(status=200)


async def list_resources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_resources

    Lists the resources that you added to a resource share or the resources that are shared with you.

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
    body = ListResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def promote_permission_created_from_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """promote_permission_created_from_policy

    &lt;p&gt;When you attach a resource-based policy to a resource, RAM automatically creates a resource share of &lt;code&gt;featureSet&lt;/code&gt;&#x3D;&lt;code&gt;CREATED_FROM_POLICY&lt;/code&gt; with a managed permission that has the same IAM permissions as the original resource-based policy. However, this type of managed permission is visible to only the resource share owner, and the associated resource share can&#39;t be modified by using RAM.&lt;/p&gt; &lt;p&gt;This operation creates a separate, fully manageable customer managed permission that has the same IAM permissions as the original resource-based policy. You can associate this customer managed permission to any resource shares.&lt;/p&gt; &lt;p&gt;Before you use &lt;a&gt;PromoteResourceShareCreatedFromPolicy&lt;/a&gt;, you should first run this operation to ensure that you have an appropriate customer managed permission that can be associated with the promoted resource share.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The original &lt;code&gt;CREATED_FROM_POLICY&lt;/code&gt; policy isn&#39;t deleted, and resource shares using that original policy aren&#39;t automatically updated.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can&#39;t modify a &lt;code&gt;CREATED_FROM_POLICY&lt;/code&gt; resource share so you can&#39;t associate the new customer managed permission by using &lt;code&gt;ReplacePermsissionAssociations&lt;/code&gt;. However, if you use &lt;a&gt;PromoteResourceShareCreatedFromPolicy&lt;/a&gt;, that operation automatically associates the fully manageable customer managed permission to the newly promoted &lt;code&gt;STANDARD&lt;/code&gt; resource share.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;After you promote a resource share, if the original &lt;code&gt;CREATED_FROM_POLICY&lt;/code&gt; managed permission has no other associations to A resource share, then RAM automatically deletes it.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = PromotePermissionCreatedFromPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def promote_resource_share_created_from_policy(request: web.Request, resource_share_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """promote_resource_share_created_from_policy

    &lt;p&gt;When you attach a resource-based policy to a resource, RAM automatically creates a resource share of &lt;code&gt;featureSet&lt;/code&gt;&#x3D;&lt;code&gt;CREATED_FROM_POLICY&lt;/code&gt; with a managed permission that has the same IAM permissions as the original resource-based policy. However, this type of managed permission is visible to only the resource share owner, and the associated resource share can&#39;t be modified by using RAM.&lt;/p&gt; &lt;p&gt;This operation promotes the resource share to a &lt;code&gt;STANDARD&lt;/code&gt; resource share that is fully manageable in RAM. When you promote a resource share, you can then manage the resource share in RAM and it becomes visible to all of the principals you shared it with.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Before you perform this operation, you should first run &lt;a&gt;PromotePermissionCreatedFromPolicy&lt;/a&gt;to ensure that you have an appropriate customer managed permission that can be associated with this resource share after its is promoted. If this operation can&#39;t find a managed permission that exactly matches the existing &lt;code&gt;CREATED_FROM_POLICY&lt;/code&gt; permission, then this operation fails.&lt;/p&gt; &lt;/important&gt;

    :param resource_share_arn: Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the resource share to promote.
    :type resource_share_arn: str
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


async def reject_resource_share_invitation(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reject_resource_share_invitation

    Rejects an invitation to a resource share from another Amazon Web Services account.

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
    body = RejectResourceShareInvitationRequest.from_dict(body)
    return web.Response(status=200)


async def replace_permission_associations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """replace_permission_associations

    &lt;p&gt;Updates all resource shares that use a managed permission to a different managed permission. This operation always applies the default version of the target managed permission. You can optionally specify that the update applies to only resource shares that currently use a specified version. This enables you to update to the latest version, without changing the which managed permission is used.&lt;/p&gt; &lt;p&gt;You can use this operation to update all of your resource shares to use the current default version of the permission by specifying the same value for the &lt;code&gt;fromPermissionArn&lt;/code&gt; and &lt;code&gt;toPermissionArn&lt;/code&gt; parameters.&lt;/p&gt; &lt;p&gt;You can use the optional &lt;code&gt;fromPermissionVersion&lt;/code&gt; parameter to update only those resources that use a specified version of the managed permission to the new managed permission.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To successfully perform this operation, you must have permission to update the resource-based policy on all affected resource types.&lt;/p&gt; &lt;/important&gt;

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
    body = ReplacePermissionAssociationsRequest.from_dict(body)
    return web.Response(status=200)


async def set_default_permission_version(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_default_permission_version

    Designates the specified version number as the default version for the specified customer managed permission. New resource shares automatically use this new default permission. Existing resource shares continue to use their original permission version, but you can use &lt;a&gt;ReplacePermissionAssociations&lt;/a&gt; to update them.

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
    body = SetDefaultPermissionVersionRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Adds the specified tag keys and values to a resource share or managed permission. If you choose a resource share, the tags are attached to only the resource share, not to the resources that are in the resource share.&lt;/p&gt; &lt;p&gt;The tags on a managed permission are the same for all versions of the managed permission.&lt;/p&gt;

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


async def untag_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes the specified tag key and value pairs from the specified resource share or managed permission.

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


async def update_resource_share(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_resource_share

    Modifies some of the properties of the specified resource share.

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
    body = UpdateResourceShareRequest.from_dict(body)
    return web.Response(status=200)
