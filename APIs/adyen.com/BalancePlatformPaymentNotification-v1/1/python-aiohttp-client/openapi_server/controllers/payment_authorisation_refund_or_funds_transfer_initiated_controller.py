from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse
from openapi_server.models.payment_notification_request import PaymentNotificationRequest
from openapi_server import util


async def post_balance_platform_payment_created(request: web.Request, payment_notification_request=None) -> web.Response:
    """Payment authorisation, refund, or funds transfer initiated

    Adyen sends this webhook when a payment authorisation, a refund, or a funds transfer has been initiated. This webhook only informs your server of requests. For the actual fund movements, you&#39;ll get the information from the subsequent outgoing or incoming transfer webhooks.   To differentiate the requests, check the content of the webhook.  * For payments, the webhook contains the authorisation result, information about the processing merchant, and shows a negative amount.   * For refunds, the webhook contains to which payment instrument the funds will be refunded, and shows a positive amount.  * For outgoing or incoming fund transfers, the webhook shows a positive or negative amount depending on the direction of the transfer, and only includes information about the balance account.

    :param payment_notification_request: 
    :type payment_notification_request: dict | bytes

    """
    payment_notification_request = PaymentNotificationRequest.from_dict(payment_notification_request)
    return web.Response(status=200)


async def post_balance_platform_payment_updated(request: web.Request, payment_notification_request=None) -> web.Response:
    """Payment authorisation expired or cancelled

    Adyen sends this webhook when a payment authorisation has expired or has been cancelled. Use the &#x60;data.id&#x60; to track the original payment authorisation from the &#x60;balancePlatform.payment.created&#x60; webhook.

    :param payment_notification_request: 
    :type payment_notification_request: dict | bytes

    """
    payment_notification_request = PaymentNotificationRequest.from_dict(payment_notification_request)
    return web.Response(status=200)
