from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_target_group import JobTargetGroup
from openapi_server.models.job_target_group_list_result import JobTargetGroupListResult
from openapi_server import util


async def job_target_groups_create_or_update(request: web.Request, resource_group_name, server_name, job_agent_name, target_group_name, subscription_id, api_version, parameters) -> web.Response:
    """job_target_groups_create_or_update

    Creates or updates a target group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param target_group_name: The name of the target group.
    :type target_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested state of the target group.
    :type parameters: dict | bytes

    """
    parameters = JobTargetGroup.from_dict(parameters)
    return web.Response(status=200)


async def job_target_groups_delete(request: web.Request, resource_group_name, server_name, job_agent_name, target_group_name, subscription_id, api_version) -> web.Response:
    """job_target_groups_delete

    Deletes a target group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param target_group_name: The name of the target group.
    :type target_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_target_groups_get(request: web.Request, resource_group_name, server_name, job_agent_name, target_group_name, subscription_id, api_version) -> web.Response:
    """job_target_groups_get

    Gets a target group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param job_agent_name: The name of the job agent.
    :type job_agent_name: str
    :param target_group_name: The name of the target group.
    :type target_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_target_groups_list_by_agent(request: web.Request, resource_group_name, server_name, job_agent_name, subscription_id, api_version) -> web.Response:
    """job_target_groups_list_by_agent

    Gets all target groups in an agent.

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
