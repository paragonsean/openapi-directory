from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversations_v1_service_service_user import ConversationsV1ServiceServiceUser
from openapi_server.models.conversations_v1_user import ConversationsV1User
from openapi_server.models.list_service_user_response import ListServiceUserResponse
from openapi_server.models.list_user_response import ListUserResponse
from openapi_server.models.service_user_enum_webhook_enabled_type import ServiceUserEnumWebhookEnabledType
from openapi_server.models.user_enum_webhook_enabled_type import UserEnumWebhookEnabledType
from openapi_server import util


async def create_service_user(request: web.Request, chat_service_sid, identity, x_twilio_webhook_enabled=None, attributes=None, friendly_name=None, role_sid=None) -> web.Response:
    """create_service_user

    Add a new conversation user to your service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with.
    :type chat_service_sid: str
    :param identity: The application-defined string that uniquely identifies the resource&#39;s User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
    :type identity: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned.
    :type attributes: str
    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str
    :param role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
    :type role_sid: str

    """
    return web.Response(status=200)


async def create_user(request: web.Request, identity, x_twilio_webhook_enabled=None, attributes=None, friendly_name=None, role_sid=None) -> web.Response:
    """create_user

    Add a new conversation user to your account&#39;s default service

    :param identity: The application-defined string that uniquely identifies the resource&#39;s User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
    :type identity: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned.
    :type attributes: str
    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str
    :param role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
    :type role_sid: str

    """
    return web.Response(status=200)


async def delete_service_user(request: web.Request, chat_service_sid, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_service_user

    Remove a conversation user from your service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to delete the User resource from.
    :type chat_service_sid: str
    :param sid: The SID of the User resource to delete. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to delete.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

    """
    return web.Response(status=200)


async def delete_user(request: web.Request, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_user

    Remove a conversation user from your account&#39;s default service

    :param sid: The SID of the User resource to delete. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to delete.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

    """
    return web.Response(status=200)


async def fetch_service_user(request: web.Request, chat_service_sid, sid) -> web.Response:
    """fetch_service_user

    Fetch a conversation user from your service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to fetch the User resource from.
    :type chat_service_sid: str
    :param sid: The SID of the User resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_user(request: web.Request, sid) -> web.Response:
    """fetch_user

    Fetch a conversation user from your account&#39;s default service

    :param sid: The SID of the User resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_service_user(request: web.Request, chat_service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service_user

    Retrieve a list of all conversation users in your service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to read the User resources from.
    :type chat_service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def list_user(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_user

    Retrieve a list of all conversation users in your account&#39;s default service

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_service_user(request: web.Request, chat_service_sid, sid, x_twilio_webhook_enabled=None, attributes=None, friendly_name=None, role_sid=None) -> web.Response:
    """update_service_user

    Update an existing conversation user in your service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with.
    :type chat_service_sid: str
    :param sid: The SID of the User resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to update.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned.
    :type attributes: str
    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str
    :param role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
    :type role_sid: str

    """
    return web.Response(status=200)


async def update_user(request: web.Request, sid, x_twilio_webhook_enabled=None, attributes=None, friendly_name=None, role_sid=None) -> web.Response:
    """update_user

    Update an existing conversation user in your account&#39;s default service

    :param sid: The SID of the User resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to update.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned.
    :type attributes: str
    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str
    :param role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
    :type role_sid: str

    """
    return web.Response(status=200)
