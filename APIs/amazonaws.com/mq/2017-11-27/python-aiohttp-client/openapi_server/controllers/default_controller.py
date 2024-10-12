from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_broker_request import CreateBrokerRequest
from openapi_server.models.create_broker_response import CreateBrokerResponse
from openapi_server.models.create_configuration_request import CreateConfigurationRequest
from openapi_server.models.create_configuration_response import CreateConfigurationResponse
from openapi_server.models.create_tags_request import CreateTagsRequest
from openapi_server.models.create_user_request import CreateUserRequest
from openapi_server.models.delete_broker_response import DeleteBrokerResponse
from openapi_server.models.describe_broker_engine_types_response import DescribeBrokerEngineTypesResponse
from openapi_server.models.describe_broker_instance_options_response import DescribeBrokerInstanceOptionsResponse
from openapi_server.models.describe_broker_response import DescribeBrokerResponse
from openapi_server.models.describe_configuration_response import DescribeConfigurationResponse
from openapi_server.models.describe_configuration_revision_response import DescribeConfigurationRevisionResponse
from openapi_server.models.describe_user_response import DescribeUserResponse
from openapi_server.models.list_brokers_response import ListBrokersResponse
from openapi_server.models.list_configuration_revisions_response import ListConfigurationRevisionsResponse
from openapi_server.models.list_configurations_response import ListConfigurationsResponse
from openapi_server.models.list_tags_response import ListTagsResponse
from openapi_server.models.list_users_response import ListUsersResponse
from openapi_server.models.promote_request import PromoteRequest
from openapi_server.models.promote_response import PromoteResponse
from openapi_server.models.update_broker_request import UpdateBrokerRequest
from openapi_server.models.update_broker_response import UpdateBrokerResponse
from openapi_server.models.update_configuration_request import UpdateConfigurationRequest
from openapi_server.models.update_configuration_response import UpdateConfigurationResponse
from openapi_server.models.update_user_request import UpdateUserRequest
from openapi_server import util


