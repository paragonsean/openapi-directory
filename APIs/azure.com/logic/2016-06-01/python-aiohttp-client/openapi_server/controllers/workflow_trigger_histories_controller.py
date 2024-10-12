from typing import List, Dict
from aiohttp import web

from openapi_server.models.workflow_trigger_history import WorkflowTriggerHistory
from openapi_server.models.workflow_trigger_history_list_result import WorkflowTriggerHistoryListResult
from openapi_server import util


async def workflow_trigger_histories_get(request: web.Request, subscription_id, resource_group_name, workflow_name, trigger_name, history_name, api_version) -> web.Response:
    """workflow_trigger_histories_get

    Gets a workflow trigger history.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param trigger_name: The workflow trigger name.
    :type trigger_name: str
    :param history_name: The workflow trigger history name. Corresponds to the run name for triggers that resulted in a run.
    :type history_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_trigger_histories_list(request: web.Request, subscription_id, resource_group_name, workflow_name, trigger_name, api_version, top=None, filter=None) -> web.Response:
    """workflow_trigger_histories_list

    Gets a list of workflow trigger histories.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param trigger_name: The workflow trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int
    :param filter: The filter to apply on the operation. Options for filters include: Status, StartTime, and ClientTrackingId.
    :type filter: str

    """
    return web.Response(status=200)


async def workflow_trigger_histories_resubmit(request: web.Request, subscription_id, resource_group_name, workflow_name, trigger_name, history_name, api_version) -> web.Response:
    """workflow_trigger_histories_resubmit

    Resubmits a workflow run based on the trigger history.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param trigger_name: The workflow trigger name.
    :type trigger_name: str
    :param history_name: The workflow trigger history name. Corresponds to the run name for triggers that resulted in a run.
    :type history_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
