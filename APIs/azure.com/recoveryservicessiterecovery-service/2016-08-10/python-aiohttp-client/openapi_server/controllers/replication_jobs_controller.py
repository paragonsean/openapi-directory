from typing import List, Dict
from aiohttp import web

from openapi_server.models.job import Job
from openapi_server.models.job_collection import JobCollection
from openapi_server.models.job_query_parameter import JobQueryParameter
from openapi_server.models.resume_job_params import ResumeJobParams
from openapi_server import util


async def replication_jobs_cancel(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, job_name) -> web.Response:
    """Cancels the specified job.

    The operation to cancel an Azure Site Recovery job.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param job_name: Job identifier.
    :type job_name: str

    """
    return web.Response(status=200)


async def replication_jobs_export(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, job_query_parameter) -> web.Response:
    """Exports the details of the Azure Site Recovery jobs of the vault.

    The operation to export the details of the Azure Site Recovery jobs of the vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param job_query_parameter: job query filter.
    :type job_query_parameter: dict | bytes

    """
    job_query_parameter = JobQueryParameter.from_dict(job_query_parameter)
    return web.Response(status=200)


async def replication_jobs_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, job_name) -> web.Response:
    """Gets the job details.

    Get the details of an Azure Site Recovery job.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param job_name: Job identifier
    :type job_name: str

    """
    return web.Response(status=200)


async def replication_jobs_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, filter=None) -> web.Response:
    """Gets the list of jobs.

    Gets the list of Azure Site Recovery Jobs for the vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param filter: OData filter options.
    :type filter: str

    """
    return web.Response(status=200)


async def replication_jobs_restart(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, job_name) -> web.Response:
    """Restarts the specified job.

    The operation to restart an Azure Site Recovery job.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param job_name: Job identifier.
    :type job_name: str

    """
    return web.Response(status=200)


async def replication_jobs_resume(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, job_name, resume_job_params) -> web.Response:
    """Resumes the specified job.

    The operation to resume an Azure Site Recovery job

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param job_name: Job identifier.
    :type job_name: str
    :param resume_job_params: Resume rob comments.
    :type resume_job_params: dict | bytes

    """
    resume_job_params = ResumeJobParams.from_dict(resume_job_params)
    return web.Response(status=200)
