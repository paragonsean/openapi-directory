from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_app_instance_admin_request import CreateAppInstanceAdminRequest
from openapi_server.models.create_app_instance_admin_response import CreateAppInstanceAdminResponse
from openapi_server.models.create_app_instance_bot_request import CreateAppInstanceBotRequest
from openapi_server.models.create_app_instance_bot_response import CreateAppInstanceBotResponse
from openapi_server.models.create_app_instance_request import CreateAppInstanceRequest
from openapi_server.models.create_app_instance_response import CreateAppInstanceResponse
from openapi_server.models.create_app_instance_user_request import CreateAppInstanceUserRequest
from openapi_server.models.create_app_instance_user_response import CreateAppInstanceUserResponse
from openapi_server.models.describe_app_instance_admin_response import DescribeAppInstanceAdminResponse
from openapi_server.models.describe_app_instance_bot_response import DescribeAppInstanceBotResponse
from openapi_server.models.describe_app_instance_response import DescribeAppInstanceResponse
from openapi_server.models.describe_app_instance_user_endpoint_response import DescribeAppInstanceUserEndpointResponse
from openapi_server.models.describe_app_instance_user_response import DescribeAppInstanceUserResponse
from openapi_server.models.get_app_instance_retention_settings_response import GetAppInstanceRetentionSettingsResponse
from openapi_server.models.list_app_instance_admins_response import ListAppInstanceAdminsResponse
from openapi_server.models.list_app_instance_bots_response import ListAppInstanceBotsResponse
from openapi_server.models.list_app_instance_user_endpoints_response import ListAppInstanceUserEndpointsResponse
from openapi_server.models.list_app_instance_users_response import ListAppInstanceUsersResponse
from openapi_server.models.list_app_instances_response import ListAppInstancesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_app_instance_retention_settings_request import PutAppInstanceRetentionSettingsRequest
from openapi_server.models.put_app_instance_retention_settings_response import PutAppInstanceRetentionSettingsResponse
from openapi_server.models.put_app_instance_user_expiration_settings_request import PutAppInstanceUserExpirationSettingsRequest
from openapi_server.models.put_app_instance_user_expiration_settings_response import PutAppInstanceUserExpirationSettingsResponse
from openapi_server.models.register_app_instance_user_endpoint_request import RegisterAppInstanceUserEndpointRequest
from openapi_server.models.register_app_instance_user_endpoint_response import RegisterAppInstanceUserEndpointResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_app_instance_bot_request import UpdateAppInstanceBotRequest
from openapi_server.models.update_app_instance_bot_response import UpdateAppInstanceBotResponse
from openapi_server.models.update_app_instance_request import UpdateAppInstanceRequest
from openapi_server.models.update_app_instance_response import UpdateAppInstanceResponse
from openapi_server.models.update_app_instance_user_endpoint_request import UpdateAppInstanceUserEndpointRequest
from openapi_server.models.update_app_instance_user_endpoint_response import UpdateAppInstanceUserEndpointResponse
from openapi_server.models.update_app_instance_user_request import UpdateAppInstanceUserRequest
from openapi_server.models.update_app_instance_user_response import UpdateAppInstanceUserResponse
from openapi_server import util


