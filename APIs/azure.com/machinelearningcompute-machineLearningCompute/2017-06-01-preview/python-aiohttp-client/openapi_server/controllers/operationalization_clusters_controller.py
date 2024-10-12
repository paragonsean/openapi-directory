from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_update_response import CheckUpdateResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operationalization_cluster import OperationalizationCluster
from openapi_server.models.operationalization_cluster_credentials import OperationalizationClusterCredentials
from openapi_server.models.operationalization_cluster_update_parameters import OperationalizationClusterUpdateParameters
from openapi_server.models.paginated_operationalization_clusters_list import PaginatedOperationalizationClustersList
from openapi_server.models.update_system_response import UpdateSystemResponse
from openapi_server import util


async def operationalization_clusters_check_update(request: web.Request, api_version, subscription_id, resource_group_name, cluster_name) -> web.Response:
    """operationalization_clusters_check_update

    Checks if updates are available for system services in the cluster

    :param api_version: The version of the Microsoft.MachineLearningCompute resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which the cluster is located.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str

    """
    return web.Response(status=200)


async def operationalization_clusters_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, cluster_name, parameters) -> web.Response:
    """operationalization_clusters_create_or_update

    Create or update an operationalization cluster.

    :param api_version: The version of the Microsoft.MachineLearningCompute resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which the cluster is located.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param parameters: Parameters supplied to create or update an Operationalization cluster.
    :type parameters: dict | bytes

    """
    parameters = OperationalizationCluster.from_dict(parameters)
    return web.Response(status=200)


async def operationalization_clusters_delete(request: web.Request, api_version, subscription_id, resource_group_name, cluster_name) -> web.Response:
    """operationalization_clusters_delete

    Deletes the specified cluster.

    :param api_version: The version of the Microsoft.MachineLearningCompute resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which the cluster is located.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str

    """
    return web.Response(status=200)


async def operationalization_clusters_get(request: web.Request, api_version, subscription_id, resource_group_name, cluster_name) -> web.Response:
    """operationalization_clusters_get

    Gets the operationalization cluster resource view. Note that the credentials are not returned by this call. Call ListKeys to get them.

    :param api_version: The version of the Microsoft.MachineLearningCompute resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which the cluster is located.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str

    """
    return web.Response(status=200)


async def operationalization_clusters_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name, skiptoken=None) -> web.Response:
    """operationalization_clusters_list_by_resource_group

    Gets the clusters in the specified resource group.

    :param api_version: The version of the Microsoft.MachineLearningCompute resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which the cluster is located.
    :type resource_group_name: str
    :param skiptoken: Continuation token for pagination.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def operationalization_clusters_list_by_subscription_id(request: web.Request, api_version, subscription_id, skiptoken=None) -> web.Response:
    """operationalization_clusters_list_by_subscription_id

    Gets the operationalization clusters in the specified subscription.

    :param api_version: The version of the Microsoft.MachineLearningCompute resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param skiptoken: Continuation token for pagination.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def operationalization_clusters_list_keys(request: web.Request, api_version, subscription_id, resource_group_name, cluster_name) -> web.Response:
    """operationalization_clusters_list_keys

    Gets the credentials for the specified cluster such as Storage, ACR and ACS credentials. This is a long running operation because it fetches keys from dependencies.

    :param api_version: The version of the Microsoft.MachineLearningCompute resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which the cluster is located.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str

    """
    return web.Response(status=200)


async def operationalization_clusters_update(request: web.Request, api_version, subscription_id, resource_group_name, cluster_name, parameters) -> web.Response:
    """operationalization_clusters_update

    The PATCH operation can be used to update only the tags for a cluster. Use PUT operation to update other properties.

    :param api_version: The version of the Microsoft.MachineLearningCompute resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which the cluster is located.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str
    :param parameters: The parameters supplied to patch the cluster.
    :type parameters: dict | bytes

    """
    parameters = OperationalizationClusterUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def operationalization_clusters_update_system(request: web.Request, api_version, subscription_id, resource_group_name, cluster_name) -> web.Response:
    """operationalization_clusters_update_system

    Updates system services in a cluster.

    :param api_version: The version of the Microsoft.MachineLearningCompute resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which the cluster is located.
    :type resource_group_name: str
    :param cluster_name: The name of the cluster.
    :type cluster_name: str

    """
    return web.Response(status=200)
