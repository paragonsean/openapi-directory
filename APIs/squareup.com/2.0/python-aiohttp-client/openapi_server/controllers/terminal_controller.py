from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancel_terminal_checkout_response import CancelTerminalCheckoutResponse
from openapi_server.models.cancel_terminal_refund_response import CancelTerminalRefundResponse
from openapi_server.models.create_terminal_checkout_request import CreateTerminalCheckoutRequest
from openapi_server.models.create_terminal_checkout_response import CreateTerminalCheckoutResponse
from openapi_server.models.create_terminal_refund_request import CreateTerminalRefundRequest
from openapi_server.models.create_terminal_refund_response import CreateTerminalRefundResponse
from openapi_server.models.get_terminal_checkout_response import GetTerminalCheckoutResponse
from openapi_server.models.get_terminal_refund_response import GetTerminalRefundResponse
from openapi_server.models.search_terminal_checkouts_request import SearchTerminalCheckoutsRequest
from openapi_server.models.search_terminal_checkouts_response import SearchTerminalCheckoutsResponse
from openapi_server.models.search_terminal_refunds_request import SearchTerminalRefundsRequest
from openapi_server.models.search_terminal_refunds_response import SearchTerminalRefundsResponse
from openapi_server import util


async def cancel_terminal_checkout(request: web.Request, checkout_id) -> web.Response:
    """CancelTerminalCheckout

    Cancels a Terminal checkout request if the status of the request permits it.

    :param checkout_id: The unique ID for the desired &#x60;TerminalCheckout&#x60;.
    :type checkout_id: str

    """
    return web.Response(status=200)


async def cancel_terminal_refund(request: web.Request, terminal_refund_id) -> web.Response:
    """CancelTerminalRefund

    Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

    :param terminal_refund_id: The unique ID for the desired &#x60;TerminalRefund&#x60;.
    :type terminal_refund_id: str

    """
    return web.Response(status=200)


async def create_terminal_checkout(request: web.Request, body) -> web.Response:
    """CreateTerminalCheckout

    Creates a Terminal checkout request and sends it to the specified device to take a payment for the requested amount.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateTerminalCheckoutRequest.from_dict(body)
    return web.Response(status=200)


async def create_terminal_refund(request: web.Request, body) -> web.Response:
    """CreateTerminalRefund

    Creates a request to refund an Interac payment completed on a Square Terminal.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateTerminalRefundRequest.from_dict(body)
    return web.Response(status=200)


async def get_terminal_checkout(request: web.Request, checkout_id) -> web.Response:
    """GetTerminalCheckout

    Retrieves a Terminal checkout request by &#x60;checkout_id&#x60;.

    :param checkout_id: The unique ID for the desired &#x60;TerminalCheckout&#x60;.
    :type checkout_id: str

    """
    return web.Response(status=200)


async def get_terminal_refund(request: web.Request, terminal_refund_id) -> web.Response:
    """GetTerminalRefund

    Retrieves an Interac Terminal refund object by ID.

    :param terminal_refund_id: The unique ID for the desired &#x60;TerminalRefund&#x60;.
    :type terminal_refund_id: str

    """
    return web.Response(status=200)


async def search_terminal_checkouts(request: web.Request, body) -> web.Response:
    """SearchTerminalCheckouts

    Retrieves a filtered list of Terminal checkout requests created by the account making the request.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchTerminalCheckoutsRequest.from_dict(body)
    return web.Response(status=200)


async def search_terminal_refunds(request: web.Request, body) -> web.Response:
    """SearchTerminalRefunds

    Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchTerminalRefundsRequest.from_dict(body)
    return web.Response(status=200)
