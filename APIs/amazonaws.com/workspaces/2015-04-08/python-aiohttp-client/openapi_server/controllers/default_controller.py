from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_connection_alias_request import AssociateConnectionAliasRequest
from openapi_server.models.associate_connection_alias_result import AssociateConnectionAliasResult
from openapi_server.models.associate_ip_groups_request import AssociateIpGroupsRequest
from openapi_server.models.authorize_ip_rules_request import AuthorizeIpRulesRequest
from openapi_server.models.copy_workspace_image_request import CopyWorkspaceImageRequest
from openapi_server.models.copy_workspace_image_result import CopyWorkspaceImageResult
from openapi_server.models.create_connect_client_add_in_request import CreateConnectClientAddInRequest
from openapi_server.models.create_connect_client_add_in_result import CreateConnectClientAddInResult
from openapi_server.models.create_connection_alias_request import CreateConnectionAliasRequest
from openapi_server.models.create_connection_alias_result import CreateConnectionAliasResult
from openapi_server.models.create_ip_group_request import CreateIpGroupRequest
from openapi_server.models.create_ip_group_result import CreateIpGroupResult
from openapi_server.models.create_standby_workspaces_request import CreateStandbyWorkspacesRequest
from openapi_server.models.create_standby_workspaces_result import CreateStandbyWorkspacesResult
from openapi_server.models.create_tags_request import CreateTagsRequest
from openapi_server.models.create_updated_workspace_image_request import CreateUpdatedWorkspaceImageRequest
from openapi_server.models.create_updated_workspace_image_result import CreateUpdatedWorkspaceImageResult
from openapi_server.models.create_workspace_bundle_request import CreateWorkspaceBundleRequest
from openapi_server.models.create_workspace_bundle_result import CreateWorkspaceBundleResult
from openapi_server.models.create_workspace_image_request import CreateWorkspaceImageRequest
from openapi_server.models.create_workspace_image_result import CreateWorkspaceImageResult
from openapi_server.models.create_workspaces_request import CreateWorkspacesRequest
from openapi_server.models.create_workspaces_result import CreateWorkspacesResult
from openapi_server.models.delete_client_branding_request import DeleteClientBrandingRequest
from openapi_server.models.delete_connect_client_add_in_request import DeleteConnectClientAddInRequest
from openapi_server.models.delete_connection_alias_request import DeleteConnectionAliasRequest
from openapi_server.models.delete_ip_group_request import DeleteIpGroupRequest
from openapi_server.models.delete_tags_request import DeleteTagsRequest
from openapi_server.models.delete_workspace_bundle_request import DeleteWorkspaceBundleRequest
from openapi_server.models.delete_workspace_image_request import DeleteWorkspaceImageRequest
from openapi_server.models.deregister_workspace_directory_request import DeregisterWorkspaceDirectoryRequest
from openapi_server.models.describe_account_modifications_request import DescribeAccountModificationsRequest
from openapi_server.models.describe_account_modifications_result import DescribeAccountModificationsResult
from openapi_server.models.describe_account_result import DescribeAccountResult
from openapi_server.models.describe_client_branding_request import DescribeClientBrandingRequest
from openapi_server.models.describe_client_branding_result import DescribeClientBrandingResult
from openapi_server.models.describe_client_properties_request import DescribeClientPropertiesRequest
from openapi_server.models.describe_client_properties_result import DescribeClientPropertiesResult
from openapi_server.models.describe_connect_client_add_ins_request import DescribeConnectClientAddInsRequest
from openapi_server.models.describe_connect_client_add_ins_result import DescribeConnectClientAddInsResult
from openapi_server.models.describe_connection_alias_permissions_request import DescribeConnectionAliasPermissionsRequest
from openapi_server.models.describe_connection_alias_permissions_result import DescribeConnectionAliasPermissionsResult
from openapi_server.models.describe_connection_aliases_request import DescribeConnectionAliasesRequest
from openapi_server.models.describe_connection_aliases_result import DescribeConnectionAliasesResult
from openapi_server.models.describe_ip_groups_request import DescribeIpGroupsRequest
from openapi_server.models.describe_ip_groups_result import DescribeIpGroupsResult
from openapi_server.models.describe_tags_request import DescribeTagsRequest
from openapi_server.models.describe_tags_result import DescribeTagsResult
from openapi_server.models.describe_workspace_bundles_request import DescribeWorkspaceBundlesRequest
from openapi_server.models.describe_workspace_bundles_result import DescribeWorkspaceBundlesResult
from openapi_server.models.describe_workspace_directories_request import DescribeWorkspaceDirectoriesRequest
from openapi_server.models.describe_workspace_directories_result import DescribeWorkspaceDirectoriesResult
from openapi_server.models.describe_workspace_image_permissions_request import DescribeWorkspaceImagePermissionsRequest
from openapi_server.models.describe_workspace_image_permissions_result import DescribeWorkspaceImagePermissionsResult
from openapi_server.models.describe_workspace_images_request import DescribeWorkspaceImagesRequest
from openapi_server.models.describe_workspace_images_result import DescribeWorkspaceImagesResult
from openapi_server.models.describe_workspace_snapshots_request import DescribeWorkspaceSnapshotsRequest
from openapi_server.models.describe_workspace_snapshots_result import DescribeWorkspaceSnapshotsResult
from openapi_server.models.describe_workspaces_connection_status_request import DescribeWorkspacesConnectionStatusRequest
from openapi_server.models.describe_workspaces_connection_status_result import DescribeWorkspacesConnectionStatusResult
from openapi_server.models.describe_workspaces_request import DescribeWorkspacesRequest
from openapi_server.models.describe_workspaces_result import DescribeWorkspacesResult
from openapi_server.models.disassociate_connection_alias_request import DisassociateConnectionAliasRequest
from openapi_server.models.disassociate_ip_groups_request import DisassociateIpGroupsRequest
from openapi_server.models.import_client_branding_request import ImportClientBrandingRequest
from openapi_server.models.import_client_branding_result import ImportClientBrandingResult
from openapi_server.models.import_workspace_image_request import ImportWorkspaceImageRequest
from openapi_server.models.import_workspace_image_result import ImportWorkspaceImageResult
from openapi_server.models.list_available_management_cidr_ranges_request import ListAvailableManagementCidrRangesRequest
from openapi_server.models.list_available_management_cidr_ranges_result import ListAvailableManagementCidrRangesResult
from openapi_server.models.migrate_workspace_request import MigrateWorkspaceRequest
from openapi_server.models.migrate_workspace_result import MigrateWorkspaceResult
from openapi_server.models.modify_account_request import ModifyAccountRequest
from openapi_server.models.modify_certificate_based_auth_properties_request import ModifyCertificateBasedAuthPropertiesRequest
from openapi_server.models.modify_client_properties_request import ModifyClientPropertiesRequest
from openapi_server.models.modify_saml_properties_request import ModifySamlPropertiesRequest
from openapi_server.models.modify_selfservice_permissions_request import ModifySelfservicePermissionsRequest
from openapi_server.models.modify_workspace_access_properties_request import ModifyWorkspaceAccessPropertiesRequest
from openapi_server.models.modify_workspace_creation_properties_request import ModifyWorkspaceCreationPropertiesRequest
from openapi_server.models.modify_workspace_properties_request import ModifyWorkspacePropertiesRequest
from openapi_server.models.modify_workspace_state_request import ModifyWorkspaceStateRequest
from openapi_server.models.reboot_workspaces_request import RebootWorkspacesRequest
from openapi_server.models.reboot_workspaces_result import RebootWorkspacesResult
from openapi_server.models.rebuild_workspaces_request import RebuildWorkspacesRequest
from openapi_server.models.rebuild_workspaces_result import RebuildWorkspacesResult
from openapi_server.models.register_workspace_directory_request import RegisterWorkspaceDirectoryRequest
from openapi_server.models.restore_workspace_request import RestoreWorkspaceRequest
from openapi_server.models.revoke_ip_rules_request import RevokeIpRulesRequest
from openapi_server.models.start_workspaces_request import StartWorkspacesRequest
from openapi_server.models.start_workspaces_result import StartWorkspacesResult
from openapi_server.models.stop_workspaces_request import StopWorkspacesRequest
from openapi_server.models.stop_workspaces_result import StopWorkspacesResult
from openapi_server.models.terminate_workspaces_request import TerminateWorkspacesRequest
from openapi_server.models.terminate_workspaces_result import TerminateWorkspacesResult
from openapi_server.models.update_connect_client_add_in_request import UpdateConnectClientAddInRequest
from openapi_server.models.update_connection_alias_permission_request import UpdateConnectionAliasPermissionRequest
from openapi_server.models.update_rules_of_ip_group_request import UpdateRulesOfIpGroupRequest
from openapi_server.models.update_workspace_bundle_request import UpdateWorkspaceBundleRequest
from openapi_server.models.update_workspace_image_permission_request import UpdateWorkspaceImagePermissionRequest
from openapi_server import util


