from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_pre_order_create_request import AppPreOrderCreateRequest
from openapi_server.models.app_pre_order_response import AppPreOrderResponse
from openapi_server.models.app_pre_order_update_request import AppPreOrderUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_pre_orders_create_instance(request: web.Request, body) -> web.Response:
    """app_pre_orders_create_instance

    

    :param body: AppPreOrder representation
    :type body: dict | bytes

    """
    body = AppPreOrderCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_pre_orders_delete_instance(request: web.Request, id) -> web.Response:
    """app_pre_orders_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def app_pre_orders_get_instance(request: web.Request, id, fields_app_pre_orders=None, include=None) -> web.Response:
    """app_pre_orders_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_pre_orders: the fields to include for returned resources of type appPreOrders
    :type fields_app_pre_orders: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_pre_orders_update_instance(request: web.Request, id, body) -> web.Response:
    """app_pre_orders_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: AppPreOrder representation
    :type body: dict | bytes

    """
    body = AppPreOrderUpdateRequest.from_dict(body)
    return web.Response(status=200)
