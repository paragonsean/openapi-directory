from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_aml_user_feature_result import ListAmlUserFeatureResult
from openapi_server.models.list_workspace_keys_result import ListWorkspaceKeysResult
from openapi_server.models.machine_learning_service_error import MachineLearningServiceError
from openapi_server.models.workspace import Workspace
from openapi_server.models.workspace_list_result import WorkspaceListResult
from openapi_server.models.workspace_update_parameters import WorkspaceUpdateParameters
from openapi_server import util


async def workspace_features_list(request: web.Request, api_version, subscription_id, resource_group_name, workspace_name) -> web.Response:
    """workspace_features_list

    Lists all enabled features for a workspace

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str

    """
    return web.Response(status=200)


async def workspaces_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, workspace_name, parameters) -> web.Response:
    """workspaces_create_or_update

    Creates or updates a workspace with the specified parameters.

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str
    :param parameters: The parameters for creating or updating a machine learning workspace.
    :type parameters: dict | bytes

    """
    parameters = Workspace.from_dict(parameters)
    return web.Response(status=200)


async def workspaces_delete(request: web.Request, api_version, subscription_id, resource_group_name, workspace_name) -> web.Response:
    """workspaces_delete

    Deletes a machine learning workspace.

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str

    """
    return web.Response(status=200)


async def workspaces_get(request: web.Request, api_version, subscription_id, resource_group_name, workspace_name) -> web.Response:
    """workspaces_get

    Gets the properties of the specified machine learning workspace.

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str

    """
    return web.Response(status=200)


async def workspaces_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name, skiptoken=None) -> web.Response:
    """workspaces_list_by_resource_group

    Lists all the available machine learning workspaces under the specified resource group.

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param skiptoken: Continuation token for pagination.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def workspaces_list_by_subscription(request: web.Request, api_version, subscription_id, skiptoken=None) -> web.Response:
    """workspaces_list_by_subscription

    Lists all the available machine learning workspaces under the specified subscription.

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param skiptoken: Continuation token for pagination.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def workspaces_list_keys(request: web.Request, api_version, subscription_id, resource_group_name, workspace_name) -> web.Response:
    """workspaces_list_keys

    Lists all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str

    """
    return web.Response(status=200)


async def workspaces_resync_keys(request: web.Request, api_version, subscription_id, resource_group_name, workspace_name) -> web.Response:
    """workspaces_resync_keys

    Resync all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str

    """
    return web.Response(status=200)


async def workspaces_update(request: web.Request, api_version, subscription_id, resource_group_name, workspace_name, parameters) -> web.Response:
    """workspaces_update

    Updates a machine learning workspace with the specified parameters.

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str
    :param parameters: The parameters for updating a machine learning workspace.
    :type parameters: dict | bytes

    """
    parameters = WorkspaceUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
