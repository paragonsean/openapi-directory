from typing import List, Dict
from aiohttp import web

from openapi_server.models.payout_request import PayoutRequest
from openapi_server.models.payout_response import PayoutResponse
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def post_payout(request: web.Request, body=None) -> web.Response:
    """Make an instant card payout

    With this call, you can pay out to your customers, and funds will be made available within 30 minutes on the cardholder&#39;s bank account (this is dependent on whether the issuer supports this functionality). Instant card payouts are only supported for Visa and Mastercard cards.

    :param body: 
    :type body: dict | bytes

    """
    body = PayoutRequest.from_dict(body)
    return web.Response(status=200)
