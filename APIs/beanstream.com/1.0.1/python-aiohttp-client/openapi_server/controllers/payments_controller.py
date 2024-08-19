from typing import List, Dict
from aiohttp import web

from openapi_server.models.beanstream_exception import BeanstreamException
from openapi_server.models.model_return import ModelReturn
from openapi_server.models.payment_request import PaymentRequest
from openapi_server.models.payment_response import PaymentResponse
from openapi_server.models.transaction import Transaction
from openapi_server import util


async def payments_post(request: web.Request, payment_request=None) -> web.Response:
    """Make Payment

    Make a payment using credit card, cash, cheque, profile, or token. Each payment type has its own json definition passed in the body. For all payments you have the standard Billing, Shipping, Comments, etc. fields that are optional. Only the amount is required along with the payment data for card, cash, cheque, profile, and token. You must change the payment_method for each payment type. Credit Card - \&quot;card\&quot;, Payment Profile - \&quot;payment_profile\&quot;, Legato Token - \&quot;token\&quot;, Cash - \&quot;cash\&quot;, Cheque - \&quot;cheque\&quot;, Interac - \&quot;interac\&quot;

    :param payment_request: 
    :type payment_request: dict | bytes

    """
    payment_request = PaymentRequest.from_dict(payment_request)
    return web.Response(status=200)


async def payments_trans_id_completions_post(request: web.Request, trans_id, payment_request=None) -> web.Response:
    """Complete pre-auth

    Complete a pre-authorized payment. The amount of the transaction to complete must be less than or equal to the original pre-auth amount. Complete must be set to true.

    :param trans_id: The transaction id.
    :type trans_id: float
    :param payment_request: 
    :type payment_request: dict | bytes

    """
    payment_request = PaymentRequest.from_dict(payment_request)
    return web.Response(status=200)


async def payments_trans_id_get(request: web.Request, trans_id) -> web.Response:
    """Get payment

    Get a previous payment (transaction).

    :param trans_id: The transaction id.
    :type trans_id: 

    """
    return web.Response(status=200)


async def payments_trans_id_returns_post(request: web.Request, trans_id, _return) -> web.Response:
    """Return payment

    Return payment.

    :param trans_id: The transaction id.
    :type trans_id: float
    :param _return: 
    :type _return: dict | bytes

    """
    _return = ModelReturn.from_dict(_return)
    return web.Response(status=200)


async def payments_trans_id_void_post(request: web.Request, trans_id, void) -> web.Response:
    """Void Transaction

    Void a transaction. You can void payments, returns, pre-auths, and completions. It will cancel that transaction.

    :param trans_id: The transaction id to void.
    :type trans_id: float
    :param void: 
    :type void: dict | bytes

    """
    void = Void.from_dict(void)
    return web.Response(status=200)
