from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversations_archive_error_schema import ConversationsArchiveErrorSchema
from openapi_server.models.conversations_archive_success_schema import ConversationsArchiveSuccessSchema
from openapi_server.models.conversations_close_error_schema import ConversationsCloseErrorSchema
from openapi_server.models.conversations_close_success_schema import ConversationsCloseSuccessSchema
from openapi_server.models.conversations_create_error_schema import ConversationsCreateErrorSchema
from openapi_server.models.conversations_create_success_schema import ConversationsCreateSuccessSchema
from openapi_server.models.conversations_history_error_schema import ConversationsHistoryErrorSchema
from openapi_server.models.conversations_history_success_schema import ConversationsHistorySuccessSchema
from openapi_server.models.conversations_info_error_schema import ConversationsInfoErrorSchema
from openapi_server.models.conversations_info_success_schema import ConversationsInfoSuccessSchema
from openapi_server.models.conversations_invite_error_schema import ConversationsInviteErrorSchema
from openapi_server.models.conversations_invite_error_schema1 import ConversationsInviteErrorSchema1
from openapi_server.models.conversations_join_error_schema import ConversationsJoinErrorSchema
from openapi_server.models.conversations_join_success_schema import ConversationsJoinSuccessSchema
from openapi_server.models.conversations_kick_error_schema import ConversationsKickErrorSchema
from openapi_server.models.conversations_kick_success_schema import ConversationsKickSuccessSchema
from openapi_server.models.conversations_leave_error_schema import ConversationsLeaveErrorSchema
from openapi_server.models.conversations_leave_success_schema import ConversationsLeaveSuccessSchema
from openapi_server.models.conversations_list_error_schema import ConversationsListErrorSchema
from openapi_server.models.conversations_list_success_schema import ConversationsListSuccessSchema
from openapi_server.models.conversations_mark_error_schema import ConversationsMarkErrorSchema
from openapi_server.models.conversations_mark_success_schema import ConversationsMarkSuccessSchema
from openapi_server.models.conversations_members_error_schema import ConversationsMembersErrorSchema
from openapi_server.models.conversations_members_success_schema import ConversationsMembersSuccessSchema
from openapi_server.models.conversations_open_error_schema import ConversationsOpenErrorSchema
from openapi_server.models.conversations_open_success_schema import ConversationsOpenSuccessSchema
from openapi_server.models.conversations_rename_error_schema import ConversationsRenameErrorSchema
from openapi_server.models.conversations_rename_success_schema import ConversationsRenameSuccessSchema
from openapi_server.models.conversations_replies_error_schema import ConversationsRepliesErrorSchema
from openapi_server.models.conversations_replies_success_schema import ConversationsRepliesSuccessSchema
from openapi_server.models.conversations_set_purpose_error_schema import ConversationsSetPurposeErrorSchema
from openapi_server.models.conversations_set_purpose_success_schema import ConversationsSetPurposeSuccessSchema
from openapi_server.models.conversations_set_topic_error_schema import ConversationsSetTopicErrorSchema
from openapi_server.models.conversations_set_topic_success_schema import ConversationsSetTopicSuccessSchema
from openapi_server.models.conversations_unarchive_error_schema import ConversationsUnarchiveErrorSchema
from openapi_server.models.conversations_unarchive_success_schema import ConversationsUnarchiveSuccessSchema
from openapi_server import util


async def conversations_archive(request: web.Request, token=None, channel=None) -> web.Response:
    """conversations_archive

    Archives a conversation.

    :param token: Authentication token. Requires scope: &#x60;conversations:write&#x60;
    :type token: str
    :param channel: ID of conversation to archive
    :type channel: str

    """
    return web.Response(status=200)


async def conversations_close(request: web.Request, token=None, channel=None) -> web.Response:
    """conversations_close

    Closes a direct message or multi-person direct message.

    :param token: Authentication token. Requires scope: &#x60;conversations:write&#x60;
    :type token: str
    :param channel: Conversation to close.
    :type channel: str

    """
    return web.Response(status=200)


async def conversations_create(request: web.Request, token=None, is_private=None, name=None) -> web.Response:
    """conversations_create

    Initiates a public or private channel-based conversation

    :param token: Authentication token. Requires scope: &#x60;conversations:write&#x60;
    :type token: str
    :param is_private: Create a private channel instead of a public one
    :type is_private: bool
    :param name: Name of the public or private channel to create
    :type name: str

    """
    return web.Response(status=200)


