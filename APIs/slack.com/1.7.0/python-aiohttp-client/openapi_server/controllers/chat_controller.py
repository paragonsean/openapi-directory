from typing import List, Dict
from aiohttp import web

from openapi_server.models.chat_delete_error_schema import ChatDeleteErrorSchema
from openapi_server.models.chat_delete_scheduled_message_error_schema import ChatDeleteScheduledMessageErrorSchema
from openapi_server.models.chat_delete_scheduled_message_schema import ChatDeleteScheduledMessageSchema
from openapi_server.models.chat_delete_success_schema import ChatDeleteSuccessSchema
from openapi_server.models.chat_get_permalink_error_schema import ChatGetPermalinkErrorSchema
from openapi_server.models.chat_get_permalink_success_schema import ChatGetPermalinkSuccessSchema
from openapi_server.models.chat_me_message_error_schema import ChatMeMessageErrorSchema
from openapi_server.models.chat_me_message_schema import ChatMeMessageSchema
from openapi_server.models.chat_post_ephemeral_error_schema import ChatPostEphemeralErrorSchema
from openapi_server.models.chat_post_ephemeral_success_schema import ChatPostEphemeralSuccessSchema
from openapi_server.models.chat_post_message_error_schema import ChatPostMessageErrorSchema
from openapi_server.models.chat_post_message_success_schema import ChatPostMessageSuccessSchema
from openapi_server.models.chat_schedule_message_error_schema import ChatScheduleMessageErrorSchema
from openapi_server.models.chat_schedule_message_success_schema import ChatScheduleMessageSuccessSchema
from openapi_server.models.chat_scheduled_messages_list_error_schema import ChatScheduledMessagesListErrorSchema
from openapi_server.models.chat_scheduled_messages_list_schema import ChatScheduledMessagesListSchema
from openapi_server.models.chat_unfurl_error_schema import ChatUnfurlErrorSchema
from openapi_server.models.chat_unfurl_success_schema import ChatUnfurlSuccessSchema
from openapi_server.models.chat_update_error_schema import ChatUpdateErrorSchema
from openapi_server.models.chat_update_success_schema import ChatUpdateSuccessSchema
from openapi_server import util


async def chat_delete(request: web.Request, token=None, as_user=None, channel=None, ts=None) -> web.Response:
    """chat_delete

    Deletes a message.

    :param token: Authentication token. Requires scope: &#x60;chat:write&#x60;
    :type token: str
    :param as_user: Pass true to delete the message as the authed user with &#x60;chat:write:user&#x60; scope. [Bot users](/bot-users) in this context are considered authed users. If unused or false, the message will be deleted with &#x60;chat:write:bot&#x60; scope.
    :type as_user: bool
    :param channel: Channel containing the message to be deleted.
    :type channel: str
    :param ts: Timestamp of the message to be deleted.
    :type ts: 

    """
    return web.Response(status=200)


async def chat_delete_scheduled_message(request: web.Request, token, channel, scheduled_message_id, as_user=None) -> web.Response:
    """chat_delete_scheduled_message

    Deletes a pending scheduled message from the queue.

    :param token: Authentication token. Requires scope: &#x60;chat:write&#x60;
    :type token: str
    :param channel: The channel the scheduled_message is posting to
    :type channel: str
    :param scheduled_message_id: &#x60;scheduled_message_id&#x60; returned from call to chat.scheduleMessage
    :type scheduled_message_id: str
    :param as_user: Pass true to delete the message as the authed user with &#x60;chat:write:user&#x60; scope. [Bot users](/bot-users) in this context are considered authed users. If unused or false, the message will be deleted with &#x60;chat:write:bot&#x60; scope.
    :type as_user: bool

    """
    return web.Response(status=200)


async def chat_get_permalink(request: web.Request, token, channel, message_ts) -> web.Response:
    """chat_get_permalink

    Retrieve a permalink URL for a specific extant message

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param channel: The ID of the conversation or channel containing the message
    :type channel: str
    :param message_ts: A message&#39;s &#x60;ts&#x60; value, uniquely identifying it within a channel
    :type message_ts: str

    """
    return web.Response(status=200)


async def chat_me_message(request: web.Request, token=None, channel=None, text=None) -> web.Response:
    """chat_me_message

    Share a me message into a channel.

    :param token: Authentication token. Requires scope: &#x60;chat:write&#x60;
    :type token: str
    :param channel: Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded ID, or a name.
    :type channel: str
    :param text: Text of the message to send.
    :type text: str

    """
    return web.Response(status=200)


