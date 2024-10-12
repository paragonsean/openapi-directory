from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def send_payment_notification2(request: web.Request, content_type, accept, order_id, payment_id) -> web.Response:
    """Send payment notification

    Send a payment notification of a given order, by order ID and payment ID.    &gt; The &#x60;Notify payment&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).    &gt; Learn more about [Transaction Details](https://help.vtex.com/en/tutorial/how-to-view-the-orders-details).      ## Request body properties    | Attribute    | Type        | Description |  | --------------- |:---------:| --------------------------------------:|  | &#x60;orderId&#x60; | string | Order Id |  | &#x60;paymentId&#x60; | string | Payment ID |

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_id: ID of the order.
    :type order_id: str
    :param payment_id: ID of the payment.
    :type payment_id: str

    """
    return web.Response(status=200)
