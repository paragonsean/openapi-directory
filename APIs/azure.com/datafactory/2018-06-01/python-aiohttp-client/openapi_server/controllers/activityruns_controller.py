from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_runs_query_response import ActivityRunsQueryResponse
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.run_filter_parameters import RunFilterParameters
from openapi_server import util


async def activity_runs_query_by_pipeline_run(request: web.Request, subscription_id, resource_group_name, factory_name, run_id, api_version, filter_parameters) -> web.Response:
    """activity_runs_query_by_pipeline_run

    Query activity runs based on input filter conditions.

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
    :param filter_parameters: Parameters to filter the activity runs.
    :type filter_parameters: dict | bytes

    """
    filter_parameters = RunFilterParameters.from_dict(filter_parameters)
    return web.Response(status=200)
