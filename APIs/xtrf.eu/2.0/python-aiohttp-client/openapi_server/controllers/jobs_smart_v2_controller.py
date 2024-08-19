from typing import List, Dict
from aiohttp import web

from openapi_server.models.external_file_dto import ExternalFileDto
from openapi_server.models.file_categorizations_dto import FileCategorizationsDto
from openapi_server.models.file_dto import FileDto
from openapi_server.models.file_link_categorizations_dto import FileLinkCategorizationsDto
from openapi_server.models.files_dto import FilesDto
from openapi_server.models.files_share_status_dto import FilesShareStatusDto
from openapi_server.models.job_dates_dto import JobDatesDto
from openapi_server.models.job_status_dto import JobStatusDTO
from openapi_server.models.project_file_dto import ProjectFileDto
from openapi_server.models.string_dto import StringDTO
from openapi_server.models.vendor_price_profile_dto import VendorPriceProfileDTO
from openapi_server import util


async def add_external_file_link(request: web.Request, job_id, body) -> web.Response:
    """add_external_file_link

    

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: Added file links to the project as added by PM.
    :type body: dict | bytes

    """
    body = ExternalFileDto.from_dict(body)
    return web.Response(status=200)


async def add_file_links(request: web.Request, job_id, body) -> web.Response:
    """Adds file link to the project as a link delivered in the job.

    Adds file link to the project as a link delivered in the job. The following properties can be specified for each file link:&lt;ul&gt;&lt;li&gt;url (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: Adds file link to the project as a link delivered in the job.
    :type body: dict | bytes

    """
    body = FileLinkCategorizationsDto.from_dict(body)
    return web.Response(status=200)


async def add_files(request: web.Request, job_id, body) -> web.Response:
    """Adds files to the project as delivered in the job.

    Adds files to the project as delivered in the job. The files have to be uploaded beforehand (see \&quot;POST /jobs/{jobId}/files/upload\&quot; operation). The following properties can be specified for each file:&lt;ul&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: Added files to the project as delivered in the job.
    :type body: dict | bytes

    """
    body = FileCategorizationsDto.from_dict(body)
    return web.Response(status=200)


async def assign_vendor1(request: web.Request, job_id, body) -> web.Response:
    """Assigns vendor to a job in a project.

    Assigns vendor to a job in a project.

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: Assigned vendor to a job in a project.
    :type body: dict | bytes

    """
    body = VendorPriceProfileDTO.from_dict(body)
    return web.Response(status=200)


async def change_dates(request: web.Request, job_id, body) -> web.Response:
    """Updates dates of a given job.

    Updates dates of a given job.

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: New job dates.
    :type body: dict | bytes

    """
    body = JobDatesDto.from_dict(body)
    return web.Response(status=200)


async def change_status1(request: web.Request, job_id, body) -> web.Response:
    """Changes job status if possible (400 Bad Request is returned otherwise).

    Changes job status if possible (400 Bad Request is returned otherwise). The status has to be specified using one of the following keys:&lt;ul&gt;&lt;li&gt;OPEN – available when the job has one of the following statuses: ACCEPTED, CANCELED&lt;/li&gt;&lt;li&gt;ACCEPTED – available when the job has one of the following statuses: OPEN (Vendor and dates have to be set before calling the operation), STARTED&lt;/li&gt;&lt;li&gt;STARTED – available when the job has one of the following statuses: ACCEPTED, READY&lt;/li&gt;&lt;li&gt;READY – available when the job has one of the following statuses: STARTED&lt;/li&gt;&lt;li&gt;CANCELLED – available when the job has one of the following statuses: OPEN, ACCEPTED, STARTED, OFFERS_SENT&lt;/li&gt;&lt;li&gt;OFFERS_SENT – not available as a target status for this operation&lt;/li&gt;&lt;/ul&gt;

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: Changed job status.
    :type body: dict | bytes

    """
    body = JobStatusDTO.from_dict(body)
    return web.Response(status=200)


