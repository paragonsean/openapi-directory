from typing import List, Dict
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing
from openapi_server import util


async def get_payment_method(request: web.Request, payment_method_number) -> web.Response:
    """Get Payment Method

    Return a Payment Method info by &#39;paymentMethodNumber&#39;

    :param payment_method_number: Payment method number
    :type payment_method_number: str

    """
    return web.Response(status=200)


async def list_payment_methods(request: web.Request, ) -> web.Response:
    """List Payment Methods

    Return a list of all Payment Methods for the current Vendor


    """
    return web.Response(status=200)


async def update_payment_method(request: web.Request, payment_method_number, active=None, paypal_subject=None) -> web.Response:
    """Update Payment Method

    Sets the provided properties to a Payment Method. Return an updated Payment Method

    :param payment_method_number: Payment method number
    :type payment_method_number: str
    :param active: If set to &#39;false&#39;, the Payment Method is disabled.
    :type active: bool
    :param paypal_subject: The e-mail address of the PayPal account for which you are making the API calls.
    :type paypal_subject: str

    """
    return web.Response(status=200)
