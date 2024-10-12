from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_gift_card_request import CreateGiftCardRequest
from openapi_server.models.create_gift_card_response import CreateGiftCardResponse
from openapi_server.models.link_customer_to_gift_card_request import LinkCustomerToGiftCardRequest
from openapi_server.models.link_customer_to_gift_card_response import LinkCustomerToGiftCardResponse
from openapi_server.models.list_gift_cards_response import ListGiftCardsResponse
from openapi_server.models.retrieve_gift_card_from_gan_request import RetrieveGiftCardFromGANRequest
from openapi_server.models.retrieve_gift_card_from_gan_response import RetrieveGiftCardFromGANResponse
from openapi_server.models.retrieve_gift_card_from_nonce_request import RetrieveGiftCardFromNonceRequest
from openapi_server.models.retrieve_gift_card_from_nonce_response import RetrieveGiftCardFromNonceResponse
from openapi_server.models.retrieve_gift_card_response import RetrieveGiftCardResponse
from openapi_server.models.unlink_customer_from_gift_card_request import UnlinkCustomerFromGiftCardRequest
from openapi_server.models.unlink_customer_from_gift_card_response import UnlinkCustomerFromGiftCardResponse
from openapi_server import util


async def create_gift_card(request: web.Request, body) -> web.Response:
    """CreateGiftCard

    Creates a digital gift card or registers a physical (plastic) gift card. You must activate the gift card before  it can be used for payment. For more information, see  [Selling gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#selling-square-gift-cards).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateGiftCardRequest.from_dict(body)
    return web.Response(status=200)


async def link_customer_to_gift_card(request: web.Request, gift_card_id, body) -> web.Response:
    """LinkCustomerToGiftCard

    Links a customer to a gift card

    :param gift_card_id: The ID of the gift card to link.
    :type gift_card_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = LinkCustomerToGiftCardRequest.from_dict(body)
    return web.Response(status=200)


async def list_gift_cards(request: web.Request, type=None, state=None, limit=None, cursor=None, customer_id=None) -> web.Response:
    """ListGiftCards

    Lists all gift cards. You can specify optional filters to retrieve  a subset of the gift cards.

    :param type: If a type is provided, gift cards of this type are returned  (see [GiftCardType](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardType)). If no type is provided, it returns gift cards of all types.
    :type type: str
    :param state: If the state is provided, it returns the gift cards in the specified state  (see [GiftCardStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardStatus)). Otherwise, it returns the gift cards of all states.
    :type state: str
    :param limit: If a value is provided, it returns only that number of results per page. The maximum number of results allowed per page is 50. The default value is 30.
    :type limit: int
    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. If a cursor is not provided, it returns the first page of the results.  For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination).
    :type cursor: str
    :param customer_id: If a value is provided, returns only the gift cards linked to the specified customer
    :type customer_id: str

    """
    return web.Response(status=200)


async def retrieve_gift_card(request: web.Request, id) -> web.Response:
    """RetrieveGiftCard

    Retrieves a gift card using its ID.

    :param id: The ID of the gift card to retrieve.
    :type id: str

    """
    return web.Response(status=200)


async def retrieve_gift_card_from_gan(request: web.Request, body) -> web.Response:
    """RetrieveGiftCardFromGAN

    Retrieves a gift card using the gift card account number (GAN).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = RetrieveGiftCardFromGANRequest.from_dict(body)
    return web.Response(status=200)


async def retrieve_gift_card_from_nonce(request: web.Request, body) -> web.Response:
    """RetrieveGiftCardFromNonce

    Retrieves a gift card using a nonce (a secure token) that represents the gift card.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = RetrieveGiftCardFromNonceRequest.from_dict(body)
    return web.Response(status=200)


async def unlink_customer_from_gift_card(request: web.Request, gift_card_id, body) -> web.Response:
    """UnlinkCustomerFromGiftCard

    Unlinks a customer from a gift card

    :param gift_card_id: 
    :type gift_card_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UnlinkCustomerFromGiftCardRequest.from_dict(body)
    return web.Response(status=200)
