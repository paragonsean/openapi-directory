from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hiu_subscription_notification_acknowledgment import HIUSubscriptionNotificationAcknowledgment
from openapi_server.models.patient_auth_notification_acknowledgement import PatientAuthNotificationAcknowledgement
from openapi_server import util


async def v05_subscriptions_hiu_on_notify_post_0(request: web.Request, authorization, body) -> web.Response:
    """Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.

    This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUSubscriptionNotificationAcknowledgment.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_on_notify_post_1(request: web.Request, authorization, body) -> web.Response:
    """callback API from HIU/HIPs as acknowledgement of auth notification (in case of DIRECT auth)

    This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthNotificationAcknowledgement.from_dict(body)
    return web.Response(status=200)