async def conversations_history(request: web.Request, token=None, channel=None, latest=None, oldest=None, inclusive=None, limit=None, cursor=None) -> web.Response:
    """conversations_history

    Fetches a conversation&#39;s history of messages and events.

    :param token: Authentication token. Requires scope: &#x60;conversations:history&#x60;
    :type token: str
    :param channel: Conversation ID to fetch history for.
    :type channel: str
    :param latest: End of time range of messages to include in results.
    :type latest: 
    :param oldest: Start of time range of messages to include in results.
    :type oldest: 
    :param inclusive: Include messages with latest or oldest timestamp in results only when either timestamp is specified.
    :type inclusive: bool
    :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn&#39;t been reached.
    :type limit: int
    :param cursor: Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail.
    :type cursor: str

    """
    return web.Response(status=200)


async def conversations_info(request: web.Request, token=None, channel=None, include_locale=None, include_num_members=None) -> web.Response:
    """conversations_info

    Retrieve information about a conversation.

    :param token: Authentication token. Requires scope: &#x60;conversations:read&#x60;
    :type token: str
    :param channel: Conversation ID to learn more about
    :type channel: str
    :param include_locale: Set this to &#x60;true&#x60; to receive the locale for this conversation. Defaults to &#x60;false&#x60;
    :type include_locale: bool
    :param include_num_members: Set to &#x60;true&#x60; to include the member count for the specified conversation. Defaults to &#x60;false&#x60;
    :type include_num_members: bool

    """
    return web.Response(status=200)


async def conversations_invite(request: web.Request, token=None, channel=None, users=None) -> web.Response:
    """conversations_invite

    Invites users to a channel.

    :param token: Authentication token. Requires scope: &#x60;conversations:write&#x60;
    :type token: str
    :param channel: The ID of the public or private channel to invite user(s) to.
    :type channel: str
    :param users: A comma separated list of user IDs. Up to 1000 users may be listed.
    :type users: str

    """
    return web.Response(status=200)


async def conversations_join(request: web.Request, token=None, channel=None) -> web.Response:
    """conversations_join

    Joins an existing conversation.

    :param token: Authentication token. Requires scope: &#x60;channels:write&#x60;
    :type token: str
    :param channel: ID of conversation to join
    :type channel: str

    """
    return web.Response(status=200)


async def conversations_kick(request: web.Request, token=None, channel=None, user=None) -> web.Response:
    """conversations_kick

    Removes a user from a conversation.

    :param token: Authentication token. Requires scope: &#x60;conversations:write&#x60;
    :type token: str
    :param channel: ID of conversation to remove user from.
    :type channel: str
    :param user: User ID to be removed.
    :type user: str

    """
    return web.Response(status=200)


async def conversations_leave(request: web.Request, token=None, channel=None) -> web.Response:
    """conversations_leave

    Leaves a conversation.

    :param token: Authentication token. Requires scope: &#x60;conversations:write&#x60;
    :type token: str
    :param channel: Conversation to leave
    :type channel: str

    """
    return web.Response(status=200)


async def conversations_list(request: web.Request, token=None, exclude_archived=None, types=None, limit=None, cursor=None) -> web.Response:
    """conversations_list

    Lists all channels in a Slack team.

    :param token: Authentication token. Requires scope: &#x60;conversations:read&#x60;
    :type token: str
    :param exclude_archived: Set to &#x60;true&#x60; to exclude archived channels from the list
    :type exclude_archived: bool
    :param types: Mix and match channel types by providing a comma-separated list of any combination of &#x60;public_channel&#x60;, &#x60;private_channel&#x60;, &#x60;mpim&#x60;, &#x60;im&#x60;
    :type types: str
    :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached. Must be an integer no larger than 1000.
    :type limit: int
    :param cursor: Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail.
    :type cursor: str

    """
    return web.Response(status=200)


async def conversations_mark(request: web.Request, token=None, channel=None, ts=None) -> web.Response:
    """conversations_mark

    Sets the read cursor in a channel.

    :param token: Authentication token. Requires scope: &#x60;conversations:write&#x60;
    :type token: str
    :param channel: Channel or conversation to set the read cursor for.
    :type channel: str
    :param ts: Unique identifier of message you want marked as most recently seen in this conversation.
    :type ts: 

    """
    return web.Response(status=200)


