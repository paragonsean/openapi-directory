from typing import List, Dict
from aiohttp import web

from openapi_server.models.basket_info200_response import BasketInfo200Response
from openapi_server.models.basket_item_add200_response import BasketItemAdd200Response
from openapi_server.models.basket_live_shipping_service_create200_response import BasketLiveShippingServiceCreate200Response
from openapi_server.models.basket_live_shipping_service_delete200_response import BasketLiveShippingServiceDelete200Response
from openapi_server.models.basket_live_shipping_service_list200_response import BasketLiveShippingServiceList200Response
from openapi_server import util


async def basket_info(request: web.Request, id, store_id=None, params=None, exclude=None, response_fields=None) -> web.Response:
    """basket_info

    Retrieve basket information.

    :param id: Entity id
    :type id: str
    :param store_id: Store Id
    :type store_id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str

    """
    return web.Response(status=200)


async def basket_item_add(request: web.Request, customer_id, product_id, variant_id=None, quantity=None, store_id=None) -> web.Response:
    """basket_item_add

    Add item to basket

    :param customer_id: Retrieves orders specified by customer id
    :type customer_id: str
    :param product_id: Defines id of the product which should be added to the basket
    :type product_id: str
    :param variant_id: Defines product&#39;s variants specified by variant id
    :type variant_id: str
    :param quantity: Defines new items quantity
    :type quantity: 
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def basket_live_shipping_service_create(request: web.Request, name, param_callback, store_id=None) -> web.Response:
    """basket_live_shipping_service_create

    Create live shipping rate service.

    :param name: Shipping Service Name
    :type name: str
    :param param_callback: Callback url that returns shipping rates. It should be able to accept POST requests with json data.
    :type param_callback: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def basket_live_shipping_service_delete(request: web.Request, id) -> web.Response:
    """basket_live_shipping_service_delete

    Delete live shipping rate service.

    :param id: Entity id
    :type id: int

    """
    return web.Response(status=200)


async def basket_live_shipping_service_list(request: web.Request, store_id=None, start=None, count=None) -> web.Response:
    """basket_live_shipping_service_list

    Retrieve a list of live shipping rate services.

    :param store_id: Store Id
    :type store_id: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int

    """
    return web.Response(status=200)
