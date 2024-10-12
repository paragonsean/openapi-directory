from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_signaling_channel_output import CreateSignalingChannelOutput
from openapi_server.models.create_signaling_channel_request import CreateSignalingChannelRequest
from openapi_server.models.create_stream_output import CreateStreamOutput
from openapi_server.models.create_stream_request import CreateStreamRequest
from openapi_server.models.delete_edge_configuration_request import DeleteEdgeConfigurationRequest
from openapi_server.models.delete_signaling_channel_request import DeleteSignalingChannelRequest
from openapi_server.models.delete_stream_request import DeleteStreamRequest
from openapi_server.models.describe_edge_configuration_output import DescribeEdgeConfigurationOutput
from openapi_server.models.describe_edge_configuration_request import DescribeEdgeConfigurationRequest
from openapi_server.models.describe_image_generation_configuration_output import DescribeImageGenerationConfigurationOutput
from openapi_server.models.describe_image_generation_configuration_request import DescribeImageGenerationConfigurationRequest
from openapi_server.models.describe_mapped_resource_configuration_output import DescribeMappedResourceConfigurationOutput
from openapi_server.models.describe_mapped_resource_configuration_request import DescribeMappedResourceConfigurationRequest
from openapi_server.models.describe_media_storage_configuration_output import DescribeMediaStorageConfigurationOutput
from openapi_server.models.describe_media_storage_configuration_request import DescribeMediaStorageConfigurationRequest
from openapi_server.models.describe_notification_configuration_output import DescribeNotificationConfigurationOutput
from openapi_server.models.describe_notification_configuration_request import DescribeNotificationConfigurationRequest
from openapi_server.models.describe_signaling_channel_output import DescribeSignalingChannelOutput
from openapi_server.models.describe_signaling_channel_request import DescribeSignalingChannelRequest
from openapi_server.models.describe_stream_output import DescribeStreamOutput
from openapi_server.models.describe_stream_request import DescribeStreamRequest
from openapi_server.models.get_data_endpoint_output import GetDataEndpointOutput
from openapi_server.models.get_data_endpoint_request import GetDataEndpointRequest
from openapi_server.models.get_signaling_channel_endpoint_output import GetSignalingChannelEndpointOutput
from openapi_server.models.get_signaling_channel_endpoint_request import GetSignalingChannelEndpointRequest
from openapi_server.models.list_edge_agent_configurations_output import ListEdgeAgentConfigurationsOutput
from openapi_server.models.list_edge_agent_configurations_request import ListEdgeAgentConfigurationsRequest
from openapi_server.models.list_signaling_channels_output import ListSignalingChannelsOutput
from openapi_server.models.list_signaling_channels_request import ListSignalingChannelsRequest
from openapi_server.models.list_streams_output import ListStreamsOutput
from openapi_server.models.list_streams_request import ListStreamsRequest
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_stream_output import ListTagsForStreamOutput
from openapi_server.models.list_tags_for_stream_request import ListTagsForStreamRequest
from openapi_server.models.start_edge_configuration_update_output import StartEdgeConfigurationUpdateOutput
from openapi_server.models.start_edge_configuration_update_request import StartEdgeConfigurationUpdateRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.tag_stream_request import TagStreamRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.untag_stream_request import UntagStreamRequest
from openapi_server.models.update_data_retention_request import UpdateDataRetentionRequest
from openapi_server.models.update_image_generation_configuration_request import UpdateImageGenerationConfigurationRequest
from openapi_server.models.update_media_storage_configuration_request import UpdateMediaStorageConfigurationRequest
from openapi_server.models.update_notification_configuration_request import UpdateNotificationConfigurationRequest
from openapi_server.models.update_signaling_channel_request import UpdateSignalingChannelRequest
from openapi_server.models.update_stream_request import UpdateStreamRequest
from openapi_server import util


