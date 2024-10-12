from typing import List, Dict
from aiohttp import web

from openapi_server.models.cobrand_login_request import CobrandLoginRequest
from openapi_server.models.cobrand_login_response import CobrandLoginResponse
from openapi_server.models.cobrand_notification_response import CobrandNotificationResponse
from openapi_server.models.cobrand_public_key_response import CobrandPublicKeyResponse
from openapi_server.models.create_cobrand_notification_event_request import CreateCobrandNotificationEventRequest
from openapi_server.models.update_cobrand_notification_event_request import UpdateCobrandNotificationEventRequest
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def cobrand_login(request: web.Request, body) -> web.Response:
    """Cobrand Login

    The cobrand login service authenticates a cobrand.&lt;br&gt;Cobrand session in the response includes the cobrand session token (cobSession) &lt;br&gt;which is used in subsequent API calls like registering or signing in the user. &lt;br&gt;The idle timeout for a cobrand session is 2 hours and the absolute timeout is 24 hours. This service can be &lt;br&gt;invoked to create a new cobrand session token. &lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; This endpoint is deprecated for customers using the API Key-based authentication and is applicable only to customers who use the SAML-based authentication.&lt;br&gt;The content type has to be passed as application/json for the body parameter. &lt;br&gt;

    :param body: cobrandLoginRequest
    :type body: dict | bytes

    """
    body = CobrandLoginRequest.from_dict(body)
    return web.Response(status=200)


async def cobrand_logout(request: web.Request, ) -> web.Response:
    """Cobrand Logout

    The cobrand logout service is used to log out the cobrand.&lt;br&gt;This service does not return a response. The HTTP response code is 204 (Success with no content).&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; This endpoint is deprecated for customers using the API Key-based authentication and is applicable only to customers who use the SAML-based authentication.&lt;br&gt;


    """
    return web.Response(status=200)


async def create_subscription_event(request: web.Request, event_name, body) -> web.Response:
    """Subscribe Event

    &lt;b&gt;Refer POST /configs/notifications/events/{eventName}.&lt;/b&gt;&lt;br&gt;The subscribe events service is used to subscribe to an event for receiving notifications.&lt;br&gt;The callback URL, where the notification will be posted should be provided to this service.&lt;br&gt;If the callback URL is invalid or inaccessible, the subscription will be unsuccessful, and an error will be thrown.&lt;br&gt;Customers can subscribe to REFRESH,DATA_UPDATES and AUTO_REFRESH_UPDATES event.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes&lt;/b&gt;:&lt;br&gt;This service is not available in developer sandbox/test environment and will be made available for testing in your dedicated environment, once the contract is signed.&lt;br&gt;The content type has to be passed as application/json for the body parameter.&lt;br&gt;

    :param event_name: eventName
    :type event_name: str
    :param body: eventRequest
    :type body: dict | bytes

    """
    body = CreateCobrandNotificationEventRequest.from_dict(body)
    return web.Response(status=200)


async def delete_subscribed_event(request: web.Request, event_name) -> web.Response:
    """Delete Subscription

    &lt;b&gt;Refer DELETE /configs/notifications/events/{eventName}.&lt;/b&gt;&lt;br&gt;The delete events service is used to unsubscribe from an events service.&lt;br&gt;

    :param event_name: eventName
    :type event_name: str

    """
    return web.Response(status=200)


async def get_public_key(request: web.Request, ) -> web.Response:
    """Get Public Key

    &lt;b&gt;Refer GET /configs/publicKey.&lt;/b&gt;&lt;br&gt;The get public key service provides the customer the public key that should be used to encrypt the user credentials before sending it to Yodlee.&lt;br&gt;This endpoint is useful only for PKI enabled.&lt;br&gt;


    """
    return web.Response(status=200)


async def get_subscribed_events(request: web.Request, event_name=None) -> web.Response:
    """Get Subscribed Events

    &lt;b&gt;Refer GET /configs/notifications/events.&lt;/b&gt;&lt;br&gt;The get events service provides the list of events for which consumers subscribed &lt;br&gt;to receive notifications. &lt;br&gt;

    :param event_name: eventName
    :type event_name: str

    """
    return web.Response(status=200)


async def update_subscribed_event(request: web.Request, event_name, body) -> web.Response:
    """Update Subscription

    &lt;b&gt;Refer PUT /configs/notifications/events/{eventName}.&lt;/b&gt;&lt;br&gt;The update events service is used to update the callback URL.&lt;br&gt;If the callback URL is invalid or inaccessible, the subscription will be unsuccessful, and an error will be thrown.&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; The content type has to be passed as application/json for the body parameter. &lt;br&gt;

    :param event_name: eventName
    :type event_name: str
    :param body: eventRequest
    :type body: dict | bytes

    """
    body = UpdateCobrandNotificationEventRequest.from_dict(body)
    return web.Response(status=200)
