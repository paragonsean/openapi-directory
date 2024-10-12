from typing import List, Dict
from aiohttp import web

from openapi_server.models.payment_link_request import PaymentLinkRequest
from openapi_server.models.payment_link_response import PaymentLinkResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.update_payment_link_request import UpdatePaymentLinkRequest
from openapi_server import util


async def get_payment_links_link_id(request: web.Request, link_id) -> web.Response:
    """Get a payment link

    Retrieves the payment link details using the payment link &#x60;id&#x60;.

    :param link_id: Unique identifier of the payment link.
    :type link_id: str

    """
    return web.Response(status=200)


async def patch_payment_links_link_id(request: web.Request, link_id, body=None) -> web.Response:
    """Update the status of a payment link

    Updates the status of a payment link. Use this endpoint to [force the expiry of a payment link](https://docs.adyen.com/online-payments/pay-by-link#update-payment-link-status).

    :param link_id: Unique identifier of the payment link.
    :type link_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePaymentLinkRequest.from_dict(body)
    return web.Response(status=200)


async def post_payment_links(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Create a payment link

    Creates a payment link to our hosted payment form where shoppers can pay. The list of payment methods presented to the shopper depends on the &#x60;currency&#x60; and &#x60;country&#x60; parameters sent in the request.  For more information, refer to [Pay by Link documentation](https://docs.adyen.com/online-payments/pay-by-link#create-payment-links-through-api).

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentLinkRequest.from_dict(body)
    return web.Response(status=200)