async def create_signaling_channel(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_signaling_channel

    &lt;p&gt;Creates a signaling channel. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateSignalingChannel&lt;/code&gt; is an asynchronous operation.&lt;/p&gt;

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
    body = CreateSignalingChannelRequest.from_dict(body)
    return web.Response(status=200)


async def create_stream(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_stream

    &lt;p&gt;Creates a new Kinesis video stream. &lt;/p&gt; &lt;p&gt;When you create a new stream, Kinesis Video Streams assigns it a version number. When you change the stream&#39;s metadata, Kinesis Video Streams updates the version. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateStream&lt;/code&gt; is an asynchronous operation.&lt;/p&gt; &lt;p&gt;For information about how the service works, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-it-works.html\&quot;&gt;How it Works&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You must have permissions for the &lt;code&gt;KinesisVideo:CreateStream&lt;/code&gt; action.&lt;/p&gt;

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
    body = CreateStreamRequest.from_dict(body)
    return web.Response(status=200)


async def delete_edge_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_edge_configuration

    &lt;p&gt;An asynchronous API that deletes a stream’s existing edge configuration, as well as the corresponding media from the Edge Agent.&lt;/p&gt; &lt;p&gt;When you invoke this API, the sync status is set to &lt;code&gt;DELETING&lt;/code&gt;. A deletion process starts, in which active edge jobs are stopped and all media is deleted from the edge device. The time to delete varies, depending on the total amount of stored media. If the deletion process fails, the sync status changes to &lt;code&gt;DELETE_FAILED&lt;/code&gt;. You will need to re-try the deletion.&lt;/p&gt; &lt;p&gt;When the deletion process has completed successfully, the edge configuration is no longer accessible.&lt;/p&gt;

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
    body = DeleteEdgeConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_signaling_channel(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_signaling_channel

    Deletes a specified signaling channel. &lt;code&gt;DeleteSignalingChannel&lt;/code&gt; is an asynchronous operation. If you don&#39;t specify the channel&#39;s current version, the most recent version is deleted.

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
    body = DeleteSignalingChannelRequest.from_dict(body)
    return web.Response(status=200)


async def delete_stream(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_stream

    &lt;p&gt;Deletes a Kinesis video stream and the data contained in the stream. &lt;/p&gt; &lt;p&gt;This method marks the stream for deletion, and makes the data in the stream inaccessible immediately.&lt;/p&gt; &lt;p&gt; &lt;/p&gt; &lt;p&gt; To ensure that you have the latest version of the stream before deleting it, you can specify the stream version. Kinesis Video Streams assigns a version to each stream. When you update a stream, Kinesis Video Streams assigns a new version number. To get the latest stream version, use the &lt;code&gt;DescribeStream&lt;/code&gt; API. &lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;KinesisVideo:DeleteStream&lt;/code&gt; action.&lt;/p&gt;

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
    body = DeleteStreamRequest.from_dict(body)
    return web.Response(status=200)


async def describe_edge_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_edge_configuration

    Describes a stream’s edge configuration that was set using the &lt;code&gt;StartEdgeConfigurationUpdate&lt;/code&gt; API and the latest status of the edge agent&#39;s recorder and uploader jobs. Use this API to get the status of the configuration to determine if the configuration is in sync with the Edge Agent. Use this API to evaluate the health of the Edge Agent.

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
    body = DescribeEdgeConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_image_generation_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_image_generation_configuration

    Gets the &lt;code&gt;ImageGenerationConfiguration&lt;/code&gt; for a given Kinesis video stream.

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
    body = DescribeImageGenerationConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_mapped_resource_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_mapped_resource_configuration

    Returns the most current information about the stream. The &lt;code&gt;streamName&lt;/code&gt; or &lt;code&gt;streamARN&lt;/code&gt; should be provided in the input.

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
    body = DescribeMappedResourceConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_media_storage_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_media_storage_configuration

    Returns the most current information about the channel. Specify the &lt;code&gt;ChannelName&lt;/code&gt; or &lt;code&gt;ChannelARN&lt;/code&gt; in the input.

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
    body = DescribeMediaStorageConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_notification_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_notification_configuration

    Gets the &lt;code&gt;NotificationConfiguration&lt;/code&gt; for a given Kinesis video stream.

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
    body = DescribeNotificationConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_signaling_channel(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_signaling_channel

    Returns the most current information about the signaling channel. You must specify either the name or the Amazon Resource Name (ARN) of the channel that you want to describe.

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
    body = DescribeSignalingChannelRequest.from_dict(body)
    return web.Response(status=200)


async def describe_stream(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_stream

    Returns the most current information about the specified stream. You must specify either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt;. 

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
    body = DescribeStreamRequest.from_dict(body)
    return web.Response(status=200)


async def get_data_endpoint(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_data_endpoint

    &lt;p&gt;Gets an endpoint for a specified stream for either reading or writing. Use this endpoint in your application to read from the specified stream (using the &lt;code&gt;GetMedia&lt;/code&gt; or &lt;code&gt;GetMediaForFragmentList&lt;/code&gt; operations) or write to it (using the &lt;code&gt;PutMedia&lt;/code&gt; operation). &lt;/p&gt; &lt;note&gt; &lt;p&gt;The returned endpoint does not have the API name appended. The client needs to add the API name to the returned endpoint.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;In the request, specify the stream either by &lt;code&gt;StreamName&lt;/code&gt; or &lt;code&gt;StreamARN&lt;/code&gt;.&lt;/p&gt;

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
    body = GetDataEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def get_signaling_channel_endpoint(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_signaling_channel_endpoint

    &lt;p&gt;Provides an endpoint for the specified signaling channel to send and receive messages. This API uses the &lt;code&gt;SingleMasterChannelEndpointConfiguration&lt;/code&gt; input parameter, which consists of the &lt;code&gt;Protocols&lt;/code&gt; and &lt;code&gt;Role&lt;/code&gt; properties.&lt;/p&gt; &lt;p&gt; &lt;code&gt;Protocols&lt;/code&gt; is used to determine the communication mechanism. For example, if you specify &lt;code&gt;WSS&lt;/code&gt; as the protocol, this API produces a secure websocket endpoint. If you specify &lt;code&gt;HTTPS&lt;/code&gt; as the protocol, this API generates an HTTPS endpoint. &lt;/p&gt; &lt;p&gt; &lt;code&gt;Role&lt;/code&gt; determines the messaging permissions. A &lt;code&gt;MASTER&lt;/code&gt; role results in this API generating an endpoint that a client can use to communicate with any of the viewers on the channel. A &lt;code&gt;VIEWER&lt;/code&gt; role results in this API generating an endpoint that a client can use to communicate only with a &lt;code&gt;MASTER&lt;/code&gt;. &lt;/p&gt;

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
    body = GetSignalingChannelEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def list_edge_agent_configurations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_edge_agent_configurations

    &lt;p&gt;Returns an array of edge configurations associated with the specified Edge Agent.&lt;/p&gt; &lt;p&gt;In the request, you must specify the Edge Agent &lt;code&gt;HubDeviceArn&lt;/code&gt;.&lt;/p&gt;

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
    body = ListEdgeAgentConfigurationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_signaling_channels(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_signaling_channels

    Returns an array of &lt;code&gt;ChannelInfo&lt;/code&gt; objects. Each object describes a signaling channel. To retrieve only those channels that satisfy a specific condition, you can specify a &lt;code&gt;ChannelNameCondition&lt;/code&gt;.

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
    body = ListSignalingChannelsRequest.from_dict(body)
    return web.Response(status=200)


async def list_streams(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_streams

    Returns an array of &lt;code&gt;StreamInfo&lt;/code&gt; objects. Each object describes a stream. To retrieve only streams that satisfy a specific condition, you can specify a &lt;code&gt;StreamNameCondition&lt;/code&gt;. 

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
    body = ListStreamsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Returns a list of tags associated with the specified signaling channel.

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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_stream(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_stream

    &lt;p&gt;Returns a list of tags associated with the specified stream.&lt;/p&gt; &lt;p&gt;In the request, you must specify either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt;. &lt;/p&gt;

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
    body = ListTagsForStreamRequest.from_dict(body)
    return web.Response(status=200)


async def start_edge_configuration_update(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_edge_configuration_update

    &lt;p&gt;An asynchronous API that updates a stream’s existing edge configuration. The Kinesis Video Stream will sync the stream’s edge configuration with the Edge Agent IoT Greengrass component that runs on an IoT Hub Device, setup at your premise. The time to sync can vary and depends on the connectivity of the Hub Device. The &lt;code&gt;SyncStatus&lt;/code&gt; will be updated as the edge configuration is acknowledged, and synced with the Edge Agent. &lt;/p&gt; &lt;p&gt;If this API is invoked for the first time, a new edge configuration will be created for the stream, and the sync status will be set to &lt;code&gt;SYNCING&lt;/code&gt;. You will have to wait for the sync status to reach a terminal state such as: &lt;code&gt;IN_SYNC&lt;/code&gt;, or &lt;code&gt;SYNC_FAILED&lt;/code&gt;, before using this API again. If you invoke this API during the syncing process, a &lt;code&gt;ResourceInUseException&lt;/code&gt; will be thrown. The connectivity of the stream’s edge configuration and the Edge Agent will be retried for 15 minutes. After 15 minutes, the status will transition into the &lt;code&gt;SYNC_FAILED&lt;/code&gt; state.&lt;/p&gt;

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
    body = StartEdgeConfigurationUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds one or more tags to a signaling channel. A &lt;i&gt;tag&lt;/i&gt; is a key-value pair (the value is optional) that you can define and assign to Amazon Web Services resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management and Cost Management User Guide&lt;/i&gt;.

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


async def tag_stream(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_stream

    &lt;p&gt;Adds one or more tags to a stream. A &lt;i&gt;tag&lt;/i&gt; is a key-value pair (the value is optional) that you can define and assign to Amazon Web Services resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management and Cost Management User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;You must provide either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;KinesisVideo:TagStream&lt;/code&gt; action.&lt;/p&gt; &lt;p&gt;A Kinesis video stream can support up to 50 tags.&lt;/p&gt;

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
    body = TagStreamRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes one or more tags from a signaling channel. In the request, specify only a tag key or keys; don&#39;t specify the value. If you specify a tag key that does not exist, it&#39;s ignored.

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


async def untag_stream(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_stream

    &lt;p&gt;Removes one or more tags from a stream. In the request, specify only a tag key or keys; don&#39;t specify the value. If you specify a tag key that does not exist, it&#39;s ignored.&lt;/p&gt; &lt;p&gt;In the request, you must provide the &lt;code&gt;StreamName&lt;/code&gt; or &lt;code&gt;StreamARN&lt;/code&gt;.&lt;/p&gt;

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
    body = UntagStreamRequest.from_dict(body)
    return web.Response(status=200)


async def update_data_retention(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_data_retention

    &lt;p&gt; Increases or decreases the stream&#39;s data retention period by the value that you specify. To indicate whether you want to increase or decrease the data retention period, specify the &lt;code&gt;Operation&lt;/code&gt; parameter in the request body. In the request, you must specify either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The retention period that you specify replaces the current value.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;KinesisVideo:UpdateDataRetention&lt;/code&gt; action.&lt;/p&gt; &lt;p&gt;Changing the data retention period affects the data in the stream as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the data retention period is increased, existing data is retained for the new retention period. For example, if the data retention period is increased from one hour to seven hours, all existing data is retained for seven hours.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the data retention period is decreased, existing data is retained for the new retention period. For example, if the data retention period is decreased from seven hours to one hour, all existing data is retained for one hour, and any data older than one hour is deleted immediately.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = UpdateDataRetentionRequest.from_dict(body)
    return web.Response(status=200)


async def update_image_generation_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_image_generation_configuration

    Updates the &lt;code&gt;StreamInfo&lt;/code&gt; and &lt;code&gt;ImageProcessingConfiguration&lt;/code&gt; fields.

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
    body = UpdateImageGenerationConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def update_media_storage_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_media_storage_configuration

    &lt;p&gt;Associates a &lt;code&gt;SignalingChannel&lt;/code&gt; to a stream to store the media. There are two signaling modes that can specified :&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the &lt;code&gt;StorageStatus&lt;/code&gt; is disabled, no data will be stored, and the &lt;code&gt;StreamARN&lt;/code&gt; parameter will not be needed. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the &lt;code&gt;StorageStatus&lt;/code&gt; is enabled, the data will be stored in the &lt;code&gt;StreamARN&lt;/code&gt; provided. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;If &lt;code&gt;StorageStatus&lt;/code&gt; is enabled, direct peer-to-peer (master-viewer) connections no longer occur. Peers connect directly to the storage session. You must call the &lt;code&gt;JoinStorageSession&lt;/code&gt; API to trigger an SDP offer send and establish a connection between a peer and the storage session. &lt;/p&gt; &lt;/important&gt;

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
    body = UpdateMediaStorageConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def update_notification_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_notification_configuration

    Updates the notification information for a stream.

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
    body = UpdateNotificationConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def update_signaling_channel(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_signaling_channel

    &lt;p&gt;Updates the existing signaling channel. This is an asynchronous operation and takes time to complete. &lt;/p&gt; &lt;p&gt;If the &lt;code&gt;MessageTtlSeconds&lt;/code&gt; value is updated (either increased or reduced), it only applies to new messages sent via this channel after it&#39;s been updated. Existing messages are still expired as per the previous &lt;code&gt;MessageTtlSeconds&lt;/code&gt; value.&lt;/p&gt;

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
    body = UpdateSignalingChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_stream(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_stream

    &lt;p&gt;Updates stream metadata, such as the device name and media type.&lt;/p&gt; &lt;p&gt;You must provide the stream name or the Amazon Resource Name (ARN) of the stream.&lt;/p&gt; &lt;p&gt;To make sure that you have the latest version of the stream before updating it, you can specify the stream version. Kinesis Video Streams assigns a version to each stream. When you update a stream, Kinesis Video Streams assigns a new version number. To get the latest stream version, use the &lt;code&gt;DescribeStream&lt;/code&gt; API. &lt;/p&gt; &lt;p&gt; &lt;code&gt;UpdateStream&lt;/code&gt; is an asynchronous operation, and takes time to complete.&lt;/p&gt;

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
    body = UpdateStreamRequest.from_dict(body)
    return web.Response(status=200)
