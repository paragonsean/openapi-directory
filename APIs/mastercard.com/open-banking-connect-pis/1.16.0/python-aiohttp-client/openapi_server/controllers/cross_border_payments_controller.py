from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_cross_border_credit_transfers_ok_body import PostPaymentsCrossBorderCreditTransfersOKBody
from openapi_server.models.post_payments_cross_border_credit_transfers_params_body import PostPaymentsCrossBorderCreditTransfersParamsBody
from openapi_server import util


async def payments_cross_border_credit_transfers_post(request: web.Request, body) -> web.Response:
    """Redeem the payment

    

    :param body: Request Body
    :type body: dict | bytes

    """
    body = PostPaymentsCrossBorderCreditTransfersParamsBody.from_dict(body)
    return web.Response(status=200)
