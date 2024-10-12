from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hiu_subscription_notification import HIUSubscriptionNotification
from openapi_server.models.hiu_subscription_request_receipt import HIUSubscriptionRequestReceipt
from openapi_server.models.subscription_approval_notification import SubscriptionApprovalNotification
from openapi_server import util


async def v05_subscription_requests_hiu_notify_post(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Notification for subscription grant/deny/revoke

    This API is used by CM to notify a HIU to grant or deny a request for subscription, and also to notify that in case an existing subscription is revoked or expired. For notifying that a particular subscription request was GRANTED or DENIED, the **subscriptionRequestId** is passed.  

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionApprovalNotification.from_dict(body)
    return web.Response(status=200)


async def v05_subscription_requests_hiu_on_init_post(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.

    This callback API acknowledges the request for subscription from a HIU, and sends back a \&quot;id\&quot; that will be used when the patient/user approves or denies the subscription.  

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUSubscriptionRequestReceipt.from_dict(body)
    return web.Response(status=200)


async def v05_subscriptions_hiu_notify_post(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Notification to HIU on basis of a granted subscription

    This API is used by CM to notify a HIU for notification relevant to subscription. Notifications are sent to subscribed HIUs whenever a new care-context is linked or new data is available on an existing linked care-context.  1. if event.category &#x3D; LINK, then only care-contexts are passed when new care-contexts are linked for patient.  2. If event.category &#x3D; DATA, then hiTypes are passed. Care-context is passed only if the subscribed HIU has any valid consent for that care-context 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUSubscriptionNotification.from_dict(body)
    return web.Response(status=200)
