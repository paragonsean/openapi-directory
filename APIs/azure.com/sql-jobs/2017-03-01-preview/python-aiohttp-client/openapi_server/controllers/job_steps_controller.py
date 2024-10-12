from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_step import JobStep
from openapi_server.models.job_step_list_result import JobStepListResult
from openapi_server import util


async def job_steps_create_or_update(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, step_name, subscription_id, api_version, parameters) -> web.Response:
    """job_steps_create_or_update

    Creates or updates a job step. This will implicitly create a new job version.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job.
    :type job_name: str
    :param step_name: The name of the job step.
    :type step_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested state of the job step.
    :type parameters: dict | bytes

    """
    parameters = JobStep.from_dict(parameters)
    return web.Response(status=200)


async def job_steps_delete(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, step_name, subscription_id, api_version) -> web.Response:
    """job_steps_delete

    Deletes a job step. This will implicitly create a new job version.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job.
    :type job_name: str
    :param step_name: The name of the job step to delete.
    :type step_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_steps_get(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, step_name, subscription_id, api_version) -> web.Response:
    """job_steps_get

    Gets a job step in a job&#39;s current version.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job.
    :type job_name: str
    :param step_name: The name of the job step.
    :type step_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_steps_get_by_version(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, job_version, step_name, subscription_id, api_version) -> web.Response:
    """job_steps_get_by_version

    Gets the specified version of a job step.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job.
    :type job_name: str
    :param job_version: The version of the job to get.
    :type job_version: int
    :param step_name: The name of the job step.
    :type step_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_steps_list_by_job(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, subscription_id, api_version) -> web.Response:
    """job_steps_list_by_job

    Gets all job steps for a job&#39;s current version.

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


async def job_steps_list_by_version(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, job_version, subscription_id, api_version) -> web.Response:
    """job_steps_list_by_version

    Gets all job steps in the specified job version.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job to get.
    :type job_name: str
    :param job_version: The version of the job to get.
    :type job_version: int
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
