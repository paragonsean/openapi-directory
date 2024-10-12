from typing import List, Dict
from aiohttp import web

from openapi_server.models.configuration_webhook_enum_target import ConfigurationWebhookEnumTarget
from openapi_server.models.conversation_scoped_webhook_enum_method import ConversationScopedWebhookEnumMethod
from openapi_server.models.conversation_scoped_webhook_enum_target import ConversationScopedWebhookEnumTarget
from openapi_server.models.conversations_v1_configuration_configuration_webhook import ConversationsV1ConfigurationConfigurationWebhook
from openapi_server.models.conversations_v1_conversation_conversation_scoped_webhook import ConversationsV1ConversationConversationScopedWebhook
from openapi_server.models.conversations_v1_service_service_configuration_service_webhook_configuration import ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration
from openapi_server.models.conversations_v1_service_service_conversation_service_conversation_scoped_webhook import ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook
from openapi_server.models.list_conversation_scoped_webhook_response import ListConversationScopedWebhookResponse
from openapi_server.models.list_service_conversation_scoped_webhook_response import ListServiceConversationScopedWebhookResponse
from openapi_server.models.service_conversation_scoped_webhook_enum_method import ServiceConversationScopedWebhookEnumMethod
from openapi_server.models.service_conversation_scoped_webhook_enum_target import ServiceConversationScopedWebhookEnumTarget
from openapi_server import util


async def create_conversation_scoped_webhook(request: web.Request, conversation_sid, target, configuration_filters=None, configuration_flow_sid=None, configuration_method=None, configuration_replay_after=None, configuration_triggers=None, configuration_url=None) -> web.Response:
    """create_conversation_scoped_webhook

    Create a new webhook scoped to the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    :type conversation_sid: str
    :param target: 
    :type target: str
    :param configuration_filters: The list of events, firing webhook event for this Conversation.
    :type configuration_filters: List[str]
    :param configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
    :type configuration_flow_sid: str
    :param configuration_method: 
    :type configuration_method: str
    :param configuration_replay_after: The message index for which and it&#39;s successors the webhook will be replayed. Not set by default
    :type configuration_replay_after: int
    :param configuration_triggers: The list of keywords, firing webhook event for this Conversation.
    :type configuration_triggers: List[str]
    :param configuration_url: The absolute url the webhook request should be sent to.
    :type configuration_url: str

    """
    return web.Response(status=200)


async def create_service_conversation_scoped_webhook(request: web.Request, chat_service_sid, conversation_sid, target, configuration_filters=None, configuration_flow_sid=None, configuration_method=None, configuration_replay_after=None, configuration_triggers=None, configuration_url=None) -> web.Response:
    """create_service_conversation_scoped_webhook

    Create a new webhook scoped to the conversation in a specific service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    :type conversation_sid: str
    :param target: 
    :type target: str
    :param configuration_filters: The list of events, firing webhook event for this Conversation.
    :type configuration_filters: List[str]
    :param configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
    :type configuration_flow_sid: str
    :param configuration_method: 
    :type configuration_method: str
    :param configuration_replay_after: The message index for which and it&#39;s successors the webhook will be replayed. Not set by default
    :type configuration_replay_after: int
    :param configuration_triggers: The list of keywords, firing webhook event for this Conversation.
    :type configuration_triggers: List[str]
    :param configuration_url: The absolute url the webhook request should be sent to.
    :type configuration_url: str

    """
    return web.Response(status=200)


async def delete_conversation_scoped_webhook(request: web.Request, conversation_sid, sid) -> web.Response:
    """delete_conversation_scoped_webhook

    Remove an existing webhook scoped to the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def delete_service_conversation_scoped_webhook(request: web.Request, chat_service_sid, conversation_sid, sid) -> web.Response:
    """delete_service_conversation_scoped_webhook

    Remove an existing webhook scoped to the conversation

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_configuration_webhook(request: web.Request, ) -> web.Response:
    """fetch_configuration_webhook

    


    """
    return web.Response(status=200)


