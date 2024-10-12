from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.remediation_request import RemediationRequest
from openapi_server.models.remediation_response import RemediationResponse
from openapi_server.models.request_failed_exception import RequestFailedException
from openapi_server.models.verification_parameters import VerificationParameters
from openapi_server.models.verification_response import VerificationResponse
from openapi_server import util


async def create_backup_remediation_async_task(request: web.Request, body) -> web.Response:
    """Reschedule unsuccessful backup tasks

    Create an asynchronous task for rescheduling unsuccessful backup tasks. 

    :param body: Parameters required to reschedule unsuccessful backup tasks. 
    :type body: dict | bytes

    """
    body = RemediationRequest.from_dict(body)
    return web.Response(status=200)


async def get_backup_remediation_async_task_status(request: web.Request, id) -> web.Response:
    """Get status of reschedule attempt

    Retrieve the details of a specified asynchronous task to use for rescheduling unsuccessful tasks. 

    :param id: Async request id.
    :type id: str

    """
    return web.Response(status=200)


async def get_backup_verification_async_request_status(request: web.Request, id) -> web.Response:
    """Get asynchronous request details for Backup Verification

    Get the details of an asynchronous request for a backup verification job. 

    :param id: ID of the asynchronous request.
    :type id: str

    """
    return web.Response(status=200)


async def verify_snapshot(request: web.Request, body) -> web.Response:
    """Trigger a job for snapshot verification

    This REST API triggers the job \&quot;BACKUP_INTEGRITY_VERIFICATION\&quot;, which verifies whether or not the specified snapshot is restorable. 

    :param body: Parameters needed to schedule a snapshot verification job. 
    :type body: dict | bytes

    """
    body = VerificationParameters.from_dict(body)
    return web.Response(status=200)
