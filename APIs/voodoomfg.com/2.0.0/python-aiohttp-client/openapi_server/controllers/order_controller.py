from typing import List, Dict
from aiohttp import web

from openapi_server.models.confirm_order_body import ConfirmOrderBody
from openapi_server.models.create_order_body import CreateOrderBody
from openapi_server.models.order import Order
from openapi_server.models.order_confirm_post200_response import OrderConfirmPost200Response
from openapi_server.models.order_create_post200_response import OrderCreatePost200Response
from openapi_server.models.order_shipping_post200_response import OrderShippingPost200Response
from openapi_server.models.shipping_options_body import ShippingOptionsBody
from openapi_server import util


async def order_confirm_post(request: web.Request, body) -> web.Response:
    """Confirms an order from a quote_id and submits it to the Voodoo factory. 

    After generating a quote for an order, you can choose to confirm the order for manufacturing by hitting this endpoint with the quote_id returned by the /order/quote endpoint. Returns the order with a unique order_id in place of the quote_id. 

    :param body: 
    :type body: dict | bytes

    """
    body = ConfirmOrderBody.from_dict(body)
    return web.Response(status=200)


async def order_create_post(request: web.Request, body) -> web.Response:
    """Quotes an order and returns a quote_id that is used to confirm the order. 

    Creates an order for the requested items, shipping address, and shipping method. This method returns the order along with a quote_id, which needs to be confirmed with /order/confirm prior to the order actually being started. quote_ids are only valid for 15 minutes. 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrderBody.from_dict(body)
    return web.Response(status=200)


async def order_get(request: web.Request, ) -> web.Response:
    """Lists all orders. 

    Gets all of orders that you&#39;ve confirmed. 


    """
    return web.Response(status=200)


async def order_order_id_get(request: web.Request, order_id) -> web.Response:
    """Retrieve a previously created model by its id. 

    In cases where you&#39;re ordering models you&#39;ve created previously, you can fetch a specific model by its id. 

    :param order_id: 
    :type order_id: str

    """
    return web.Response(status=200)


async def order_shipping_post(request: web.Request, body) -> web.Response:
    """List shipping options and prices for a given shipment. 

    Get quotes for shipping your order to the given shipping address. Because shipping quotes depend on the items being shipped, you should use the same array of print descriptions here that you do to create the order.  This endpoint should allow you to select the appropriate shipping method using the \&quot;service\&quot; field of the desired shipping method. 

    :param body: 
    :type body: dict | bytes

    """
    body = ShippingOptionsBody.from_dict(body)
    return web.Response(status=200)
