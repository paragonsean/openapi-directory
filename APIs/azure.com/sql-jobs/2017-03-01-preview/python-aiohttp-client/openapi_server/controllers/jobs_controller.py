from typing import List, Dict
from aiohttp import web

from openapi_server.models.job import Job
from openapi_server.models.job_list_result import JobListResult
from openapi_server import util


async def jobs_create_or_update(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, subscription_id, api_version, parameters) -> web.Response:
    """jobs_create_or_update

    Creates or updates a job.

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
    :param parameters: The requested job state.
    :type parameters: dict | bytes

    """
    parameters = Job.from_dict(parameters)
    return web.Response(status=200)


async def jobs_delete(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, subscription_id, api_version) -> web.Response:
    """jobs_delete

    Deletes a job.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param job_name: The name of the job to delete.
    :type job_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def jobs_get(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, subscription_id, api_version) -> web.Response:
    """jobs_get

    Gets a job.

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


async def jobs_list_by_agent(request: web.Request, resource_group_name, server_name, job_agent_name, subscription_id, api_version) -> web.Response:
    """jobs_list_by_agent

    Gets a list of jobs.

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

    """
    return web.Response(status=200)
