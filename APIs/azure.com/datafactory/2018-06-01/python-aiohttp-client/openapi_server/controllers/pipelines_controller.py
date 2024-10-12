from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.create_run_response import CreateRunResponse
from openapi_server.models.pipeline_list_response import PipelineListResponse
from openapi_server.models.pipeline_resource import PipelineResource
from openapi_server import util


async def pipelines_create_or_update(request: web.Request, subscription_id, resource_group_name, factory_name, pipeline_name, api_version, pipeline, if_match=None) -> web.Response:
    """pipelines_create_or_update

    Creates or updates a pipeline.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param pipeline_name: The pipeline name.
    :type pipeline_name: str
    :param api_version: The API version.
    :type api_version: str
    :param pipeline: Pipeline resource definition.
    :type pipeline: dict | bytes
    :param if_match: ETag of the pipeline entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    :type if_match: str

    """
    pipeline = PipelineResource.from_dict(pipeline)
    return web.Response(status=200)


async def pipelines_create_run(request: web.Request, subscription_id, resource_group_name, factory_name, pipeline_name, api_version, reference_pipeline_run_id=None, is_recovery=None, start_activity_name=None, parameters=None) -> web.Response:
    """pipelines_create_run

    Creates a run of a pipeline.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param pipeline_name: The pipeline name.
    :type pipeline_name: str
    :param api_version: The API version.
    :type api_version: str
    :param reference_pipeline_run_id: The pipeline run identifier. If run ID is specified the parameters of the specified run will be used to create a new run.
    :type reference_pipeline_run_id: str
    :param is_recovery: Recovery mode flag. If recovery mode is set to true, the specified referenced pipeline run and the new run will be grouped under the same groupId.
    :type is_recovery: bool
    :param start_activity_name: In recovery mode, the rerun will start from this activity. If not specified, all activities will run.
    :type start_activity_name: str
    :param parameters: Parameters of the pipeline run. These parameters will be used only if the runId is not specified.
    :type parameters: Dict[str, ]

    """
    return web.Response(status=200)


async def pipelines_delete(request: web.Request, subscription_id, resource_group_name, factory_name, pipeline_name, api_version) -> web.Response:
    """pipelines_delete

    Deletes a pipeline.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param pipeline_name: The pipeline name.
    :type pipeline_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def pipelines_get(request: web.Request, subscription_id, resource_group_name, factory_name, pipeline_name, api_version, if_none_match=None) -> web.Response:
    """pipelines_get

    Gets a pipeline.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param pipeline_name: The pipeline name.
    :type pipeline_name: str
    :param api_version: The API version.
    :type api_version: str
    :param if_none_match: ETag of the pipeline entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def pipelines_list_by_factory(request: web.Request, subscription_id, resource_group_name, factory_name, api_version) -> web.Response:
    """pipelines_list_by_factory

    Lists pipelines.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
