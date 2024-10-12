from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversations_v1_service_service_user_service_user_conversation import ConversationsV1ServiceServiceUserServiceUserConversation
from openapi_server.models.conversations_v1_user_user_conversation import ConversationsV1UserUserConversation
from openapi_server.models.list_service_user_conversation_response import ListServiceUserConversationResponse
from openapi_server.models.list_user_conversation_response import ListUserConversationResponse
from openapi_server.models.service_user_conversation_enum_notification_level import ServiceUserConversationEnumNotificationLevel
from openapi_server.models.user_conversation_enum_notification_level import UserConversationEnumNotificationLevel
from openapi_server import util


async def delete_service_user_conversation(request: web.Request, chat_service_sid, user_sid, conversation_sid) -> web.Response:
    """delete_service_user_conversation

    Delete a specific User Conversation.

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    :type chat_service_sid: str
    :param user_sid: The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource.
    :type user_sid: str
    :param conversation_sid: The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
    :type conversation_sid: str

    """
    return web.Response(status=200)


async def delete_user_conversation(request: web.Request, user_sid, conversation_sid) -> web.Response:
    """delete_user_conversation

    Delete a specific User Conversation.

    :param user_sid: The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource.
    :type user_sid: str
    :param conversation_sid: The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
    :type conversation_sid: str

    """
    return web.Response(status=200)


async def fetch_service_user_conversation(request: web.Request, chat_service_sid, user_sid, conversation_sid) -> web.Response:
    """fetch_service_user_conversation

    Fetch a specific User Conversation.

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    :type chat_service_sid: str
    :param user_sid: The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource.
    :type user_sid: str
    :param conversation_sid: The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
    :type conversation_sid: str

    """
    return web.Response(status=200)


async def fetch_user_conversation(request: web.Request, user_sid, conversation_sid) -> web.Response:
    """fetch_user_conversation

    Fetch a specific User Conversation.

    :param user_sid: The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource.
    :type user_sid: str
    :param conversation_sid: The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
    :type conversation_sid: str

    """
    return web.Response(status=200)


async def list_service_user_conversation(request: web.Request, chat_service_sid, user_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service_user_conversation

    Retrieve a list of all User Conversations for the User.

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    :type chat_service_sid: str
    :param user_sid: The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource.
    :type user_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def list_user_conversation(request: web.Request, user_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_user_conversation

    Retrieve a list of all User Conversations for the User.

    :param user_sid: The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource.
    :type user_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_service_user_conversation(request: web.Request, chat_service_sid, user_sid, conversation_sid, last_read_message_index=None, last_read_timestamp=None, notification_level=None) -> web.Response:
    """update_service_user_conversation

    Update a specific User Conversation.

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    :type chat_service_sid: str
    :param user_sid: The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource.
    :type user_sid: str
    :param conversation_sid: The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
    :type conversation_sid: str
    :param last_read_message_index: The index of the last Message in the Conversation that the Participant has read.
    :type last_read_message_index: int
    :param last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601 format.
    :type last_read_timestamp: str
    :param notification_level: 
    :type notification_level: str

    """
    last_read_timestamp = util.deserialize_datetime(last_read_timestamp)
    return web.Response(status=200)


async def update_user_conversation(request: web.Request, user_sid, conversation_sid, last_read_message_index=None, last_read_timestamp=None, notification_level=None) -> web.Response:
    """update_user_conversation

    Update a specific User Conversation.

    :param user_sid: The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource.
    :type user_sid: str
    :param conversation_sid: The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
    :type conversation_sid: str
    :param last_read_message_index: The index of the last Message in the Conversation that the Participant has read.
    :type last_read_message_index: int
    :param last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601 format.
    :type last_read_timestamp: str
    :param notification_level: 
    :type notification_level: str

    """
    last_read_timestamp = util.deserialize_datetime(last_read_timestamp)
    return web.Response(status=200)
