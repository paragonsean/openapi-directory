from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_result_payment_link import ListResultPaymentLink
from openapi_server.models.payment_link import PaymentLink
from openapi_server.models.payment_link_uri_api_model import PaymentLinkUriApiModel
from openapi_server import util


async def payment_link_api_all(request: web.Request, x_auth_key, x_auth_secret, query_options_page=None, query_options_page_size=None) -> web.Response:
    """Create a payment link

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param query_options_page: 
    :type query_options_page: int
    :param query_options_page_size: 
    :type query_options_page_size: int

    """
    return web.Response(status=200)


async def payment_link_api_delete(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Delete an existing payment link

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentLink.from_dict(body)
    return web.Response(status=200)


async def payment_link_api_new(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Create a payment link

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentLink.from_dict(body)
    return web.Response(status=200)


async def payment_link_api_uri(request: web.Request, id, x_auth_key, x_auth_secret) -> web.Response:
    """Return the unique url to the client&#39;s payment link

    

    :param id: 
    :type id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)
