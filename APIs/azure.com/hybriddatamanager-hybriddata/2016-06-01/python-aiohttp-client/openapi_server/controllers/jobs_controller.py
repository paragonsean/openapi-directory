from typing import List, Dict
from aiohttp import web

from openapi_server.models.job import Job
from openapi_server.models.job_list import JobList
from openapi_server import util


async def jobs_cancel(request: web.Request, data_service_name, job_definition_name, job_id, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """jobs_cancel

    Cancels the given job.

    :param data_service_name: The name of the data service of the job definition.
    :type data_service_name: str
    :param job_definition_name: The name of the job definition of the job.
    :type job_definition_name: str
    :param job_id: The job id of the job queried.
    :type job_id: str
    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def jobs_get(request: web.Request, data_service_name, job_definition_name, job_id, subscription_id, resource_group_name, data_manager_name, api_version, expand=None) -> web.Response:
    """jobs_get

    This method gets a data manager job given the jobId.

    :param data_service_name: The name of the data service of the job definition.
    :type data_service_name: str
    :param job_definition_name: The name of the job definition of the job.
    :type job_definition_name: str
    :param job_id: The job id of the job queried.
    :type job_id: str
    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str
    :param expand: $expand is supported on details parameter for job, which provides details on the job stages.
    :type expand: str

    """
    return web.Response(status=200)


async def jobs_list_by_data_manager(request: web.Request, subscription_id, resource_group_name, data_manager_name, api_version, filter=None) -> web.Response:
    """jobs_list_by_data_manager

    This method gets all the jobs at the data manager resource level.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)


async def jobs_list_by_data_service(request: web.Request, data_service_name, subscription_id, resource_group_name, data_manager_name, api_version, filter=None) -> web.Response:
    """jobs_list_by_data_service

    This method gets all the jobs of a data service type in a given resource.

    :param data_service_name: The name of the data service of interest.
    :type data_service_name: str
    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)


async def jobs_list_by_job_definition(request: web.Request, data_service_name, job_definition_name, subscription_id, resource_group_name, data_manager_name, api_version, filter=None) -> web.Response:
    """jobs_list_by_job_definition

    This method gets all the jobs of a given job definition.

    :param data_service_name: The name of the data service of the job definition.
    :type data_service_name: str
    :param job_definition_name: The name of the job definition for which jobs are needed.
    :type job_definition_name: str
    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)


async def jobs_resume(request: web.Request, data_service_name, job_definition_name, job_id, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """jobs_resume

    Resumes the given job.

    :param data_service_name: The name of the data service of the job definition.
    :type data_service_name: str
    :param job_definition_name: The name of the job definition of the job.
    :type job_definition_name: str
    :param job_id: The job id of the job queried.
    :type job_id: str
    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)