async def associate_connection_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_connection_alias

    &lt;p&gt;Associates the specified connection alias with the specified directory to enable cross-Region redirection. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html\&quot;&gt; Cross-Region Redirection for Amazon WorkSpaces&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before performing this operation, call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectionAliases.html\&quot;&gt; DescribeConnectionAliases&lt;/a&gt; to make sure that the current state of the connection alias is &lt;code&gt;CREATED&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = AssociateConnectionAliasRequest.from_dict(body)
    return web.Response(status=200)


async def associate_ip_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_ip_groups

    Associates the specified IP access control group with the specified directory.

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
    body = AssociateIpGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def authorize_ip_rules(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """authorize_ip_rules

    &lt;p&gt;Adds one or more rules to the specified IP access control group.&lt;/p&gt; &lt;p&gt;This action gives users permission to access their WorkSpaces from the CIDR address ranges specified in the rules.&lt;/p&gt;

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
    body = AuthorizeIpRulesRequest.from_dict(body)
    return web.Response(status=200)


async def copy_workspace_image(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """copy_workspace_image

    &lt;p&gt;Copies the specified image from the specified Region to the current Region. For more information about copying images, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/copy-custom-image.html\&quot;&gt; Copy a Custom WorkSpaces Image&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;In the China (Ningxia) Region, you can copy images only within the same Region.&lt;/p&gt; &lt;p&gt;In Amazon Web Services GovCloud (US), to copy images to and from other Regions, contact Amazon Web Services Support.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Before copying a shared image, be sure to verify that it has been shared from the correct Amazon Web Services account. To determine if an image has been shared and to see the ID of the Amazon Web Services account that owns an image, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImages.html\&quot;&gt;DescribeWorkSpaceImages&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImagePermissions.html\&quot;&gt;DescribeWorkspaceImagePermissions&lt;/a&gt; API operations. &lt;/p&gt; &lt;/important&gt;

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
    body = CopyWorkspaceImageRequest.from_dict(body)
    return web.Response(status=200)


async def create_connect_client_add_in(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_connect_client_add_in

    &lt;p&gt;Creates a client-add-in for Amazon Connect within a directory. You can create only one Amazon Connect client add-in within a directory.&lt;/p&gt; &lt;p&gt;This client add-in allows WorkSpaces users to seamlessly connect to Amazon Connect.&lt;/p&gt;

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
    body = CreateConnectClientAddInRequest.from_dict(body)
    return web.Response(status=200)


async def create_connection_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_connection_alias

    Creates the specified connection alias for use with cross-Region redirection. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html\&quot;&gt; Cross-Region Redirection for Amazon WorkSpaces&lt;/a&gt;.

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
    body = CreateConnectionAliasRequest.from_dict(body)
    return web.Response(status=200)


async def create_ip_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_ip_group

    &lt;p&gt;Creates an IP access control group.&lt;/p&gt; &lt;p&gt;An IP access control group provides you with the ability to control the IP addresses from which users are allowed to access their WorkSpaces. To specify the CIDR address ranges, add rules to your IP access control group and then associate the group with your directory. You can add rules when you create the group or at any time using &lt;a&gt;AuthorizeIpRules&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;There is a default IP access control group associated with your directory. If you don&#39;t associate an IP access control group with your directory, the default group is used. The default group includes a default rule that allows users to access their WorkSpaces from anywhere. You cannot modify the default IP access control group for your directory.&lt;/p&gt;

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
    body = CreateIpGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_standby_workspaces(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_standby_workspaces

    Creates a standby WorkSpace in a secondary Region.

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
    body = CreateStandbyWorkspacesRequest.from_dict(body)
    return web.Response(status=200)


async def create_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_tags

    Creates the specified tags for the specified WorkSpaces resource.

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
    body = CreateTagsRequest.from_dict(body)
    return web.Response(status=200)


async def create_updated_workspace_image(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_updated_workspace_image

    &lt;p&gt;Creates a new updated WorkSpace image based on the specified source image. The new updated WorkSpace image has the latest drivers and other updates required by the Amazon WorkSpaces components.&lt;/p&gt; &lt;p&gt;To determine which WorkSpace images need to be updated with the latest Amazon WorkSpaces requirements, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImages.html\&quot;&gt; DescribeWorkspaceImages&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Only Windows 10, Windows Server 2016, and Windows Server 2019 WorkSpace images can be programmatically updated at this time.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Microsoft Windows updates and other application updates are not included in the update process.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The source WorkSpace image is not deleted. You can delete the source image after you&#39;ve verified your new updated image and created a new bundle. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = CreateUpdatedWorkspaceImageRequest.from_dict(body)
    return web.Response(status=200)


async def create_workspace_bundle(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_workspace_bundle

    Creates the specified WorkSpace bundle. For more information about creating WorkSpace bundles, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/create-custom-bundle.html\&quot;&gt; Create a Custom WorkSpaces Image and Bundle&lt;/a&gt;.

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
    body = CreateWorkspaceBundleRequest.from_dict(body)
    return web.Response(status=200)


async def create_workspace_image(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_workspace_image

    Creates a new WorkSpace image from an existing WorkSpace.

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
    body = CreateWorkspaceImageRequest.from_dict(body)
    return web.Response(status=200)


async def create_workspaces(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_workspaces

    &lt;p&gt;Creates one or more WorkSpaces.&lt;/p&gt; &lt;p&gt;This operation is asynchronous and returns before the WorkSpaces are created.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;MANUAL&lt;/code&gt; running mode value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/workspaces/core/\&quot;&gt;Amazon WorkSpaces Core&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateWorkspacesRequest.from_dict(body)
    return web.Response(status=200)


async def delete_client_branding(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_client_branding

    &lt;p&gt;Deletes customized client branding. Client branding allows you to customize your WorkSpace&#39;s client login portal. You can tailor your login portal company logo, the support email address, support link, link to reset password, and a custom message for users trying to sign in.&lt;/p&gt; &lt;p&gt;After you delete your customized client branding, your login portal reverts to the default client branding.&lt;/p&gt;

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
    body = DeleteClientBrandingRequest.from_dict(body)
    return web.Response(status=200)


async def delete_connect_client_add_in(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_connect_client_add_in

    Deletes a client-add-in for Amazon Connect that is configured within a directory.

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
    body = DeleteConnectClientAddInRequest.from_dict(body)
    return web.Response(status=200)


async def delete_connection_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_connection_alias

    &lt;p&gt;Deletes the specified connection alias. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html\&quot;&gt; Cross-Region Redirection for Amazon WorkSpaces&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;If you will no longer be using a fully qualified domain name (FQDN) as the registration code for your WorkSpaces users, you must take certain precautions to prevent potential security issues.&lt;/b&gt; For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html#cross-region-redirection-security-considerations\&quot;&gt; Security Considerations if You Stop Using Cross-Region Redirection&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;To delete a connection alias that has been shared, the shared account must first disassociate the connection alias from any directories it has been associated with. Then you must unshare the connection alias from the account it has been shared with. You can delete a connection alias only after it is no longer shared with any accounts or associated with any directories.&lt;/p&gt; &lt;/note&gt;

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
    body = DeleteConnectionAliasRequest.from_dict(body)
    return web.Response(status=200)


async def delete_ip_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_ip_group

    &lt;p&gt;Deletes the specified IP access control group.&lt;/p&gt; &lt;p&gt;You cannot delete an IP access control group that is associated with a directory.&lt;/p&gt;

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
    body = DeleteIpGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_tags

    Deletes the specified tags from the specified WorkSpaces resource.

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
    body = DeleteTagsRequest.from_dict(body)
    return web.Response(status=200)


async def delete_workspace_bundle(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_workspace_bundle

    Deletes the specified WorkSpace bundle. For more information about deleting WorkSpace bundles, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/delete_bundle.html\&quot;&gt; Delete a Custom WorkSpaces Bundle or Image&lt;/a&gt;.

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
    body = DeleteWorkspaceBundleRequest.from_dict(body)
    return web.Response(status=200)


async def delete_workspace_image(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_workspace_image

    Deletes the specified image from your account. To delete an image, you must first delete any bundles that are associated with the image and unshare the image if it is shared with other accounts. 

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
    body = DeleteWorkspaceImageRequest.from_dict(body)
    return web.Response(status=200)


async def deregister_workspace_directory(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_workspace_directory

    &lt;p&gt;Deregisters the specified directory. This operation is asynchronous and returns before the WorkSpace directory is deregistered. If any WorkSpaces are registered to this directory, you must remove them before you can deregister the directory.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Simple AD and AD Connector are made available to you free of charge to use with WorkSpaces. If there are no WorkSpaces being used with your Simple AD or AD Connector directory for 30 consecutive days, this directory will be automatically deregistered for use with Amazon WorkSpaces, and you will be charged for this directory as per the &lt;a href&#x3D;\&quot;http://aws.amazon.com/directoryservice/pricing/\&quot;&gt;Directory Service pricing terms&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To delete empty directories, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/delete-workspaces-directory.html\&quot;&gt; Delete the Directory for Your WorkSpaces&lt;/a&gt;. If you delete your Simple AD or AD Connector directory, you can always create a new one when you want to start using WorkSpaces again.&lt;/p&gt; &lt;/note&gt;

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
    body = DeregisterWorkspaceDirectoryRequest.from_dict(body)
    return web.Response(status=200)


async def describe_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_account

    Retrieves a list that describes the configuration of Bring Your Own License (BYOL) for the specified account.

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


async def describe_account_modifications(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_account_modifications

    Retrieves a list that describes modifications to the configuration of Bring Your Own License (BYOL) for the specified account.

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
    body = DescribeAccountModificationsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_client_branding(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_client_branding

    &lt;p&gt;Describes the specified client branding. Client branding allows you to customize the log in page of various device types for your users. You can add your company logo, the support email address, support link, link to reset password, and a custom message for users trying to sign in.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only device types that have branding information configured will be shown in the response.&lt;/p&gt; &lt;/note&gt;

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
    body = DescribeClientBrandingRequest.from_dict(body)
    return web.Response(status=200)


async def describe_client_properties(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_client_properties

    Retrieves a list that describes one or more specified Amazon WorkSpaces clients.

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
    body = DescribeClientPropertiesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_connect_client_add_ins(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_connect_client_add_ins

    Retrieves a list of Amazon Connect client add-ins that have been created.

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
    body = DescribeConnectClientAddInsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_connection_alias_permissions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_connection_alias_permissions

    Describes the permissions that the owner of a connection alias has granted to another Amazon Web Services account for the specified connection alias. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html\&quot;&gt; Cross-Region Redirection for Amazon WorkSpaces&lt;/a&gt;.

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
    body = DescribeConnectionAliasPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_connection_aliases(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_connection_aliases

    Retrieves a list that describes the connection aliases used for cross-Region redirection. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html\&quot;&gt; Cross-Region Redirection for Amazon WorkSpaces&lt;/a&gt;.

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
    body = DescribeConnectionAliasesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_ip_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_ip_groups

    Describes one or more of your IP access control groups.

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
    body = DescribeIpGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_tags

    Describes the specified tags for the specified WorkSpaces resource.

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
    body = DescribeTagsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_workspace_bundles(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """describe_workspace_bundles

    &lt;p&gt;Retrieves a list that describes the available WorkSpace bundles.&lt;/p&gt; &lt;p&gt;You can filter the results using either bundle ID or owner, but not both.&lt;/p&gt;

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
    body = DescribeWorkspaceBundlesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_workspace_directories(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """describe_workspace_directories

    Describes the available directories that are registered with Amazon WorkSpaces.

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
    body = DescribeWorkspaceDirectoriesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_workspace_image_permissions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_workspace_image_permissions

    Describes the permissions that the owner of an image has granted to other Amazon Web Services accounts for an image.

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
    body = DescribeWorkspaceImagePermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_workspace_images(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_workspace_images

    Retrieves a list that describes one or more specified images, if the image identifiers are provided. Otherwise, all images in the account are described. 

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
    body = DescribeWorkspaceImagesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_workspace_snapshots(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_workspace_snapshots

    Describes the snapshots for the specified WorkSpace.

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
    body = DescribeWorkspaceSnapshotsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_workspaces(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_workspaces

    &lt;p&gt;Describes the specified WorkSpaces.&lt;/p&gt; &lt;p&gt;You can filter the results by using the bundle identifier, directory identifier, or owner, but you can specify only one filter at a time.&lt;/p&gt;

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
    :param limit: Pagination limit
    :type limit: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeWorkspacesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_workspaces_connection_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_workspaces_connection_status

    Describes the connection status of the specified WorkSpaces.

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
    body = DescribeWorkspacesConnectionStatusRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_connection_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_connection_alias

    &lt;p&gt;Disassociates a connection alias from a directory. Disassociating a connection alias disables cross-Region redirection between two directories in different Regions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html\&quot;&gt; Cross-Region Redirection for Amazon WorkSpaces&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before performing this operation, call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectionAliases.html\&quot;&gt; DescribeConnectionAliases&lt;/a&gt; to make sure that the current state of the connection alias is &lt;code&gt;CREATED&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = DisassociateConnectionAliasRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_ip_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_ip_groups

    Disassociates the specified IP access control group from the specified directory.

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
    body = DisassociateIpGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def import_client_branding(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """import_client_branding

    &lt;p&gt;Imports client branding. Client branding allows you to customize your WorkSpace&#39;s client login portal. You can tailor your login portal company logo, the support email address, support link, link to reset password, and a custom message for users trying to sign in.&lt;/p&gt; &lt;p&gt;After you import client branding, the default branding experience for the specified platform type is replaced with the imported experience&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must specify at least one platform type when importing client branding.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can import up to 6 MB of data with each request. If your request exceeds this limit, you can import client branding for different platform types using separate requests.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;In each platform type, the &lt;code&gt;SupportEmail&lt;/code&gt; and &lt;code&gt;SupportLink&lt;/code&gt; parameters are mutually exclusive. You can specify only one parameter for each platform type, but not both.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Imported data can take up to a minute to appear in the WorkSpaces client.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = ImportClientBrandingRequest.from_dict(body)
    return web.Response(status=200)


async def import_workspace_image(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """import_workspace_image

    Imports the specified Windows 10 or 11 Bring Your Own License (BYOL) image into Amazon WorkSpaces. The image must be an already licensed Amazon EC2 image that is in your Amazon Web Services account, and you must own the image. For more information about creating BYOL images, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html\&quot;&gt; Bring Your Own Windows Desktop Licenses&lt;/a&gt;.

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
    body = ImportWorkspaceImageRequest.from_dict(body)
    return web.Response(status=200)


async def list_available_management_cidr_ranges(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_available_management_cidr_ranges

    &lt;p&gt;Retrieves a list of IP address ranges, specified as IPv4 CIDR blocks, that you can use for the network management interface when you enable Bring Your Own License (BYOL). &lt;/p&gt; &lt;p&gt;This operation can be run only by Amazon Web Services accounts that are enabled for BYOL. If your account isn&#39;t enabled for BYOL, you&#39;ll receive an &lt;code&gt;AccessDeniedException&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;The management network interface is connected to a secure Amazon WorkSpaces management network. It is used for interactive streaming of the WorkSpace desktop to Amazon WorkSpaces clients, and to allow Amazon WorkSpaces to manage the WorkSpace.&lt;/p&gt;

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
    body = ListAvailableManagementCidrRangesRequest.from_dict(body)
    return web.Response(status=200)


async def migrate_workspace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """migrate_workspace

    &lt;p&gt;Migrates a WorkSpace from one operating system or bundle type to another, while retaining the data on the user volume.&lt;/p&gt; &lt;p&gt;The migration process recreates the WorkSpace by using a new root volume from the target bundle image and the user volume from the last available snapshot of the original WorkSpace. During migration, the original &lt;code&gt;D:\\Users\\%USERNAME%&lt;/code&gt; user profile folder is renamed to &lt;code&gt;D:\\Users\\%USERNAME%MMddyyTHHmmss%.NotMigrated&lt;/code&gt;. A new &lt;code&gt;D:\\Users\\%USERNAME%\\&lt;/code&gt; folder is generated by the new OS. Certain files in the old user profile are moved to the new user profile.&lt;/p&gt; &lt;p&gt;For available migration scenarios, details about what happens during migration, and best practices, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/migrate-workspaces.html\&quot;&gt;Migrate a WorkSpace&lt;/a&gt;.&lt;/p&gt;

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
    body = MigrateWorkspaceRequest.from_dict(body)
    return web.Response(status=200)


async def modify_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_account

    Modifies the configuration of Bring Your Own License (BYOL) for the specified account.

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
    body = ModifyAccountRequest.from_dict(body)
    return web.Response(status=200)


async def modify_certificate_based_auth_properties(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_certificate_based_auth_properties

    Modifies the properties of the certificate-based authentication you want to use with your WorkSpaces.

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
    body = ModifyCertificateBasedAuthPropertiesRequest.from_dict(body)
    return web.Response(status=200)


async def modify_client_properties(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_client_properties

    Modifies the properties of the specified Amazon WorkSpaces clients.

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
    body = ModifyClientPropertiesRequest.from_dict(body)
    return web.Response(status=200)


async def modify_saml_properties(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_saml_properties

    Modifies multiple properties related to SAML 2.0 authentication, including the enablement status, user access URL, and relay state parameter name that are used for configuring federation with an SAML 2.0 identity provider.

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
    body = ModifySamlPropertiesRequest.from_dict(body)
    return web.Response(status=200)


async def modify_selfservice_permissions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_selfservice_permissions

    Modifies the self-service WorkSpace management capabilities for your users. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-user-self-service-workspace-management.html\&quot;&gt;Enable Self-Service WorkSpace Management Capabilities for Your Users&lt;/a&gt;.

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
    body = ModifySelfservicePermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def modify_workspace_access_properties(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_workspace_access_properties

    Specifies which devices and operating systems users can use to access their WorkSpaces. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html#control-device-access\&quot;&gt; Control Device Access&lt;/a&gt;.

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
    body = ModifyWorkspaceAccessPropertiesRequest.from_dict(body)
    return web.Response(status=200)


async def modify_workspace_creation_properties(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_workspace_creation_properties

    Modify the default properties used to create WorkSpaces.

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
    body = ModifyWorkspaceCreationPropertiesRequest.from_dict(body)
    return web.Response(status=200)


async def modify_workspace_properties(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_workspace_properties

    &lt;p&gt;Modifies the specified WorkSpace properties. For important information about how to modify the size of the root and user volumes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html\&quot;&gt; Modify a WorkSpace&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;MANUAL&lt;/code&gt; running mode value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/workspaces/core/\&quot;&gt;Amazon WorkSpaces Core&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = ModifyWorkspacePropertiesRequest.from_dict(body)
    return web.Response(status=200)


async def modify_workspace_state(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_workspace_state

    &lt;p&gt;Sets the state of the specified WorkSpace.&lt;/p&gt; &lt;p&gt;To maintain a WorkSpace without being interrupted, set the WorkSpace state to &lt;code&gt;ADMIN_MAINTENANCE&lt;/code&gt;. WorkSpaces in this state do not respond to requests to reboot, stop, start, rebuild, or restore. An AutoStop WorkSpace in this state is not stopped. Users cannot log into a WorkSpace in the &lt;code&gt;ADMIN_MAINTENANCE&lt;/code&gt; state.&lt;/p&gt;

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
    body = ModifyWorkspaceStateRequest.from_dict(body)
    return web.Response(status=200)


async def reboot_workspaces(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reboot_workspaces

    &lt;p&gt;Reboots the specified WorkSpaces.&lt;/p&gt; &lt;p&gt;You cannot reboot a WorkSpace unless its state is &lt;code&gt;AVAILABLE&lt;/code&gt; or &lt;code&gt;UNHEALTHY&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation is asynchronous and returns before the WorkSpaces have rebooted.&lt;/p&gt;

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
    body = RebootWorkspacesRequest.from_dict(body)
    return web.Response(status=200)


async def rebuild_workspaces(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """rebuild_workspaces

    &lt;p&gt;Rebuilds the specified WorkSpace.&lt;/p&gt; &lt;p&gt;You cannot rebuild a WorkSpace unless its state is &lt;code&gt;AVAILABLE&lt;/code&gt;, &lt;code&gt;ERROR&lt;/code&gt;, &lt;code&gt;UNHEALTHY&lt;/code&gt;, &lt;code&gt;STOPPED&lt;/code&gt;, or &lt;code&gt;REBOOTING&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Rebuilding a WorkSpace is a potentially destructive action that can result in the loss of data. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/reset-workspace.html\&quot;&gt;Rebuild a WorkSpace&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation is asynchronous and returns before the WorkSpaces have been completely rebuilt.&lt;/p&gt;

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
    body = RebuildWorkspacesRequest.from_dict(body)
    return web.Response(status=200)


async def register_workspace_directory(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_workspace_directory

    Registers the specified directory. This operation is asynchronous and returns before the WorkSpace directory is registered. If this is the first time you are registering a directory, you will need to create the workspaces_DefaultRole role before you can register a directory. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html#create-default-role\&quot;&gt; Creating the workspaces_DefaultRole Role&lt;/a&gt;.

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
    body = RegisterWorkspaceDirectoryRequest.from_dict(body)
    return web.Response(status=200)


async def restore_workspace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """restore_workspace

    &lt;p&gt;Restores the specified WorkSpace to its last known healthy state.&lt;/p&gt; &lt;p&gt;You cannot restore a WorkSpace unless its state is &lt;code&gt; AVAILABLE&lt;/code&gt;, &lt;code&gt;ERROR&lt;/code&gt;, &lt;code&gt;UNHEALTHY&lt;/code&gt;, or &lt;code&gt;STOPPED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Restoring a WorkSpace is a potentially destructive action that can result in the loss of data. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/restore-workspace.html\&quot;&gt;Restore a WorkSpace&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation is asynchronous and returns before the WorkSpace is completely restored.&lt;/p&gt;

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
    body = RestoreWorkspaceRequest.from_dict(body)
    return web.Response(status=200)


async def revoke_ip_rules(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """revoke_ip_rules

    Removes one or more rules from the specified IP access control group.

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
    body = RevokeIpRulesRequest.from_dict(body)
    return web.Response(status=200)


async def start_workspaces(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_workspaces

    &lt;p&gt;Starts the specified WorkSpaces.&lt;/p&gt; &lt;p&gt;You cannot start a WorkSpace unless it has a running mode of &lt;code&gt;AutoStop&lt;/code&gt; and a state of &lt;code&gt;STOPPED&lt;/code&gt;.&lt;/p&gt;

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
    body = StartWorkspacesRequest.from_dict(body)
    return web.Response(status=200)


async def stop_workspaces(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_workspaces

    &lt;p&gt; Stops the specified WorkSpaces.&lt;/p&gt; &lt;p&gt;You cannot stop a WorkSpace unless it has a running mode of &lt;code&gt;AutoStop&lt;/code&gt; and a state of &lt;code&gt;AVAILABLE&lt;/code&gt;, &lt;code&gt;IMPAIRED&lt;/code&gt;, &lt;code&gt;UNHEALTHY&lt;/code&gt;, or &lt;code&gt;ERROR&lt;/code&gt;.&lt;/p&gt;

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
    body = StopWorkspacesRequest.from_dict(body)
    return web.Response(status=200)


async def terminate_workspaces(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """terminate_workspaces

    &lt;p&gt;Terminates the specified WorkSpaces.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Terminating a WorkSpace is a permanent action and cannot be undone. The user&#39;s data is destroyed. If you need to archive any user data, contact Amazon Web Services Support before terminating the WorkSpace.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;You can terminate a WorkSpace that is in any state except &lt;code&gt;SUSPENDED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation is asynchronous and returns before the WorkSpaces have been completely terminated. After a WorkSpace is terminated, the &lt;code&gt;TERMINATED&lt;/code&gt; state is returned only briefly before the WorkSpace directory metadata is cleaned up, so this state is rarely returned. To confirm that a WorkSpace is terminated, check for the WorkSpace ID by using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html\&quot;&gt; DescribeWorkSpaces&lt;/a&gt;. If the WorkSpace ID isn&#39;t returned, then the WorkSpace has been successfully terminated.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Simple AD and AD Connector are made available to you free of charge to use with WorkSpaces. If there are no WorkSpaces being used with your Simple AD or AD Connector directory for 30 consecutive days, this directory will be automatically deregistered for use with Amazon WorkSpaces, and you will be charged for this directory as per the &lt;a href&#x3D;\&quot;http://aws.amazon.com/directoryservice/pricing/\&quot;&gt;Directory Service pricing terms&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To delete empty directories, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/delete-workspaces-directory.html\&quot;&gt; Delete the Directory for Your WorkSpaces&lt;/a&gt;. If you delete your Simple AD or AD Connector directory, you can always create a new one when you want to start using WorkSpaces again.&lt;/p&gt; &lt;/note&gt;

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
    body = TerminateWorkspacesRequest.from_dict(body)
    return web.Response(status=200)


async def update_connect_client_add_in(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_connect_client_add_in

    Updates a Amazon Connect client add-in. Use this action to update the name and endpoint URL of a Amazon Connect client add-in.

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
    body = UpdateConnectClientAddInRequest.from_dict(body)
    return web.Response(status=200)


async def update_connection_alias_permission(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_connection_alias_permission

    &lt;p&gt;Shares or unshares a connection alias with one account by specifying whether that account has permission to associate the connection alias with a directory. If the association permission is granted, the connection alias is shared with that account. If the association permission is revoked, the connection alias is unshared with the account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html\&quot;&gt; Cross-Region Redirection for Amazon WorkSpaces&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Before performing this operation, call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectionAliases.html\&quot;&gt; DescribeConnectionAliases&lt;/a&gt; to make sure that the current state of the connection alias is &lt;code&gt;CREATED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To delete a connection alias that has been shared, the shared account must first disassociate the connection alias from any directories it has been associated with. Then you must unshare the connection alias from the account it has been shared with. You can delete a connection alias only after it is no longer shared with any accounts or associated with any directories.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = UpdateConnectionAliasPermissionRequest.from_dict(body)
    return web.Response(status=200)


async def update_rules_of_ip_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_rules_of_ip_group

    Replaces the current rules of the specified IP access control group with the specified rules.

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
    body = UpdateRulesOfIpGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_workspace_bundle(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_workspace_bundle

    &lt;p&gt;Updates a WorkSpace bundle with a new image. For more information about updating WorkSpace bundles, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/update-custom-bundle.html\&quot;&gt; Update a Custom WorkSpaces Bundle&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Existing WorkSpaces aren&#39;t automatically updated when you update the bundle that they&#39;re based on. To update existing WorkSpaces that are based on a bundle that you&#39;ve updated, you must either rebuild the WorkSpaces or delete and recreate them.&lt;/p&gt; &lt;/important&gt;

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
    body = UpdateWorkspaceBundleRequest.from_dict(body)
    return web.Response(status=200)


async def update_workspace_image_permission(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_workspace_image_permission

    &lt;p&gt;Shares or unshares an image with one account in the same Amazon Web Services Region by specifying whether that account has permission to copy the image. If the copy image permission is granted, the image is shared with that account. If the copy image permission is revoked, the image is unshared with the account.&lt;/p&gt; &lt;p&gt;After an image has been shared, the recipient account can copy the image to other Regions as needed.&lt;/p&gt; &lt;p&gt;In the China (Ningxia) Region, you can copy images only within the same Region.&lt;/p&gt; &lt;p&gt;In Amazon Web Services GovCloud (US), to copy images to and from other Regions, contact Amazon Web Services Support.&lt;/p&gt; &lt;p&gt;For more information about sharing images, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/share-custom-image.html\&quot;&gt; Share or Unshare a Custom WorkSpaces Image&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To delete an image that has been shared, you must unshare the image before you delete it.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Sharing Bring Your Own License (BYOL) images across Amazon Web Services accounts isn&#39;t supported at this time in Amazon Web Services GovCloud (US). To share BYOL images across accounts in Amazon Web Services GovCloud (US), contact Amazon Web Services Support.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = UpdateWorkspaceImagePermissionRequest.from_dict(body)
    return web.Response(status=200)