async def fetch_conversation_scoped_webhook(request: web.Request, conversation_sid, sid) -> web.Response:
    """fetch_conversation_scoped_webhook

    Fetch the configuration of a conversation-scoped webhook

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service_conversation_scoped_webhook(request: web.Request, chat_service_sid, conversation_sid, sid) -> web.Response:
    """fetch_service_conversation_scoped_webhook

    Fetch the configuration of a conversation-scoped webhook

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service_webhook_configuration(request: web.Request, chat_service_sid) -> web.Response:
    """fetch_service_webhook_configuration

    Fetch a specific service webhook configuration.

    :param chat_service_sid: The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
    :type chat_service_sid: str

    """
    return web.Response(status=200)


async def list_conversation_scoped_webhook(request: web.Request, conversation_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_conversation_scoped_webhook

    Retrieve a list of all webhooks scoped to the conversation

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    :type conversation_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def list_service_conversation_scoped_webhook(request: web.Request, chat_service_sid, conversation_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service_conversation_scoped_webhook

    Retrieve a list of all webhooks scoped to the conversation

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    :type conversation_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_configuration_webhook(request: web.Request, filters=None, method=None, post_webhook_url=None, pre_webhook_url=None, target=None) -> web.Response:
    """update_configuration_webhook

    

    :param filters: The list of webhook event triggers that are enabled for this Service: &#x60;onMessageAdded&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onParticipantRemoved&#x60;
    :type filters: List[str]
    :param method: The HTTP method to be used when sending a webhook request.
    :type method: str
    :param post_webhook_url: The absolute url the post-event webhook request should be sent to.
    :type post_webhook_url: str
    :param pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
    :type pre_webhook_url: str
    :param target: 
    :type target: str

    """
    return web.Response(status=200)


async def update_conversation_scoped_webhook(request: web.Request, conversation_sid, sid, configuration_filters=None, configuration_flow_sid=None, configuration_method=None, configuration_triggers=None, configuration_url=None) -> web.Response:
    """update_conversation_scoped_webhook

    Update an existing conversation-scoped webhook

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str
    :param configuration_filters: The list of events, firing webhook event for this Conversation.
    :type configuration_filters: List[str]
    :param configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
    :type configuration_flow_sid: str
    :param configuration_method: 
    :type configuration_method: str
    :param configuration_triggers: The list of keywords, firing webhook event for this Conversation.
    :type configuration_triggers: List[str]
    :param configuration_url: The absolute url the webhook request should be sent to.
    :type configuration_url: str

    """
    return web.Response(status=200)


async def update_service_conversation_scoped_webhook(request: web.Request, chat_service_sid, conversation_sid, sid, configuration_filters=None, configuration_flow_sid=None, configuration_method=None, configuration_triggers=None, configuration_url=None) -> web.Response:
    """update_service_conversation_scoped_webhook

    Update an existing conversation-scoped webhook

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    :type conversation_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str
    :param configuration_filters: The list of events, firing webhook event for this Conversation.
    :type configuration_filters: List[str]
    :param configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
    :type configuration_flow_sid: str
    :param configuration_method: 
    :type configuration_method: str
    :param configuration_triggers: The list of keywords, firing webhook event for this Conversation.
    :type configuration_triggers: List[str]
    :param configuration_url: The absolute url the webhook request should be sent to.
    :type configuration_url: str

    """
    return web.Response(status=200)


async def update_service_webhook_configuration(request: web.Request, chat_service_sid, filters=None, method=None, post_webhook_url=None, pre_webhook_url=None) -> web.Response:
    """update_service_webhook_configuration

    Update a specific Webhook.

    :param chat_service_sid: The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
    :type chat_service_sid: str
    :param filters: The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are &#x60;onParticipantAdd&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onDeliveryUpdated&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationRemove&#x60;, &#x60;onParticipantRemove&#x60;, &#x60;onConversationUpdate&#x60;, &#x60;onMessageAdd&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onConversationAdded&#x60;, &#x60;onMessageAdded&#x60;, &#x60;onConversationAdd&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantUpdate&#x60;, &#x60;onMessageRemove&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onParticipantRemoved&#x60;, &#x60;onMessageUpdate&#x60; or &#x60;onConversationStateUpdated&#x60;.
    :type filters: List[str]
    :param method: The HTTP method to be used when sending a webhook request. One of &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type method: str
    :param post_webhook_url: The absolute url the post-event webhook request should be sent to.
    :type post_webhook_url: str
    :param pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
    :type pre_webhook_url: str

    """
    return web.Response(status=200)
