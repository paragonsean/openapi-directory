from typing import List, Dict
from aiohttp import web

from openapi_server.models.configs_notification_response import ConfigsNotificationResponse
from openapi_server.models.configs_public_key_response import ConfigsPublicKeyResponse
from openapi_server.models.create_configs_notification_event_request import CreateConfigsNotificationEventRequest
from openapi_server.models.update_configs_notification_event_request import UpdateConfigsNotificationEventRequest
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def create_subscription_notification_event(request: web.Request, event_name, body) -> web.Response:
    """Subscribe For Notification Event

    The subscribe events service is used to subscribe to an event for receiving notifications.&lt;br&gt;The callback URL, where the notification will be posted should be provided to this service.&lt;br&gt;If the callback URL is invalid or inaccessible, the subscription will be unsuccessful, and an error will be thrown.&lt;br&gt;Customers can subscribe to REFRESH,DATA_UPDATES and AUTO_REFRESH_UPDATES event.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;li&gt;This service is not available in developer sandbox/test environment and will be made available for testing in your dedicated environment, once the contract is signed.&lt;li&gt;The content type has to be passed as application/json for the body parameter.&lt;/li&gt;

    :param event_name: eventName
    :type event_name: str
    :param body: eventRequest
    :type body: dict | bytes

    """
    body = CreateConfigsNotificationEventRequest.from_dict(body)
    return web.Response(status=200)


async def delete_subscribed_notification_event(request: web.Request, event_name) -> web.Response:
    """Delete Notification Subscription

    The delete events service is used to unsubscribe from an events service.&lt;br&gt;

    :param event_name: eventName
    :type event_name: str

    """
    return web.Response(status=200)


async def get_public_encryption_key(request: web.Request, ) -> web.Response:
    """Get Public Key

    The get public key service provides the public key that should be used to encrypt user credentials while invoking POST /providerAccounts and PUT /providerAccounts endpoints.&lt;br&gt;This service will only work if the PKI (public key infrastructure) feature is enabled for the customer.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt; The key in the response is a string in PEM format.&lt;/li&gt;&lt;li&gt;This endpoint is not available in the Sandbox environment and it is useful only if the PKI feature is enabled.&lt;/li&gt;


    """
    return web.Response(status=200)


async def get_subscribed_notification_events(request: web.Request, event_name=None) -> web.Response:
    """Get Subscribed Notification Events

    The get events service provides the list of events for which consumers subscribed to receive notifications. &lt;br&gt;

    :param event_name: eventName
    :type event_name: str

    """
    return web.Response(status=200)


async def update_subscribed_notification_event(request: web.Request, event_name, body) -> web.Response:
    """Update Notification Subscription

    The update events service is used to update the callback URL.&lt;br&gt;If the callback URL is invalid or inaccessible, the subscription will be unsuccessful, and an error will be thrown.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;The content type has to be passed as application/json for the body parameter. &lt;br&gt;

    :param event_name: eventName
    :type event_name: str
    :param body: eventRequest
    :type body: dict | bytes

    """
    body = UpdateConfigsNotificationEventRequest.from_dict(body)
    return web.Response(status=200)
