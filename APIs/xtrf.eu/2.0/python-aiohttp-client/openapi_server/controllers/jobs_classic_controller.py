from typing import List, Dict
from aiohttp import web

from openapi_server.models.assign_vendor_dto import AssignVendorDTO
from openapi_server.models.file_metadata_dto import FileMetadataDTO
from openapi_server.models.instructions_dto import InstructionsDTO
from openapi_server.models.job_dates_dto import JobDatesDto
from openapi_server.models.job_dto import JobDto
from openapi_server.models.job_files_dto import JobFilesDTO
from openapi_server.models.job_status_dto import JobStatusDTO
from openapi_server.models.task_file_dto import TaskFileDTO
from openapi_server import util


async def assign_file_to_job_output(request: web.Request, job_id, body) -> web.Response:
    """assign_file_to_job_output

    

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: Assigns file to job output files.
    :type body: dict | bytes

    """
    body = TaskFileDTO.from_dict(body)
    return web.Response(status=200)


async def assign_vendor(request: web.Request, job_id, body) -> web.Response:
    """Assigns vendor to a job in a project.

    Assigns vendor to a job in a project.

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: Assigned vendor to a job in a project.
    :type body: dict | bytes

    """
    body = AssignVendorDTO.from_dict(body)
    return web.Response(status=200)


async def change_status(request: web.Request, job_id, body) -> web.Response:
    """Changes job status if possible (400 Bad Request is returned otherwise).

    Changes job status if possible (400 Bad Request is returned otherwise). The status has to be specified using one of the following keys:&lt;ul&gt;&lt;li&gt;OPEN – available when the job has one of the following statuses: ACCEPTED, CANCELED&lt;/li&gt;&lt;li&gt;ACCEPTED – available when the job has one of the following statuses: OPEN (Vendor and dates have to be set before calling the operation), STARTED&lt;/li&gt;&lt;li&gt;STARTED – available when the job has one of the following statuses: ACCEPTED, READY&lt;/li&gt;&lt;li&gt;READY – available when the job has one of the following statuses: STARTED&lt;/li&gt;&lt;li&gt;CANCELLED – available when the job has one of the following statuses: OPEN, ACCEPTED, STARTED, OFFERS_SENT&lt;/li&gt;&lt;li&gt;OFFERS_SENT – not available as a target status for this operation&lt;/li&gt;&lt;/ul&gt;

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: Changed job status.
    :type body: dict | bytes

    """
    body = JobStatusDTO.from_dict(body)
    return web.Response(status=200)


async def get_job_details(request: web.Request, job_id) -> web.Response:
    """Returns job details by jobId.

    Returns job details by jobId.

    :param job_id: job&#39;s internal identifier
    :type job_id: str

    """
    return web.Response(status=200)


async def get_job_files(request: web.Request, job_id) -> web.Response:
    """Returns list of input and output files of a job.

    Returns list of input and output files of a job.

    :param job_id: job&#39;s internal identifier
    :type job_id: str

    """
    return web.Response(status=200)


async def get_job_files1(request: web.Request, job_id, file_id) -> web.Response:
    """Returns file metadata.

    Returns file metadata.

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param file_id: file&#39;s internal identifier
    :type file_id: int

    """
    return web.Response(status=200)


async def update_dates(request: web.Request, job_id, body) -> web.Response:
    """Updates dates of a given job.

    Updates dates of a given job.

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: New job dates.
    :type body: dict | bytes

    """
    body = JobDatesDto.from_dict(body)
    return web.Response(status=200)


async def update_instructions(request: web.Request, job_id, body) -> web.Response:
    """Updates instructions for a job.

    Updates instructions for a job.

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: Updated instructions for a job.
    :type body: dict | bytes

    """
    body = InstructionsDTO.from_dict(body)
    return web.Response(status=200)
