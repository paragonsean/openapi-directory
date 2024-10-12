from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.expression_traces import ExpressionTraces
from openapi_server.models.request_history import RequestHistory
from openapi_server.models.request_history_list_result import RequestHistoryListResult
from openapi_server.models.workflow_run_action import WorkflowRunAction
from openapi_server.models.workflow_run_action_list_result import WorkflowRunActionListResult
from openapi_server.models.workflow_run_action_repetition_definition import WorkflowRunActionRepetitionDefinition
from openapi_server.models.workflow_run_action_repetition_definition_collection import WorkflowRunActionRepetitionDefinitionCollection
from openapi_server import util


async def workflow_run_action_repetitions_get(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, action_name, repetition_name, api_version) -> web.Response:
    """workflow_run_action_repetitions_get

    Get a workflow run action repetition.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param action_name: The workflow action name.
    :type action_name: str
    :param repetition_name: The workflow repetition.
    :type repetition_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_run_action_repetitions_list(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, action_name, api_version) -> web.Response:
    """workflow_run_action_repetitions_list

    Get all of a workflow run action repetitions.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param action_name: The workflow action name.
    :type action_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_run_action_repetitions_list_expression_traces(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, action_name, repetition_name, api_version) -> web.Response:
    """workflow_run_action_repetitions_list_expression_traces

    Lists a workflow run expression trace.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param action_name: The workflow action name.
    :type action_name: str
    :param repetition_name: The workflow repetition.
    :type repetition_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_run_action_repetitions_request_histories_get(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, action_name, repetition_name, request_history_name, api_version) -> web.Response:
    """workflow_run_action_repetitions_request_histories_get

    Gets a workflow run repetition request history.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param action_name: The workflow action name.
    :type action_name: str
    :param repetition_name: The workflow repetition.
    :type repetition_name: str
    :param request_history_name: The request history name.
    :type request_history_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_run_action_repetitions_request_histories_list(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, action_name, repetition_name, api_version) -> web.Response:
    """workflow_run_action_repetitions_request_histories_list

    List a workflow run repetition request history.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param action_name: The workflow action name.
    :type action_name: str
    :param repetition_name: The workflow repetition.
    :type repetition_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_run_action_request_histories_get(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, action_name, request_history_name, api_version) -> web.Response:
    """workflow_run_action_request_histories_get

    Gets a workflow run request history.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param action_name: The workflow action name.
    :type action_name: str
    :param request_history_name: The request history name.
    :type request_history_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_run_action_request_histories_list(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, action_name, api_version) -> web.Response:
    """workflow_run_action_request_histories_list

    List a workflow run request history.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param action_name: The workflow action name.
    :type action_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_run_action_scoped_repetitions_get(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, action_name, repetition_name, api_version) -> web.Response:
    """workflow_run_action_scoped_repetitions_get

    Get a workflow run action scoped repetition.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param action_name: The workflow action name.
    :type action_name: str
    :param repetition_name: The workflow repetition.
    :type repetition_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_run_action_scoped_repetitions_list(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, action_name, api_version) -> web.Response:
    """workflow_run_action_scoped_repetitions_list

    List the workflow run action scoped repetitions.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param action_name: The workflow action name.
    :type action_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_run_actions_get(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, action_name, api_version) -> web.Response:
    """workflow_run_actions_get

    Gets a workflow run action.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param action_name: The workflow action name.
    :type action_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_run_actions_list(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, api_version, top=None, filter=None) -> web.Response:
    """workflow_run_actions_list

    Gets a list of workflow run actions.

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
    :param top: The number of items to be included in the result.
    :type top: int
    :param filter: The filter to apply on the operation. Options for filters include: Status.
    :type filter: str

    """
    return web.Response(status=200)


async def workflow_run_actions_list_expression_traces(request: web.Request, subscription_id, resource_group_name, workflow_name, run_name, action_name, api_version) -> web.Response:
    """workflow_run_actions_list_expression_traces

    Lists a workflow run expression trace.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param run_name: The workflow run name.
    :type run_name: str
    :param action_name: The workflow action name.
    :type action_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
