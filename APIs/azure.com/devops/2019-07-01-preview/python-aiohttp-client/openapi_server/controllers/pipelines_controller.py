from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.pipeline import Pipeline
from openapi_server.models.pipeline_list_result import PipelineListResult
from openapi_server.models.pipeline_update_parameters import PipelineUpdateParameters
from openapi_server import util


async def pipelines_create_or_update(request: web.Request, subscription_id, resource_group_name, api_version, pipeline_name, create_operation_parameters) -> web.Response:
    """pipelines_create_or_update

    Creates or updates an Azure Pipeline.

    :param subscription_id: Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param api_version: API version to be used with the HTTP request.
    :type api_version: str
    :param pipeline_name: The name of the Azure Pipeline resource in ARM.
    :type pipeline_name: str
    :param create_operation_parameters: The request payload to create the Azure Pipeline.
    :type create_operation_parameters: dict | bytes

    """
    create_operation_parameters = Pipeline.from_dict(create_operation_parameters)
    return web.Response(status=200)


async def pipelines_delete(request: web.Request, subscription_id, resource_group_name, api_version, pipeline_name) -> web.Response:
    """pipelines_delete

    Deletes an Azure Pipeline.

    :param subscription_id: Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param api_version: API version to be used with the HTTP request.
    :type api_version: str
    :param pipeline_name: The name of the Azure Pipeline resource.
    :type pipeline_name: str

    """
    return web.Response(status=200)


async def pipelines_get(request: web.Request, subscription_id, resource_group_name, api_version, pipeline_name) -> web.Response:
    """pipelines_get

    Gets an existing Azure Pipeline.

    :param subscription_id: Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param api_version: API version to be used with the HTTP request.
    :type api_version: str
    :param pipeline_name: The name of the Azure Pipeline resource in ARM.
    :type pipeline_name: str

    """
    return web.Response(status=200)


async def pipelines_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """pipelines_list_by_resource_group

    Lists all Azure Pipelines under the specified resource group.

    :param subscription_id: Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param api_version: API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def pipelines_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """pipelines_list_by_subscription

    Lists all Azure Pipelines under the specified subscription.

    :param subscription_id: Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def pipelines_update(request: web.Request, subscription_id, resource_group_name, api_version, pipeline_name, update_operation_parameters) -> web.Response:
    """pipelines_update

    Updates the properties of an Azure Pipeline. Currently, only tags can be updated.

    :param subscription_id: Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param api_version: API version to be used with the HTTP request.
    :type api_version: str
    :param pipeline_name: The name of the Azure Pipeline resource.
    :type pipeline_name: str
    :param update_operation_parameters: The request payload containing the properties to update in the Azure Pipeline.
    :type update_operation_parameters: dict | bytes

    """
    update_operation_parameters = PipelineUpdateParameters.from_dict(update_operation_parameters)
    return web.Response(status=200)
