from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_channel_group_request import CreateChannelGroupRequest
from openapi_server.models.create_channel_group_response import CreateChannelGroupResponse
from openapi_server.models.create_channel_request import CreateChannelRequest
from openapi_server.models.create_channel_response import CreateChannelResponse
from openapi_server.models.create_origin_endpoint_request import CreateOriginEndpointRequest
from openapi_server.models.create_origin_endpoint_response import CreateOriginEndpointResponse
from openapi_server.models.get_channel_group_response import GetChannelGroupResponse
from openapi_server.models.get_channel_policy_response import GetChannelPolicyResponse
from openapi_server.models.get_channel_response import GetChannelResponse
from openapi_server.models.get_origin_endpoint_policy_response import GetOriginEndpointPolicyResponse
from openapi_server.models.get_origin_endpoint_response import GetOriginEndpointResponse
from openapi_server.models.list_channel_groups_response import ListChannelGroupsResponse
from openapi_server.models.list_channels_response import ListChannelsResponse
from openapi_server.models.list_origin_endpoints_response import ListOriginEndpointsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_channel_policy_request import PutChannelPolicyRequest
from openapi_server.models.put_origin_endpoint_policy_request import PutOriginEndpointPolicyRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_channel_group_request import UpdateChannelGroupRequest
from openapi_server.models.update_channel_group_response import UpdateChannelGroupResponse
from openapi_server.models.update_channel_request import UpdateChannelRequest
from openapi_server.models.update_channel_response import UpdateChannelResponse
from openapi_server.models.update_origin_endpoint_request import UpdateOriginEndpointRequest
from openapi_server.models.update_origin_endpoint_response import UpdateOriginEndpointResponse
from openapi_server import util


