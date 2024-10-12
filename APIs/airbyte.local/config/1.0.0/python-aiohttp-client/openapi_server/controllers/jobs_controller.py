from typing import List, Dict
from aiohttp import web

from openapi_server.models.attempt_normalization_status_read_list import AttemptNormalizationStatusReadList
from openapi_server.models.connection_id_request_body import ConnectionIdRequestBody
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.job_debug_info_read import JobDebugInfoRead
from openapi_server.models.job_id_request_body import JobIdRequestBody
from openapi_server.models.job_info_light_read import JobInfoLightRead
from openapi_server.models.job_info_read import JobInfoRead
from openapi_server.models.job_list_request_body import JobListRequestBody
from openapi_server.models.job_optional_read import JobOptionalRead
from openapi_server.models.job_read_list import JobReadList
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server import util


async def cancel_job(request: web.Request, body) -> web.Response:
    """Cancels a job

    

    :param body: 
    :type body: dict | bytes

    """
    body = JobIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_attempt_normalization_statuses_for_job(request: web.Request, body=None) -> web.Response:
    """Get normalization status to determine if we can bypass normalization phase

    

    :param body: 
    :type body: dict | bytes

    """
    body = JobIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_job_debug_info(request: web.Request, body) -> web.Response:
    """Gets all information needed to debug this job

    

    :param body: 
    :type body: dict | bytes

    """
    body = JobIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_job_info(request: web.Request, body) -> web.Response:
    """Get information about a job

    

    :param body: 
    :type body: dict | bytes

    """
    body = JobIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_job_info_light(request: web.Request, body) -> web.Response:
    """Get information about a job excluding attempt info and logs

    

    :param body: 
    :type body: dict | bytes

    """
    body = JobIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_last_replication_job(request: web.Request, body) -> web.Response:
    """get_last_replication_job

    

    :param body: 
    :type body: dict | bytes

    """
    body = ConnectionIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def list_jobs_for(request: web.Request, body) -> web.Response:
    """Returns recent jobs for a connection. Jobs are returned in descending order by createdAt.

    

    :param body: 
    :type body: dict | bytes

    """
    body = JobListRequestBody.from_dict(body)
    return web.Response(status=200)
