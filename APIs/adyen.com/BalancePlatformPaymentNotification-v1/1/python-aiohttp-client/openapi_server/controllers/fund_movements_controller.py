from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse
from openapi_server.models.incoming_transfer_notification_request import IncomingTransferNotificationRequest
from openapi_server.models.outgoing_transfer_notification_request import OutgoingTransferNotificationRequest
from openapi_server import util


async def post_balance_platform_incoming_transfer_created(request: web.Request, incoming_transfer_notification_request=None) -> web.Response:
    """Incoming transfer created

    Adyen sends this webhook when there are incoming funds due to a refund or a fund transfer. Use the &#x60;paymentId&#x60; to link to the original refund request or funds transfer request. Check the content of the webhook to differentiate the events.  * For refunds, the webhook includes the payment instrument to which funds will be refunded.  * For incoming fund transfers, the webhook only includes information about the balance account.

    :param incoming_transfer_notification_request: 
    :type incoming_transfer_notification_request: dict | bytes

    """
    incoming_transfer_notification_request = IncomingTransferNotificationRequest.from_dict(incoming_transfer_notification_request)
    return web.Response(status=200)


async def post_balance_platform_incoming_transfer_updated(request: web.Request, incoming_transfer_notification_request=None) -> web.Response:
    """Incoming transfer updated

    Adyen sends this webhook when funds were added to the balance account. This could be due to a refund or a funds transfer. Use the &#x60;data.id&#x60; to track the original incoming transfer resource in the &#x60;balancePlatform.incomingTransfer.created&#x60; webhook.  The &#x60;status&#x60; field indicates the event that triggered the webhook.   * For refunds, the &#x60;status&#x60; is **Refunded**.   * For incoming fund transfers, the &#x60;status&#x60; is **IncomingTransfer**.

    :param incoming_transfer_notification_request: 
    :type incoming_transfer_notification_request: dict | bytes

    """
    incoming_transfer_notification_request = IncomingTransferNotificationRequest.from_dict(incoming_transfer_notification_request)
    return web.Response(status=200)


async def post_balance_platform_outgoing_transfer_created(request: web.Request, outgoing_transfer_notification_request=None) -> web.Response:
    """Outgoing transfer created

    Adyen sends this webhook when funds were deducted from a balance account due to a capture or a funds transfer. Use the &#x60;paymentId&#x60; to link to the original payment authorisation or funds transfer request.  The &#x60;status&#x60; field indicates the event that triggered the webhook.   * For captures, the &#x60;status&#x60; will be **Captured**.   * For outgoing fund transfers, the &#x60;status&#x60; will be **OutgoingTransfer**.

    :param outgoing_transfer_notification_request: 
    :type outgoing_transfer_notification_request: dict | bytes

    """
    outgoing_transfer_notification_request = OutgoingTransferNotificationRequest.from_dict(outgoing_transfer_notification_request)
    return web.Response(status=200)


async def post_balance_platform_outgoing_transfer_updated(request: web.Request, outgoing_transfer_notification_request=None) -> web.Response:
    """Outgoing transfer updated

    Adyen sends this webhook when there is updated information after funds have been deducted from a balance account. For example, if the fund transfer failed.  Use the &#x60;data.id&#x60; to track the original outgoing transfer resource from the &#x60;balancePlatform.outgoingTransfer.created&#x60; webhook.

    :param outgoing_transfer_notification_request: 
    :type outgoing_transfer_notification_request: dict | bytes

    """
    outgoing_transfer_notification_request = OutgoingTransferNotificationRequest.from_dict(outgoing_transfer_notification_request)
    return web.Response(status=200)
