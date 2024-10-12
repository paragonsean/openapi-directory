from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_resource_request import AssociateResourceRequest
from openapi_server.models.create_canary_request import CreateCanaryRequest
from openapi_server.models.create_canary_response import CreateCanaryResponse
from openapi_server.models.create_group_request import CreateGroupRequest
from openapi_server.models.create_group_response import CreateGroupResponse
from openapi_server.models.describe_canaries_last_run_request import DescribeCanariesLastRunRequest
from openapi_server.models.describe_canaries_last_run_response import DescribeCanariesLastRunResponse
from openapi_server.models.describe_canaries_request import DescribeCanariesRequest
from openapi_server.models.describe_canaries_response import DescribeCanariesResponse
from openapi_server.models.describe_runtime_versions_request import DescribeRuntimeVersionsRequest
from openapi_server.models.describe_runtime_versions_response import DescribeRuntimeVersionsResponse
from openapi_server.models.disassociate_resource_request import DisassociateResourceRequest
from openapi_server.models.get_canary_response import GetCanaryResponse
from openapi_server.models.get_canary_runs_request import GetCanaryRunsRequest
from openapi_server.models.get_canary_runs_response import GetCanaryRunsResponse
from openapi_server.models.get_group_response import GetGroupResponse
from openapi_server.models.list_associated_groups_request import ListAssociatedGroupsRequest
from openapi_server.models.list_associated_groups_response import ListAssociatedGroupsResponse
from openapi_server.models.list_group_resources_request import ListGroupResourcesRequest
from openapi_server.models.list_group_resources_response import ListGroupResourcesResponse
from openapi_server.models.list_groups_request import ListGroupsRequest
from openapi_server.models.list_groups_response import ListGroupsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_canary_request import UpdateCanaryRequest
from openapi_server import util


