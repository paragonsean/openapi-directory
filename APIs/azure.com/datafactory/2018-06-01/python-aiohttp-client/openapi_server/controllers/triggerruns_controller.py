from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.run_filter_parameters import RunFilterParameters
from openapi_server.models.trigger_runs_query_response import TriggerRunsQueryResponse
from openapi_server import util


async def trigger_runs_query_by_factory(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, filter_parameters) -> web.Response:
    """trigger_runs_query_by_factory

    Query trigger runs.

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
    filter_parameters = RunFilterParameters.from_dict(filter_parameters)
    return web.Response(status=200)


async def trigger_runs_rerun(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, run_id, api_version) -> web.Response:
    """trigger_runs_rerun

    Rerun single trigger instance by runId.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param run_id: The pipeline run identifier.
    :type run_id: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
