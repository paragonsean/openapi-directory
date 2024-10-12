from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hiu_subscription_notification_acknowledgment import HIUSubscriptionNotificationAcknowledgment
from openapi_server.models.hiu_subscription_request_notification_acknowledgement import HIUSubscriptionRequestNotificationAcknowledgement
from openapi_server.models.subscription_request import SubscriptionRequest
from openapi_server import util


async def v05_subscription_requests_cm_init_post(request: web.Request, authorization, body) -> web.Response:
    """Request for subscription

    creates a request for subscription. The subscription categories can be for care-contexts linkages or availability of data against existing care-contexts. Note that the requester must have HIU role

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def v05_subscription_requests_hiu_on_notify_post(request: web.Request, authorization, body) -> web.Response:
    """Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.

    This API is called by HIU as acknowledgement to subscription request relevant notifications.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUSubscriptionRequestNotificationAcknowledgement.from_dict(body)
    return web.Response(status=200)


async def v05_subscriptions_hiu_on_notify_post(request: web.Request, authorization, body) -> web.Response:
    """Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.

    This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUSubscriptionNotificationAcknowledgment.from_dict(body)
    return web.Response(status=200)
