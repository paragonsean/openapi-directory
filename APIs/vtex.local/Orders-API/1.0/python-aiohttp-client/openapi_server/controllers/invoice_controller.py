from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancel_order200_response import CancelOrder200Response
from openapi_server.models.invoice_notification_request import InvoiceNotificationRequest
from openapi_server.models.updatepartialinvoice_send_tracking_number import UpdatepartialinvoiceSendTrackingNumber
from openapi_server.models.updatepartialinvoice_send_tracking_number_request import UpdatepartialinvoiceSendTrackingNumberRequest
from openapi_server import util


async def invoice_notification(request: web.Request, accept, content_type, order_id, body) -> web.Response:
    """Order invoice notification

    Entering the [invoice in the order](https://help.vtex.com/en/tracks/orders--2xkTisx4SXOWXQel8Jg8sa/2WgQrlHTyVo4hLjhUs1LMT) is a required step for its [status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196#order-status-details) to change to Invoiced - a sign that the order has been successfully completed. Remember that once an order is read as invoiced by the system, this status cannot be changed.   The total value of the order will be updated after the insertion of the invoice, even when there&#39;s a [Partial invoice](https://help.vtex.com/en/tracks/orders--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe) scenario. The updated value is settled by VTEX&#39;s Payment Gateway. The reimbursement for the shopper is automatic.   We strongly recommend that you always send the object of the invoiced items. With this practice, rounding errors will be avoided.   When returning items, an input invoice must be sent through this call. For that, the &#x60;type&#x60; field should be filled in with &#x60;input&#x60;.   It is not allowed to use the same &#x60;invoiceNumber&#x60; in more than one request to the Order Invoice Notification endpoint.  For marketplace integrations: once the order is invoiced, the seller should use this request to send the invoice information to the marketplace. Be aware that this endpoint is also used by the seller to send the order tracking information. This, however, should be done in a separate moment, once the seller has the tracking information.      &gt; The &#x60;Notify invoice&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).    &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Orders onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/orders-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Orders and is organized by focusing on the developer&#39;s journey.    

    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param order_id: Unique code that identifies the order whose invoice is being sent.
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = InvoiceNotificationRequest.from_dict(body)
    return web.Response(status=200)


async def updatepartialinvoice_send_tracking_number(request: web.Request, content_type, accept, order_id, invoice_number, body) -> web.Response:
    """Update order&#39;s partial invoice (send tracking number)

    Update a given order, adding its tracking number to its [Partial invoice](https://help.vtex.com/en/tracks/pedidos--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe).    After using this call to add a tracking number to an order, you can use the [Update order tracking status](https://developers.vtex.com/vtex-rest-api/reference/tracking#updatetrackingstatus) API request to add tracking events.    &gt; The &#x60;Notify invoice&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc).

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_id: Unique code that identifies the order whose invoice is being sent.
    :type order_id: str
    :param invoice_number: Number that identifies the invoice.
    :type invoice_number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatepartialinvoiceSendTrackingNumberRequest.from_dict(body)
    return web.Response(status=200)
