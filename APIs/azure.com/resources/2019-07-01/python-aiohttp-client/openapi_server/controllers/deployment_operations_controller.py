from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.deployment_operation import DeploymentOperation
from openapi_server.models.deployment_operations_list_result import DeploymentOperationsListResult
from openapi_server import util


async def deployment_operations_get(request: web.Request, resource_group_name, deployment_name, operation_id, api_version, subscription_id) -> web.Response:
    """deployment_operations_get

    Gets a deployments operation.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param operation_id: The ID of the operation to get.
    :type operation_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployment_operations_get_at_management_group_scope(request: web.Request, group_id, deployment_name, operation_id, api_version) -> web.Response:
    """deployment_operations_get_at_management_group_scope

    Gets a deployments operation.

    :param group_id: The management group ID.
    :type group_id: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param operation_id: The ID of the operation to get.
    :type operation_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployment_operations_get_at_scope(request: web.Request, scope, deployment_name, operation_id, api_version) -> web.Response:
    """deployment_operations_get_at_scope

    Gets a deployments operation.

    :param scope: The scope of a deployment.
    :type scope: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param operation_id: The ID of the operation to get.
    :type operation_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployment_operations_get_at_subscription_scope(request: web.Request, deployment_name, operation_id, api_version, subscription_id) -> web.Response:
    """deployment_operations_get_at_subscription_scope

    Gets a deployments operation.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param operation_id: The ID of the operation to get.
    :type operation_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployment_operations_get_at_tenant_scope(request: web.Request, deployment_name, operation_id, api_version) -> web.Response:
    """deployment_operations_get_at_tenant_scope

    Gets a deployments operation.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param operation_id: The ID of the operation to get.
    :type operation_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployment_operations_list(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id, top=None) -> web.Response:
    """deployment_operations_list

    Gets all deployments operations for a deployment.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param top: The number of results to return.
    :type top: int

    """
    return web.Response(status=200)


async def deployment_operations_list_at_management_group_scope(request: web.Request, group_id, deployment_name, api_version, top=None) -> web.Response:
    """deployment_operations_list_at_management_group_scope

    Gets all deployments operations for a deployment.

    :param group_id: The management group ID.
    :type group_id: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param top: The number of results to return.
    :type top: int

    """
    return web.Response(status=200)


async def deployment_operations_list_at_scope(request: web.Request, scope, deployment_name, api_version, top=None) -> web.Response:
    """deployment_operations_list_at_scope

    Gets all deployments operations for a deployment.

    :param scope: The scope of a deployment.
    :type scope: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param top: The number of results to return.
    :type top: int

    """
    return web.Response(status=200)


async def deployment_operations_list_at_subscription_scope(request: web.Request, deployment_name, api_version, subscription_id, top=None) -> web.Response:
    """deployment_operations_list_at_subscription_scope

    Gets all deployments operations for a deployment.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param top: The number of results to return.
    :type top: int

    """
    return web.Response(status=200)


async def deployment_operations_list_at_tenant_scope(request: web.Request, deployment_name, api_version, top=None) -> web.Response:
    """deployment_operations_list_at_tenant_scope

    Gets all deployments operations for a deployment.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param top: The number of results to return.
    :type top: int

    """
    return web.Response(status=200)
