from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_domestic_credit_transfers_ok_body import PostPaymentsDomesticCreditTransfersOKBody
from openapi_server.models.post_payments_domestic_credit_transfers_params_body import PostPaymentsDomesticCreditTransfersParamsBody
from openapi_server import util


async def payments_domestic_credit_transfers_post(request: web.Request, body) -> web.Response:
    """Redeem the payment

    Redeem the payment which was previously consented by the PSU.

    :param body: Request Body
    :type body: dict | bytes

    """
    body = PostPaymentsDomesticCreditTransfersParamsBody.from_dict(body)
    return web.Response(status=200)
