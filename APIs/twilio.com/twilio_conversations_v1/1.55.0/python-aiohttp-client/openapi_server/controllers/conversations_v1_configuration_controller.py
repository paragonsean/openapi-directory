from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversations_v1_configuration import ConversationsV1Configuration
from openapi_server.models.conversations_v1_service_service_configuration import ConversationsV1ServiceServiceConfiguration
from openapi_server import util


async def fetch_configuration(request: web.Request, ) -> web.Response:
    """fetch_configuration

    Fetch the global configuration of conversations on your account


    """
    return web.Response(status=200)


async def fetch_service_configuration(request: web.Request, chat_service_sid) -> web.Response:
    """fetch_service_configuration

    Fetch the configuration of a conversation service

    :param chat_service_sid: The SID of the Service configuration resource to fetch.
    :type chat_service_sid: str

    """
    return web.Response(status=200)


async def update_configuration(request: web.Request, default_chat_service_sid=None, default_closed_timer=None, default_inactive_timer=None, default_messaging_service_sid=None) -> web.Response:
    """update_configuration

    Update the global configuration of conversations on your account

    :param default_chat_service_sid: The SID of the default [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to use when creating a conversation.
    :type default_chat_service_sid: str
    :param default_closed_timer: Default ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes.
    :type default_closed_timer: str
    :param default_inactive_timer: Default ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute.
    :type default_inactive_timer: str
    :param default_messaging_service_sid: The SID of the default [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to use when creating a conversation.
    :type default_messaging_service_sid: str

    """
    return web.Response(status=200)


async def update_service_configuration(request: web.Request, chat_service_sid, default_chat_service_role_sid=None, default_conversation_creator_role_sid=None, default_conversation_role_sid=None, reachability_enabled=None) -> web.Response:
    """update_service_configuration

    Update configuration settings of a conversation service

    :param chat_service_sid: The SID of the Service configuration resource to update.
    :type chat_service_sid: str
    :param default_chat_service_role_sid: The service-level role assigned to users when they are added to the service. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
    :type default_chat_service_role_sid: str
    :param default_conversation_creator_role_sid: The conversation-level role assigned to a conversation creator when they join a new conversation. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
    :type default_conversation_creator_role_sid: str
    :param default_conversation_role_sid: The conversation-level role assigned to users when they are added to a conversation. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
    :type default_conversation_role_sid: str
    :param reachability_enabled: Whether the [Reachability Indicator](https://www.twilio.com/docs/conversations/reachability) is enabled for this Conversations Service. The default is &#x60;false&#x60;.
    :type reachability_enabled: bool

    """
    return web.Response(status=200)
