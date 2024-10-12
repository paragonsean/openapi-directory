from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_version import JobVersion
from openapi_server.models.job_version_list_result import JobVersionListResult
from openapi_server import util


async def job_versions_get(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, job_version, subscription_id, api_version) -> web.Response:
    """job_versions_get

    Gets a job version.

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
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_versions_list_by_job(request: web.Request, resource_group_name, server_name, job_agent_name, job_name, subscription_id, api_version) -> web.Response:
    """job_versions_list_by_job

    Gets all versions of a job.

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
