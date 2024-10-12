from typing import List, Dict
from aiohttp import web

from openapi_server.models.merchant_cancellation200_response import MerchantCancellation200Response
from openapi_server.models.merchant_cancellation400_response import MerchantCancellation400Response
from openapi_server.models.merchant_cancellation_request import MerchantCancellationRequest
from openapi_server import util


async def merchant_cancellation(request: web.Request, accept_language, body=None) -> web.Response:
    """/merchant/cancellation

    Cancel a booking **Note**: This service has been replaced by the [cancellationReasons](#operation/cancellationReasons), [bookingQuote](#operation/bookingQuote) and [cancelBooking](#operation/cancelBooking) endpoints 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = MerchantCancellationRequest.from_dict(body)
    return web.Response(status=200)
