from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.pipeline_run import PipelineRun
from openapi_server.models.pipeline_run_filter_parameters import PipelineRunFilterParameters
from openapi_server.models.pipeline_run_query_response import PipelineRunQueryResponse
from openapi_server import util


async def factories_cancel_pipeline_run(request: web.Request, subscription_id, resource_group_name, factory_name, run_id, api_version) -> web.Response:
    """factories_cancel_pipeline_run

    Cancel a pipeline run by its run ID.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param run_id: The pipeline run identifier.
    :type run_id: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def pipeline_runs_get(request: web.Request, subscription_id, resource_group_name, factory_name, run_id, api_version) -> web.Response:
    """pipeline_runs_get

    Get a pipeline run by its run ID.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param run_id: The pipeline run identifier.
    :type run_id: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def pipeline_runs_query_by_factory(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, filter_parameters) -> web.Response:
    """pipeline_runs_query_by_factory

    Query pipeline runs in the factory based on input filter conditions.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param filter_parameters: Parameters to filter the pipeline run.
    :type filter_parameters: dict | bytes

    """
    filter_parameters = PipelineRunFilterParameters.from_dict(filter_parameters)
    return web.Response(status=200)
