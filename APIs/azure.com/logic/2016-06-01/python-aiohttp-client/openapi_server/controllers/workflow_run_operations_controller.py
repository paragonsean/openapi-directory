from typing import List, Dict
from aiohttp import web

from openapi_server.models.workflow_run import WorkflowRun
from openapi_server import util


async def workflow_run_operations_get(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, operation_id, api_version) -> web.Response:
    """workflow_run_operations_get

    Gets an operation for a run.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param operation_id: The workflow operation id.
    :type operation_id: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
