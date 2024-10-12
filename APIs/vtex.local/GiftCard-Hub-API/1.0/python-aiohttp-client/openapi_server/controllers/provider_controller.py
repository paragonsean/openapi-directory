from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_gift_card_providerby_id(request: web.Request, accept, content_type, x_vtex_api_app_key, x_vtex_api_app_token, gift_card_provider_id) -> web.Response:
    """Get GiftCard Provider by ID

    Returns a giftcard provider from a store.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json.
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json.
    :type content_type: str
    :param x_vtex_api_app_key: VTEX API AppKey
    :type x_vtex_api_app_key: str
    :param x_vtex_api_app_token: VTEX API AppToken
    :type x_vtex_api_app_token: str
    :param gift_card_provider_id: Gift Card provider&#39;s ID.
    :type gift_card_provider_id: str

    """
    return web.Response(status=200)


async def list_all_gift_card_providers(request: web.Request, accept, content_type, x_vtex_api_app_key, x_vtex_api_app_token, rest_range=None) -> web.Response:
    """List All GiftCard Providers

    Returns a collection of giftcard providers from a store.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json.
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json.
    :type content_type: str
    :param x_vtex_api_app_key: VTEX API AppKey
    :type x_vtex_api_app_key: str
    :param x_vtex_api_app_token: VTEX API AppToken
    :type x_vtex_api_app_token: str
    :param rest_range: Pagination control. This query variable must follow the format _resources&#x3D;{from}-{to}_.
    :type rest_range: str

    """
    return web.Response(status=200)
