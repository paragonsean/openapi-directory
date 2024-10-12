from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_warehouse_request_body import CreateWarehouseRequestBody
from openapi_server.models.create_warehouse_response_body import CreateWarehouseResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_warehouse_by_id_response_body import GetWarehouseByIdResponseBody
from openapi_server.models.list_warehouses_response_body import ListWarehousesResponseBody
from openapi_server.models.update_warehouse_request_body import UpdateWarehouseRequestBody
from openapi_server.models.update_warehouse_settings_request_body import UpdateWarehouseSettingsRequestBody
from openapi_server import util


async def create_warehouse(request: web.Request, body) -> web.Response:
    """Create Warehouse

    Create a warehouse location that you can use to create shipping items by simply passing in the generated warehouse id. If the return address is not supplied in the request body then it is assumed that the origin address is the return address as well 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateWarehouseRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_warehouse(request: web.Request, warehouse_id) -> web.Response:
    """Delete Warehouse By ID

    Delete a warehouse by ID

    :param warehouse_id: Warehouse ID
    :type warehouse_id: str

    """
    return web.Response(status=200)


async def get_warehouse_by_id(request: web.Request, warehouse_id) -> web.Response:
    """Get Warehouse By Id

    Retrieve warehouse data based on the warehouse ID

    :param warehouse_id: Warehouse ID
    :type warehouse_id: str

    """
    return web.Response(status=200)


async def list_warehouses(request: web.Request, ) -> web.Response:
    """List Warehouses

    Retrieve a list of warehouses associated with this account.


    """
    return web.Response(status=200)


async def update_warehouse(request: web.Request, warehouse_id, body) -> web.Response:
    """Update Warehouse By Id

    Update Warehouse object information

    :param warehouse_id: Warehouse ID
    :type warehouse_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateWarehouseRequestBody.from_dict(body)
    return web.Response(status=200)


async def update_warehouse_settings(request: web.Request, warehouse_id, body) -> web.Response:
    """Update Warehouse Settings

    Update Warehouse settings object information

    :param warehouse_id: Warehouse ID
    :type warehouse_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateWarehouseSettingsRequestBody.from_dict(body)
    return web.Response(status=200)
