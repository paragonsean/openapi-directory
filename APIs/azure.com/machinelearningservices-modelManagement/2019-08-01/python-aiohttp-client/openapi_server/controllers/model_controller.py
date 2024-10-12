from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_patch_operation import JsonPatchOperation
from openapi_server.models.model import Model
from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server.models.model_operational_state import ModelOperationalState
from openapi_server.models.paginated_model_list import PaginatedModelList
from openapi_server import util


async def m_l_models_delete(request: web.Request, subscription_id, resource_group, workspace, id) -> web.Response:
    """Delete the specified Model.

    Deletes a model if it exists.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The model id.
    :type id: str

    """
    return web.Response(status=200)


async def m_l_models_get_metrics(request: web.Request, subscription_id, resource_group, workspace, id, start_date=None, end_date=None) -> web.Response:
    """Retrieve the metrics for a Model.

    The operational events collected for the Model are returned.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The Model Id.
    :type id: str
    :param start_date: The start date from which to retrieve metrics, ISO 8601 literal format.
    :type start_date: str
    :param end_date: The end date from which to retrieve metrics, ISO 8601 literal format.
    :type end_date: str

    """
    return web.Response(status=200)


async def m_l_models_list_query(request: web.Request, subscription_id, resource_group, workspace, name=None, framework=None, description=None, count=None, skip_token=None, tags=None, properties=None, run_id=None, order_by=None) -> web.Response:
    """Query the list of Models in a workspace.

    The result list can be filtered using tag and name. If no filter is passed, the query lists all the Models in the given workspace. The returned list is paginated and the count of items in each page is an optional parameter.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param name: The object name.
    :type name: str
    :param framework: The framework.
    :type framework: str
    :param description: The object description.
    :type description: str
    :param count: The number of items to retrieve in a page.
    :type count: int
    :param skip_token: The continuation token to retrieve the next page.
    :type skip_token: str
    :param tags: A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key&#x3D;value              Example: tagKey1,tagKey2,tagKey3&#x3D;value3
    :type tags: str
    :param properties: A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key&#x3D;value              Example: propKey1,propKey2,propKey3&#x3D;value3
    :type properties: str
    :param run_id: The runId which created the model.
    :type run_id: str
    :param order_by: An option to specify how the models are ordered in the response.
    :type order_by: str

    """
    return web.Response(status=200)


async def m_l_models_patch(request: web.Request, subscription_id, resource_group, workspace, id, patch) -> web.Response:
    """Patch a specific model.

    Updates an existing model with the specified patch.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The model id.
    :type id: str
    :param patch: The payload that is used to patch the model.
    :type patch: list | bytes

    """
    patch = [JsonPatchOperation.from_dict(d) for d in patch]
    return web.Response(status=200)


async def m_l_models_query_by_id(request: web.Request, subscription_id, resource_group, workspace, id) -> web.Response:
    """Gets a model.

    Gets a model by model id.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The model id.
    :type id: str

    """
    return web.Response(status=200)


async def m_l_models_register(request: web.Request, subscription_id, resource_group, workspace, model) -> web.Response:
    """Register a model.

    Register the model provided.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param model: The payload that is used to register the model.
    :type model: dict | bytes

    """
    model = Model.from_dict(model)
    return web.Response(status=200)
