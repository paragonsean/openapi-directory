from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.order_detail_vo import OrderDetailVO
from openapi_server.models.order_detail_with_indicator_vo import OrderDetailWithIndicatorVO
from openapi_server.models.order_expand_workgroup_level_vo import OrderExpandWorkgroupLevelVO
from openapi_server.models.order_list_vo import OrderListVO
from openapi_server.models.order_po import OrderPO
from openapi_server.models.order_upd_persist_vo import OrderUpdPersistVO
from openapi_server.models.order_vo import OrderVO
from openapi_server.models.order_workgroup_level_list_vo import OrderWorkgroupLevelListVO
from openapi_server import util


async def get_buy_order(request: web.Request, workgroup_id, project_id, order_id) -> web.Response:
    """Get a specific buy order

    Get a specific buy order

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param order_id: 
    :type order_id: str

    """
    return web.Response(status=200)


async def get_buy_order_list(request: web.Request, workgroup_id, project_id) -> web.Response:
    """List the buy orders

    List the buy orders

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def get_buy_order_list_of_workgroup(request: web.Request, workgroup_id) -> web.Response:
    """List the buy orders of workgroup

    List the buy orders of workgroup

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_buy_order_of_workgroup(request: web.Request, workgroup_id, order_id) -> web.Response:
    """Get a specific buy order of workgroup

    Get a specific buy order of workgroup

    :param workgroup_id: 
    :type workgroup_id: str
    :param order_id: 
    :type order_id: str

    """
    return web.Response(status=200)


async def get_order(request: web.Request, workgroup_id, project_id, order_id) -> web.Response:
    """Get a specific buy/sell order

    Get a specific buy/sell order

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param order_id: 
    :type order_id: str

    """
    return web.Response(status=200)


async def get_sell_order(request: web.Request, workgroup_id, project_id, order_id) -> web.Response:
    """Get a specific sell order

    Get a specific sell order

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param order_id: 
    :type order_id: str

    """
    return web.Response(status=200)


async def get_sell_order_list(request: web.Request, workgroup_id, project_id) -> web.Response:
    """List the sell orders

    List the sell orders

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def get_sell_order_list_of_workgroup(request: web.Request, workgroup_id) -> web.Response:
    """List the sell orders of workgrop

    List the sell orders of workgrop

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_sell_order_of_workgroup(request: web.Request, workgroup_id, order_id) -> web.Response:
    """Get a specific sell order

    Get a specific sell order

    :param workgroup_id: 
    :type workgroup_id: str
    :param order_id: 
    :type order_id: str

    """
    return web.Response(status=200)


async def post_buy_order(request: web.Request, workgroup_id, project_id, body=None) -> web.Response:
    """Create a quick buy order

    Create a quick buy order

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrderPO.from_dict(body)
    return web.Response(status=200)


async def put_buy_order(request: web.Request, workgroup_id, project_id, order_id, body=None) -> web.Response:
    """Update a specific buy order

    Update a specific buy order

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param order_id: 
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrderUpdPersistVO.from_dict(body)
    return web.Response(status=200)


async def put_sell_order(request: web.Request, workgroup_id, project_id, order_id, body=None) -> web.Response:
    """Update / Accept or Reject a specific sell order

    Update / Accept or Reject a specific sell order

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param order_id: 
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrderUpdPersistVO.from_dict(body)
    return web.Response(status=200)
