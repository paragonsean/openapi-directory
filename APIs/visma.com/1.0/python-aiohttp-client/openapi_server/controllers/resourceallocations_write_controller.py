from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.resource_allocation_input_model import ResourceAllocationInputModel
from openapi_server.models.resource_allocation_output_model import ResourceAllocationOutputModel
from openapi_server.models.role_allocation_input_model import RoleAllocationInputModel
from openapi_server.models.role_allocation_output_model import RoleAllocationOutputModel
from openapi_server import util


async def resource_allocations_patch_resource_allocation(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a resource allocation or a part of it

    

    :param guid: ID of the resource allocation
    :type guid: str
    :param body: JSON Patch document of ResourceAllocationModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def resource_allocations_post_resource_allocation(request: web.Request, body=None) -> web.Response:
    """Insert a resource allocation

    

    :param body: ResourceAllocationInputModel
    :type body: dict | bytes

    """
    body = ResourceAllocationInputModel.from_dict(body)
    return web.Response(status=200)


async def role_allocations_patch_role_allocation(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a role allocation.

    

    :param guid: ID of the role allocation.
    :type guid: str
    :param body: JSON Patch document of RoleAllocationModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def role_allocations_post_role_allocation(request: web.Request, body=None) -> web.Response:
    """Insert a role allocation.

    

    :param body: Role allocation to insert.
    :type body: dict | bytes

    """
    body = RoleAllocationInputModel.from_dict(body)
    return web.Response(status=200)
