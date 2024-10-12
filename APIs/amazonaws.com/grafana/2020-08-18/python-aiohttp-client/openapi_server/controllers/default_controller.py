from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_license_response import AssociateLicenseResponse
from openapi_server.models.create_workspace_api_key_request import CreateWorkspaceApiKeyRequest
from openapi_server.models.create_workspace_api_key_response import CreateWorkspaceApiKeyResponse
from openapi_server.models.create_workspace_request import CreateWorkspaceRequest
from openapi_server.models.create_workspace_response import CreateWorkspaceResponse
from openapi_server.models.delete_workspace_api_key_response import DeleteWorkspaceApiKeyResponse
from openapi_server.models.delete_workspace_response import DeleteWorkspaceResponse
from openapi_server.models.describe_workspace_authentication_response import DescribeWorkspaceAuthenticationResponse
from openapi_server.models.describe_workspace_configuration_response import DescribeWorkspaceConfigurationResponse
from openapi_server.models.describe_workspace_response import DescribeWorkspaceResponse
from openapi_server.models.disassociate_license_response import DisassociateLicenseResponse
from openapi_server.models.list_permissions_response import ListPermissionsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_versions_response import ListVersionsResponse
from openapi_server.models.list_workspaces_response import ListWorkspacesResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_permissions_request import UpdatePermissionsRequest
from openapi_server.models.update_permissions_response import UpdatePermissionsResponse
from openapi_server.models.update_workspace_authentication_request import UpdateWorkspaceAuthenticationRequest
from openapi_server.models.update_workspace_authentication_response import UpdateWorkspaceAuthenticationResponse
from openapi_server.models.update_workspace_configuration_request import UpdateWorkspaceConfigurationRequest
from openapi_server.models.update_workspace_request import UpdateWorkspaceRequest
from openapi_server.models.update_workspace_response import UpdateWorkspaceResponse
from openapi_server import util


