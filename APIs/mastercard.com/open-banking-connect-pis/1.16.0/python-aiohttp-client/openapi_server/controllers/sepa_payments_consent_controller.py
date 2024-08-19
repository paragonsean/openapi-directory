from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_sepa_credit_transfers_consents_ok_body import PostPaymentsSepaCreditTransfersConsentsOKBody
from openapi_server.models.post_payments_sepa_credit_transfers_consents_params_body import PostPaymentsSepaCreditTransfersConsentsParamsBody
from openapi_server import util


async def payments_sepa_credit_transfers_consents_post(request: web.Request, body) -> web.Response:
    """Request consent initiation via redirect

    Request a SEPA credit transfer consent on behalf of the PSU via a URL redirect to the ASPSP.

    :param body: 
    :type body: dict | bytes

    """
    body = PostPaymentsSepaCreditTransfersConsentsParamsBody.from_dict(body)
    return web.Response(status=200)
