from typing import List, Dict
from aiohttp import web

from openapi_server.models.job import Job
from openapi_server.models.job_list import JobList
from openapi_server import util


async def jobs_cancel(request: web.Request, device_name, job_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """jobs_cancel

    Cancels a job on the device.

    :param device_name: The device name
    :type device_name: str
    :param job_name: The jobName.
    :type job_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def jobs_get(request: web.Request, device_name, job_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """jobs_get

    Gets the details of the specified job name.

    :param device_name: The device name
    :type device_name: str
    :param job_name: The job Name.
    :type job_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def jobs_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, filter=None) -> web.Response:
    """jobs_list_by_device

    Gets all the jobs for specified device. With optional OData query parameters, a filtered set of jobs is returned.

    :param device_name: The device name
    :type device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)


async def jobs_list_by_manager(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, filter=None) -> web.Response:
    """jobs_list_by_manager

    Gets all the jobs for the specified manager. With optional OData query parameters, a filtered set of jobs is returned.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)
