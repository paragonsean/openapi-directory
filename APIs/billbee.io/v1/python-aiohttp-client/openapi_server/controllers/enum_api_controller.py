from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def enum_api_get_order_states(request: web.Request, ) -> web.Response:
    """Returns a list with all defined orderstates

    


    """
    return web.Response(status=200)


async def enum_api_get_payment_types(request: web.Request, ) -> web.Response:
    """Returns a list with all defined paymenttypes

    


    """
    return web.Response(status=200)


async def enum_api_get_shipment_types(request: web.Request, ) -> web.Response:
    """Returns a list with all defined shipmenttypes

    


    """
    return web.Response(status=200)


async def enum_api_get_shipping_carriers(request: web.Request, ) -> web.Response:
    """Returns a list with all defined shippingcarriers

    


    """
    return web.Response(status=200)