async def create_app_instance(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_app_instance

    &lt;p&gt;Creates an Amazon Chime SDK messaging &lt;code&gt;AppInstance&lt;/code&gt; under an AWS account. Only SDK messaging customers use this API. &lt;code&gt;CreateAppInstance&lt;/code&gt; supports idempotency behavior as described in the AWS API Standard.&lt;/p&gt; &lt;p&gt;identity&lt;/p&gt;

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
    body = CreateAppInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def create_app_instance_admin(request: web.Request, app_instance_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_app_instance_admin

    &lt;p&gt;Promotes an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; to an &lt;code&gt;AppInstanceAdmin&lt;/code&gt;. The promoted entity can perform the following actions. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ChannelModerator&lt;/code&gt; actions across all channels in the &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeleteChannelMessage&lt;/code&gt; actions.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Only an &lt;code&gt;AppInstanceUser&lt;/code&gt; and &lt;code&gt;AppInstanceBot&lt;/code&gt; can be promoted to an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; role.&lt;/p&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
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
    body = CreateAppInstanceAdminRequest.from_dict(body)
    return web.Response(status=200)


async def create_app_instance_bot(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_app_instance_bot

    Creates a bot under an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;. The request consists of a unique &lt;code&gt;Configuration&lt;/code&gt; and &lt;code&gt;Name&lt;/code&gt; for that bot.

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
    body = CreateAppInstanceBotRequest.from_dict(body)
    return web.Response(status=200)


async def create_app_instance_user(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_app_instance_user

    Creates a user under an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;. The request consists of a unique &lt;code&gt;appInstanceUserId&lt;/code&gt; and &lt;code&gt;Name&lt;/code&gt; for that user.

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
    body = CreateAppInstanceUserRequest.from_dict(body)
    return web.Response(status=200)


async def delete_app_instance(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_instance

    Deletes an &lt;code&gt;AppInstance&lt;/code&gt; and all associated data asynchronously.

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_app_instance_admin(request: web.Request, app_instance_admin_arn, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_instance_admin

    Demotes an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; to an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt;. This action does not delete the user.

    :param app_instance_admin_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;&#39;s administrator.
    :type app_instance_admin_arn: str
    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_app_instance_bot(request: web.Request, app_instance_bot_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_instance_bot

    Deletes an &lt;code&gt;AppInstanceBot&lt;/code&gt;.

    :param app_instance_bot_arn: The ARN of the &lt;code&gt;AppInstanceBot&lt;/code&gt; being deleted.
    :type app_instance_bot_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_app_instance_user(request: web.Request, app_instance_user_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_instance_user

    Deletes an &lt;code&gt;AppInstanceUser&lt;/code&gt;.

    :param app_instance_user_arn: The ARN of the user request being deleted.
    :type app_instance_user_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def deregister_app_instance_user_endpoint(request: web.Request, app_instance_user_arn, endpoint_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_app_instance_user_endpoint

    Deregisters an &lt;code&gt;AppInstanceUserEndpoint&lt;/code&gt;.

    :param app_instance_user_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;.
    :type app_instance_user_arn: str
    :param endpoint_id: The unique identifier of the &lt;code&gt;AppInstanceUserEndpoint&lt;/code&gt;.
    :type endpoint_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_app_instance(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_instance

    Returns the full details of an &lt;code&gt;AppInstance&lt;/code&gt;.

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_app_instance_admin(request: web.Request, app_instance_admin_arn, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_instance_admin

    Returns the full details of an &lt;code&gt;AppInstanceAdmin&lt;/code&gt;.

    :param app_instance_admin_arn: The ARN of the &lt;code&gt;AppInstanceAdmin&lt;/code&gt;.
    :type app_instance_admin_arn: str
    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_app_instance_bot(request: web.Request, app_instance_bot_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_instance_bot

    The &lt;code&gt;AppInstanceBot&#39;s&lt;/code&gt; information.

    :param app_instance_bot_arn: The ARN of the &lt;code&gt;AppInstanceBot&lt;/code&gt;.
    :type app_instance_bot_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_app_instance_user(request: web.Request, app_instance_user_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_instance_user

    Returns the full details of an &lt;code&gt;AppInstanceUser&lt;/code&gt;.

    :param app_instance_user_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;.
    :type app_instance_user_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_app_instance_user_endpoint(request: web.Request, app_instance_user_arn, endpoint_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_instance_user_endpoint

    Returns the full details of an &lt;code&gt;AppInstanceUserEndpoint&lt;/code&gt;.

    :param app_instance_user_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;.
    :type app_instance_user_arn: str
    :param endpoint_id: The unique identifier of the &lt;code&gt;AppInstanceUserEndpoint&lt;/code&gt;.
    :type endpoint_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_app_instance_retention_settings(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_app_instance_retention_settings

    Gets the retention settings for an &lt;code&gt;AppInstance&lt;/code&gt;.

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def list_app_instance_admins(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_app_instance_admins

    Returns a list of the administrators in the &lt;code&gt;AppInstance&lt;/code&gt;.

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of administrators that you want to return.
    :type max_results: int
    :param next_token: The token returned from previous API requests until the number of administrators is reached.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_app_instance_bots(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_app_instance_bots

    Lists all &lt;code&gt;AppInstanceBots&lt;/code&gt; created under a single &lt;code&gt;AppInstance&lt;/code&gt;.

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of requests to return.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested bots are returned.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_app_instance_user_endpoints(request: web.Request, app_instance_user_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_app_instance_user_endpoints

    Lists all the &lt;code&gt;AppInstanceUserEndpoints&lt;/code&gt; created under a single &lt;code&gt;AppInstanceUser&lt;/code&gt;.

    :param app_instance_user_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;.
    :type app_instance_user_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of endpoints that you want to return.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested endpoints are returned.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_app_instance_users(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_app_instance_users

    List all &lt;code&gt;AppInstanceUsers&lt;/code&gt; created under a single &lt;code&gt;AppInstance&lt;/code&gt;.

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of requests that you want returned.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested users are returned.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_app_instances(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_app_instances

    Lists all Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;s created under a single AWS account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of &lt;code&gt;AppInstance&lt;/code&gt;s that you want to return.
    :type max_results: int
    :param next_token: The token passed by previous API requests until you reach the maximum number of &lt;code&gt;AppInstances&lt;/code&gt;.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags applied to an Amazon Chime SDK identity resource.

    :param arn: The ARN of the resource.
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


async def put_app_instance_retention_settings(request: web.Request, app_instance_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_app_instance_retention_settings

    Sets the amount of time in days that a given &lt;code&gt;AppInstance&lt;/code&gt; retains data.

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
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
    body = PutAppInstanceRetentionSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def put_app_instance_user_expiration_settings(request: web.Request, app_instance_user_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_app_instance_user_expiration_settings

    &lt;p&gt;Sets the number of days before the &lt;code&gt;AppInstanceUser&lt;/code&gt; is automatically deleted.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A background process deletes expired &lt;code&gt;AppInstanceUsers&lt;/code&gt; within 6 hours of expiration. Actual deletion times may vary.&lt;/p&gt; &lt;p&gt;Expired &lt;code&gt;AppInstanceUsers&lt;/code&gt; that have not yet been deleted appear as active, and you can update their expiration settings. The system honors the new settings.&lt;/p&gt; &lt;/note&gt;

    :param app_instance_user_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;.
    :type app_instance_user_arn: str
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
    body = PutAppInstanceUserExpirationSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def register_app_instance_user_endpoint(request: web.Request, app_instance_user_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_app_instance_user_endpoint

    Registers an endpoint under an Amazon Chime &lt;code&gt;AppInstanceUser&lt;/code&gt;. The endpoint receives messages for a user. For push notifications, the endpoint is a mobile device used to receive mobile push notifications for a user.

    :param app_instance_user_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;.
    :type app_instance_user_arn: str
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
    body = RegisterAppInstanceUserEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Applies the specified tags to the specified Amazon Chime SDK identity resource.

    :param operation: 
    :type operation: str
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


async def untag_resource(request: web.Request, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes the specified tags from the specified Amazon Chime SDK identity resource.

    :param operation: 
    :type operation: str
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


async def update_app_instance(request: web.Request, app_instance_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_app_instance

    Updates &lt;code&gt;AppInstance&lt;/code&gt; metadata.

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
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
    body = UpdateAppInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def update_app_instance_bot(request: web.Request, app_instance_bot_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_app_instance_bot

    Updates the name and metadata of an &lt;code&gt;AppInstanceBot&lt;/code&gt;.

    :param app_instance_bot_arn: The ARN of the &lt;code&gt;AppInstanceBot&lt;/code&gt;.
    :type app_instance_bot_arn: str
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
    body = UpdateAppInstanceBotRequest.from_dict(body)
    return web.Response(status=200)


async def update_app_instance_user(request: web.Request, app_instance_user_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_app_instance_user

    Updates the details of an &lt;code&gt;AppInstanceUser&lt;/code&gt;. You can update names and metadata.

    :param app_instance_user_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;.
    :type app_instance_user_arn: str
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
    body = UpdateAppInstanceUserRequest.from_dict(body)
    return web.Response(status=200)


async def update_app_instance_user_endpoint(request: web.Request, app_instance_user_arn, endpoint_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_app_instance_user_endpoint

    Updates the details of an &lt;code&gt;AppInstanceUserEndpoint&lt;/code&gt;. You can update the name and &lt;code&gt;AllowMessage&lt;/code&gt; values.

    :param app_instance_user_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;.
    :type app_instance_user_arn: str
    :param endpoint_id: The unique identifier of the &lt;code&gt;AppInstanceUserEndpoint&lt;/code&gt;.
    :type endpoint_id: str
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
    body = UpdateAppInstanceUserEndpointRequest.from_dict(body)
    return web.Response(status=200)
