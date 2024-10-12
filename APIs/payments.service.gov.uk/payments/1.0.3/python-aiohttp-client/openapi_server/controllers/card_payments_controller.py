from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_card_payment_request import CreateCardPaymentRequest
from openapi_server.models.create_payment_result import CreatePaymentResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_payment_result import GetPaymentResult
from openapi_server.models.payment_error import PaymentError
from openapi_server.models.payment_events import PaymentEvents
from openapi_server.models.payment_search_results import PaymentSearchResults
from openapi_server import util


async def cancel_a_payment(request: web.Request, payment_id) -> web.Response:
    """Cancel payment

    Cancel a payment based on the provided payment ID and the Authorisation token. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;. A payment can only be cancelled if it&#39;s in a state that isn&#39;t finished.

    :param payment_id: Payment identifier
    :type payment_id: str

    """
    return web.Response(status=200)


async def capture_a_payment(request: web.Request, payment_id) -> web.Response:
    """Capture payment

    Capture a payment based on the provided payment ID and the Authorisation token. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;. A payment can only be captured if it&#39;s in &#39;submitted&#39; state

    :param payment_id: Payment identifier
    :type payment_id: str

    """
    return web.Response(status=200)


async def create_a_payment(request: web.Request, body) -> web.Response:
    """Create new payment

    Create a new payment for the account associated to the Authorisation token. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

    :param body: requestPayload
    :type body: dict | bytes

    """
    body = CreateCardPaymentRequest.from_dict(body)
    return web.Response(status=200)


async def get_a_payment(request: web.Request, payment_id) -> web.Response:
    """Find payment by ID

    Return information about the payment The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

    :param payment_id: Payment identifier
    :type payment_id: str

    """
    return web.Response(status=200)


async def get_events_for_a_payment(request: web.Request, payment_id) -> web.Response:
    """Return payment events by ID

    Return payment events information about a certain payment The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

    :param payment_id: Payment identifier
    :type payment_id: str

    """
    return web.Response(status=200)


async def search_payments(request: web.Request, reference=None, email=None, state=None, card_brand=None, from_date=None, to_date=None, page=None, display_size=None, cardholder_name=None, first_digits_card_number=None, last_digits_card_number=None, from_settled_date=None, to_settled_date=None) -> web.Response:
    """Search payments

    Search payments by reference, state, &#39;from&#39; and &#39;to&#39; date. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

    :param reference: Your payment reference to search (exact match, case insensitive)
    :type reference: str
    :param email: The user email used in the payment to be searched
    :type email: str
    :param state: State of payments to be searched. Example&#x3D;success
    :type state: str
    :param card_brand: Card brand used for payment. Example&#x3D;master-card
    :type card_brand: str
    :param from_date: From date of payments to be searched (this date is inclusive). Example&#x3D;2015-08-13T12:35:00Z
    :type from_date: str
    :param to_date: To date of payments to be searched (this date is exclusive). Example&#x3D;2015-08-14T12:35:00Z
    :type to_date: str
    :param page: Page number requested for the search, should be a positive integer (optional, defaults to 1)
    :type page: str
    :param display_size: Number of results to be shown per page, should be a positive integer (optional, defaults to 500, max 500)
    :type display_size: str
    :param cardholder_name: Name on card used to make payment
    :type cardholder_name: str
    :param first_digits_card_number: First six digits of the card used to make payment
    :type first_digits_card_number: str
    :param last_digits_card_number: Last four digits of the card used to make payment
    :type last_digits_card_number: str
    :param from_settled_date: From settled date of payment to be searched (this date is inclusive). Example&#x3D;2015-08-13
    :type from_settled_date: str
    :param to_settled_date: To settled date of payment to be searched (this date is inclusive). Example&#x3D;2015-08-14
    :type to_settled_date: str

    """
    return web.Response(status=200)
