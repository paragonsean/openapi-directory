from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_tracking_status import UpdateTrackingStatus
from openapi_server.models.update_tracking_status_request import UpdateTrackingStatusRequest
from openapi_server import util


async def update_tracking_status(request: web.Request, content_type, accept, order_id, invoice_number, body) -> web.Response:
    """Update order tracking status

    This endpoint sends a tracking event to an order that already has a tracking number registered to its invoice.    This request is not meant to send tracking number and URL to the invoice. If you wish to send tracking number and URL to an order, use the [Update order&#39;s partial invoice API request](https://developers.vtex.com/docs/api-reference/orders-api#patch-/api/oms/pvt/orders/-orderId-/invoice/-invoiceNumber-). You can also learn more about [Partial invoice](https://help.vtex.com/en/tracks/partial-invoices--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe) scenarios.     &gt; The &#x60;Notify invoice&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc).

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_id: Order ID is a unique code that identifies an order.
    :type order_id: str
    :param invoice_number: Number that identifies the invoice.
    :type invoice_number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateTrackingStatusRequest.from_dict(body)
    return web.Response(status=200)
