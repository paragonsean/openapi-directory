from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_group_output import CreateGroupOutput
from openapi_server.models.create_group_request import CreateGroupRequest
from openapi_server.models.delete_group_output import DeleteGroupOutput
from openapi_server.models.delete_group_request import DeleteGroupRequest
from openapi_server.models.get_account_settings_output import GetAccountSettingsOutput
from openapi_server.models.get_group_configuration_output import GetGroupConfigurationOutput
from openapi_server.models.get_group_configuration_request import GetGroupConfigurationRequest
from openapi_server.models.get_group_output import GetGroupOutput
from openapi_server.models.get_group_query_output import GetGroupQueryOutput
from openapi_server.models.get_group_query_request import GetGroupQueryRequest
from openapi_server.models.get_group_request import GetGroupRequest
from openapi_server.models.get_tags_output import GetTagsOutput
from openapi_server.models.group_resources_output import GroupResourcesOutput
from openapi_server.models.group_resources_request import GroupResourcesRequest
from openapi_server.models.list_group_resources_output import ListGroupResourcesOutput
from openapi_server.models.list_group_resources_request import ListGroupResourcesRequest
from openapi_server.models.list_groups_output import ListGroupsOutput
from openapi_server.models.list_groups_request import ListGroupsRequest
from openapi_server.models.put_group_configuration_request import PutGroupConfigurationRequest
from openapi_server.models.search_resources_output import SearchResourcesOutput
from openapi_server.models.search_resources_request import SearchResourcesRequest
from openapi_server.models.tag_output import TagOutput
from openapi_server.models.tag_request import TagRequest
from openapi_server.models.ungroup_resources_output import UngroupResourcesOutput
from openapi_server.models.ungroup_resources_request import UngroupResourcesRequest
from openapi_server.models.untag_output import UntagOutput
from openapi_server.models.untag_request import UntagRequest
from openapi_server.models.update_account_settings_output import UpdateAccountSettingsOutput
from openapi_server.models.update_account_settings_request import UpdateAccountSettingsRequest
from openapi_server.models.update_group_output import UpdateGroupOutput
from openapi_server.models.update_group_query_output import UpdateGroupQueryOutput
from openapi_server.models.update_group_query_request import UpdateGroupQueryRequest
from openapi_server.models.update_group_request import UpdateGroupRequest
from openapi_server import util


