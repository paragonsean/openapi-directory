from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_sepa_credit_transfers_payment_status_ok_body import PostPaymentsSepaCreditTransfersPaymentStatusOKBody
from openapi_server.models.post_payments_sepa_credit_transfers_payment_status_params_body import PostPaymentsSepaCreditTransfersPaymentStatusParamsBody
from openapi_server import util


async def payments_sepa_credit_transfers_payment_status_post(request: web.Request, body) -> web.Response:
    """Get payment status

    Get the status of an existing SEPA credit transfer

    :param body: Request Body
    :type body: dict | bytes

    """
    body = PostPaymentsSepaCreditTransfersPaymentStatusParamsBody.from_dict(body)
    return web.Response(status=200)
