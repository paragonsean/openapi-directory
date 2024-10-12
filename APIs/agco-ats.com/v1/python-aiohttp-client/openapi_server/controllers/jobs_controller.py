from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_build_system_shared_dto_job import APIPagedResponseBuildSystemSharedDTOJob
from openapi_server.models.build_system_shared_dto_job import BuildSystemSharedDTOJob
from openapi_server import util


async def jobs_delete_job(request: web.Request, job_id) -> web.Response:
    """Mark the delete flag for the Job

    Deletes a Job. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

    :param job_id: The id of the job to delete
    :type job_id: int

    """
    return web.Response(status=200)


async def jobs_get_job(request: web.Request, job_id, is_include_deleted=None) -> web.Response:
    """Get a Job by ID

    Gets a Job by ID. When successful, the response is the requested Job.              If unsuccessful, an appropriate ApiError is returned.

    :param job_id: The ID of the Job to get.
    :type job_id: int
    :param is_include_deleted: Does it include deleted job, or not
    :type is_include_deleted: bool

    """
    return web.Response(status=200)


async def jobs_get_jobs(request: web.Request, limit=None, offset=None, is_include_deleted=None) -> web.Response:
    """Get Jobs

    Gets a collection of Jobs. When successful, the response is a PagedResponse of Jobs.              If unsuccessful, an appropriate ApiError is returned.               ///

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param is_include_deleted: Does it include deleted job, or not
    :type is_include_deleted: bool

    """
    return web.Response(status=200)


async def jobs_post_job(request: web.Request, body) -> web.Response:
    """Create a Job

    Creates a Job.  The body of the POST is the Job to create.  The JobID will be assigned on              creation of the Job.  When successful, the response is the JobID.  If unsuccessful, an               appropriate ApiError is returned.

    :param body: The job to create.  The JobID will be assigned on creation of the Job.
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOJob.from_dict(body)
    return web.Response(status=200)


async def jobs_put_job(request: web.Request, job_id, body) -> web.Response:
    """Update a Job

    Updates a Job.  The body of the PUT is the updated Job.  When successful, the response is empty.              If unsuccessful, an appropriate ApiError is returned.

    :param job_id: The id of the job to update
    :type job_id: int
    :param body: The updated job
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOJob.from_dict(body)
    return web.Response(status=200)
