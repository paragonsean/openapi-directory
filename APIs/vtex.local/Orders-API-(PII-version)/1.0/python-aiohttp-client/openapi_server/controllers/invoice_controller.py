from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancel_order2200_response import CancelOrder2200Response
from openapi_server.models.invoice_notification_request import InvoiceNotificationRequest
from openapi_server import util


async def invoice_notification2(request: web.Request, content_type, accept, order_id, body) -> web.Response:
    """Order invoice notification

    Once the order is invoiced, the seller should use this request to send the invoice information to the marketplace.  We strongly recommend that you always send the object of the invoiced items. With this practice, rounding errors will be avoided.  It is not allowed to use the same &#x60;invoiceNumber&#x60; in more than one request to the Order Invoice Notification endpoint.  Be aware that this endpoint is also used by the seller to send the order tracking information. This, however, should be done in a separate moment, once the seller has the tracking information.    &gt; The &#x60;Notify invoice&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_id: ID of the order.
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = InvoiceNotificationRequest.from_dict(body)
    return web.Response(status=200)