async def conversations_members(request: web.Request, token=None, channel=None, limit=None, cursor=None) -> web.Response:
    """conversations_members

    Retrieve members of a conversation.

    :param token: Authentication token. Requires scope: &#x60;conversations:read&#x60;
    :type token: str
    :param channel: ID of the conversation to retrieve members for
    :type channel: str
    :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn&#39;t been reached.
    :type limit: int
    :param cursor: Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail.
    :type cursor: str

    """
    return web.Response(status=200)


async def conversations_open(request: web.Request, token=None, channel=None, return_im=None, users=None) -> web.Response:
    """conversations_open

    Opens or resumes a direct message or multi-person direct message.

    :param token: Authentication token. Requires scope: &#x60;conversations:write&#x60;
    :type token: str
    :param channel: Resume a conversation by supplying an &#x60;im&#x60; or &#x60;mpim&#x60;&#39;s ID. Or provide the &#x60;users&#x60; field instead.
    :type channel: str
    :param return_im: Boolean, indicates you want the full IM channel definition in the response.
    :type return_im: bool
    :param users: Comma separated lists of users. If only one user is included, this creates a 1:1 DM.  The ordering of the users is preserved whenever a multi-person direct message is returned. Supply a &#x60;channel&#x60; when not supplying &#x60;users&#x60;.
    :type users: str

    """
    return web.Response(status=200)


async def conversations_rename(request: web.Request, token=None, channel=None, name=None) -> web.Response:
    """conversations_rename

    Renames a conversation.

    :param token: Authentication token. Requires scope: &#x60;conversations:write&#x60;
    :type token: str
    :param channel: ID of conversation to rename
    :type channel: str
    :param name: New name for conversation.
    :type name: str

    """
    return web.Response(status=200)


async def conversations_replies(request: web.Request, token=None, channel=None, ts=None, latest=None, oldest=None, inclusive=None, limit=None, cursor=None) -> web.Response:
    """conversations_replies

    Retrieve a thread of messages posted to a conversation

    :param token: Authentication token. Requires scope: &#x60;conversations:history&#x60;
    :type token: str
    :param channel: Conversation ID to fetch thread from.
    :type channel: str
    :param ts: Unique identifier of a thread&#39;s parent message. &#x60;ts&#x60; must be the timestamp of an existing message with 0 or more replies. If there are no replies then just the single message referenced by &#x60;ts&#x60; will return - it is just an ordinary, unthreaded message.
    :type ts: 
    :param latest: End of time range of messages to include in results.
    :type latest: 
    :param oldest: Start of time range of messages to include in results.
    :type oldest: 
    :param inclusive: Include messages with latest or oldest timestamp in results only when either timestamp is specified.
    :type inclusive: bool
    :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn&#39;t been reached.
    :type limit: int
    :param cursor: Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail.
    :type cursor: str

    """
    return web.Response(status=200)


async def conversations_set_purpose(request: web.Request, token=None, channel=None, purpose=None) -> web.Response:
    """conversations_set_purpose

    Sets the purpose for a conversation.

    :param token: Authentication token. Requires scope: &#x60;conversations:write&#x60;
    :type token: str
    :param channel: Conversation to set the purpose of
    :type channel: str
    :param purpose: A new, specialer purpose
    :type purpose: str

    """
    return web.Response(status=200)


async def conversations_set_topic(request: web.Request, token=None, channel=None, topic=None) -> web.Response:
    """conversations_set_topic

    Sets the topic for a conversation.

    :param token: Authentication token. Requires scope: &#x60;conversations:write&#x60;
    :type token: str
    :param channel: Conversation to set the topic of
    :type channel: str
    :param topic: The new topic string. Does not support formatting or linkification.
    :type topic: str

    """
    return web.Response(status=200)


async def conversations_unarchive(request: web.Request, token=None, channel=None) -> web.Response:
    """conversations_unarchive

    Reverses conversation archival.

    :param token: Authentication token. Requires scope: &#x60;conversations:write&#x60;
    :type token: str
    :param channel: ID of conversation to unarchive
    :type channel: str

    """
    return web.Response(status=200)
