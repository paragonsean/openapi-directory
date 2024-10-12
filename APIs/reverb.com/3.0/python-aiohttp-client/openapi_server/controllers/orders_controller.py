from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def orders_order_id_feedback_buyer_get(request: web.Request, order_id) -> web.Response:
    """Feedback details for an order&#39;s buyer

    Feedback details for an order&#39;s buyer

    :param order_id: 
    :type order_id: str

    """
    return web.Response(status=200)


async def orders_order_id_feedback_buyer_post(request: web.Request, order_id) -> web.Response:
    """Add feedback about an order&#39;s buyer

    Add feedback about an order&#39;s buyer

    :param order_id: 
    :type order_id: str

    """
    return web.Response(status=200)


async def orders_order_id_feedback_seller_get(request: web.Request, order_id) -> web.Response:
    """Feedback details for an order&#39;s seller

    Feedback details for an order&#39;s seller

    :param order_id: 
    :type order_id: str

    """
    return web.Response(status=200)


async def orders_order_id_feedback_seller_post(request: web.Request, order_id) -> web.Response:
    """Add feedback about an order&#39;s seller

    Add feedback about an order&#39;s seller

    :param order_id: 
    :type order_id: str

    """
    return web.Response(status=200)
