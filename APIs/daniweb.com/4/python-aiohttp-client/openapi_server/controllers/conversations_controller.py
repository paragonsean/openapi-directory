from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_get_conversations_id import EndpointGetConversationsID
from openapi_server.models.endpoint_get_conversations_id_messages import EndpointGetConversationsIDMessages
from openapi_server.models.endpoint_get_conversations_id_statuses import EndpointGetConversationsIDStatuses
from openapi_server.models.endpoint_get_conversations_statuses import EndpointGetConversationsStatuses
from openapi_server.models.endpoint_patch_conversations_id_statuses import EndpointPatchConversationsIDStatuses
from openapi_server.models.endpoint_post_conversations_id_messages import EndpointPostConversationsIDMessages
from openapi_server.models.endpoint_post_conversations_id_schedules import EndpointPostConversationsIDSchedules
from openapi_server.models.endpoint_post_conversations_id_searches import EndpointPostConversationsIDSearches
from openapi_server.models.endpoint_post_conversations_schedules import EndpointPostConversationsSchedules
from openapi_server.models.endpoint_post_conversations_searches import EndpointPostConversationsSearches
from openapi_server import util


async def conversations_id_messages_get(request: web.Request, id, gt_message_id=None, exclude_self=None, _date=None, bubbled=None, record_seen=None, timeout=None, offset=None, limit=None) -> web.Response:
    """conversations_id_messages_get

    Retrieve the last {limit} messages in the conversation, provided the conversations exist within the current access token&#39;s bubble. If a timeout is 0 or greater, the batch is sorted oldest first. Otherwise, if timeout is a negative number, the transcript is paginated and sorted newest first. Specify a timeout for long polling (which delays the server sending back results for up to n seconds or until results are available, whichever comes first), or default to 0 for immediate results. Optionally record your status as online along with sharing the latest message you&#39;ve seen with the other conversation participant. Optionally specify a gt_message_id to retrieve only messages with an ID greater than that specified (such as greater than the latest message ID received in the last poll). Optionally only poll for messages authored by the other person in the conversation, and echo messages authored by you when sending, for a perceived increase in performance. Optionally only retrieve messages that were posted from within the current access token&#39;s bubble. Optionally specify a date formatted as YYYY-MM-DD to retrieve a transcript of messages from a single day. When record_seen is set to true, the new message count for the conversation is reset to zero.

    :param id: 
    :type id: int
    :param gt_message_id: 
    :type gt_message_id: int
    :param exclude_self: 
    :type exclude_self: bool
    :param _date: 
    :type _date: str
    :param bubbled: 
    :type bubbled: bool
    :param record_seen: 
    :type record_seen: bool
    :param timeout: 
    :type timeout: int
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def conversations_id_messages_post(request: web.Request, id, text_raw, bubbled=None, metadata_0_key=None, metadata_0_privacy=None, metadata_0_values=None, metadata_1_key=None, metadata_1_privacy=None, metadata_1_values=None, metadata_2_key=None, metadata_2_privacy=None, metadata_2_values=None, text_emoticons=None) -> web.Response:
    """conversations_id_messages_post

    Post a message to a conversation that is with a user who exists within the current access token&#39;s bubble. Optionally specify whether emoticons should be parsed into smiley images. Optionally specify whether the message should be bubbled within the app. Additionally, optionally attach a single metadata key/value pair to the message upon submission.

    :param id: 
    :type id: int
    :param text_raw: 
    :type text_raw: str
    :param bubbled: 
    :type bubbled: bool
    :param metadata_0_key: 
    :type metadata_0_key: str
    :param metadata_0_privacy: 
    :type metadata_0_privacy: str
    :param metadata_0_values: 
    :type metadata_0_values: List[str]
    :param metadata_1_key: 
    :type metadata_1_key: str
    :param metadata_1_privacy: 
    :type metadata_1_privacy: str
    :param metadata_1_values: 
    :type metadata_1_values: List[str]
    :param metadata_2_key: 
    :type metadata_2_key: str
    :param metadata_2_privacy: 
    :type metadata_2_privacy: str
    :param metadata_2_values: 
    :type metadata_2_values: List[str]
    :param text_emoticons: 
    :type text_emoticons: bool

    """
    return web.Response(status=200)


async def conversations_id_schedules_post(request: web.Request, id, _date=None, limit=None, offset=None, roll_up=None, sort=None) -> web.Response:
    """conversations_id_schedules_post

    Paginated report of information about messages contributed by conversation and date. Only conversations that exist within the current access token&#39;s bubble are considered in the calculations. Optionally roll up all conversations to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages within the conversation(s).

    :param id: 
    :type id: List[int]
    :param _date: 
    :type _date: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int
    :param roll_up: 
    :type roll_up: bool
    :param sort: 
    :type sort: str

    """
    return web.Response(status=200)


async def conversations_id_searches_post(request: web.Request, id, query, _date=None, gt_message_id=None, limit=None, offset=None) -> web.Response:
    """conversations_id_searches_post

    Fetch messages authored from within specified conversations that match a query string passed in as a search parameter along with their relevancy score.

    :param id: 
    :type id: List[int]
    :param query: 
    :type query: str
    :param _date: 
    :type _date: str
    :param gt_message_id: 
    :type gt_message_id: int
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def conversations_id_statuses_get(request: web.Request, id) -> web.Response:
    """conversations_id_statuses_get

    Status information about your current relationship with one or more conversations you participating in, provided the conversations exist within the current access token&#39;s bubble.

    :param id: 
    :type id: List[int]

    """
    return web.Response(status=200)


