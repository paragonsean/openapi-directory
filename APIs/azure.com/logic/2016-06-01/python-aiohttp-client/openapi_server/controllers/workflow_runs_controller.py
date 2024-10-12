from typing import List, Dict
from aiohttp import web

from openapi_server.models.workflow_run import WorkflowRun
from openapi_server.models.workflow_run_list_result import WorkflowRunListResult
from openapi_server import util


async def workflow_runs_cancel(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, api_version) -> web.Response:
    """workflow_runs_cancel

    Cancels a workflow run.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_runs_delete(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, api_version) -> web.Response:
    """workflow_runs_delete

    Deletes a workflow run.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_runs_get(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, api_version) -> web.Response:
    """workflow_runs_get

    Gets a workflow run.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_runs_list(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version, top=None, filter=None) -> web.Response:
    """workflow_runs_list

    Gets a list of workflow runs.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int
    :param filter: The filter to apply on the operation. Options for filters include: Status, StartTime, and ClientTrackingId.
    :type filter: str

    """
    return web.Response(status=200)