async def chat_post_ephemeral(request: web.Request, token, channel, user, as_user=None, attachments=None, blocks=None, icon_emoji=None, icon_url=None, link_names=None, parse=None, text=None, thread_ts=None, username=None) -> web.Response:
    """chat_post_ephemeral

    Sends an ephemeral message to a user in a channel.

    :param token: Authentication token. Requires scope: &#x60;chat:write&#x60;
    :type token: str
    :param channel: Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name.
    :type channel: str
    :param user: &#x60;id&#x60; of the user who will receive the ephemeral message. The user should be in the channel specified by the &#x60;channel&#x60; argument.
    :type user: str
    :param as_user: Pass true to post the message as the authed user. Defaults to true if the chat:write:bot scope is not included. Otherwise, defaults to false.
    :type as_user: bool
    :param attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
    :type attachments: str
    :param blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
    :type blocks: str
    :param icon_emoji: Emoji to use as the icon for this message. Overrides &#x60;icon_url&#x60;. Must be used in conjunction with &#x60;as_user&#x60; set to &#x60;false&#x60;, otherwise ignored. See [authorship](#authorship) below.
    :type icon_emoji: str
    :param icon_url: URL to an image to use as the icon for this message. Must be used in conjunction with &#x60;as_user&#x60; set to false, otherwise ignored. See [authorship](#authorship) below.
    :type icon_url: str
    :param link_names: Find and link channel names and usernames.
    :type link_names: bool
    :param parse: Change how messages are treated. Defaults to &#x60;none&#x60;. See [below](#formatting).
    :type parse: str
    :param text: How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.
    :type text: str
    :param thread_ts: Provide another message&#39;s &#x60;ts&#x60; value to post this message in a thread. Avoid using a reply&#39;s &#x60;ts&#x60; value; use its parent&#39;s value instead. Ephemeral messages in threads are only shown if there is already an active thread.
    :type thread_ts: str
    :param username: Set your bot&#39;s user name. Must be used in conjunction with &#x60;as_user&#x60; set to false, otherwise ignored. See [authorship](#authorship) below.
    :type username: str

    """
    return web.Response(status=200)


async def chat_post_message(request: web.Request, token, channel, as_user=None, attachments=None, blocks=None, icon_emoji=None, icon_url=None, link_names=None, mrkdwn=None, parse=None, reply_broadcast=None, text=None, thread_ts=None, unfurl_links=None, unfurl_media=None, username=None) -> web.Response:
    """chat_post_message

    Sends a message to a channel.

    :param token: Authentication token. Requires scope: &#x60;chat:write&#x60;
    :type token: str
    :param channel: Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See [below](#channels) for more details.
    :type channel: str
    :param as_user: Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [authorship](#authorship) below.
    :type as_user: str
    :param attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
    :type attachments: str
    :param blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
    :type blocks: str
    :param icon_emoji: Emoji to use as the icon for this message. Overrides &#x60;icon_url&#x60;. Must be used in conjunction with &#x60;as_user&#x60; set to &#x60;false&#x60;, otherwise ignored. See [authorship](#authorship) below.
    :type icon_emoji: str
    :param icon_url: URL to an image to use as the icon for this message. Must be used in conjunction with &#x60;as_user&#x60; set to false, otherwise ignored. See [authorship](#authorship) below.
    :type icon_url: str
    :param link_names: Find and link channel names and usernames.
    :type link_names: bool
    :param mrkdwn: Disable Slack markup parsing by setting to &#x60;false&#x60;. Enabled by default.
    :type mrkdwn: bool
    :param parse: Change how messages are treated. Defaults to &#x60;none&#x60;. See [below](#formatting).
    :type parse: str
    :param reply_broadcast: Used in conjunction with &#x60;thread_ts&#x60; and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to &#x60;false&#x60;.
    :type reply_broadcast: bool
    :param text: How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.
    :type text: str
    :param thread_ts: Provide another message&#39;s &#x60;ts&#x60; value to make this message a reply. Avoid using a reply&#39;s &#x60;ts&#x60; value; use its parent instead.
    :type thread_ts: str
    :param unfurl_links: Pass true to enable unfurling of primarily text-based content.
    :type unfurl_links: bool
    :param unfurl_media: Pass false to disable unfurling of media content.
    :type unfurl_media: bool
    :param username: Set your bot&#39;s user name. Must be used in conjunction with &#x60;as_user&#x60; set to false, otherwise ignored. See [authorship](#authorship) below.
    :type username: str

    """
    return web.Response(status=200)


