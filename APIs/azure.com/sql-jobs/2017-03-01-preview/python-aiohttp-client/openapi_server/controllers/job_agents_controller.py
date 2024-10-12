from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_agent import JobAgent
from openapi_server.models.job_agent_list_result import JobAgentListResult
from openapi_server.models.job_agent_update import JobAgentUpdate
from openapi_server import util


async def job_agents_create_or_update(request: web.Request, resource_group_name, server_name, job_agent_name, subscription_id, api_version, parameters) -> web.Response:
    """job_agents_create_or_update

    Creates or updates a job agent.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent to be created or updated.
    :type job_agent_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested job agent resource state.
    :type parameters: dict | bytes

    """
    parameters = JobAgent.from_dict(parameters)
    return web.Response(status=200)


async def job_agents_delete(request: web.Request, resource_group_name, server_name, job_agent_name, subscription_id, api_version) -> web.Response:
    """job_agents_delete

    Deletes a job agent.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent to be deleted.
    :type job_agent_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_agents_get(request: web.Request, resource_group_name, server_name, job_agent_name, subscription_id, api_version) -> web.Response:
    """job_agents_get

    Gets a job agent.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent to be retrieved.
    :type job_agent_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_agents_list_by_server(request: web.Request, resource_group_name, server_name, subscription_id, api_version) -> web.Response:
    """job_agents_list_by_server

    Gets a list of job agents in a server.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_agents_update(request: web.Request, resource_group_name, server_name, job_agent_name, subscription_id, api_version, parameters) -> web.Response:
    """job_agents_update

    Updates a job agent.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent to be updated.
    :type job_agent_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The update to the job agent.
    :type parameters: dict | bytes

    """
    parameters = JobAgentUpdate.from_dict(parameters)
    return web.Response(status=200)
