from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_cross_border_credit_transfers_payment_status_ok_body import PostPaymentsCrossBorderCreditTransfersPaymentStatusOKBody
from openapi_server.models.post_payments_cross_border_credit_transfers_payment_status_params_body import PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody
from openapi_server import util


async def payments_cross_border_credit_transfers_payment_status_post(request: web.Request, body) -> web.Response:
    """Get payment status

    

    :param body: Request Body
    :type body: dict | bytes

    """
    body = PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody.from_dict(body)
    return web.Response(status=200)
