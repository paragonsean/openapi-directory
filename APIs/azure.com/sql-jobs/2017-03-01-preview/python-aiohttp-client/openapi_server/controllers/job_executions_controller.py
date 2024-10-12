from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_execution import JobExecution
from openapi_server.models.job_execution_list_result import JobExecutionListResult
from openapi_server import util


async def job_executions_cancel(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, job_execution_id, subscription_id, api_version) -> web.Response:
    """job_executions_cancel

    Requests cancellation of a job execution.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job.
    :type job_name: str
    :param job_execution_id: The id of the job execution to cancel.
    :type job_execution_id: str
    :type job_execution_id: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_executions_create(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, subscription_id, api_version) -> web.Response:
    """job_executions_create

    Starts an elastic job execution.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job to get.
    :type job_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_executions_create_or_update(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, job_execution_id, subscription_id, api_version) -> web.Response:
    """job_executions_create_or_update

    Creates or updates a job execution.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job to get.
    :type job_name: str
    :param job_execution_id: The job execution id to create the job execution under.
    :type job_execution_id: str
    :type job_execution_id: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_executions_get(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, job_execution_id, subscription_id, api_version) -> web.Response:
    """job_executions_get

    Gets a job execution.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job.
    :type job_name: str
    :param job_execution_id: The id of the job execution
    :type job_execution_id: str
    :type job_execution_id: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_executions_list_by_agent(request: web.Request, resource_group_name, server_name, job_agent_name, subscription_id, api_version, create_time_min=None, create_time_max=None, end_time_min=None, end_time_max=None, is_active=None, skip=None, top=None) -> web.Response:
    """job_executions_list_by_agent

    Lists all executions in a job agent.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
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


async def job_executions_list_by_job(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, subscription_id, api_version, create_time_min=None, create_time_max=None, end_time_min=None, end_time_max=None, is_active=None, skip=None, top=None) -> web.Response:
    """job_executions_list_by_job

    Lists a job&#39;s executions.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job to get.
    :type job_name: str
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
