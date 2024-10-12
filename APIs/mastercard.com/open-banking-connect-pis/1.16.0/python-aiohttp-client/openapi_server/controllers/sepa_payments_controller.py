from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_sepa_credit_transfers_ok_body import PostPaymentsSepaCreditTransfersOKBody
from openapi_server.models.post_payments_sepa_credit_transfers_params_body import PostPaymentsSepaCreditTransfersParamsBody
from openapi_server import util


async def payments_sepa_credit_transfers_post(request: web.Request, body) -> web.Response:
    """Redeem the payment

    Redeem a SEPA credit transfer previously consented by the PSU.

    :param body: Request Body
    :type body: dict | bytes

    """
    body = PostPaymentsSepaCreditTransfersParamsBody.from_dict(body)
    return web.Response(status=200)
