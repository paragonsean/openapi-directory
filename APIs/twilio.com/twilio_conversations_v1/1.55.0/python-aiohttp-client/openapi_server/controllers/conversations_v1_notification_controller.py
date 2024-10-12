from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversations_v1_service_service_configuration_service_notification import ConversationsV1ServiceServiceConfigurationServiceNotification
from openapi_server import util


async def fetch_service_notification(request: web.Request, chat_service_sid) -> web.Response:
    """fetch_service_notification

    Fetch push notification service settings

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to.
    :type chat_service_sid: str

    """
    return web.Response(status=200)


async def update_service_notification(request: web.Request, chat_service_sid, added_to_conversation_enabled=None, added_to_conversation_sound=None, added_to_conversation_template=None, log_enabled=None, new_message_badge_count_enabled=None, new_message_enabled=None, new_message_sound=None, new_message_template=None, new_message_with_media_enabled=None, new_message_with_media_template=None, removed_from_conversation_enabled=None, removed_from_conversation_sound=None, removed_from_conversation_template=None) -> web.Response:
    """update_service_notification

    Update push notification service settings

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to.
    :type chat_service_sid: str
    :param added_to_conversation_enabled: Whether to send a notification when a participant is added to a conversation. The default is &#x60;false&#x60;.
    :type added_to_conversation_enabled: bool
    :param added_to_conversation_sound: The name of the sound to play when a participant is added to a conversation and &#x60;added_to_conversation.enabled&#x60; is &#x60;true&#x60;.
    :type added_to_conversation_sound: str
    :param added_to_conversation_template: The template to use to create the notification text displayed when a participant is added to a conversation and &#x60;added_to_conversation.enabled&#x60; is &#x60;true&#x60;.
    :type added_to_conversation_template: str
    :param log_enabled: Weather the notification logging is enabled.
    :type log_enabled: bool
    :param new_message_badge_count_enabled: Whether the new message badge is enabled. The default is &#x60;false&#x60;.
    :type new_message_badge_count_enabled: bool
    :param new_message_enabled: Whether to send a notification when a new message is added to a conversation. The default is &#x60;false&#x60;.
    :type new_message_enabled: bool
    :param new_message_sound: The name of the sound to play when a new message is added to a conversation and &#x60;new_message.enabled&#x60; is &#x60;true&#x60;.
    :type new_message_sound: str
    :param new_message_template: The template to use to create the notification text displayed when a new message is added to a conversation and &#x60;new_message.enabled&#x60; is &#x60;true&#x60;.
    :type new_message_template: str
    :param new_message_with_media_enabled: Whether to send a notification when a new message with media/file attachments is added to a conversation. The default is &#x60;false&#x60;.
    :type new_message_with_media_enabled: bool
    :param new_message_with_media_template: The template to use to create the notification text displayed when a new message with media/file attachments is added to a conversation and &#x60;new_message.attachments.enabled&#x60; is &#x60;true&#x60;.
    :type new_message_with_media_template: str
    :param removed_from_conversation_enabled: Whether to send a notification to a user when they are removed from a conversation. The default is &#x60;false&#x60;.
    :type removed_from_conversation_enabled: bool
    :param removed_from_conversation_sound: The name of the sound to play to a user when they are removed from a conversation and &#x60;removed_from_conversation.enabled&#x60; is &#x60;true&#x60;.
    :type removed_from_conversation_sound: str
    :param removed_from_conversation_template: The template to use to create the notification text displayed to a user when they are removed from a conversation and &#x60;removed_from_conversation.enabled&#x60; is &#x60;true&#x60;.
    :type removed_from_conversation_template: str

    """
    return web.Response(status=200)
