from typing import List, Dict
from aiohttp import web

from openapi_server.models.all_warehouses200_response_inner import AllWarehouses200ResponseInner
from openapi_server.models.create_update_warehouse_request import CreateUpdateWarehouseRequest
from openapi_server.models.warehouse_by_id200_response import WarehouseById200Response
from openapi_server import util


async def activate_warehouse(request: web.Request, content_type, accept, warehouse_id) -> web.Response:
    """Activate warehouse

    Activates a given warehouse, by warehouse ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param warehouse_id: 
    :type warehouse_id: str

    """
    return web.Response(status=200)


async def all_warehouses(request: web.Request, content_type, accept) -> web.Response:
    """List all warehouses

    Lists information about all warehouses set up in your store.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str

    """
    return web.Response(status=200)


async def create_update_warehouse(request: web.Request, accept, content_type, body) -> web.Response:
    """Create/update warehouse

    Creates or updates your store&#39;s warehouses

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateUpdateWarehouseRequest.from_dict(body)
    return web.Response(status=200)


async def deactivate_warehouse(request: web.Request, content_type, accept, warehouse_id) -> web.Response:
    """Deactivate warehouse

    Deactivates a given warehouse by warehouse ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param warehouse_id: 
    :type warehouse_id: str

    """
    return web.Response(status=200)


async def remove_warehouse(request: web.Request, content_type, accept, warehouse_id) -> web.Response:
    """Remove warehouse

    Deletes given warehouse by warehouse ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param warehouse_id: 
    :type warehouse_id: str

    """
    return web.Response(status=200)


async def warehouse_by_id(request: web.Request, content_type, accept, warehouse_id) -> web.Response:
    """List warehouse by ID

    Lists the information of a given warehouse, searching by warehouse ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param warehouse_id: 
    :type warehouse_id: str

    """
    return web.Response(status=200)
