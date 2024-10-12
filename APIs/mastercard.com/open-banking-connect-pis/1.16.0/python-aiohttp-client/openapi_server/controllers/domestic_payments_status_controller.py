from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_domestic_credit_transfers_payment_status_ok_body import PostPaymentsDomesticCreditTransfersPaymentStatusOKBody
from openapi_server.models.post_payments_domestic_credit_transfers_payment_status_params_body import PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody
from openapi_server import util


async def payments_domestic_credit_transfers_payment_status_post(request: web.Request, body) -> web.Response:
    """Get payment status

    Get the status for an existing domestic credit transfer payment.

    :param body: Request Body
    :type body: dict | bytes

    """
    body = PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody.from_dict(body)
    return web.Response(status=200)
