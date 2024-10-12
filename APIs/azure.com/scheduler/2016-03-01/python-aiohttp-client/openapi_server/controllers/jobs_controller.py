from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_definition import JobDefinition
from openapi_server.models.job_history_list_result import JobHistoryListResult
from openapi_server.models.job_list_result import JobListResult
from openapi_server import util


async def jobs_create_or_update(request: web.Request, subscription_id, resource_group_name, job_collection_name, job_name, api_version, job) -> web.Response:
    """jobs_create_or_update

    Provisions a new job or updates an existing job.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param job_name: The job name.
    :type job_name: str
    :param api_version: The API version.
    :type api_version: str
    :param job: The job definition.
    :type job: dict | bytes

    """
    job = JobDefinition.from_dict(job)
    return web.Response(status=200)


async def jobs_delete(request: web.Request, subscription_id, resource_group_name, job_collection_name, job_name, api_version) -> web.Response:
    """jobs_delete

    Deletes a job.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param job_name: The job name.
    :type job_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def jobs_get(request: web.Request, subscription_id, resource_group_name, job_collection_name, job_name, api_version) -> web.Response:
    """jobs_get

    Gets a job.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param job_name: The job name.
    :type job_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def jobs_list(request: web.Request, subscription_id, resource_group_name, job_collection_name, api_version, top=None, skip=None, filter=None) -> web.Response:
    """jobs_list

    Lists all jobs under the specified job collection.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of jobs to request, in the of range of [1..100].
    :type top: int
    :param skip: The (0-based) index of the job history list from which to begin requesting entries.
    :type skip: int
    :param filter: The filter to apply on the job state.
    :type filter: str

    """
    return web.Response(status=200)


async def jobs_list_job_history(request: web.Request, subscription_id, resource_group_name, job_collection_name, job_name, api_version, top=None, skip=None, filter=None) -> web.Response:
    """jobs_list_job_history

    Lists job history.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param job_name: The job name.
    :type job_name: str
    :param api_version: The API version.
    :type api_version: str
    :param top: the number of job history to request, in the of range of [1..100].
    :type top: int
    :param skip: The (0-based) index of the job history list from which to begin requesting entries.
    :type skip: int
    :param filter: The filter to apply on the job state.
    :type filter: str

    """
    return web.Response(status=200)


async def jobs_patch(request: web.Request, subscription_id, resource_group_name, job_collection_name, job_name, api_version, job) -> web.Response:
    """jobs_patch

    Patches an existing job.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param job_name: The job name.
    :type job_name: str
    :param api_version: The API version.
    :type api_version: str
    :param job: The job definition.
    :type job: dict | bytes

    """
    job = JobDefinition.from_dict(job)
    return web.Response(status=200)


async def jobs_run(request: web.Request, subscription_id, resource_group_name, job_collection_name, job_name, api_version) -> web.Response:
    """jobs_run

    Runs a job.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param job_name: The job name.
    :type job_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
