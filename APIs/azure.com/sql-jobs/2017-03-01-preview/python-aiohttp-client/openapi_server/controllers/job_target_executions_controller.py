from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_execution import JobExecution
from openapi_server.models.job_execution_list_result import JobExecutionListResult
from openapi_server import util


async def job_target_executions_get(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, job_execution_id, step_name, target_id, subscription_id, api_version) -> web.Response:
    """job_target_executions_get

    Gets a target execution.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job to get.
    :type job_name: str
    :param job_execution_id: The unique id of the job execution
    :type job_execution_id: str
    :type job_execution_id: str
    :param step_name: The name of the step.
    :type step_name: str
    :param target_id: The target id.
    :type target_id: str
    :type target_id: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_target_executions_list_by_job_execution(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, job_execution_id, subscription_id, api_version, create_time_min=None, create_time_max=None, end_time_min=None, end_time_max=None, is_active=None, skip=None, top=None) -> web.Response:
    """job_target_executions_list_by_job_execution

    Lists target executions for all steps of a job execution.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job to get.
    :type job_name: str
    :param job_execution_id: The id of the job execution
    :type job_execution_id: str
    :type job_execution_id: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param create_time_min: If specified, only job executions created at or after the specified time are included.
    :type create_time_min: str
    :param create_time_max: If specified, only job executions created before the specified time are included.
    :type create_time_max: str
    :param end_time_min: If specified, only job executions completed at or after the specified time are included.
    :type end_time_min: str
    :param end_time_max: If specified, only job executions completed before the specified time are included.
    :type end_time_max: str
    :param is_active: If specified, only active or only completed job executions are included.
    :type is_active: bool
    :param skip: The number of elements in the collection to skip.
    :type skip: int
    :param top: The number of elements to return from the collection.
    :type top: int

    """
    create_time_min = util.deserialize_datetime(create_time_min)
    create_time_max = util.deserialize_datetime(create_time_max)
    end_time_min = util.deserialize_datetime(end_time_min)
    end_time_max = util.deserialize_datetime(end_time_max)
    return web.Response(status=200)


async def job_target_executions_list_by_step(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, job_execution_id, step_name, subscription_id, api_version, create_time_min=None, create_time_max=None, end_time_min=None, end_time_max=None, is_active=None, skip=None, top=None) -> web.Response:
    """job_target_executions_list_by_step

    Lists the target executions of a job step execution.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job to get.
    :type job_name: str
    :param job_execution_id: The id of the job execution
    :type job_execution_id: str
    :type job_execution_id: str
    :param step_name: The name of the step.
    :type step_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param create_time_min: If specified, only job executions created at or after the specified time are included.
    :type create_time_min: str
    :param create_time_max: If specified, only job executions created before the specified time are included.
    :type create_time_max: str
    :param end_time_min: If specified, only job executions completed at or after the specified time are included.
    :type end_time_min: str
    :param end_time_max: If specified, only job executions completed before the specified time are included.
    :type end_time_max: str
    :param is_active: If specified, only active or only completed job executions are included.
    :type is_active: bool
    :param skip: The number of elements in the collection to skip.
    :type skip: int
    :param top: The number of elements to return from the collection.
    :type top: int

    """
    create_time_min = util.deserialize_datetime(create_time_min)
    create_time_max = util.deserialize_datetime(create_time_max)
    end_time_min = util.deserialize_datetime(end_time_min)
    end_time_max = util.deserialize_datetime(end_time_max)
    return web.Response(status=200)