async def create_group(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_group

    &lt;p&gt;Creates a resource group with the specified name and description. You can optionally include either a resource query or a service configuration. For more information about constructing a resource query, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/userguide/getting_started-query.html\&quot;&gt;Build queries and groups in Resource Groups&lt;/a&gt; in the &lt;i&gt;Resource Groups User Guide&lt;/i&gt;. For more information about service-linked groups and service configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html\&quot;&gt;Service configurations for Resource Groups&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:CreateGroup&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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


async def delete_group(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_group

    &lt;p&gt;Deletes the specified resource group. Deleting a resource group does not delete any resources that are members of the group; it only deletes the group structure.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:DeleteGroup&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DeleteGroupRequest.from_dict(body)
    return web.Response(status=200)


async def get_account_settings(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account_settings

    Retrieves the current status of optional features in Resource Groups.

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


async def get_group(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_group

    &lt;p&gt;Returns information about a specified resource group.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:GetGroup&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = GetGroupRequest.from_dict(body)
    return web.Response(status=200)


async def get_group_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_group_configuration

    &lt;p&gt;Retrieves the service configuration associated with the specified resource group. For details about the service configuration syntax, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html\&quot;&gt;Service configurations for Resource Groups&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:GetGroupConfiguration&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = GetGroupConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def get_group_query(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_group_query

    &lt;p&gt;Retrieves the resource query associated with the specified resource group. For more information about resource queries, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag\&quot;&gt;Create a tag-based group in Resource Groups&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:GetGroupQuery&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = GetGroupQueryRequest.from_dict(body)
    return web.Response(status=200)


async def get_tags(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_tags

    &lt;p&gt;Returns a list of tags that are associated with a resource group, specified by an ARN.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:GetTags&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param arn: The ARN of the resource group whose tags you want to retrieve.
    :type arn: str
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


async def group_resources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """group_resources

    &lt;p&gt;Adds the specified resources to the specified group.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You can use this operation with only resource groups that are configured with the following types:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AWS::EC2::HostManagement&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AWS::EC2::CapacityReservationPool&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Other resource group type and resource types aren&#39;t currently supported by this operation.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:GroupResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = GroupResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def list_group_resources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_group_resources

    &lt;p&gt;Returns a list of ARNs of the resources that are members of a specified resource group.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:ListGroupResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cloudformation:DescribeStacks&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cloudformation:ListStackResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tag:GetResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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


async def list_groups(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_groups

    &lt;p&gt;Returns a list of existing Resource Groups in your account.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:ListGroups&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    :param max_results: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the &lt;code&gt;NextToken&lt;/code&gt; response element is present and has a value (is not null). Include that value as the &lt;code&gt;NextToken&lt;/code&gt; request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check &lt;code&gt;NextToken&lt;/code&gt; after every operation to ensure that you receive all of the results.
    :type max_results: int
    :param next_token: The parameter for receiving additional results if you receive a &lt;code&gt;NextToken&lt;/code&gt; response in a previous request. A &lt;code&gt;NextToken&lt;/code&gt; response indicates that more output is available. Set this parameter to the value provided by a previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to indicate where the output should continue from.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    body = ListGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def put_group_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_group_configuration

    &lt;p&gt;Attaches a service configuration to the specified group. This occurs asynchronously, and can take time to complete. You can use &lt;a&gt;GetGroupConfiguration&lt;/a&gt; to check the status of the update.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:PutGroupConfiguration&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = PutGroupConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def search_resources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_resources

    &lt;p&gt;Returns a list of Amazon Web Services resource identifiers that matches the specified query. The query uses the same format as a resource query in a &lt;a&gt;CreateGroup&lt;/a&gt; or &lt;a&gt;UpdateGroupQuery&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:SearchResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cloudformation:DescribeStacks&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cloudformation:ListStackResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tag:GetResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = SearchResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def tag(request: web.Request, arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag

    &lt;p&gt;Adds tags to a resource group with the specified ARN. Existing tags on a resource group are not changed if they are not specified in the request parameters.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:Tag&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param arn: The ARN of the resource group to which to add tags.
    :type arn: str
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
    body = TagRequest.from_dict(body)
    return web.Response(status=200)


async def ungroup_resources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """ungroup_resources

    &lt;p&gt;Removes the specified resources from the specified group. This operation works only with static groups that you populated using the &lt;a&gt;GroupResources&lt;/a&gt; operation. It doesn&#39;t work with any resource groups that are automatically populated by tag-based or CloudFormation stack-based queries.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:UngroupResources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = UngroupResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def untag(request: web.Request, arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag

    &lt;p&gt;Deletes tags from a specified resource group.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:Untag&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param arn: The ARN of the resource group from which to remove tags. The command removed both the specified keys and any values associated with those keys.
    :type arn: str
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
    body = UntagRequest.from_dict(body)
    return web.Response(status=200)


async def update_account_settings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_account_settings

    &lt;p&gt;Turns on or turns off optional features in Resource Groups.&lt;/p&gt; &lt;p&gt;The preceding example shows that the request to turn on group lifecycle events is &lt;code&gt;IN_PROGRESS&lt;/code&gt;. You can call the &lt;a&gt;GetAccountSettings&lt;/a&gt; operation to check for completion by looking for &lt;code&gt;GroupLifecycleEventsStatus&lt;/code&gt; to change to &lt;code&gt;ACTIVE&lt;/code&gt;.&lt;/p&gt;

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
    body = UpdateAccountSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_group(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_group

    &lt;p&gt;Updates the description for an existing group. You cannot update the name of a resource group.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:UpdateGroup&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = UpdateGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_group_query(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_group_query

    &lt;p&gt;Updates the resource query of a group. For more information about resource queries, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag\&quot;&gt;Create a tag-based group in Resource Groups&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To run this command, you must have the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resource-groups:UpdateGroupQuery&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = UpdateGroupQueryRequest.from_dict(body)
    return web.Response(status=200)