async def get_by_external_id(request: web.Request, external_project_id=None, external_id=None) -> web.Response:
    """get_by_external_id

    

    :param external_project_id: job&#39;s externalProjectId
    :type external_project_id: str
    :param external_id: job&#39;s external identifier
    :type external_id: str

    """
    return web.Response(status=200)


async def get_delivered_files(request: web.Request, job_id) -> web.Response:
    """Returns list of files delivered in the job.

    Returns list of files delivered in the job.

    :param job_id: job&#39;s internal identifier
    :type job_id: str

    """
    return web.Response(status=200)


async def get_file_by_id1(request: web.Request, job_id) -> web.Response:
    """Returns details for a job.

    Returns details for a job.

    :param job_id: job&#39;s internal identifier
    :type job_id: str

    """
    return web.Response(status=200)


async def get_shared_reference_files(request: web.Request, job_id) -> web.Response:
    """Returns list of files shared with the job as Reference Files.

    Returns list of files shared with the job as Reference Files.

    :param job_id: job&#39;s internal identifier
    :type job_id: str

    """
    return web.Response(status=200)


async def get_shared_work_files(request: web.Request, job_id) -> web.Response:
    """Returns list of files shared with the job as Work Files.

    Returns list of files shared with the job as Work Files.

    :param job_id: job&#39;s internal identifier
    :type job_id: str

    """
    return web.Response(status=200)


async def share_as_reference_files(request: web.Request, job_id, body) -> web.Response:
    """Shares selected files as Reference Files with a job in a project.

    Shares selected files as Reference Files with a job in a project. The files and the job have to be part of the same project. The operation is finished successfully even if some of the selected files were already shared with the job. If a file was shared with the job as Work File, it will now be shared as Reference File (and not as Work File).

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: Shared selected files as Reference Files with a job in a project.
    :type body: dict | bytes

    """
    body = FilesDto.from_dict(body)
    return web.Response(status=200)


async def share_as_work_files(request: web.Request, job_id, body) -> web.Response:
    """Shares selected files as Work Files with a job in a project.

    Shares selected files as Work Files with a job in a project. The files and the job have to be part of the same project. The operation is finished successfully even if some of the selected files were already shared with the job. If a file was shared with the job as Reference File, it will now be shared as Work File (and not as Reference File).

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: Shared selected files as Work Files with a job in a project.
    :type body: dict | bytes

    """
    body = FilesDto.from_dict(body)
    return web.Response(status=200)


async def stop_sharing(request: web.Request, job_id, body) -> web.Response:
    """Stops sharing selected files with a job in a project.

    Stops sharing selected files with a job in a project. The files and the job have to be part of the same project. The operation is finished successfully even if some of the selected files were not shared with the job.

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: File sharing stopped for a project task.
    :type body: dict | bytes

    """
    body = FilesDto.from_dict(body)
    return web.Response(status=200)


async def update_instructions4(request: web.Request, job_id, body) -> web.Response:
    """Updates instructions for a job.

    Updates instructions for a job. See also \&quot;PUT /projects/{projectId}/vendorInstructions\&quot; and \&quot;PUT /quotes/{quoteId}/vendorInstructions\&quot; for updating instructions for all jobs in a project or quote.

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param body: Updated instructions for a job.
    :type body: dict | bytes

    """
    body = StringDTO.from_dict(body)
    return web.Response(status=200)


async def upload_file1(request: web.Request, job_id, file=None) -> web.Response:
    """Uploads file to the project as a file delivered in the job.

    Uploads file to the project as a file delivered in the job. Only one file can be uploaded at once. When the upload is finished the file has to be added by specifying its category and languages (see \&quot;PUT /jobs/{jobId}/files/add\&quot; operation).

    :param job_id: job&#39;s internal identifier
    :type job_id: str
    :param file: 
    :type file: str

    """
    return web.Response(status=200)