async def create_broker(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_broker

    &lt;p&gt;Creates a broker. Note: This API is asynchronous.&lt;/p&gt; &lt;p&gt;To create a broker, you must either use the AmazonMQFullAccess IAM policy or include the following EC2 permissions in your IAM policy.&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;ec2:CreateNetworkInterface&lt;/p&gt; &lt;p&gt;This permission is required to allow Amazon MQ to create an elastic network interface (ENI) on behalf of your account.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:CreateNetworkInterfacePermission&lt;/p&gt; &lt;p&gt;This permission is required to attach the ENI to the broker instance.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DeleteNetworkInterface&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DeleteNetworkInterfacePermission&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DetachNetworkInterface&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeInternetGateways&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeNetworkInterfaces&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeNetworkInterfacePermissions&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeRouteTables&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeSecurityGroups&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeSubnets&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;ec2:DescribeVpcs&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/amazon-mq-setting-up.html#create-iam-user\&quot;&gt;Create an IAM User and Get Your Amazon Web Services Credentials&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/connecting-to-amazon-mq.html#never-modify-delete-elastic-network-interface\&quot;&gt;Never Modify or Delete the Amazon MQ Elastic Network Interface&lt;/a&gt; in the &lt;i&gt;Amazon MQ Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CreateBrokerRequest.from_dict(body)
    return web.Response(status=200)


async def create_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_configuration

    Creates a new configuration for the specified configuration name. Amazon MQ uses the default configuration (the engine type and version).

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
    body = CreateConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def create_tags(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_tags

    Add a tag to a resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource tag.
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
    body = CreateTagsRequest.from_dict(body)
    return web.Response(status=200)


async def create_user(request: web.Request, broker_id, username, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_user

    &lt;p&gt;Creates an ActiveMQ user.&lt;/p&gt; &lt;important&gt;&lt;p&gt;Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames. Broker usernames are accessible to other Amazon Web Services services, including CloudWatch Logs. Broker usernames are not intended to be used for private or sensitive data.&lt;/p&gt;&lt;/important&gt;

    :param broker_id: The unique ID that Amazon MQ generates for the broker.
    :type broker_id: str
    :param username: The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
    :type username: str
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
    body = CreateUserRequest.from_dict(body)
    return web.Response(status=200)


async def delete_broker(request: web.Request, broker_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_broker

    Deletes a broker. Note: This API is asynchronous.

    :param broker_id: The unique ID that Amazon MQ generates for the broker.
    :type broker_id: str
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


async def delete_tags(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_tags

    Removes a tag from a resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource tag.
    :type resource_arn: str
    :param tag_keys: An array of tag keys to delete
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


async def delete_user(request: web.Request, broker_id, username, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_user

    Deletes an ActiveMQ user.

    :param broker_id: The unique ID that Amazon MQ generates for the broker.
    :type broker_id: str
    :param username: The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
    :type username: str
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


async def describe_broker(request: web.Request, broker_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_broker

    Returns information about the specified broker.

    :param broker_id: The unique ID that Amazon MQ generates for the broker.
    :type broker_id: str
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


async def describe_broker_engine_types(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, engine_type=None, max_results=None, next_token=None) -> web.Response:
    """describe_broker_engine_types

    Describe available engine types and versions.

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
    :param engine_type: Filter response by engine type.
    :type engine_type: str
    :param max_results: The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
    :type max_results: int
    :param next_token: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
    :type next_token: str

    """
    return web.Response(status=200)


async def describe_broker_instance_options(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, engine_type=None, host_instance_type=None, max_results=None, next_token=None, storage_type=None) -> web.Response:
    """describe_broker_instance_options

    Describe available broker instance options.

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
    :param engine_type: Filter response by engine type.
    :type engine_type: str
    :param host_instance_type: Filter response by host instance type.
    :type host_instance_type: str
    :param max_results: The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
    :type max_results: int
    :param next_token: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
    :type next_token: str
    :param storage_type: Filter response by storage type.
    :type storage_type: str

    """
    return web.Response(status=200)


async def describe_configuration(request: web.Request, configuration_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_configuration

    Returns information about the specified configuration.

    :param configuration_id: The unique ID that Amazon MQ generates for the configuration.
    :type configuration_id: str
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


async def describe_configuration_revision(request: web.Request, configuration_id, configuration_revision, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_configuration_revision

    Returns the specified configuration revision for the specified configuration.

    :param configuration_id: The unique ID that Amazon MQ generates for the configuration.
    :type configuration_id: str
    :param configuration_revision: The revision of the configuration.
    :type configuration_revision: str
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


async def describe_user(request: web.Request, broker_id, username, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_user

    Returns information about an ActiveMQ user.

    :param broker_id: The unique ID that Amazon MQ generates for the broker.
    :type broker_id: str
    :param username: The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
    :type username: str
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


async def list_brokers(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_brokers

    Returns a list of all brokers.

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
    :param max_results: The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
    :type max_results: int
    :param next_token: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_configuration_revisions(request: web.Request, configuration_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_configuration_revisions

    Returns a list of all revisions for the specified configuration.

    :param configuration_id: The unique ID that Amazon MQ generates for the configuration.
    :type configuration_id: str
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
    :param max_results: The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
    :type max_results: int
    :param next_token: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_configurations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_configurations

    Returns a list of all configurations.

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
    :param max_results: The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
    :type max_results: int
    :param next_token: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags

    Lists tags for a resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource tag.
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


async def list_users(request: web.Request, broker_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_users

    Returns a list of all ActiveMQ users.

    :param broker_id: The unique ID that Amazon MQ generates for the broker.
    :type broker_id: str
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
    :param max_results: The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
    :type max_results: int
    :param next_token: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
    :type next_token: str

    """
    return web.Response(status=200)


async def promote(request: web.Request, broker_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """promote

    Promotes a data replication replica broker to the primary broker role.

    :param broker_id: The unique ID that Amazon MQ generates for the broker.
    :type broker_id: str
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
    body = PromoteRequest.from_dict(body)
    return web.Response(status=200)


async def reboot_broker(request: web.Request, broker_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reboot_broker

    Reboots a broker. Note: This API is asynchronous.

    :param broker_id: The unique ID that Amazon MQ generates for the broker.
    :type broker_id: str
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


async def update_broker(request: web.Request, broker_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_broker

    Adds a pending configuration change to a broker.

    :param broker_id: The unique ID that Amazon MQ generates for the broker.
    :type broker_id: str
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
    body = UpdateBrokerRequest.from_dict(body)
    return web.Response(status=200)


async def update_configuration(request: web.Request, configuration_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_configuration

    Updates the specified configuration.

    :param configuration_id: The unique ID that Amazon MQ generates for the configuration.
    :type configuration_id: str
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
    body = UpdateConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def update_user(request: web.Request, broker_id, username, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user

    Updates the information for an ActiveMQ user.

    :param broker_id: The unique ID that Amazon MQ generates for the broker.
    :type broker_id: str
    :param username: The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
    :type username: str
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
    body = UpdateUserRequest.from_dict(body)
    return web.Response(status=200)
