from typing import List, Dict
from aiohttp import web

from openapi_server.models.compute_resource import ComputeResource
from openapi_server.models.compute_secrets import ComputeSecrets
from openapi_server.models.machine_learning_service_error import MachineLearningServiceError
from openapi_server.models.paginated_compute_resources_list import PaginatedComputeResourcesList
from openapi_server import util


async def machine_learning_compute_create_or_update_0(request: web.Request, subscription_id, resource_group_name, workspace_name, compute_name, api_version, parameters) -> web.Response:
    """machine_learning_compute_create_or_update_0

    Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet.

    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str
    :param compute_name: Name of the Azure Machine Learning compute.
    :type compute_name: str
    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param parameters: Payload with Machine Learning compute definition.
    :type parameters: dict | bytes

    """
    parameters = ComputeResource.from_dict(parameters)
    return web.Response(status=200)


async def machine_learning_compute_delete_0(request: web.Request, subscription_id, resource_group_name, workspace_name, compute_name, api_version) -> web.Response:
    """machine_learning_compute_delete_0

    Deletes specified Machine Learning compute.

    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str
    :param compute_name: Name of the Azure Machine Learning compute.
    :type compute_name: str
    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str

    """
    return web.Response(status=200)


async def machine_learning_compute_get_0(request: web.Request, subscription_id, resource_group_name, workspace_name, compute_name, api_version) -> web.Response:
    """machine_learning_compute_get_0

    Gets compute definition by its name. Any secrets (storage keys, service credentials, etc) are not returned - use &#39;keys&#39; nested resource to get them.

    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str
    :param compute_name: Name of the Azure Machine Learning compute.
    :type compute_name: str
    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str

    """
    return web.Response(status=200)


async def machine_learning_compute_list_by_workspace_0(request: web.Request, subscription_id, resource_group_name, workspace_name, api_version, skiptoken=None) -> web.Response:
    """machine_learning_compute_list_by_workspace_0

    Gets computes in specified workspace.

    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str
    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param skiptoken: Continuation token for pagination.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def machine_learning_compute_list_keys_0(request: web.Request, subscription_id, resource_group_name, workspace_name, compute_name, api_version) -> web.Response:
    """machine_learning_compute_list_keys_0

    Gets secrets related to Machine Learning compute (storage keys, service credentials, etc).

    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str
    :param compute_name: Name of the Azure Machine Learning compute.
    :type compute_name: str
    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str

    """
    return web.Response(status=200)


async def machine_learning_compute_system_update_0(request: web.Request, subscription_id, resource_group_name, workspace_name, compute_name, api_version) -> web.Response:
    """machine_learning_compute_system_update_0

    System Update On Machine Learning compute.

    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str
    :param compute_name: Name of the Azure Machine Learning compute.
    :type compute_name: str
    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str

    """
    return web.Response(status=200)
