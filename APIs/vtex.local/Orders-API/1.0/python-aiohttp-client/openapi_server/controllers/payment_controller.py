from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_paymenttransaction import GetPaymenttransaction
from openapi_server import util


async def get_paymenttransaction(request: web.Request, accept, content_type, order_id) -> web.Response:
    """Retrieve payment transaction

    Retrieves transaction details by order ID. All events in the transaction will be registered in this call&#39;s response body.   In scenarios of [order changes](https://developers.vtex.com/vtex-rest-api/reference/registerchange), it is possible to insert a [Partial invoice](https://help.vtex.com/en/tracks/pedidos--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe). The total value of the order will be updated after the insertion of the invoice, even when there is a [Partial invoice](https://help.vtex.com/en/tracks/pedidos--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe) scenario. The updated value is settled by VTEX&#39;s Payment Gateway. The reimbursement for the shopper is automatic.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param order_id: Order ID is a unique code that identifies an order.
    :type order_id: str

    """
    return web.Response(status=200)


async def send_payment_notification(request: web.Request, accept, content_type, order_id, payment_id) -> web.Response:
    """Send payment notification

    Send a payment notification of a given order, by order ID.    &gt; The &#x60;Notify payment&#x60; resource is needed to use this API request. This is included in &#x60;OMS - Full access&#x60; and &#x60;IntegrationProfile - Fulfillment Oms&#x60;, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param order_id: Order ID is a unique code that identifies an order.
    :type order_id: str
    :param payment_id: VTEX payment identifier.
    :type payment_id: str

    """
    return web.Response(status=200)
