from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_domestic_credit_transfers_consents_ok_body import PostPaymentsDomesticCreditTransfersConsentsOKBody
from openapi_server.models.post_payments_domestic_credit_transfers_consents_params_body import PostPaymentsDomesticCreditTransfersConsentsParamsBody
from openapi_server import util


async def payments_domestic_credit_transfers_consents_post(request: web.Request, body) -> web.Response:
    """Request consent initiation via redirect

    Request Payment Initiation Consent for a domestic credit transfer on behalf of the PSU.

    :param body: Domestic Payment consent to be wired via Faster Payment System
    :type body: dict | bytes

    """
    body = PostPaymentsDomesticCreditTransfersConsentsParamsBody.from_dict(body)
    return web.Response(status=200)
