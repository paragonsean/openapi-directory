from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_cross_border_credit_transfers_consents_ok_body import PostPaymentsCrossBorderCreditTransfersConsentsOKBody
from openapi_server.models.post_payments_cross_border_credit_transfers_consents_params_body import PostPaymentsCrossBorderCreditTransfersConsentsParamsBody
from openapi_server import util


async def payments_cross_border_credit_transfers_consents_post(request: web.Request, body) -> web.Response:
    """Request consent initiation via redirect

    

    :param body: Cross border payment consent
    :type body: dict | bytes

    """
    body = PostPaymentsCrossBorderCreditTransfersConsentsParamsBody.from_dict(body)
    return web.Response(status=200)
