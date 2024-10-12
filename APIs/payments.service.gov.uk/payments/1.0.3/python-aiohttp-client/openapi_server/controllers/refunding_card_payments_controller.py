from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.payment_error import PaymentError
from openapi_server.models.payment_refund_request import PaymentRefundRequest
from openapi_server.models.refund import Refund
from openapi_server.models.refund_error import RefundError
from openapi_server.models.refund_for_search_result import RefundForSearchResult
from openapi_server.models.refund_search_results import RefundSearchResults
from openapi_server import util


async def get_a_payment_refund(request: web.Request, payment_id, refund_id) -> web.Response:
    """Find payment refund by ID

    Return payment refund information by Refund ID The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

    :param payment_id: 
    :type payment_id: str
    :param refund_id: 
    :type refund_id: str

    """
    return web.Response(status=200)


async def get_all_refunds_for_a_payment(request: web.Request, payment_id) -> web.Response:
    """Get all refunds for a payment

    Return refunds for a payment. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

    :param payment_id: 
    :type payment_id: str

    """
    return web.Response(status=200)


async def search_refunds(request: web.Request, from_date=None, to_date=None, from_settled_date=None, to_settled_date=None, page=None, display_size=None) -> web.Response:
    """Search refunds

    Search refunds by &#39;from&#39; and &#39;to&#39; date. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

    :param from_date: From date of refunds to be searched (this date is inclusive). Example&#x3D;2015-08-13T12:35:00Z
    :type from_date: str
    :param to_date: To date of refunds to be searched (this date is exclusive). Example&#x3D;2015-08-14T12:35:00Z
    :type to_date: str
    :param from_settled_date: From settled date of refund to be searched (this date is inclusive). Example&#x3D;2015-08-13
    :type from_settled_date: str
    :param to_settled_date: To settled date of refund to be searched (this date is inclusive). Example&#x3D;2015-08-13
    :type to_settled_date: str
    :param page: Page number requested for the search, should be a positive integer (optional, defaults to 1)
    :type page: str
    :param display_size: Number of results to be shown per page, should be a positive integer (optional, defaults to 500, max 500)
    :type display_size: str

    """
    return web.Response(status=200)


async def submit_a_refund_for_a_payment(request: web.Request, payment_id, body) -> web.Response:
    """Submit a refund for a payment

    Return issued refund information. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

    :param payment_id: paymentId
    :type payment_id: str
    :param body: requestPayload
    :type body: dict | bytes

    """
    body = PaymentRefundRequest.from_dict(body)
    return web.Response(status=200)