async def associate_license(request: web.Request, license_type, workspace_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_license

    Assigns a Grafana Enterprise license to a workspace. Upgrading to Grafana Enterprise incurs additional fees. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html\&quot;&gt;Upgrade a workspace to Grafana Enterprise&lt;/a&gt;.

    :param license_type: The type of license to associate with the workspace.
    :type license_type: str
    :param workspace_id: The ID of the workspace to associate the license with.
    :type workspace_id: str
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


async def create_workspace(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_workspace

    &lt;p&gt;Creates a &lt;i&gt;workspace&lt;/i&gt;. In a workspace, you can create Grafana dashboards and visualizations to analyze your metrics, logs, and traces. You don&#39;t have to build, package, or deploy any hardware to run the Grafana server.&lt;/p&gt; &lt;p&gt;Don&#39;t use &lt;code&gt;CreateWorkspace&lt;/code&gt; to modify an existing workspace. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspace.html\&quot;&gt;UpdateWorkspace&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateWorkspaceRequest.from_dict(body)
    return web.Response(status=200)


async def create_workspace_api_key(request: web.Request, workspace_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_workspace_api_key

    Creates a Grafana API key for the workspace. This key can be used to authenticate requests sent to the workspace&#39;s HTTP API. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html\&quot;&gt;https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html&lt;/a&gt; for available APIs and example requests.

    :param workspace_id: The ID of the workspace to create an API key.
    :type workspace_id: str
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
    body = CreateWorkspaceApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_workspace(request: web.Request, workspace_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_workspace

    Deletes an Amazon Managed Grafana workspace.

    :param workspace_id: The ID of the workspace to delete.
    :type workspace_id: str
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


async def delete_workspace_api_key(request: web.Request, key_name, workspace_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_workspace_api_key

    Deletes a Grafana API key for the workspace.

    :param key_name: The name of the API key to delete.
    :type key_name: str
    :param workspace_id: The ID of the workspace to delete.
    :type workspace_id: str
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


async def describe_workspace(request: web.Request, workspace_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_workspace

    Displays information about one Amazon Managed Grafana workspace.

    :param workspace_id: The ID of the workspace to display information about.
    :type workspace_id: str
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


async def describe_workspace_authentication(request: web.Request, workspace_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_workspace_authentication

    Displays information about the authentication methods used in one Amazon Managed Grafana workspace.

    :param workspace_id: The ID of the workspace to return authentication information about.
    :type workspace_id: str
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


async def describe_workspace_configuration(request: web.Request, workspace_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_workspace_configuration

    Gets the current configuration string for the given workspace.

    :param workspace_id: The ID of the workspace to get configuration information for.
    :type workspace_id: str
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


async def disassociate_license(request: web.Request, license_type, workspace_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_license

    Removes the Grafana Enterprise license from a workspace.

    :param license_type: The type of license to remove from the workspace.
    :type license_type: str
    :param workspace_id: The ID of the workspace to remove the Grafana Enterprise license from.
    :type workspace_id: str
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


async def list_permissions(request: web.Request, workspace_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, group_id=None, max_results=None, next_token=None, user_id=None, user_type=None) -> web.Response:
    """list_permissions

    Lists the users and groups who have the Grafana &lt;code&gt;Admin&lt;/code&gt; and &lt;code&gt;Editor&lt;/code&gt; roles in this workspace. If you use this operation without specifying &lt;code&gt;userId&lt;/code&gt; or &lt;code&gt;groupId&lt;/code&gt;, the operation returns the roles of all users and groups. If you specify a &lt;code&gt;userId&lt;/code&gt; or a &lt;code&gt;groupId&lt;/code&gt;, only the roles for that user or group are returned. If you do this, you can specify only one &lt;code&gt;userId&lt;/code&gt; or one &lt;code&gt;groupId&lt;/code&gt;.

    :param workspace_id: The ID of the workspace to list permissions for. This parameter is required.
    :type workspace_id: str
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
    :param group_id: (Optional) Limits the results to only the group that matches this ID.
    :type group_id: str
    :param max_results: The maximum number of results to include in the response.
    :type max_results: int
    :param next_token: The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListPermissions&lt;/code&gt; operation.
    :type next_token: str
    :param user_id: (Optional) Limits the results to only the user that matches this ID.
    :type user_id: str
    :param user_type: (Optional) If you specify &lt;code&gt;SSO_USER&lt;/code&gt;, then only the permissions of IAM Identity Center users are returned. If you specify &lt;code&gt;SSO_GROUP&lt;/code&gt;, only the permissions of IAM Identity Center groups are returned.
    :type user_type: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    The &lt;code&gt;ListTagsForResource&lt;/code&gt; operation returns the tags that are associated with the Amazon Managed Service for Grafana resource specified by the &lt;code&gt;resourceArn&lt;/code&gt;. Currently, the only resource that can be tagged is a workspace. 

    :param resource_arn: The ARN of the resource the list of tags are associated with.
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


async def list_versions(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, workspace_id=None) -> web.Response:
    """list_versions

    Lists available versions of Grafana. These are available when calling &lt;code&gt;CreateWorkspace&lt;/code&gt;. Optionally, include a workspace to list the versions to which it can be upgraded.

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
    :param max_results: The maximum number of results to include in the response.
    :type max_results: int
    :param next_token: The token to use when requesting the next set of results. You receive this token from a previous &lt;code&gt;ListVersions&lt;/code&gt; operation.
    :type next_token: str
    :param workspace_id: The ID of the workspace to list the available upgrade versions. If not included, lists all versions of Grafana that are supported for &lt;code&gt;CreateWorkspace&lt;/code&gt;.
    :type workspace_id: str

    """
    return web.Response(status=200)


async def list_workspaces(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_workspaces

    Returns a list of Amazon Managed Grafana workspaces in the account, with some information about each workspace. For more complete information about one workspace, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AAMG/latest/APIReference/API_DescribeWorkspace.html\&quot;&gt;DescribeWorkspace&lt;/a&gt;.

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
    :param max_results: The maximum number of workspaces to include in the results.
    :type max_results: int
    :param next_token: The token for the next set of workspaces to return. (You receive this token from a previous &lt;code&gt;ListWorkspaces&lt;/code&gt; operation.)
    :type next_token: str

    """
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;The &lt;code&gt;TagResource&lt;/code&gt; operation associates tags with an Amazon Managed Grafana resource. Currently, the only resource that can be tagged is workspaces. &lt;/p&gt; &lt;p&gt;If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt;

    :param resource_arn: The ARN of the resource the tag is associated with.
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

    The &lt;code&gt;UntagResource&lt;/code&gt; operation removes the association of the tag with the Amazon Managed Grafana resource. 

    :param resource_arn: The ARN of the resource the tag association is removed from. 
    :type resource_arn: str
    :param tag_keys: The key values of the tag to be removed from the resource.
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


async def update_permissions(request: web.Request, workspace_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_permissions

    Updates which users in a workspace have the Grafana &lt;code&gt;Admin&lt;/code&gt; or &lt;code&gt;Editor&lt;/code&gt; roles.

    :param workspace_id: The ID of the workspace to update.
    :type workspace_id: str
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
    body = UpdatePermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def update_workspace(request: web.Request, workspace_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_workspace

    &lt;p&gt;Modifies an existing Amazon Managed Grafana workspace. If you use this operation and omit any optional parameters, the existing values of those parameters are not changed.&lt;/p&gt; &lt;p&gt;To modify the user authentication methods that the workspace uses, such as SAML or IAM Identity Center, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspaceAuthentication.html\&quot;&gt;UpdateWorkspaceAuthentication&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To modify which users in the workspace have the &lt;code&gt;Admin&lt;/code&gt; and &lt;code&gt;Editor&lt;/code&gt; Grafana roles, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdatePermissions.html\&quot;&gt;UpdatePermissions&lt;/a&gt;.&lt;/p&gt;

    :param workspace_id: The ID of the workspace to update.
    :type workspace_id: str
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
    body = UpdateWorkspaceRequest.from_dict(body)
    return web.Response(status=200)


async def update_workspace_authentication(request: web.Request, workspace_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_workspace_authentication

    &lt;p&gt;Use this operation to define the identity provider (IdP) that this workspace authenticates users from, using SAML. You can also map SAML assertion attributes to workspace user information and define which groups in the assertion attribute are to have the &lt;code&gt;Admin&lt;/code&gt; and &lt;code&gt;Editor&lt;/code&gt; roles in the workspace.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Changes to the authentication method for a workspace may take a few minutes to take effect.&lt;/p&gt; &lt;/note&gt;

    :param workspace_id: The ID of the workspace to update the authentication for.
    :type workspace_id: str
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
    body = UpdateWorkspaceAuthenticationRequest.from_dict(body)
    return web.Response(status=200)


async def update_workspace_configuration(request: web.Request, workspace_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_workspace_configuration

    Updates the configuration string for the given workspace

    :param workspace_id: The ID of the workspace to update.
    :type workspace_id: str
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
    body = UpdateWorkspaceConfigurationRequest.from_dict(body)
    return web.Response(status=200)
