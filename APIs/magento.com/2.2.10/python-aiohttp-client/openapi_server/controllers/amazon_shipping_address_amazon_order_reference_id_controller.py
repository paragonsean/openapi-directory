from typing import List, Dict
from aiohttp import web

from openapi_server.models.amazon_payment_address_management_v1_get_billing_address_put_request import AmazonPaymentAddressManagementV1GetBillingAddressPutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def amazon_payment_address_management_v1_get_shipping_address_put(request: web.Request, amazon_order_reference_id, body=None) -> web.Response:
    """amazon-shipping-address/{amazonOrderReferenceId}

    

    :param amazon_order_reference_id: 
    :type amazon_order_reference_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AmazonPaymentAddressManagementV1GetBillingAddressPutRequest.from_dict(body)
    return web.Response(status=200)
