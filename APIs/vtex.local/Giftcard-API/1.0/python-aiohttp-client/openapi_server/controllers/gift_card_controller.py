from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_gift_card_request import CreateGiftCardRequest
from openapi_server.models.get_gift_cardusing_json_request import GetGiftCardusingJSONRequest
from openapi_server.models.response import Response
from openapi_server.models.response2 import Response2
from openapi_server import util


async def create_gift_card(request: web.Request, content_type, accept, x_vtex_api_app_key, x_vtex_api_app_token, body) -> web.Response:
    """Create GiftCard

    Creates a GiftCard for a specific user

    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param x_vtex_api_app_key: The AppKey configured by the merchant
    :type x_vtex_api_app_key: str
    :param x_vtex_api_app_token: The AppToken configured by the merchant
    :type x_vtex_api_app_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateGiftCardRequest.from_dict(body)
    return web.Response(status=200)


async def get_gift_cardby_id(request: web.Request, accept, content_type, gift_card_id) -> web.Response:
    """Get GiftCard by ID

    Returns associated data for a specified giftcardId.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param gift_card_id: 
    :type gift_card_id: str

    """
    return web.Response(status=200)


async def get_gift_cardusing_json(request: web.Request, accept, content_type, body, rest_range=None) -> web.Response:
    """Get GiftCard using JSON

    Returns the giftcards based on the cart data.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes
    :param rest_range: PaginationB control.B ThisB queryB variableB mustB followB theB formatB _resources&#x3D;{from}-{to}_.
    :type rest_range: str

    """
    body = GetGiftCardusingJSONRequest.from_dict(body)
    return web.Response(status=200)
