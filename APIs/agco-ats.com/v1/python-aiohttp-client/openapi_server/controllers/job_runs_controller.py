from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_build_system_shared_dto_job_run import APIPagedResponseBuildSystemSharedDTOJobRun
from openapi_server.models.build_system_shared_dto_job_run import BuildSystemSharedDTOJobRun
from openapi_server import util


async def job_runs_delete_job_run(request: web.Request, job_run_id) -> web.Response:
    """Delete a JobRun

    Deletes a JobRun. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

    :param job_run_id: The id of the JobRun to delete
    :type job_run_id: int

    """
    return web.Response(status=200)


async def job_runs_get_job_run(request: web.Request, job_run_id, include_activity_run_details=None) -> web.Response:
    """Get a JobRun by ID

    Gets a JobRun by ID. When successful, the response is the requested JobRun.              If unsuccessful, an appropriate ApiError is returned.

    :param job_run_id: The ID of the JobRun to get.
    :type job_run_id: int
    :param include_activity_run_details: Optional. Indicates whether to include ActivityRun details.  Defaults to false.
    :type include_activity_run_details: bool

    """
    return web.Response(status=200)


async def job_runs_get_job_runs(request: web.Request, limit=None, offset=None, include_activity_run_details=None) -> web.Response:
    """Get JobRuns

    Gets a collection of JobRuns. When successful, the response is a PagedResponse of JobRuns.              If unsuccessful, an appropriate ApiError is returned.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param include_activity_run_details: Optional. Indicates whether to include ActivityRun details.  Defaults to false.
    :type include_activity_run_details: bool

    """
    return web.Response(status=200)


async def job_runs_post_job_run(request: web.Request, body) -> web.Response:
    """Create a JobRun

    Creates a JobRun.  The body of the POST is the JobRun to create.  The JobRunID will be assigned on              creation of the JobRun.  When successful, the response is the JobRunID.  If unsuccessful, an               appropriate ApiError is returned.

    :param body: The JobRun to create.  The JobRunID will be assigned on creation of the JobRun.
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOJobRun.from_dict(body)
    return web.Response(status=200)


async def job_runs_put_job_run(request: web.Request, job_run_id, body) -> web.Response:
    """Update a JobRun

    ///               Updates a JobRun.  The body of the PUT is the updated JobRun.              When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

    :param job_run_id: The id of the JobRun to update
    :type job_run_id: int
    :param body: The updated JobRun
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOJobRun.from_dict(body)
    return web.Response(status=200)