async def create_channel(request: web.Request, channel_group_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """create_channel

    Create a channel to start receiving content streams. The channel represents the input to MediaPackage for incoming live content from an encoder such as AWS Elemental MediaLive. The channel receives content, and after packaging it, outputs it through an origin endpoint to downstream devices (such as video players or CDNs) that request the content. You can create only one channel with each request. We recommend that you spread out channels between channel groups, such as putting redundant channels in the same AWS Region in different channel groups.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
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
    :param x_amzn_client_token: A unique, case-sensitive token that you provide to ensure the idempotency of the request.
    :type x_amzn_client_token: str

    """
    body = CreateChannelRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel_group(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """create_channel_group

    Create a channel group to group your channels and origin endpoints. A channel group is the top-level resource that consists of channels and origin endpoints that are associated with it and that provides predictable URLs for stream delivery. All channels and origin endpoints within the channel group are guaranteed to share the DNS. You can create only one channel group with each request. 

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
    :param x_amzn_client_token: A unique, case-sensitive token that you provide to ensure the idempotency of the request.
    :type x_amzn_client_token: str

    """
    body = CreateChannelGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_origin_endpoint(request: web.Request, channel_group_name, channel_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_client_token=None) -> web.Response:
    """create_origin_endpoint

    The endpoint is attached to a channel, and represents the output of the live content. You can associate multiple endpoints to a single channel. Each endpoint gives players and downstream CDNs (such as Amazon CloudFront) access to the content for playback. Content can&#39;t be served from a channel until it has an endpoint. You can create only one endpoint with each request. 

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
    :type channel_name: str
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
    :param x_amzn_client_token: A unique, case-sensitive token that you provide to ensure the idempotency of the request.
    :type x_amzn_client_token: str

    """
    body = CreateOriginEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def delete_channel(request: web.Request, channel_group_name, channel_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_channel

    Delete a channel to stop AWS Elemental MediaPackage from receiving further content. You must delete the channel&#39;s origin endpoints before you can delete the channel.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
    :type channel_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_channel_group(request: web.Request, channel_group_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_channel_group

    Delete a channel group. You must delete the channel group&#39;s channels and origin endpoints before you can delete the channel group. If you delete a channel group, you&#39;ll lose access to the egress domain and will have to create a new channel group to replace it.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_channel_policy(request: web.Request, channel_group_name, channel_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_channel_policy

    Delete a channel policy.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
    :type channel_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_origin_endpoint(request: web.Request, channel_group_name, channel_name, origin_endpoint_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_origin_endpoint

    Origin endpoints can serve content until they&#39;re deleted. Delete the endpoint if it should no longer respond to playback requests. You must delete all endpoints from a channel before you can delete the channel.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
    :type channel_name: str
    :param origin_endpoint_name: The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. 
    :type origin_endpoint_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_origin_endpoint_policy(request: web.Request, channel_group_name, channel_name, origin_endpoint_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_origin_endpoint_policy

    Delete an origin endpoint policy.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
    :type channel_name: str
    :param origin_endpoint_name: The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. 
    :type origin_endpoint_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_channel(request: web.Request, channel_group_name, channel_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_channel

    Retrieves the specified channel that&#39;s configured in AWS Elemental MediaPackage, including the origin endpoints that are associated with it.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
    :type channel_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_channel_group(request: web.Request, channel_group_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_channel_group

    Retrieves the specified channel group that&#39;s configured in AWS Elemental MediaPackage, including the channels and origin endpoints that are associated with it.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_channel_policy(request: web.Request, channel_group_name, channel_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_channel_policy

    Retrieves the specified channel policy that&#39;s configured in AWS Elemental MediaPackage. With policies, you can specify who has access to AWS resources and what actions they can perform on those resources.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
    :type channel_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_origin_endpoint(request: web.Request, channel_group_name, channel_name, origin_endpoint_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_origin_endpoint

    Retrieves the specified origin endpoint that&#39;s configured in AWS Elemental MediaPackage to obtain its playback URL and to view the packaging settings that it&#39;s currently using.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
    :type channel_name: str
    :param origin_endpoint_name: The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. 
    :type origin_endpoint_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_origin_endpoint_policy(request: web.Request, channel_group_name, channel_name, origin_endpoint_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_origin_endpoint_policy

    Retrieves the specified origin endpoint policy that&#39;s configured in AWS Elemental MediaPackage.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
    :type channel_name: str
    :param origin_endpoint_name: The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. 
    :type origin_endpoint_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def list_channel_groups(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channel_groups

    Retrieves all channel groups that are configured in AWS Elemental MediaPackage, including the channels and origin endpoints that are associated with it.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return in the response.
    :type max_results: int
    :param next_token: The pagination token from the GET list request. Use the token to fetch the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channels(request: web.Request, channel_group_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channels

    Retrieves all channels in a specific channel group that are configured in AWS Elemental MediaPackage, including the origin endpoints that are associated with it.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return in the response.
    :type max_results: int
    :param next_token: The pagination token from the GET list request. Use the token to fetch the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_origin_endpoints(request: web.Request, channel_group_name, channel_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_origin_endpoints

    Retrieves all origin endpoints in a specific channel that are configured in AWS Elemental MediaPackage.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
    :type channel_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return in the response.
    :type max_results: int
    :param next_token: The pagination token from the GET list request. Use the token to fetch the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags assigned to a resource.

    :param resource_arn: The ARN of the CloudWatch resource that you want to view tags for.
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


async def put_channel_policy(request: web.Request, channel_group_name, channel_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_channel_policy

    Attaches an IAM policy to the specified channel. With policies, you can specify who has access to AWS resources and what actions they can perform on those resources. You can attach only one policy with each request.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
    :type channel_name: str
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
    body = PutChannelPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_origin_endpoint_policy(request: web.Request, channel_group_name, channel_name, origin_endpoint_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_origin_endpoint_policy

    Attaches an IAM policy to the specified origin endpoint. You can attach only one policy with each request.

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
    :type channel_name: str
    :param origin_endpoint_name: The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. 
    :type origin_endpoint_name: str
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
    body = PutOriginEndpointPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns one of more tags (key-value pairs) to the specified MediaPackage resource.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values. You can use the TagResource operation with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt;

    :param resource_arn: The ARN of the MediaPackage resource that you&#39;re adding tags to.
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

    :param resource_arn: The ARN of the MediaPackage resource that you&#39;re removing tags from.
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


async def update_channel(request: web.Request, channel_group_name, channel_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_channel

    &lt;p&gt;Update the specified channel. You can edit if MediaPackage sends ingest or egress access logs to the CloudWatch log group, if content will be encrypted, the description on a channel, and your channel&#39;s policy settings. You can&#39;t edit the name of the channel or CloudFront distribution details.&lt;/p&gt; &lt;p&gt;Any edits you make that impact the video output may not be reflected for a few minutes.&lt;/p&gt;

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
    :type channel_name: str
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
    body = UpdateChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_channel_group(request: web.Request, channel_group_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_channel_group

    &lt;p&gt;Update the specified channel group. You can edit the description on a channel group for easier identification later from the AWS Elemental MediaPackage console. You can&#39;t edit the name of the channel group.&lt;/p&gt; &lt;p&gt;Any edits you make that impact the video output may not be reflected for a few minutes.&lt;/p&gt;

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
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
    body = UpdateChannelGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_origin_endpoint(request: web.Request, channel_group_name, channel_name, origin_endpoint_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_origin_endpoint

    &lt;p&gt;Update the specified origin endpoint. Edit the packaging preferences on an endpoint to optimize the viewing experience. You can&#39;t edit the name of the endpoint.&lt;/p&gt; &lt;p&gt;Any edits you make that impact the video output may not be reflected for a few minutes.&lt;/p&gt;

    :param channel_group_name: The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
    :type channel_group_name: str
    :param channel_name: The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. 
    :type channel_name: str
    :param origin_endpoint_name: The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. 
    :type origin_endpoint_name: str
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
    body = UpdateOriginEndpointRequest.from_dict(body)
    return web.Response(status=200)
