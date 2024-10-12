from typing import List, Dict
from aiohttp import web

from openapi_server.models.change_order_status_api_model import ChangeOrderStatusApiModel
from openapi_server.models.list_result_order_details_api_model import ListResultOrderDetailsApiModel
from openapi_server.models.order_create_api_model import OrderCreateApiModel
from openapi_server.models.order_delete_api_model import OrderDeleteApiModel
from openapi_server.models.order_full_details_api_model import OrderFullDetailsApiModel
from openapi_server.models.order_shipping_details_api_model import OrderShippingDetailsApiModel
from openapi_server import util


async def order_api_all(request: web.Request, x_auth_key, x_auth_secret, query_options_page=None, query_options_page_size=None) -> web.Response:
    """Return all orders for the account

    

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


async def order_api_change_shipping_details(request: web.Request, order_id, x_auth_key, x_auth_secret, body) -> web.Response:
    """Change order shipping details

    

    :param order_id: 
    :type order_id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrderShippingDetailsApiModel.from_dict(body)
    return web.Response(status=200)


async def order_api_change_status(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Change order status

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeOrderStatusApiModel.from_dict(body)
    return web.Response(status=200)


async def order_api_delete(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Delete an existing order

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrderDeleteApiModel.from_dict(body)
    return web.Response(status=200)


async def order_api_details(request: web.Request, id, x_auth_key, x_auth_secret) -> web.Response:
    """Return order details

    

    :param id: 
    :type id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def order_api_new(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Create an order

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrderCreateApiModel.from_dict(body)
    return web.Response(status=200)
