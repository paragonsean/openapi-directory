from typing import List, Dict
from aiohttp import web

from openapi_server.models.describe_job_execution_response import DescribeJobExecutionResponse
from openapi_server.models.get_pending_job_executions_response import GetPendingJobExecutionsResponse
from openapi_server.models.start_next_pending_job_execution_request import StartNextPendingJobExecutionRequest
from openapi_server.models.start_next_pending_job_execution_response import StartNextPendingJobExecutionResponse
from openapi_server.models.update_job_execution_request import UpdateJobExecutionRequest
from openapi_server.models.update_job_execution_response import UpdateJobExecutionResponse
from openapi_server import util


async def describe_job_execution(request: web.Request, job_id, thing_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, include_job_document=None, execution_number=None) -> web.Response:
    """describe_job_execution

    Gets details of a job execution.

    :param job_id: The unique identifier assigned to this job when it was created.
    :type job_id: str
    :param thing_name: The thing name associated with the device the job execution is running on.
    :type thing_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param include_job_document: Optional. When set to true, the response contains the job document. The default is false.
    :type include_job_document: bool
    :param execution_number: Optional. A number that identifies a particular job execution on a particular device. If not specified, the latest job execution is returned.
    :type execution_number: int

    """
    return web.Response(status=200)


async def get_pending_job_executions(request: web.Request, thing_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_pending_job_executions

    Gets the list of all jobs for a thing that are not in a terminal status.

    :param thing_name: The name of the thing that is executing the job.
    :type thing_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def start_next_pending_job_execution(request: web.Request, thing_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_next_pending_job_execution

    Gets and starts the next pending (status IN_PROGRESS or QUEUED) job execution for a thing.

    :param thing_name: The name of the thing associated with the device.
    :type thing_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartNextPendingJobExecutionRequest.from_dict(body)
    return web.Response(status=200)


async def update_job_execution(request: web.Request, job_id, thing_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_job_execution

    Updates the status of a job execution.

    :param job_id: The unique identifier assigned to this job when it was created.
    :type job_id: str
    :param thing_name: The name of the thing associated with the device.
    :type thing_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateJobExecutionRequest.from_dict(body)
    return web.Response(status=200)