async def chat_schedule_message(request: web.Request, token=None, as_user=None, attachments=None, blocks=None, channel=None, link_names=None, parse=None, post_at=None, reply_broadcast=None, text=None, thread_ts=None, unfurl_links=None, unfurl_media=None) -> web.Response:
    """chat_schedule_message

    Schedules a message to be sent to a channel.

    :param token: Authentication token. Requires scope: &#x60;chat:write&#x60;
    :type token: str
    :param as_user: Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [chat.postMessage](chat.postMessage#authorship).
    :type as_user: bool
    :param attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
    :type attachments: str
    :param blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
    :type blocks: str
    :param channel: Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See [below](#channels) for more details.
    :type channel: str
    :param link_names: Find and link channel names and usernames.
    :type link_names: bool
    :param parse: Change how messages are treated. Defaults to &#x60;none&#x60;. See [chat.postMessage](chat.postMessage#formatting).
    :type parse: str
    :param post_at: Unix EPOCH timestamp of time in future to send the message.
    :type post_at: str
    :param reply_broadcast: Used in conjunction with &#x60;thread_ts&#x60; and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to &#x60;false&#x60;.
    :type reply_broadcast: bool
    :param text: How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.
    :type text: str
    :param thread_ts: Provide another message&#39;s &#x60;ts&#x60; value to make this message a reply. Avoid using a reply&#39;s &#x60;ts&#x60; value; use its parent instead.
    :type thread_ts: 
    :param unfurl_links: Pass true to enable unfurling of primarily text-based content.
    :type unfurl_links: bool
    :param unfurl_media: Pass false to disable unfurling of media content.
    :type unfurl_media: bool

    """
    return web.Response(status=200)


async def chat_scheduled_messages_list_0(request: web.Request, token=None, channel=None, latest=None, oldest=None, limit=None, cursor=None) -> web.Response:
    """chat_scheduled_messages_list_0

    Returns a list of scheduled messages.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param channel: The channel of the scheduled messages
    :type channel: str
    :param latest: A UNIX timestamp of the latest value in the time range
    :type latest: 
    :param oldest: A UNIX timestamp of the oldest value in the time range
    :type oldest: 
    :param limit: Maximum number of original entries to return.
    :type limit: int
    :param cursor: For pagination purposes, this is the &#x60;cursor&#x60; value returned from a previous call to &#x60;chat.scheduledmessages.list&#x60; indicating where you want to start this call from.
    :type cursor: str

    """
    return web.Response(status=200)


async def chat_unfurl(request: web.Request, token, channel, ts, unfurls=None, user_auth_message=None, user_auth_required=None, user_auth_url=None) -> web.Response:
    """chat_unfurl

    Provide custom unfurl behavior for user-posted URLs

    :param token: Authentication token. Requires scope: &#x60;links:write&#x60;
    :type token: str
    :param channel: Channel ID of the message
    :type channel: str
    :param ts: Timestamp of the message to add unfurl behavior to.
    :type ts: str
    :param unfurls: URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl blocks or message attachments.
    :type unfurls: str
    :param user_auth_message: Provide a simply-formatted string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior
    :type user_auth_message: str
    :param user_auth_required: Set to &#x60;true&#x60; or &#x60;1&#x60; to indicate the user must install your Slack app to trigger unfurls for this domain
    :type user_auth_required: bool
    :param user_auth_url: Send users to this custom URL where they will complete authentication in your app to fully trigger unfurling. Value should be properly URL-encoded.
    :type user_auth_url: str

    """
    return web.Response(status=200)


async def chat_update(request: web.Request, token, channel, ts, as_user=None, attachments=None, blocks=None, link_names=None, parse=None, text=None) -> web.Response:
    """chat_update

    Updates a message.

    :param token: Authentication token. Requires scope: &#x60;chat:write&#x60;
    :type token: str
    :param channel: Channel containing the message to be updated.
    :type channel: str
    :param ts: Timestamp of the message to be updated.
    :type ts: str
    :param as_user: Pass true to update the message as the authed user. [Bot users](/bot-users) in this context are considered authed users.
    :type as_user: str
    :param attachments: A JSON-based array of structured attachments, presented as a URL-encoded string. This field is required when not presenting &#x60;text&#x60;. If you don&#39;t include this field, the message&#39;s previous &#x60;attachments&#x60; will be retained. To remove previous &#x60;attachments&#x60;, include an empty array for this field.
    :type attachments: str
    :param blocks: A JSON-based array of [structured blocks](/block-kit/building), presented as a URL-encoded string. If you don&#39;t include this field, the message&#39;s previous &#x60;blocks&#x60; will be retained. To remove previous &#x60;blocks&#x60;, include an empty array for this field.
    :type blocks: str
    :param link_names: Find and link channel names and usernames. Defaults to &#x60;none&#x60;. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, &#x60;none&#x60;.
    :type link_names: str
    :param parse: Change how messages are treated. Defaults to &#x60;client&#x60;, unlike &#x60;chat.postMessage&#x60;. Accepts either &#x60;none&#x60; or &#x60;full&#x60;. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, &#x60;client&#x60;.
    :type parse: str
    :param text: New text for the message, using the [default formatting rules](/reference/surfaces/formatting). It&#39;s not required when presenting &#x60;blocks&#x60; or &#x60;attachments&#x60;.
    :type text: str

    """
    return web.Response(status=200)
