from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_channel_flow_request import AssociateChannelFlowRequest
from openapi_server.models.batch_create_channel_membership_request import BatchCreateChannelMembershipRequest
from openapi_server.models.batch_create_channel_membership_response import BatchCreateChannelMembershipResponse
from openapi_server.models.channel_flow_callback_request import ChannelFlowCallbackRequest
from openapi_server.models.channel_flow_callback_response import ChannelFlowCallbackResponse
from openapi_server.models.create_channel_ban_request import CreateChannelBanRequest
from openapi_server.models.create_channel_ban_response import CreateChannelBanResponse
from openapi_server.models.create_channel_flow_request import CreateChannelFlowRequest
from openapi_server.models.create_channel_flow_response import CreateChannelFlowResponse
from openapi_server.models.create_channel_membership_request import CreateChannelMembershipRequest
from openapi_server.models.create_channel_membership_response import CreateChannelMembershipResponse
from openapi_server.models.create_channel_moderator_request import CreateChannelModeratorRequest
from openapi_server.models.create_channel_moderator_response import CreateChannelModeratorResponse
from openapi_server.models.create_channel_request import CreateChannelRequest
from openapi_server.models.create_channel_response import CreateChannelResponse
from openapi_server.models.describe_channel_ban_response import DescribeChannelBanResponse
from openapi_server.models.describe_channel_flow_response import DescribeChannelFlowResponse
from openapi_server.models.describe_channel_membership_for_app_instance_user_response import DescribeChannelMembershipForAppInstanceUserResponse
from openapi_server.models.describe_channel_membership_response import DescribeChannelMembershipResponse
from openapi_server.models.describe_channel_moderated_by_app_instance_user_response import DescribeChannelModeratedByAppInstanceUserResponse
from openapi_server.models.describe_channel_moderator_response import DescribeChannelModeratorResponse
from openapi_server.models.describe_channel_response import DescribeChannelResponse
from openapi_server.models.get_channel_membership_preferences_response import GetChannelMembershipPreferencesResponse
from openapi_server.models.get_channel_message_response import GetChannelMessageResponse
from openapi_server.models.get_channel_message_status_response import GetChannelMessageStatusResponse
from openapi_server.models.get_messaging_session_endpoint_response import GetMessagingSessionEndpointResponse
from openapi_server.models.get_messaging_streaming_configurations_response import GetMessagingStreamingConfigurationsResponse
from openapi_server.models.list_channel_bans_response import ListChannelBansResponse
from openapi_server.models.list_channel_flows_response import ListChannelFlowsResponse
from openapi_server.models.list_channel_memberships_for_app_instance_user_response import ListChannelMembershipsForAppInstanceUserResponse
from openapi_server.models.list_channel_memberships_response import ListChannelMembershipsResponse
from openapi_server.models.list_channel_messages_response import ListChannelMessagesResponse
from openapi_server.models.list_channel_moderators_response import ListChannelModeratorsResponse
from openapi_server.models.list_channels_associated_with_channel_flow_response import ListChannelsAssociatedWithChannelFlowResponse
from openapi_server.models.list_channels_moderated_by_app_instance_user_response import ListChannelsModeratedByAppInstanceUserResponse
from openapi_server.models.list_channels_response import ListChannelsResponse
from openapi_server.models.list_sub_channels_response import ListSubChannelsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_channel_expiration_settings_request import PutChannelExpirationSettingsRequest
from openapi_server.models.put_channel_expiration_settings_response import PutChannelExpirationSettingsResponse
from openapi_server.models.put_channel_membership_preferences_request import PutChannelMembershipPreferencesRequest
from openapi_server.models.put_channel_membership_preferences_response import PutChannelMembershipPreferencesResponse
from openapi_server.models.put_messaging_streaming_configurations_request import PutMessagingStreamingConfigurationsRequest
from openapi_server.models.put_messaging_streaming_configurations_response import PutMessagingStreamingConfigurationsResponse
from openapi_server.models.redact_channel_message_request import RedactChannelMessageRequest
from openapi_server.models.redact_channel_message_response import RedactChannelMessageResponse
from openapi_server.models.search_channels_request import SearchChannelsRequest
from openapi_server.models.search_channels_response import SearchChannelsResponse
from openapi_server.models.send_channel_message_request import SendChannelMessageRequest
from openapi_server.models.send_channel_message_response import SendChannelMessageResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_channel_flow_request import UpdateChannelFlowRequest
from openapi_server.models.update_channel_flow_response import UpdateChannelFlowResponse
from openapi_server.models.update_channel_message_request import UpdateChannelMessageRequest
from openapi_server.models.update_channel_message_response import UpdateChannelMessageResponse
from openapi_server.models.update_channel_read_marker_response import UpdateChannelReadMarkerResponse
from openapi_server.models.update_channel_request import UpdateChannelRequest
from openapi_server.models.update_channel_response import UpdateChannelResponse
from openapi_server import util


