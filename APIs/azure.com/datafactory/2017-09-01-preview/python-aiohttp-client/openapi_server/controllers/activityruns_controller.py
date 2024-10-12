from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_runs_list_response import ActivityRunsListResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def activity_runs_list_by_pipeline_run(request: web.Request, subscription_id, resource_group_name, factory_name, run_id, api_version, start_time, end_time, status=None, activity_name=None, linked_service_name=None) -> web.Response:
    """activity_runs_list_by_pipeline_run

    List activity runs based on input filter conditions.

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
    :param start_time: The start time of activity runs in ISO8601 format.
    :type start_time: str
    :param end_time: The end time of activity runs in ISO8601 format.
    :type end_time: str
    :param status: The status of the pipeline run.
    :type status: str
    :param activity_name: The name of the activity.
    :type activity_name: str
    :param linked_service_name: The linked service name.
    :type linked_service_name: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)
