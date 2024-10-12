from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_permission_group_request import CreatePermissionGroupRequest
from openapi_server.models.permission_group_model import PermissionGroupModel
from openapi_server.models.permission_group_model_haljson import PermissionGroupModelHaljson
from openapi_server.models.update_permission_group_request import UpdatePermissionGroupRequest
from openapi_server import util


async def create_permission_group(request: web.Request, product_id, body) -> web.Response:
    """Create Permission Group

    This endpoint creates a new Permission Group in a specified Product  identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreatePermissionGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_permission_group(request: web.Request, permission_group_id) -> web.Response:
    """Delete Permission Group

    This endpoint removes a Permission Group identified by the &#x60;permissionGroupId&#x60; parameter.

    :param permission_group_id: The identifier of the Permission Group.
    :type permission_group_id: int

    """
    return web.Response(status=200)


async def get_permission_group(request: web.Request, permission_group_id) -> web.Response:
    """Get Permission Group

    This endpoint returns the metadata of a Permission Group  identified by the &#x60;permissionGroupId&#x60;.

    :param permission_group_id: The identifier of the Permission Group.
    :type permission_group_id: int

    """
    return web.Response(status=200)


async def get_permission_groups(request: web.Request, product_id) -> web.Response:
    """List Permission Groups

    This endpoint returns the list of the Permission Groups that belongs to the given Product identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str

    """
    return web.Response(status=200)


async def update_permission_group(request: web.Request, permission_group_id, body) -> web.Response:
    """Update Permission Group

    This endpoint updates a Permission Group identified by the &#x60;permissionGroupId&#x60; parameter.

    :param permission_group_id: The identifier of the Permission Group.
    :type permission_group_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePermissionGroupRequest.from_dict(body)
    return web.Response(status=200)
