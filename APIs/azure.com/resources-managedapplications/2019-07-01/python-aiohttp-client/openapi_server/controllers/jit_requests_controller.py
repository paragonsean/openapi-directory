from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.jit_request_definition import JitRequestDefinition
from openapi_server.models.jit_request_definition_list_result import JitRequestDefinitionListResult
from openapi_server.models.jit_request_patchable import JitRequestPatchable
from openapi_server import util


async def jit_requests_create_or_update(request: web.Request, resource_group_name, jit_request_name, api_version, subscription_id, parameters) -> web.Response:
    """jit_requests_create_or_update

    Creates or updates the JIT request.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param jit_request_name: The name of the JIT request.
    :type jit_request_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to the update JIT request.
    :type parameters: dict | bytes

    """
    parameters = JitRequestDefinition.from_dict(parameters)
    return web.Response(status=200)


async def jit_requests_delete(request: web.Request, resource_group_name, jit_request_name, api_version, subscription_id) -> web.Response:
    """jit_requests_delete

    Deletes the JIT request.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param jit_request_name: The name of the JIT request.
    :type jit_request_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def jit_requests_get(request: web.Request, resource_group_name, jit_request_name, api_version, subscription_id) -> web.Response:
    """jit_requests_get

    Gets the JIT request.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param jit_request_name: The name of the JIT request.
    :type jit_request_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def jit_requests_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """jit_requests_list_by_resource_group

    Retrieves all JIT requests within the resource group.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def jit_requests_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """jit_requests_list_by_subscription

    Retrieves all JIT requests within the subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def jit_requests_update(request: web.Request, resource_group_name, jit_request_name, api_version, subscription_id, parameters) -> web.Response:
    """jit_requests_update

    Updates the JIT request.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param jit_request_name: The name of the JIT request.
    :type jit_request_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to the update JIT request.
    :type parameters: dict | bytes

    """
    parameters = JitRequestPatchable.from_dict(parameters)
    return web.Response(status=200)
