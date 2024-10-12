from typing import List, Dict
from aiohttp import web

from openapi_server.models.big_decimal_dto import BigDecimalDTO
from openapi_server.models.cat_tool_project_dto import CATToolProjectDTO
from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.external_file_dto import ExternalFileDto
from openapi_server.models.file_categorizations_dto import FileCategorizationsDto
from openapi_server.models.file_dto import FileDto
from openapi_server.models.file_link_categorizations_dto import FileLinkCategorizationsDto
from openapi_server.models.files_archive_dto import FilesArchiveDto
from openapi_server.models.files_dto import FilesDto
from openapi_server.models.finance_dto import FinanceDTO
from openapi_server.models.job_dto import JobDto
from openapi_server.models.payable_create_dto import PayableCreateDTO
from openapi_server.models.payable_dto import PayableDTO
from openapi_server.models.project_create_dto import ProjectCreateDTO
from openapi_server.models.project_dtov2 import ProjectDTOv2
from openapi_server.models.project_file_dto import ProjectFileDto
from openapi_server.models.project_status_dto import ProjectStatusDTO
from openapi_server.models.receivable_create_dto import ReceivableCreateDTO
from openapi_server.models.receivable_dto import ReceivableDTO
from openapi_server.models.smart_contacts_dto import SmartContactsDTO
from openapi_server.models.smart_custom_field_dto import SmartCustomFieldDTO
from openapi_server.models.source_language_dto import SourceLanguageDTO
from openapi_server.models.specialization_dto import SpecializationDTO
from openapi_server.models.string_dto import StringDTO
from openapi_server.models.target_languages_dto import TargetLanguagesDTO
from openapi_server.models.time_dto import TimeDTO
from openapi_server import util


async def add_external_file_links(request: web.Request, project_id, body) -> web.Response:
    """add_external_file_links

    

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Added file links to the project as added by PM.
    :type body: dict | bytes

    """
    body = ExternalFileDto.from_dict(body)
    return web.Response(status=200)


async def add_file_links1(request: web.Request, project_id, body) -> web.Response:
    """Adds file links to the project as added by PM.

    Adds file links to the project as added by PM. The following properties can be specified for each file link:&lt;ul&gt;&lt;li&gt;url (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Added file links to the project as added by PM.
    :type body: dict | bytes

    """
    body = FileLinkCategorizationsDto.from_dict(body)
    return web.Response(status=200)


async def add_files1(request: web.Request, project_id, body) -> web.Response:
    """Adds files to the project as added by PM.

    Adds files to the project as added by PM. The files have to be uploaded beforehand (see \&quot;POST /v2/projects/{projectId}/files/upload\&quot; operation). The following properties can be specified for each file:&lt;ul&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Added files to the project as added by PM.
    :type body: dict | bytes

    """
    body = FileCategorizationsDto.from_dict(body)
    return web.Response(status=200)


async def add_job_to_process(request: web.Request, project_id) -> web.Response:
    """Returns process id.

    

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def archive(request: web.Request, body) -> web.Response:
    """Prepares a ZIP archive that contains the specified files.

    Prepares a ZIP archive that contains the specified files.

    :param body: Prepared ZIP archive that contains the specified files.
    :type body: dict | bytes

    """
    body = FilesDto.from_dict(body)
    return web.Response(status=200)


async def change_status2(request: web.Request, project_id, body) -> web.Response:
    """Changes project status if possible (400 Bad Request is returned otherwise).

    Changes project status if possible (400 Bad Request is returned otherwise). The status has to be specified using one of the following keys: &lt;ul&gt;&lt;li&gt;CANCELLED – available when the job has one of the following statuses: OPEN, STARTED&lt;/li&gt;&lt;/ul&gt;

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Changed project status.
    :type body: dict | bytes

    """
    body = ProjectStatusDTO.from_dict(body)
    return web.Response(status=200)


async def create6(request: web.Request, body=None) -> web.Response:
    """Creates a new Smart Project.

    Creates a new Smart Project. If the specified service ID refers to Classic Project, 400 Bad Request is returned instead.

    :param body: 
    :type body: dict | bytes

    """
    body = ProjectCreateDTO.from_dict(body)
    return web.Response(status=200)


async def create_payable2(request: web.Request, project_id, body) -> web.Response:
    """Adds a payable to a project.

    Adds a payable to a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PayableCreateDTO.from_dict(body)
    return web.Response(status=200)


