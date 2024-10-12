from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversation_message_enum_order_type import ConversationMessageEnumOrderType
from openapi_server.models.conversation_message_enum_webhook_enabled_type import ConversationMessageEnumWebhookEnabledType
from openapi_server.models.conversations_v1_conversation_conversation_message import ConversationsV1ConversationConversationMessage
from openapi_server.models.conversations_v1_service_service_conversation_service_conversation_message import ConversationsV1ServiceServiceConversationServiceConversationMessage
from openapi_server.models.list_conversation_message_response import ListConversationMessageResponse
from openapi_server.models.list_service_conversation_message_response import ListServiceConversationMessageResponse
from openapi_server.models.service_conversation_message_enum_order_type import ServiceConversationMessageEnumOrderType
from openapi_server.models.service_conversation_message_enum_webhook_enabled_type import ServiceConversationMessageEnumWebhookEnabledType
from openapi_server import util


async def create_conversation_message(request: web.Request, conversation_sid, x_twilio_webhook_enabled=None, attributes=None, author=None, body=None, content_sid=None, content_variables=None, date_created=None, date_updated=None, media_sid=None, subject=None) -> web.Response:
    """create_conversation_message

    Add a new message to the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :type conversation_sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned.
    :type attributes: str
    :param author: The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;.
    :type author: str
    :param body: The content of the message, can be up to 1,600 characters long.
    :type body: str
    :param content_sid: The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content) template, required for template-generated messages.  **Note** that if this field is set, &#x60;Body&#x60; and &#x60;MediaSid&#x60; parameters are ignored.
    :type content_sid: str
    :param content_variables: A structurally valid JSON string that contains values to resolve Rich Content template variables.
    :type content_variables: str
    :param date_created: The date that this resource was created.
    :type date_created: str
    :param date_updated: The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited.
    :type date_updated: str
    :param media_sid: The Media SID to be attached to the new Message.
    :type media_sid: str
    :param subject: The subject of the message, can be up to 256 characters long.
    :type subject: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def create_service_conversation_message(request: web.Request, chat_service_sid, conversation_sid, x_twilio_webhook_enabled=None, attributes=None, author=None, body=None, content_sid=None, content_variables=None, date_created=None, date_updated=None, media_sid=None, subject=None) -> web.Response:
    """create_service_conversation_message

    Add a new message to the conversation in a specific service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :type conversation_sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned.
    :type attributes: str
    :param author: The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;.
    :type author: str
    :param body: The content of the message, can be up to 1,600 characters long.
    :type body: str
    :param content_sid: The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content) template, required for template-generated messages.  **Note** that if this field is set, &#x60;Body&#x60; and &#x60;MediaSid&#x60; parameters are ignored.
    :type content_sid: str
    :param content_variables: A structurally valid JSON string that contains values to resolve Rich Content template variables.
    :type content_variables: str
    :param date_created: The date that this resource was created.
    :type date_created: str
    :param date_updated: The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited.
    :type date_updated: str
    :param media_sid: The Media SID to be attached to the new Message.
    :type media_sid: str
    :param subject: The subject of the message, can be up to 256 characters long.
    :type subject: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def delete_conversation_message(request: web.Request, conversation_sid, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_conversation_message

    Remove a message from the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

    """
    return web.Response(status=200)


async def delete_service_conversation_message(request: web.Request, chat_service_sid, conversation_sid, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_service_conversation_message

    Remove a message from the conversation

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

    """
    return web.Response(status=200)


async def fetch_conversation_message(request: web.Request, conversation_sid, sid) -> web.Response:
    """fetch_conversation_message

    Fetch a message from the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service_conversation_message(request: web.Request, chat_service_sid, conversation_sid, sid) -> web.Response:
    """fetch_service_conversation_message

    Fetch a message from the conversation

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_conversation_message(request: web.Request, conversation_sid, order=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_conversation_message

    Retrieve a list of all messages in the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages.
    :type conversation_sid: str
    :param order: The sort order of the returned messages. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending), with &#x60;asc&#x60; as the default.
    :type order: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def list_service_conversation_message(request: web.Request, chat_service_sid, conversation_sid, order=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service_conversation_message

    Retrieve a list of all messages in the conversation

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages.
    :type conversation_sid: str
    :param order: The sort order of the returned messages. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending), with &#x60;asc&#x60; as the default.
    :type order: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_conversation_message(request: web.Request, conversation_sid, sid, x_twilio_webhook_enabled=None, attributes=None, author=None, body=None, date_created=None, date_updated=None, subject=None) -> web.Response:
    """update_conversation_message

    Update an existing message in the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned.
    :type attributes: str
    :param author: The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;.
    :type author: str
    :param body: The content of the message, can be up to 1,600 characters long.
    :type body: str
    :param date_created: The date that this resource was created.
    :type date_created: str
    :param date_updated: The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited.
    :type date_updated: str
    :param subject: The subject of the message, can be up to 256 characters long.
    :type subject: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def update_service_conversation_message(request: web.Request, chat_service_sid, conversation_sid, sid, x_twilio_webhook_enabled=None, attributes=None, author=None, body=None, date_created=None, date_updated=None, subject=None) -> web.Response:
    """update_service_conversation_message

    Update an existing message in the conversation

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned.
    :type attributes: str
    :param author: The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;.
    :type author: str
    :param body: The content of the message, can be up to 1,600 characters long.
    :type body: str
    :param date_created: The date that this resource was created.
    :type date_created: str
    :param date_updated: The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited.
    :type date_updated: str
    :param subject: The subject of the message, can be up to 256 characters long.
    :type subject: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)
