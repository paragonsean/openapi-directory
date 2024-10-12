from typing import List, Dict
from aiohttp import web

from openapi_server.models.shop_put_request import ShopPutRequest
from openapi_server import util


async def shop_get(request: web.Request, ) -> web.Response:
    """Get your own shop details

    Get your own shop details


    """
    return web.Response(status=200)


async def shop_listing_conditions_get(request: web.Request, ) -> web.Response:
    """List of supported product conditions

    List of supported product conditions


    """
    return web.Response(status=200)


async def shop_payment_methods_get(request: web.Request, ) -> web.Response:
    """Get accepted payment methods

    Get accepted payment methods


    """
    return web.Response(status=200)


async def shop_put(request: web.Request, body=None) -> web.Response:
    """Update your shop profile

    Update your shop profile

    :param body: the content of the request
    :type body: dict | bytes

    """
    body = ShopPutRequest.from_dict(body)
    return web.Response(status=200)


async def shop_vacation_delete(request: web.Request, ) -> web.Response:
    """Disable vacation mode. All listings will be re-enabled.

    Disable vacation mode. All listings will be re-enabled.


    """
    return web.Response(status=200)


async def shop_vacation_get(request: web.Request, ) -> web.Response:
    """Returns shop vacation status

    Returns shop vacation status


    """
    return web.Response(status=200)


async def shop_vacation_post(request: web.Request, ) -> web.Response:
    """Enable vacation mode. All listings will be unavailable until vacation mode is turned off.

    Enable vacation mode. All listings will be unavailable until vacation mode is turned off.


    """
    return web.Response(status=200)