async def create_receivable2(request: web.Request, project_id, body) -> web.Response:
    """Adds a receivable to a project.

    Adds a receivable to a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReceivableCreateDTO.from_dict(body)
    return web.Response(status=200)


async def delete_payable2(request: web.Request, project_id, payable_id) -> web.Response:
    """Deletes a payable.

    Deletes a payable.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param payable_id: payable&#39;s internal identifier
    :type payable_id: int

    """
    return web.Response(status=200)


async def delete_receivable2(request: web.Request, project_id, receivable_id) -> web.Response:
    """Deletes a receivable.

    Deletes a receivable.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param receivable_id: receivable&#39;s internal identifier
    :type receivable_id: int

    """
    return web.Response(status=200)


async def get_by_external_id1(request: web.Request, external_project_id) -> web.Response:
    """Returns project details.

    Returns project details.

    :param external_project_id: project&#39;s external identifier
    :type external_project_id: str

    """
    return web.Response(status=200)


async def get_by_id9(request: web.Request, project_id) -> web.Response:
    """Returns project details.

    Returns project details. If the specified project ID refers to Classic Project, 400 Bad Request is returned instead.

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def get_cat_tool_project_info(request: web.Request, project_id) -> web.Response:
    """Returns if cat tool project is created or queued.

    

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def get_contacts2(request: web.Request, project_id) -> web.Response:
    """Returns Client Contacts information for a project.

    Returns Client Contacts information for a project

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def get_custom_fields8(request: web.Request, project_id) -> web.Response:
    """Returns a list of custom field keys and values for a project.

    Returns a list of custom field keys and values for a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def get_deliverable_files(request: web.Request, project_id) -> web.Response:
    """Returns list of files in a project, that are ready to be delivered to client.

    Returns list of files in a project, that are ready to be delivered to client. A file is considered deliverable to client when all of the following criteria are met:&lt;ul&gt;&lt;li&gt;the file was added to a job in the last step in the process&lt;/li&gt;&lt;li&gt;the file is marked as verified (if it was added in a verification step and the file is verifiable, according to its category)&lt;/li&gt;&lt;li&gt;the job is finished (has Ready status)&lt;/li&gt;&lt;/ul&gt;

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def get_file_by_id2(request: web.Request, file_id) -> web.Response:
    """Returns details of a file.

    Returns details of a file.

    :param file_id: file&#39;s internal identifier
    :type file_id: str

    """
    return web.Response(status=200)


async def get_file_content_by_id(request: web.Request, file_id, file_name) -> web.Response:
    """Downloads a file content.

    Downloads a file content.

    :param file_id: file&#39;s internal identifier
    :type file_id: str
    :param file_name: file&#39;s name
    :type file_name: str

    """
    return web.Response(status=200)


async def get_files(request: web.Request, project_id) -> web.Response:
    """Returns list of files in a project.

    Returns list of files in a project. Only files added to the project (i.e. files that have assigned category and languages) are listed.

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def get_finance2(request: web.Request, project_id) -> web.Response:
    """Returns finance information for a project.

    Returns finance information for a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def get_jobs(request: web.Request, project_id) -> web.Response:
    """Returns list of jobs in a project.

    Returns list of jobs in a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def get_process_id(request: web.Request, project_id) -> web.Response:
    """Returns process id.

    

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def update_client_deadline(request: web.Request, project_id, body) -> web.Response:
    """Updates Client Deadline for a project.

    Updates Client Deadline for a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated Client Deadline for a project.
    :type body: dict | bytes

    """
    body = TimeDTO.from_dict(body)
    return web.Response(status=200)


async def update_client_notes(request: web.Request, project_id, body) -> web.Response:
    """Updates Client Notes for a project.

    Updates Client Notes for a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated Client Notes for a project.
    :type body: dict | bytes

    """
    body = StringDTO.from_dict(body)
    return web.Response(status=200)


