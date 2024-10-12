from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversation_participant_enum_webhook_enabled_type import ConversationParticipantEnumWebhookEnabledType
from openapi_server.models.conversations_v1_conversation_conversation_participant import ConversationsV1ConversationConversationParticipant
from openapi_server.models.conversations_v1_service_service_conversation_service_conversation_participant import ConversationsV1ServiceServiceConversationServiceConversationParticipant
from openapi_server.models.list_conversation_participant_response import ListConversationParticipantResponse
from openapi_server.models.list_service_conversation_participant_response import ListServiceConversationParticipantResponse
from openapi_server.models.service_conversation_participant_enum_webhook_enabled_type import ServiceConversationParticipantEnumWebhookEnabledType
from openapi_server import util


async def create_conversation_participant(request: web.Request, conversation_sid, x_twilio_webhook_enabled=None, attributes=None, date_created=None, date_updated=None, identity=None, messaging_binding_address=None, messaging_binding_projected_address=None, messaging_binding_proxy_address=None, role_sid=None) -> web.Response:
    """create_conversation_participant

    Add a new participant to the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    :type conversation_sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned.
    :type attributes: str
    :param date_created: The date that this resource was created.
    :type date_created: str
    :param date_updated: The date that this resource was last updated.
    :type date_updated: str
    :param identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
    :type identity: str
    :param messaging_binding_address: The address of the participant&#39;s device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with proxy_address) is only null when the participant is interacting from an SDK endpoint (see the &#39;identity&#39; field).
    :type messaging_binding_address: str
    :param messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS. Communication mask for the Conversation participant with Identity.
    :type messaging_binding_projected_address: str
    :param messaging_binding_proxy_address: The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the &#39;identity&#39; field).
    :type messaging_binding_proxy_address: str
    :param role_sid: The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
    :type role_sid: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def create_service_conversation_participant(request: web.Request, chat_service_sid, conversation_sid, x_twilio_webhook_enabled=None, attributes=None, date_created=None, date_updated=None, identity=None, messaging_binding_address=None, messaging_binding_projected_address=None, messaging_binding_proxy_address=None, role_sid=None) -> web.Response:
    """create_service_conversation_participant

    Add a new participant to the conversation in a specific service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    :type conversation_sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set &#x60;{}&#x60; will be returned.
    :type attributes: str
    :param date_created: The date on which this resource was created.
    :type date_created: str
    :param date_updated: The date on which this resource was last updated.
    :type date_updated: str
    :param identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](https://www.twilio.com/docs/conversations/sdk-overview) to communicate. Limited to 256 characters.
    :type identity: str
    :param messaging_binding_address: The address of the participant&#39;s device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with &#x60;proxy_address&#x60;) is only null when the participant is interacting from an SDK endpoint (see the &#x60;identity&#x60; field).
    :type messaging_binding_address: str
    :param messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
    :type messaging_binding_projected_address: str
    :param messaging_binding_proxy_address: The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the &#x60;identity&#x60; field).
    :type messaging_binding_proxy_address: str
    :param role_sid: The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
    :type role_sid: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def delete_conversation_participant(request: web.Request, conversation_sid, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_conversation_participant

    Remove a participant from the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

    """
    return web.Response(status=200)


async def delete_service_conversation_participant(request: web.Request, chat_service_sid, conversation_sid, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_service_conversation_participant

    Remove a participant from the conversation

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

    """
    return web.Response(status=200)


async def fetch_conversation_participant(request: web.Request, conversation_sid, sid) -> web.Response:
    """fetch_conversation_participant

    Fetch a participant of the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource. Alternatively, you can pass a Participant&#39;s &#x60;identity&#x60; rather than the SID.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service_conversation_participant(request: web.Request, chat_service_sid, conversation_sid, sid) -> web.Response:
    """fetch_service_conversation_participant

    Fetch a participant of the conversation

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource. Alternatively, you can pass a Participant&#39;s &#x60;identity&#x60; rather than the SID.
    :type sid: str

    """
    return web.Response(status=200)


async def list_conversation_participant(request: web.Request, conversation_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_conversation_participant

    Retrieve a list of all participants of the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for participants.
    :type conversation_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def list_service_conversation_participant(request: web.Request, chat_service_sid, conversation_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service_conversation_participant

    Retrieve a list of all participants of the conversation

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for participants.
    :type conversation_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_conversation_participant(request: web.Request, conversation_sid, sid, x_twilio_webhook_enabled=None, attributes=None, date_created=None, date_updated=None, identity=None, last_read_message_index=None, last_read_timestamp=None, messaging_binding_projected_address=None, messaging_binding_proxy_address=None, role_sid=None) -> web.Response:
    """update_conversation_participant

    Update an existing participant in the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned.
    :type attributes: str
    :param date_created: The date that this resource was created.
    :type date_created: str
    :param date_updated: The date that this resource was last updated.
    :type date_updated: str
    :param identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
    :type identity: str
    :param last_read_message_index: Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
    :type last_read_message_index: int
    :param last_read_timestamp: Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
    :type last_read_timestamp: str
    :param messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS. &#39;null&#39; value will remove it.
    :type messaging_binding_projected_address: str
    :param messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact with. &#39;null&#39; value will remove it.
    :type messaging_binding_proxy_address: str
    :param role_sid: The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
    :type role_sid: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def update_service_conversation_participant(request: web.Request, chat_service_sid, conversation_sid, sid, x_twilio_webhook_enabled=None, attributes=None, date_created=None, date_updated=None, identity=None, last_read_message_index=None, last_read_timestamp=None, messaging_binding_projected_address=None, messaging_binding_proxy_address=None, role_sid=None) -> web.Response:
    """update_service_conversation_participant

    Update an existing participant in the conversation

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set &#x60;{}&#x60; will be returned.
    :type attributes: str
    :param date_created: The date on which this resource was created.
    :type date_created: str
    :param date_updated: The date on which this resource was last updated.
    :type date_updated: str
    :param identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](https://www.twilio.com/docs/conversations/sdk-overview) to communicate. Limited to 256 characters.
    :type identity: str
    :param last_read_message_index: Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
    :type last_read_message_index: int
    :param last_read_timestamp: Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
    :type last_read_timestamp: str
    :param messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS. &#39;null&#39; value will remove it.
    :type messaging_binding_projected_address: str
    :param messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact with. &#39;null&#39; value will remove it.
    :type messaging_binding_proxy_address: str
    :param role_sid: The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
    :type role_sid: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)
