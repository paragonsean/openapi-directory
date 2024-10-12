from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.order_list_full import OrderListFull
from openapi_server.models.order_list_light import OrderListLight
from openapi_server.models.order_list_request import OrderListRequest
from openapi_server import util


async def get_order_list_full(request: web.Request, accept_encoding, body) -> web.Response:
    """[DEPRECATED] Get a paginated list of all Orders with all Order and Order Item(s) properties

    DEPRECATED - Use /orders/v3 instead The purpose of this operation is to reduce the amount of request to the API.\\ \\ Previous implmentation of this feature only returned a partial (light) version of the Orders. The purpose of this API is to reduce the number of incoming requests by returning the complete (full) Order and Order Item(s) properties. 

    :param accept_encoding: Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size
    :type accept_encoding: List[str]
    :param body: 
    :type body: dict | bytes

    """
    body = OrderListRequest.from_dict(body)
    return web.Response(status=200)


async def get_order_list_light(request: web.Request, body) -> web.Response:
    """[DEPRECATED] Get a paginated list of all Orders without details

    Use /orders/v3 instead

    :param body: 
    :type body: dict | bytes

    """
    body = OrderListRequest.from_dict(body)
    return web.Response(status=200)