async def update_client_reference_number(request: web.Request, project_id, body) -> web.Response:
    """Updates Client Reference Number for a project.

    Updates Client Reference Number for a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated Client Reference Number for a project.
    :type body: dict | bytes

    """
    body = StringDTO.from_dict(body)
    return web.Response(status=200)


async def update_contacts2(request: web.Request, project_id, body) -> web.Response:
    """Updates Client Contacts for a project.

    Updates Client Contacts for a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated Client Contacts for a project.
    :type body: dict | bytes

    """
    body = SmartContactsDTO.from_dict(body)
    return web.Response(status=200)


async def update_custom_field2(request: web.Request, project_id, key, body) -> web.Response:
    """Updates a custom field with a specified key in a project

    Updates a custom field with a specified key in a project

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param key: custom field&#39;s key
    :type key: str
    :param body: Updated custom field with a specified key in a project.
    :type body: dict | bytes

    """
    body = SmartCustomFieldDTO.from_dict(body)
    return web.Response(status=200)


async def update_internal_notes(request: web.Request, project_id, body) -> web.Response:
    """Updates Internal Notes for a project.

    Updates Internal Notes for a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated Internal Notes for a project.
    :type body: dict | bytes

    """
    body = StringDTO.from_dict(body)
    return web.Response(status=200)


async def update_ordered_on(request: web.Request, project_id, body) -> web.Response:
    """Updates Order Date for a project.

    Updates Order Date for a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated Order Date for a project.
    :type body: dict | bytes

    """
    body = TimeDTO.from_dict(body)
    return web.Response(status=200)


async def update_payable2(request: web.Request, project_id, payable_id, body) -> web.Response:
    """Updates a payable.

    Updates a payable.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param payable_id: payable&#39;s internal identifier
    :type payable_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PayableDTO.from_dict(body)
    return web.Response(status=200)


async def update_receivable2(request: web.Request, project_id, receivable_id, body) -> web.Response:
    """Updates a receivable.

    Updates a receivable.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param receivable_id: receivable&#39;s internal identifier
    :type receivable_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReceivableDTO.from_dict(body)
    return web.Response(status=200)


async def update_source_language(request: web.Request, project_id, body) -> web.Response:
    """Updates source language for a project.

    Updates source language for a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated source language for a project.
    :type body: dict | bytes

    """
    body = SourceLanguageDTO.from_dict(body)
    return web.Response(status=200)


async def update_specialization(request: web.Request, project_id, body) -> web.Response:
    """Updates specialization for a project.

    Updates specialization for a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated specialization for a project.
    :type body: dict | bytes

    """
    body = SpecializationDTO.from_dict(body)
    return web.Response(status=200)


async def update_target_languages(request: web.Request, project_id, body) -> web.Response:
    """Updates target languages for a project.

    Updates target languages for a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated target languages for a project.
    :type body: dict | bytes

    """
    body = TargetLanguagesDTO.from_dict(body)
    return web.Response(status=200)


async def update_vendor_instructions(request: web.Request, project_id, body) -> web.Response:
    """Updates instructions for all vendors performing the jobs in a project.

    Updates instructions for all vendors performing the jobs in a project. See also \&quot;PUT /jobs/{jobId}/instructions\&quot; for updating instructions for a specific job in a project or quote.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated instructions for all vendors performing the jobs in a project.
    :type body: dict | bytes

    """
    body = StringDTO.from_dict(body)
    return web.Response(status=200)


async def update_volume(request: web.Request, project_id, body) -> web.Response:
    """Updates volume for a project.

    Updates volume for a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated volume for a project.
    :type body: dict | bytes

    """
    body = BigDecimalDTO.from_dict(body)
    return web.Response(status=200)


async def upload_file2(request: web.Request, project_id, file=None) -> web.Response:
    """Uploads file to the project as a file uploaded by PM.

    Uploads file to the project as a file uploaded by PM. Only one file can be uploaded at once. When the upload is finished the file has to be added by specifying its category and languages (see \&quot;PUT /v2/projects/{projectId}/files/add\&quot; operation

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param file: 
    :type file: str

    """
    return web.Response(status=200)
