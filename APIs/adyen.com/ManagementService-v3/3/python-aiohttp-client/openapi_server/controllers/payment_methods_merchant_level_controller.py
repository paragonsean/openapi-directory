from typing import List, Dict
from aiohttp import web

from openapi_server.models.apple_pay_info import ApplePayInfo
from openapi_server.models.payment_method import PaymentMethod
from openapi_server.models.payment_method_response import PaymentMethodResponse
from openapi_server.models.payment_method_setup_info import PaymentMethodSetupInfo
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.update_payment_method_info import UpdatePaymentMethodInfo
from openapi_server import util


async def get_merchants_merchant_id_payment_method_settings(request: web.Request, merchant_id, store_id=None, business_line_id=None, page_size=None, page_number=None) -> web.Response:
    """Get all payment methods

    Returns details for all payment methods of the merchant account identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read 

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param store_id: The unique identifier of the store for which to return the payment methods.
    :type store_id: str
    :param business_line_id: The unique identifier of the Business Line for which to return the payment methods.
    :type business_line_id: str
    :param page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
    :type page_size: int
    :param page_number: The number of the page to fetch.
    :type page_number: int

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_payment_method_settings_payment_method_id(request: web.Request, merchant_id, payment_method_id) -> web.Response:
    """Get payment method details

    Returns details for the merchant account and the payment method identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read 

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param payment_method_id: The unique identifier of the payment method.
    :type payment_method_id: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains(request: web.Request, merchant_id, payment_method_id) -> web.Response:
    """Get Apple Pay domains

    Returns all Apple Pay domains that are registered with the merchant account and the payment method identified in the path. For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/enable-apple-pay#register-merchant-domain).  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read 

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param payment_method_id: The unique identifier of the payment method.
    :type payment_method_id: str

    """
    return web.Response(status=200)


async def patch_merchants_merchant_id_payment_method_settings_payment_method_id(request: web.Request, merchant_id, payment_method_id, body=None) -> web.Response:
    """Update a payment method

    Updates payment method details for the merchant account and the payment method identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read and write 

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param payment_method_id: The unique identifier of the payment method.
    :type payment_method_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePaymentMethodInfo.from_dict(body)
    return web.Response(status=200)


async def post_merchants_merchant_id_payment_method_settings(request: web.Request, merchant_id, body=None) -> web.Response:
    """Request a payment method

    Sends a request to add a new payment method to the merchant account identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read and write 

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentMethodSetupInfo.from_dict(body)
    return web.Response(status=200)


async def post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains(request: web.Request, merchant_id, payment_method_id, body=None) -> web.Response:
    """Add an Apple Pay domain

    Adds the new domain to the list of Apple Pay domains that are registered with the merchant account and the payment method identified in the path. For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/enable-apple-pay#register-merchant-domain).  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read and write 

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param payment_method_id: The unique identifier of the payment method.
    :type payment_method_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApplePayInfo.from_dict(body)
    return web.Response(status=200)