async def associate_channel_flow(request: web.Request, channel_arn, x_amz_chime_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_channel_flow

    &lt;p&gt;Associates a channel flow with a channel. Once associated, all messages to that channel go through channel flow processors. To stop processing, use the &lt;code&gt;DisassociateChannelFlow&lt;/code&gt; API.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only administrators or channel moderators can associate a channel flow. The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call.
    :type x_amz_chime_bearer: str
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
    body = AssociateChannelFlowRequest.from_dict(body)
    return web.Response(status=200)


async def batch_create_channel_membership(request: web.Request, channel_arn, x_amz_chime_bearer, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_create_channel_membership

    Adds a specified number of users and bots to a channel. 

    :param channel_arn: The ARN of the channel to which you&#39;re adding users or bots.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
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
    body = BatchCreateChannelMembershipRequest.from_dict(body)
    return web.Response(status=200)


async def channel_flow_callback(request: web.Request, channel_arn, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """channel_flow_callback

    &lt;p&gt;Calls back Amazon Chime SDK messaging with a processing response message. This should be invoked from the processor Lambda. This is a developer API.&lt;/p&gt; &lt;p&gt;You can return one of the following processing responses:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Update message content or metadata&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deny a message&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Make no changes to the message&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
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
    body = ChannelFlowCallbackRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel(request: web.Request, x_amz_chime_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_channel

    &lt;p&gt;Creates a channel to which you can add users and send messages.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Restriction&lt;/b&gt;: You can&#39;t change a channel&#39;s privacy.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
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
    body = CreateChannelRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel_ban(request: web.Request, channel_arn, x_amz_chime_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_channel_ban

    &lt;p&gt;Permanently bans a member from a channel. Moderators can&#39;t add banned members to a channel. To undo a ban, you first have to &lt;code&gt;DeleteChannelBan&lt;/code&gt;, and then &lt;code&gt;CreateChannelMembership&lt;/code&gt;. Bans are cleaned up when you delete users or channels.&lt;/p&gt; &lt;p&gt;If you ban a user who is already part of a channel, that user is automatically kicked from the channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the ban request.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
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
    body = CreateChannelBanRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel_flow(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_channel_flow

    &lt;p&gt;Creates a channel flow, a container for processors. Processors are AWS Lambda functions that perform actions on chat messages, such as stripping out profanity. You can associate channel flows with channels, and the processors in the channel flow then take action on all messages sent to that channel. This is a developer API.&lt;/p&gt; &lt;p&gt;Channel flows process the following items:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;New and updated messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Persistent and non-persistent messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Standard message type&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;note&gt; &lt;p&gt;Channel flows don&#39;t process Control or System messages. For more information about the message types provided by Chime SDK messaging, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/dg/using-the-messaging-sdk.html#msg-types\&quot;&gt;Message types&lt;/a&gt; in the &lt;i&gt;Amazon Chime developer guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateChannelFlowRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel_membership(request: web.Request, channel_arn, x_amz_chime_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_channel_membership

    &lt;p&gt;Adds a member to a channel. The &lt;code&gt;InvitedBy&lt;/code&gt; field in &lt;code&gt;ChannelMembership&lt;/code&gt; is derived from the request header. A channel member can:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;List messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Send messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Receive messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Edit their own messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Leave the channel&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Privacy settings impact this action as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Public Channels: You do not need to be a member to list messages, but you must be a member to send messages.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Private Channels: You must be a member to list or send messages.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel to which you&#39;re adding users.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
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
    body = CreateChannelMembershipRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel_moderator(request: web.Request, channel_arn, x_amz_chime_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_channel_moderator

    &lt;p&gt;Creates a new &lt;code&gt;ChannelModerator&lt;/code&gt;. A channel moderator can:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Add and remove other members of the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add and remove other moderators of the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add and remove user bans for the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Redact messages in the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;List messages in the channel.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt;of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
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
    body = CreateChannelModeratorRequest.from_dict(body)
    return web.Response(status=200)


async def delete_channel(request: web.Request, channel_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_channel

    &lt;p&gt;Immediately makes a channel and its memberships inaccessible and marks them for deletion. This is an irreversible process.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel being deleted.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_channel_ban(request: web.Request, channel_arn, member_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_channel_ban

    &lt;p&gt;Removes a member from a channel&#39;s ban list.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel from which the &lt;code&gt;AppInstanceUser&lt;/code&gt; was banned.
    :type channel_arn: str
    :param member_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; that you want to reinstate.
    :type member_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_channel_flow(request: web.Request, channel_flow_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_channel_flow

    &lt;p&gt;Deletes a channel flow, an irreversible process. This is a developer API.&lt;/p&gt; &lt;note&gt; &lt;p&gt; This API works only when the channel flow is not associated with any channel. To get a list of all channels that a channel flow is associated with, use the &lt;code&gt;ListChannelsAssociatedWithChannelFlow&lt;/code&gt; API. Use the &lt;code&gt;DisassociateChannelFlow&lt;/code&gt; API to disassociate a channel flow from all channels. &lt;/p&gt; &lt;/note&gt;

    :param channel_flow_arn: The ARN of the channel flow.
    :type channel_flow_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_channel_membership(request: web.Request, channel_arn, member_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sub_channel_id=None) -> web.Response:
    """delete_channel_membership

    &lt;p&gt;Removes a member from a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel from which you want to remove the user.
    :type channel_arn: str
    :param member_arn: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member that you&#39;re removing from the channel.
    :type member_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param sub_channel_id: &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only for use by moderators.&lt;/p&gt; &lt;/note&gt;
    :type sub_channel_id: str

    """
    return web.Response(status=200)


async def delete_channel_message(request: web.Request, channel_arn, message_id, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sub_channel_id=None) -> web.Response:
    """delete_channel_message

    &lt;p&gt;Deletes a channel message. Only admins can perform this action. Deletion makes messages inaccessible immediately. A background process deletes any revisions created by &lt;code&gt;UpdateChannelMessage&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param message_id: The ID of the message being deleted.
    :type message_id: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param sub_channel_id: &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when deleting messages in a SubChannel that the user belongs to.&lt;/p&gt; &lt;/note&gt;
    :type sub_channel_id: str

    """
    return web.Response(status=200)


async def delete_channel_moderator(request: web.Request, channel_arn, channel_moderator_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_channel_moderator

    &lt;p&gt;Deletes a channel moderator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param channel_moderator_arn: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the moderator being deleted.
    :type channel_moderator_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_messaging_streaming_configurations(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_messaging_streaming_configurations

    Deletes the streaming configurations for an &lt;code&gt;AppInstance&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html\&quot;&gt;Streaming messaging data&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.

    :param app_instance_arn: The ARN of the streaming configurations being deleted.
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


async def describe_channel(request: web.Request, channel_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_channel

    &lt;p&gt;Returns the full details of a channel in an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_channel_ban(request: web.Request, channel_arn, member_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_channel_ban

    &lt;p&gt;Returns the full details of a channel ban.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel from which the user is banned.
    :type channel_arn: str
    :param member_arn: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member being banned.
    :type member_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_channel_flow(request: web.Request, channel_flow_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_channel_flow

    Returns the full details of a channel flow in an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;. This is a developer API.

    :param channel_flow_arn: The ARN of the channel flow.
    :type channel_flow_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_channel_membership(request: web.Request, channel_arn, member_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sub_channel_id=None) -> web.Response:
    """describe_channel_membership

    &lt;p&gt;Returns the full details of a user&#39;s channel membership.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param member_arn: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member.
    :type member_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param sub_channel_id: &lt;p&gt;The ID of the SubChannel in the request. The response contains an &lt;code&gt;ElasticChannelConfiguration&lt;/code&gt; object.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required to get a user’s SubChannel membership details.&lt;/p&gt; &lt;/note&gt;
    :type sub_channel_id: str

    """
    return web.Response(status=200)


async def describe_channel_membership_for_app_instance_user(request: web.Request, channel_arn, app_instance_user_arn, x_amz_chime_bearer, scope, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_channel_membership_for_app_instance_user

    &lt;p&gt; Returns the details of a channel based on the membership of the specified &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel to which the user belongs.
    :type channel_arn: str
    :param app_instance_user_arn: The ARN of the user or bot in a channel.
    :type app_instance_user_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param scope: 
    :type scope: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_channel_moderated_by_app_instance_user(request: web.Request, channel_arn, app_instance_user_arn, x_amz_chime_bearer, scope, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_channel_moderated_by_app_instance_user

    &lt;p&gt;Returns the full details of a channel moderated by the specified &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the moderated channel.
    :type channel_arn: str
    :param app_instance_user_arn: The ARN of the user or bot in the moderated channel.
    :type app_instance_user_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param scope: 
    :type scope: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_channel_moderator(request: web.Request, channel_arn, channel_moderator_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_channel_moderator

    &lt;p&gt;Returns the full details of a single ChannelModerator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param channel_moderator_arn: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the channel moderator.
    :type channel_moderator_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def disassociate_channel_flow(request: web.Request, channel_arn, channel_flow_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_channel_flow

    &lt;p&gt;Disassociates a channel flow from all its channels. Once disassociated, all messages to that channel stop going through the channel flow processor.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only administrators or channel moderators can disassociate a channel flow.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param channel_flow_arn: The ARN of the channel flow.
    :type channel_flow_arn: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_channel_membership_preferences(request: web.Request, channel_arn, member_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_channel_membership_preferences

    &lt;p&gt;Gets the membership preferences of an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; for the specified channel. A user or a bot must be a member of the channel and own the membership in order to retrieve membership preferences. Users or bots in the &lt;code&gt;AppInstanceAdmin&lt;/code&gt; and channel moderator roles can&#39;t retrieve preferences for other users or bots. Banned users or bots can&#39;t retrieve membership preferences for the channel from which they are banned.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param member_arn: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member retrieving the preferences.
    :type member_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_channel_message(request: web.Request, channel_arn, message_id, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sub_channel_id=None) -> web.Response:
    """get_channel_message

    &lt;p&gt;Gets the full details of a channel message.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param message_id: The ID of the message.
    :type message_id: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param sub_channel_id: &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when getting messages in a SubChannel that the user belongs to.&lt;/p&gt; &lt;/note&gt;
    :type sub_channel_id: str

    """
    return web.Response(status=200)


async def get_channel_message_status(request: web.Request, channel_arn, message_id, x_amz_chime_bearer, scope, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sub_channel_id=None) -> web.Response:
    """get_channel_message_status

    &lt;p&gt;Gets message status for a specified &lt;code&gt;messageId&lt;/code&gt;. Use this API to determine the intermediate status of messages going through channel flow processing. The API provides an alternative to retrieving message status if the event was not received because a client wasn&#39;t connected to a websocket. &lt;/p&gt; &lt;p&gt;Messages can have any one of these statuses.&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;SENT&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Message processed successfully&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;PENDING&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Ongoing processing&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;FAILED&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Processing failed&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;DENIED&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Message denied by the processor&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This API does not return statuses for denied messages, because we don&#39;t store them once the processor denies them. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Only the message sender can invoke this API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel
    :type channel_arn: str
    :param message_id: The ID of the message.
    :type message_id: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call.
    :type x_amz_chime_bearer: str
    :param scope: 
    :type scope: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param sub_channel_id: &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when getting message status in a SubChannel that the user belongs to.&lt;/p&gt; &lt;/note&gt;
    :type sub_channel_id: str

    """
    return web.Response(status=200)


async def get_messaging_session_endpoint(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_messaging_session_endpoint

    The details of the endpoint for the messaging session.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_messaging_streaming_configurations(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_messaging_streaming_configurations

    Retrieves the data streaming configuration for an &lt;code&gt;AppInstance&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html\&quot;&gt;Streaming messaging data&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.

    :param app_instance_arn: The ARN of the streaming configurations.
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


async def list_channel_bans(request: web.Request, channel_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channel_bans

    &lt;p&gt;Lists all the users and bots banned from a particular channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of bans that you want returned.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested bans are returned.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channel_flows(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channel_flows

    Returns a paginated lists of all the channel flows created under a single Chime. This is a developer API.

    :param app_instance_arn: The ARN of the app instance.
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
    :param max_results: The maximum number of channel flows that you want to return.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested channel flows are returned.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channel_memberships(request: web.Request, channel_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type=None, max_results=None, next_token=None, sub_channel_id=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channel_memberships

    &lt;p&gt;Lists all channel memberships in a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;If you want to list the channels to which a specific app instance user belongs, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html\&quot;&gt;ListChannelMembershipsForAppInstanceUser&lt;/a&gt; API.&lt;/p&gt;

    :param channel_arn: The maximum number of channel memberships that you want returned.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param type: The membership type of a user, &lt;code&gt;DEFAULT&lt;/code&gt; or &lt;code&gt;HIDDEN&lt;/code&gt;. Default members are returned as part of &lt;code&gt;ListChannelMemberships&lt;/code&gt; if no type is specified. Hidden members are only returned if the type filter in &lt;code&gt;ListChannelMemberships&lt;/code&gt; equals &lt;code&gt;HIDDEN&lt;/code&gt;.
    :type type: str
    :param max_results: The maximum number of channel memberships that you want returned.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested channel memberships are returned.
    :type next_token: str
    :param sub_channel_id: &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when listing a user&#39;s memberships in a particular sub-channel of an elastic channel.&lt;/p&gt; &lt;/note&gt;
    :type sub_channel_id: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channel_memberships_for_app_instance_user(request: web.Request, x_amz_chime_bearer, scope, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, app_instance_user_arn=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channel_memberships_for_app_instance_user

    &lt;p&gt; Lists all channels that an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; is a part of. Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can call the API with a user ARN that is not their own. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param scope: 
    :type scope: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param app_instance_user_arn: The ARN of the user or bot.
    :type app_instance_user_arn: str
    :param max_results: The maximum number of users that you want returned.
    :type max_results: int
    :param next_token: The token returned from previous API requests until the number of channel memberships is reached.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channel_messages(request: web.Request, channel_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sort_order=None, not_before=None, not_after=None, max_results=None, next_token=None, sub_channel_id=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channel_messages

    &lt;p&gt;List all the messages in a channel. Returns a paginated list of &lt;code&gt;ChannelMessages&lt;/code&gt;. By default, sorted by creation timestamp in descending order.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Redacted messages appear in the results as empty, since they are only redacted, not deleted. Deleted messages do not appear in the results. This action always returns the latest version of an edited message.&lt;/p&gt; &lt;p&gt;Also, the &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param sort_order: The order in which you want messages sorted. Default is Descending, based on time created.
    :type sort_order: str
    :param not_before: The initial or starting time stamp for your requested messages.
    :type not_before: str
    :param not_after: The final or ending time stamp for your requested messages.
    :type not_after: str
    :param max_results: The maximum number of messages that you want returned.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested messages are returned.
    :type next_token: str
    :param sub_channel_id: &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when listing the messages in a SubChannel that the user belongs to.&lt;/p&gt; &lt;/note&gt;
    :type sub_channel_id: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    not_before = util.deserialize_datetime(not_before)
    not_after = util.deserialize_datetime(not_after)
    return web.Response(status=200)


async def list_channel_moderators(request: web.Request, channel_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channel_moderators

    &lt;p&gt;Lists all the moderators for a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of moderators that you want returned.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested moderators are returned.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channels(request: web.Request, app_instance_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, privacy=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channels

    &lt;p&gt;Lists all Channels created under a single Chime App as a paginated list. You can specify filters to narrow results.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Functionality &amp;amp; restrictions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use privacy &#x3D; &lt;code&gt;PUBLIC&lt;/code&gt; to retrieve all public channels in the account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can set privacy &#x3D; &lt;code&gt;PRIVATE&lt;/code&gt; to list the private channels in an account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param privacy: The privacy setting. &lt;code&gt;PUBLIC&lt;/code&gt; retrieves all the public channels. &lt;code&gt;PRIVATE&lt;/code&gt; retrieves private channels. Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can retrieve private channels. 
    :type privacy: str
    :param max_results: The maximum number of channels that you want to return.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested channels are returned.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channels_associated_with_channel_flow(request: web.Request, channel_flow_arn, scope, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channels_associated_with_channel_flow

    Lists all channels associated with a specified channel flow. You can associate a channel flow with multiple channels, but you can only associate a channel with one channel flow. This is a developer API.

    :param channel_flow_arn: The ARN of the channel flow.
    :type channel_flow_arn: str
    :param scope: 
    :type scope: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of channels that you want to return.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested channels are returned.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channels_moderated_by_app_instance_user(request: web.Request, x_amz_chime_bearer, scope, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, app_instance_user_arn=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channels_moderated_by_app_instance_user

    &lt;p&gt;A list of the channels moderated by an &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param scope: 
    :type scope: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param app_instance_user_arn: The ARN of the user or bot in the moderated channel.
    :type app_instance_user_arn: str
    :param max_results: The maximum number of channels in the request.
    :type max_results: int
    :param next_token: The token returned from previous API requests until the number of channels moderated by the user is reached.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_sub_channels(request: web.Request, channel_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_sub_channels

    Lists all the SubChannels in an elastic channel when given a channel ID. Available only to the app instance admins and channel moderators of elastic channels.

    :param channel_arn: The ARN of elastic channel.
    :type channel_arn: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of sub-channels that you want to return.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested sub-channels are returned.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags applied to an Amazon Chime SDK messaging resource.

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


async def put_channel_expiration_settings(request: web.Request, channel_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """put_channel_expiration_settings

    &lt;p&gt;Sets the number of days before the channel is automatically deleted.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A background process deletes expired channels within 6 hours of expiration. Actual deletion times may vary.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Expired channels that have not yet been deleted appear as active, and you can update their expiration settings. The system honors the new settings.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
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
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str

    """
    body = PutChannelExpirationSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def put_channel_membership_preferences(request: web.Request, channel_arn, member_arn, x_amz_chime_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_channel_membership_preferences

    &lt;p&gt;Sets the membership preferences of an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; for the specified channel. The user or bot must be a member of the channel. Only the user or bot who owns the membership can set preferences. Users or bots in the &lt;code&gt;AppInstanceAdmin&lt;/code&gt; and channel moderator roles can&#39;t set preferences for other users. Banned users or bots can&#39;t set membership preferences for the channel from which they are banned.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The x-amz-chime-bearer request header is mandatory. Use the ARN of an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param member_arn: The ARN of the member setting the preferences.
    :type member_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
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
    body = PutChannelMembershipPreferencesRequest.from_dict(body)
    return web.Response(status=200)


async def put_messaging_streaming_configurations(request: web.Request, app_instance_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_messaging_streaming_configurations

    Sets the data streaming configuration for an &lt;code&gt;AppInstance&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html\&quot;&gt;Streaming messaging data&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.

    :param app_instance_arn: The ARN of the streaming configuration.
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
    body = PutMessagingStreamingConfigurationsRequest.from_dict(body)
    return web.Response(status=200)


async def redact_channel_message(request: web.Request, channel_arn, message_id, x_amz_chime_bearer, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """redact_channel_message

    &lt;p&gt;Redacts message content, but not metadata. The message exists in the back end, but the action returns null content, and the state shows as redacted.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel containing the messages that you want to redact.
    :type channel_arn: str
    :param message_id: The ID of the message being redacted.
    :type message_id: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
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
    body = RedactChannelMessageRequest.from_dict(body)
    return web.Response(status=200)


async def search_channels(request: web.Request, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """search_channels

    &lt;p&gt;Allows the &lt;code&gt;ChimeBearer&lt;/code&gt; to search channels by channel members. Users or bots can search across the channels that they belong to. Users in the &lt;code&gt;AppInstanceAdmin&lt;/code&gt; role can search across all channels.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt;

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
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call.
    :type x_amz_chime_bearer: str
    :param max_results: The maximum number of channels that you want returned.
    :type max_results: int
    :param next_token: The token returned from previous API requests until the number of channels is reached.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    body = SearchChannelsRequest.from_dict(body)
    return web.Response(status=200)


async def send_channel_message(request: web.Request, channel_arn, x_amz_chime_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_channel_message

    &lt;p&gt;Sends a message to a particular channel that the member is a part of.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;p&gt;Also, &lt;code&gt;STANDARD&lt;/code&gt; messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CONTROL&lt;/code&gt; messages are limited to 30 bytes and do not contain metadata.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
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
    body = SendChannelMessageRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Applies the specified tags to the specified Amazon Chime SDK messaging resource.

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

    Removes the specified tags from the specified Amazon Chime SDK messaging resource.

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


async def update_channel(request: web.Request, channel_arn, x_amz_chime_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_channel

    &lt;p&gt;Update a channel&#39;s attributes.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Restriction&lt;/b&gt;: You can&#39;t change a channel&#39;s privacy. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
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


async def update_channel_flow(request: web.Request, channel_flow_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_channel_flow

    Updates channel flow attributes. This is a developer API.

    :param channel_flow_arn: The ARN of the channel flow.
    :type channel_flow_arn: str
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
    body = UpdateChannelFlowRequest.from_dict(body)
    return web.Response(status=200)


async def update_channel_message(request: web.Request, channel_arn, message_id, x_amz_chime_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_channel_message

    &lt;p&gt;Updates the content of a message.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param message_id: The ID string of the message being updated.
    :type message_id: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
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
    body = UpdateChannelMessageRequest.from_dict(body)
    return web.Response(status=200)


async def update_channel_read_marker(request: web.Request, channel_arn, x_amz_chime_bearer, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_channel_read_marker

    &lt;p&gt;The details of the time when a user last read messages in a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_chime_bearer: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call.
    :type x_amz_chime_bearer: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