async def associate_resource(request: web.Request, group_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_resource

    &lt;p&gt;Associates a canary with a group. Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group. &lt;/p&gt; &lt;p&gt;You must run this operation in the Region where the canary exists.&lt;/p&gt;

    :param group_identifier: Specifies the group. You can specify the group name, the ARN, or the group ID as the &lt;code&gt;GroupIdentifier&lt;/code&gt;.
    :type group_identifier: str
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
    body = AssociateResourceRequest.from_dict(body)
    return web.Response(status=200)


async def create_canary(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_canary

    &lt;p&gt;Creates a canary. Canaries are scripts that monitor your endpoints and APIs from the outside-in. Canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. You can set up a canary to run continuously or just once. &lt;/p&gt; &lt;p&gt;Do not use &lt;code&gt;CreateCanary&lt;/code&gt; to modify an existing canary. Use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UpdateCanary.html\&quot;&gt;UpdateCanary&lt;/a&gt; instead.&lt;/p&gt; &lt;p&gt;To create canaries, you must have the &lt;code&gt;CloudWatchSyntheticsFullAccess&lt;/code&gt; policy. If you are creating a new IAM role for the canary, you also need the &lt;code&gt;iam:CreateRole&lt;/code&gt;, &lt;code&gt;iam:CreatePolicy&lt;/code&gt; and &lt;code&gt;iam:AttachRolePolicy&lt;/code&gt; permissions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Roles\&quot;&gt;Necessary Roles and Permissions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Do not include secrets or proprietary information in your canary names. The canary name makes up part of the Amazon Resource Name (ARN) for the canary, and the ARN is included in outbound calls over the internet. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html\&quot;&gt;Security Considerations for Synthetics Canaries&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateCanaryRequest.from_dict(body)
    return web.Response(status=200)


async def create_group(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_group

    &lt;p&gt;Creates a group which you can use to associate canaries with each other, including cross-Region canaries. Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group. &lt;/p&gt; &lt;p&gt;Groups are global resources. When you create a group, it is replicated across Amazon Web Services Regions, and you can view it and add canaries to it from any Region. Although the group ARN format reflects the Region name where it was created, a group is not constrained to any Region. This means that you can put canaries from multiple Regions into the same group, and then use that group to view and manage all of those canaries in a single view.&lt;/p&gt; &lt;p&gt;Groups are supported in all Regions except the Regions that are disabled by default. For more information about these Regions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable\&quot;&gt;Enabling a Region&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Each group can contain as many as 10 canaries. You can have as many as 20 groups in your account. Any single canary can be a member of up to 10 groups.&lt;/p&gt;

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
    body = CreateGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_canary(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, delete_lambda=None) -> web.Response:
    """delete_canary

    &lt;p&gt;Permanently deletes the specified canary.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;DeleteLambda&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;, CloudWatch Synthetics also deletes the Lambda functions and layers that are used by the canary.&lt;/p&gt; &lt;p&gt;Other resources used and created by the canary are not automatically deleted. After you delete a canary that you do not intend to use again, you should also delete the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The CloudWatch alarms created for this canary. These alarms have a name of &lt;code&gt;Synthetics-SharpDrop-Alarm-&lt;i&gt;MyCanaryName&lt;/i&gt; &lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon S3 objects and buckets, such as the canary&#39;s artifact location.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;IAM roles created for the canary. If they were created in the console, these roles have the name &lt;code&gt; role/service-role/CloudWatchSyntheticsRole-&lt;i&gt;MyCanaryName&lt;/i&gt; &lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CloudWatch Logs log groups created for the canary. These logs groups have the name &lt;code&gt;/aws/lambda/cwsyn-&lt;i&gt;MyCanaryName&lt;/i&gt; &lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Before you delete a canary, you might want to use &lt;code&gt;GetCanary&lt;/code&gt; to display the information about this canary. Make note of the information returned by this operation so that you can delete these resources after you delete the canary.&lt;/p&gt;

    :param name: The name of the canary that you want to delete. To find the names of your canaries, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\&quot;&gt;DescribeCanaries&lt;/a&gt;.
    :type name: str
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
    :param delete_lambda: &lt;p&gt;Specifies whether to also delete the Lambda functions and layers used by this canary. The default is false.&lt;/p&gt; &lt;p&gt;Type: Boolean&lt;/p&gt;
    :type delete_lambda: bool

    """
    return web.Response(status=200)


async def delete_group(request: web.Request, group_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_group

    &lt;p&gt;Deletes a group. The group doesn&#39;t need to be empty to be deleted. If there are canaries in the group, they are not deleted when you delete the group. &lt;/p&gt; &lt;p&gt;Groups are a global resource that appear in all Regions, but the request to delete a group must be made from its home Region. You can find the home Region of a group within its ARN.&lt;/p&gt;

    :param group_identifier: Specifies which group to delete. You can specify the group name, the ARN, or the group ID as the &lt;code&gt;GroupIdentifier&lt;/code&gt;.
    :type group_identifier: str
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


async def describe_canaries(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_canaries

    &lt;p&gt;This operation returns a list of the canaries in your account, along with full details about each canary.&lt;/p&gt; &lt;p&gt;This operation supports resource-level authorization using an IAM policy and the &lt;code&gt;Names&lt;/code&gt; parameter. If you specify the &lt;code&gt;Names&lt;/code&gt; parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.&lt;/p&gt; &lt;p&gt;You are required to use the &lt;code&gt;Names&lt;/code&gt; parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html\&quot;&gt; Limiting a user to viewing specific canaries&lt;/a&gt;.&lt;/p&gt;

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
    body = DescribeCanariesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_canaries_last_run(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_canaries_last_run

    &lt;p&gt;Use this operation to see information from the most recent run of each canary that you have created.&lt;/p&gt; &lt;p&gt;This operation supports resource-level authorization using an IAM policy and the &lt;code&gt;Names&lt;/code&gt; parameter. If you specify the &lt;code&gt;Names&lt;/code&gt; parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.&lt;/p&gt; &lt;p&gt;You are required to use the &lt;code&gt;Names&lt;/code&gt; parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html\&quot;&gt; Limiting a user to viewing specific canaries&lt;/a&gt;.&lt;/p&gt;

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
    body = DescribeCanariesLastRunRequest.from_dict(body)
    return web.Response(status=200)


async def describe_runtime_versions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_runtime_versions

    Returns a list of Synthetics canary runtime versions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html\&quot;&gt; Canary Runtime Versions&lt;/a&gt;.

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
    body = DescribeRuntimeVersionsRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_resource(request: web.Request, group_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_resource

    Removes a canary from a group. You must run this operation in the Region where the canary exists.

    :param group_identifier: Specifies the group. You can specify the group name, the ARN, or the group ID as the &lt;code&gt;GroupIdentifier&lt;/code&gt;.
    :type group_identifier: str
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
    body = DisassociateResourceRequest.from_dict(body)
    return web.Response(status=200)


async def get_canary(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_canary

    Retrieves complete information about one canary. You must specify the name of the canary that you want. To get a list of canaries and their names, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\&quot;&gt;DescribeCanaries&lt;/a&gt;.

    :param name: The name of the canary that you want details for.
    :type name: str
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


async def get_canary_runs(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_canary_runs

    Retrieves a list of runs for a specified canary.

    :param name: The name of the canary that you want to see runs for.
    :type name: str
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
    body = GetCanaryRunsRequest.from_dict(body)
    return web.Response(status=200)


async def get_group(request: web.Request, group_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_group

    Returns information about one group. Groups are a global resource, so you can use this operation from any Region.

    :param group_identifier: Specifies the group to return information for. You can specify the group name, the ARN, or the group ID as the &lt;code&gt;GroupIdentifier&lt;/code&gt;.
    :type group_identifier: str
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


async def list_associated_groups(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_associated_groups

    Returns a list of the groups that the specified canary is associated with. The canary that you specify must be in the current Region.

    :param resource_arn: The ARN of the canary that you want to view groups for.
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAssociatedGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def list_group_resources(request: web.Request, group_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_group_resources

    This operation returns a list of the ARNs of the canaries that are associated with the specified group.

    :param group_identifier: Specifies the group to return information for. You can specify the group name, the ARN, or the group ID as the &lt;code&gt;GroupIdentifier&lt;/code&gt;.
    :type group_identifier: str
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
    body = ListGroupResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def list_groups(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_groups

    Returns a list of all groups in the account, displaying their names, unique IDs, and ARNs. The groups from all Regions are returned.

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
    body = ListGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Displays the tags associated with a canary or group.

    :param resource_arn: &lt;p&gt;The ARN of the canary or group that you want to view tags for.&lt;/p&gt; &lt;p&gt;The ARN format of a canary is &lt;code&gt;arn:aws:synthetics:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:canary:&lt;i&gt;canary-name&lt;/i&gt; &lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The ARN format of a group is &lt;code&gt;arn:aws:synthetics:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:group:&lt;i&gt;group-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt;
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


async def start_canary(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_canary

    Use this operation to run a canary that has already been created. The frequency of the canary runs is determined by the value of the canary&#39;s &lt;code&gt;Schedule&lt;/code&gt;. To see a canary&#39;s schedule, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanary.html\&quot;&gt;GetCanary&lt;/a&gt;.

    :param name: The name of the canary that you want to run. To find canary names, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\&quot;&gt;DescribeCanaries&lt;/a&gt;.
    :type name: str
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


async def stop_canary(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_canary

    &lt;p&gt;Stops the canary to prevent all future runs. If the canary is currently running,the run that is in progress completes on its own, publishes metrics, and uploads artifacts, but it is not recorded in Synthetics as a completed run.&lt;/p&gt; &lt;p&gt;You can use &lt;code&gt;StartCanary&lt;/code&gt; to start it running again with the canary’s current schedule at any point in the future. &lt;/p&gt;

    :param name: The name of the canary that you want to stop. To find the names of your canaries, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\&quot;&gt;ListCanaries&lt;/a&gt;.
    :type name: str
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


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns one or more tags (key-value pairs) to the specified canary or group. &lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; action with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a canary or group.&lt;/p&gt;

    :param resource_arn: &lt;p&gt;The ARN of the canary or group that you&#39;re adding tags to.&lt;/p&gt; &lt;p&gt;The ARN format of a canary is &lt;code&gt;arn:aws:synthetics:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:canary:&lt;i&gt;canary-name&lt;/i&gt; &lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The ARN format of a group is &lt;code&gt;arn:aws:synthetics:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:group:&lt;i&gt;group-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt;
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

    Removes one or more tags from the specified resource.

    :param resource_arn: &lt;p&gt;The ARN of the canary or group that you&#39;re removing tags from.&lt;/p&gt; &lt;p&gt;The ARN format of a canary is &lt;code&gt;arn:aws:synthetics:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:canary:&lt;i&gt;canary-name&lt;/i&gt; &lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The ARN format of a group is &lt;code&gt;arn:aws:synthetics:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:group:&lt;i&gt;group-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt;
    :type resource_arn: str
    :param tag_keys: The list of tag keys to remove from the resource.
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


async def update_canary(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_canary

    &lt;p&gt;Updates the configuration of a canary that has already been created.&lt;/p&gt; &lt;p&gt;You can&#39;t use this operation to update the tags of an existing canary. To change the tags of an existing canary, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;.&lt;/p&gt;

    :param name: &lt;p&gt;The name of the canary that you want to update. To find the names of your canaries, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html\&quot;&gt;DescribeCanaries&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You cannot change the name of a canary that has already been created.&lt;/p&gt;
    :type name: str
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
    body = UpdateCanaryRequest.from_dict(body)
    return web.Response(status=200)