async def conversations_id_statuses_patch(request: web.Request, id, archived_status) -> web.Response:
    """conversations_id_statuses_patch

    Archive or unarchive a conversation that is with a user who exists within the same bubble.

    :param id: 
    :type id: int
    :param archived_status: 
    :type archived_status: bool

    """
    return web.Response(status=200)


async def conversations_idget(request: web.Request, id) -> web.Response:
    """conversations_idget

    Fetch an array of conversations. You can only retrieve conversations with users who exist within the current access token&#39;s bubble.

    :param id: 
    :type id: List[int]

    """
    return web.Response(status=200)


async def conversations_schedules_post(request: web.Request, _date=None, limit=None, offset=None, roll_up=None, sort=None) -> web.Response:
    """conversations_schedules_post

    Paginated report of information about messages contributed by conversation and date. Only conversations that exist within the current access token&#39;s bubble are considered in the calculations. Optionally roll up all conversations to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages.

    :param _date: 
    :type _date: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int
    :param roll_up: 
    :type roll_up: bool
    :param sort: 
    :type sort: str

    """
    return web.Response(status=200)


async def conversations_searches_post(request: web.Request, query, _date=None, gt_message_id=None, limit=None, offset=None) -> web.Response:
    """conversations_searches_post

    Fetch messages authored from within the current bubble that match a query string passed in as a search parameter along with their relevancy score.

    :param query: 
    :type query: str
    :param _date: 
    :type _date: str
    :param gt_message_id: 
    :type gt_message_id: int
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def conversations_statuses_get(request: web.Request, filter=None, include_archived=None, bubbled=None, offset=None, limit=None) -> web.Response:
    """conversations_statuses_get

    Retrieve conversations that you are participating in with users who exists within the same bubble, along with your current relationship with the conversations. The user_a / user_b properties of the conversation are populated with as much data as is available if the user is not you. If the user is you, only the id field is populated. There is a separate status endpoint to retrieve relationship information for individual conversations. Optionally filter: &#39;new&#39; to only show conversations with messages you haven&#39;t yet seen; &#39;introductions&#39; to only show conversations where users have introduced themselves to you but nothing more; &#39;unreplied&#39; to only show conversations where you have introduced yourself to other users but nothing more; &#39;notifications&#39; to show all conversations where the other user was the last person to message. Optionally only show conversations engaging within the existing access token&#39;s bubble. This report is limited to your ~500-1000 most recently active conversations you&#39;ve engaged in within current the access token&#39;s bubble.

    :param filter: 
    :type filter: str
    :param include_archived: 
    :type include_archived: bool
    :param bubbled: 
    :type bubbled: bool
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)
