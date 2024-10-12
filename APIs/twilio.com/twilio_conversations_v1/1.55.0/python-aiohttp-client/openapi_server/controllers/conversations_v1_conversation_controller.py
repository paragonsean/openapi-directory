from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversation_enum_state import ConversationEnumState
from openapi_server.models.conversation_enum_webhook_enabled_type import ConversationEnumWebhookEnabledType
from openapi_server.models.conversations_v1_conversation import ConversationsV1Conversation
from openapi_server.models.conversations_v1_service_service_conversation import ConversationsV1ServiceServiceConversation
from openapi_server.models.list_conversation_response import ListConversationResponse
from openapi_server.models.list_service_conversation_response import ListServiceConversationResponse
from openapi_server.models.service_conversation_enum_state import ServiceConversationEnumState
from openapi_server.models.service_conversation_enum_webhook_enabled_type import ServiceConversationEnumWebhookEnabledType
from openapi_server import util


async def create_conversation(request: web.Request, x_twilio_webhook_enabled=None, attributes=None, bindings_email_address=None, bindings_email_name=None, date_created=None, date_updated=None, friendly_name=None, messaging_service_sid=None, state=None, timers_closed=None, timers_inactive=None, unique_name=None) -> web.Response:
    """create_conversation

    Create a new conversation in your account&#39;s default service

    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned.
    :type attributes: str
    :param bindings_email_address: The default email address that will be used when sending outbound emails in this conversation.
    :type bindings_email_address: str
    :param bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
    :type bindings_email_name: str
    :param date_created: The date that this resource was created.
    :type date_created: str
    :param date_updated: The date that this resource was last updated.
    :type date_updated: str
    :param friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
    :type friendly_name: str
    :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to.
    :type messaging_service_sid: str
    :param state: 
    :type state: str
    :param timers_closed: ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes.
    :type timers_closed: str
    :param timers_inactive: ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute.
    :type timers_inactive: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL.
    :type unique_name: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def create_service_conversation(request: web.Request, chat_service_sid, x_twilio_webhook_enabled=None, attributes=None, bindings_email_address=None, bindings_email_name=None, date_created=None, date_updated=None, friendly_name=None, messaging_service_sid=None, state=None, timers_closed=None, timers_inactive=None, unique_name=None) -> web.Response:
    """create_service_conversation

    Create a new conversation in your service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    :type chat_service_sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned.
    :type attributes: str
    :param bindings_email_address: The default email address that will be used when sending outbound emails in this conversation.
    :type bindings_email_address: str
    :param bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
    :type bindings_email_name: str
    :param date_created: The date that this resource was created.
    :type date_created: str
    :param date_updated: The date that this resource was last updated.
    :type date_updated: str
    :param friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
    :type friendly_name: str
    :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to.
    :type messaging_service_sid: str
    :param state: 
    :type state: str
    :param timers_closed: ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes.
    :type timers_closed: str
    :param timers_inactive: ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute.
    :type timers_inactive: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL.
    :type unique_name: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def delete_conversation(request: web.Request, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_conversation

    Remove a conversation from your account&#39;s default service

    :param sid: A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

    """
    return web.Response(status=200)


async def delete_service_conversation(request: web.Request, chat_service_sid, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_service_conversation

    Remove a conversation from your service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    :type chat_service_sid: str
    :param sid: A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

    """
    return web.Response(status=200)


async def fetch_conversation(request: web.Request, sid) -> web.Response:
    """fetch_conversation

    Fetch a conversation from your account&#39;s default service

    :param sid: A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service_conversation(request: web.Request, chat_service_sid, sid) -> web.Response:
    """fetch_service_conversation

    Fetch a conversation from your service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    :type chat_service_sid: str
    :param sid: A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation.
    :type sid: str

    """
    return web.Response(status=200)


async def list_conversation(request: web.Request, start_date=None, end_date=None, state=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_conversation

    Retrieve a list of conversations in your account&#39;s default service

    :param start_date: Start date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the start time of the date is used (YYYY-MM-DDT00:00:00Z). Can be combined with other filters.
    :type start_date: str
    :param end_date: End date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the end time of the date is used (YYYY-MM-DDT23:59:59Z). Can be combined with other filters.
    :type end_date: str
    :param state: State for sorting and filtering list of Conversations. Can be &#x60;active&#x60;, &#x60;inactive&#x60; or &#x60;closed&#x60;
    :type state: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def list_service_conversation(request: web.Request, chat_service_sid, start_date=None, end_date=None, state=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service_conversation

    Retrieve a list of conversations in your service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    :type chat_service_sid: str
    :param start_date: Start date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the start time of the date is used (YYYY-MM-DDT00:00:00Z). Can be combined with other filters.
    :type start_date: str
    :param end_date: End date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the end time of the date is used (YYYY-MM-DDT23:59:59Z). Can be combined with other filters.
    :type end_date: str
    :param state: State for sorting and filtering list of Conversations. Can be &#x60;active&#x60;, &#x60;inactive&#x60; or &#x60;closed&#x60;
    :type state: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_conversation(request: web.Request, sid, x_twilio_webhook_enabled=None, attributes=None, bindings_email_address=None, bindings_email_name=None, date_created=None, date_updated=None, friendly_name=None, messaging_service_sid=None, state=None, timers_closed=None, timers_inactive=None, unique_name=None) -> web.Response:
    """update_conversation

    Update an existing conversation in your account&#39;s default service

    :param sid: A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned.
    :type attributes: str
    :param bindings_email_address: The default email address that will be used when sending outbound emails in this conversation.
    :type bindings_email_address: str
    :param bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
    :type bindings_email_name: str
    :param date_created: The date that this resource was created.
    :type date_created: str
    :param date_updated: The date that this resource was last updated.
    :type date_updated: str
    :param friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
    :type friendly_name: str
    :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to.
    :type messaging_service_sid: str
    :param state: 
    :type state: str
    :param timers_closed: ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes.
    :type timers_closed: str
    :param timers_inactive: ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute.
    :type timers_inactive: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL.
    :type unique_name: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def update_service_conversation(request: web.Request, chat_service_sid, sid, x_twilio_webhook_enabled=None, attributes=None, bindings_email_address=None, bindings_email_name=None, date_created=None, date_updated=None, friendly_name=None, messaging_service_sid=None, state=None, timers_closed=None, timers_inactive=None, unique_name=None) -> web.Response:
    """update_service_conversation

    Update an existing conversation in your service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    :type chat_service_sid: str
    :param sid: A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned.
    :type attributes: str
    :param bindings_email_address: The default email address that will be used when sending outbound emails in this conversation.
    :type bindings_email_address: str
    :param bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
    :type bindings_email_name: str
    :param date_created: The date that this resource was created.
    :type date_created: str
    :param date_updated: The date that this resource was last updated.
    :type date_updated: str
    :param friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
    :type friendly_name: str
    :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to.
    :type messaging_service_sid: str
    :param state: 
    :type state: str
    :param timers_closed: ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes.
    :type timers_closed: str
    :param timers_inactive: ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute.
    :type timers_inactive: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL.
    :type unique_name: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)
