from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancel_gift_card_transaction_request import CancelGiftCardTransactionRequest
from openapi_server.models.create_gift_card_transaction_request import CreateGiftCardTransactionRequest
from openapi_server.models.response3 import Response3
from openapi_server.models.response5 import Response5
from openapi_server.models.response6 import Response6
from openapi_server.models.response7 import Response7
from openapi_server.models.settle_gift_card_transaction_request import SettleGiftCardTransactionRequest
from openapi_server import util


async def cancel_gift_card_transaction(request: web.Request, accept, content_type, gift_card_id, transaction_id, body) -> web.Response:
    """Cancel GiftCard Transaction

    Creates a cancellation in the transaction. Cancel a item reservation or create a refund.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param gift_card_id: 
    :type gift_card_id: str
    :param transaction_id: 
    :type transaction_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CancelGiftCardTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def create_gift_card_transaction(request: web.Request, accept, content_type, gift_card_id, body=None) -> web.Response:
    """Create GiftCard Transaction

    Register a new giftcard transaction and authorize the item reservation.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param gift_card_id: 
    :type gift_card_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateGiftCardTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def get_gift_card_transactionby_id(request: web.Request, accept, content_type, gift_card_id, transaction_id) -> web.Response:
    """Get GiftCard Transaction by ID

    

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param gift_card_id: 
    :type gift_card_id: str
    :param transaction_id: 
    :type transaction_id: str

    """
    return web.Response(status=200)


async def get_gift_card_transactions(request: web.Request, accept, content_type, gift_card_id) -> web.Response:
    """Get GiftCard Transactions

    Returns all transaction of a giftcard.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param gift_card_id: 
    :type gift_card_id: str

    """
    return web.Response(status=200)


async def get_transaction_authorizations(request: web.Request, accept, content_type, gift_card_id, transaction_id) -> web.Response:
    """Get Transaction Authorizations

    Returns the giftcard transaction authorizations.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param gift_card_id: 
    :type gift_card_id: str
    :param transaction_id: 
    :type transaction_id: str

    """
    return web.Response(status=200)


async def get_transaction_cancellations(request: web.Request, accept, content_type, gift_card_id, transaction_id) -> web.Response:
    """Get Transaction Cancellations

    Returns the giftcard transaction cancellations.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param gift_card_id: 
    :type gift_card_id: str
    :param transaction_id: 
    :type transaction_id: str

    """
    return web.Response(status=200)


async def get_transaction_settlements(request: web.Request, accept, content_type, gift_card_id, transaction_id) -> web.Response:
    """Get Transaction Settlements

    Returns the giftcard transaction settlements.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param gift_card_id: 
    :type gift_card_id: str
    :param transaction_id: 
    :type transaction_id: str

    """
    return web.Response(status=200)


async def settle_gift_card_transaction(request: web.Request, accept, content_type, gift_card_id, transaction_id, body) -> web.Response:
    """Settle GiftCard Transaction

    Creates a giftcard transaction settlement.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param gift_card_id: 
    :type gift_card_id: str
    :param transaction_id: 
    :type transaction_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SettleGiftCardTransactionRequest.from_dict(body)
    return web.Response(status=200)
