from typing import List, Dict
from aiohttp import web

from openapi_server.models.contacts_dto import ContactsDTO
from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.file_dto import FileDTO
from openapi_server.models.instructions_dto import InstructionsDTO
from openapi_server.models.project_dates_dto import ProjectDatesDTO
from openapi_server.models.string_dto import StringDTO
from openapi_server.models.task_files_dto import TaskFilesDTO
from openapi_server.models.task_progress_dto import TaskProgressDTO
from openapi_server import util


async def add_file(request: web.Request, task_id, body) -> web.Response:
    """Adds files to a given task.

    Adds files to a given task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = FileDTO.from_dict(body)
    return web.Response(status=200)


async def delete14(request: web.Request, task_id, remove_files_from_disc=None, remove_external_projects=None, force_jobs_removal=None) -> web.Response:
    """Removes a task.

    Removes a task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str
    :param remove_files_from_disc: remove files from disc
    :type remove_files_from_disc: bool
    :param remove_external_projects: remove external projects (ie. from CAT Tool)
    :type remove_external_projects: bool
    :param force_jobs_removal: force jobs removal (ie. started or ready)
    :type force_jobs_removal: bool

    """
    return web.Response(status=200)


async def get_contacts1(request: web.Request, task_id) -> web.Response:
    """Returns contacts of a given task.

    Returns contacts of a given task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str

    """
    return web.Response(status=200)


async def get_custom_fields7(request: web.Request, task_id) -> web.Response:
    """Returns custom fields of a given task.

    Returns custom fields of a given task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str

    """
    return web.Response(status=200)


async def get_dates3(request: web.Request, task_id) -> web.Response:
    """Returns dates of a given task.

    Returns dates of a given task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str

    """
    return web.Response(status=200)


async def get_instructions2(request: web.Request, task_id) -> web.Response:
    """Returns instructions of a given task.

    Returns instructions of a given task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str

    """
    return web.Response(status=200)


async def get_progress(request: web.Request, task_id) -> web.Response:
    """Returns progress of a given task.

    Returns progress of a given task. Progress contains information about task&#39;s status (ie. opened or ready) and current phase (ie. translation). Workflow phase is defined as the first one which contains not ready jobs (ie. opened or started). When no such job exists then workflow phase is not included.

    :param task_id: task&#39;s internal identifier
    :type task_id: str

    """
    return web.Response(status=200)


async def get_task_files(request: web.Request, task_id) -> web.Response:
    """Returns lists of files of a given task.

    Returns several lists of files for a given task: input files divided by type, output files, bundles, files per job, preview files.

    :param task_id: task&#39;s internal identifier
    :type task_id: str

    """
    return web.Response(status=200)


async def start1(request: web.Request, task_id) -> web.Response:
    """Starts a task.

    Starts a task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str

    """
    return web.Response(status=200)


async def update_client_task_po_number(request: web.Request, task_id, body) -> web.Response:
    """Updates Client Task PO Number of a given task.

    Updates Client Task PO Number of a given task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str
    :param body: Updated Client Task PO Number of a given task.
    :type body: dict | bytes

    """
    body = StringDTO.from_dict(body)
    return web.Response(status=200)


async def update_contacts1(request: web.Request, task_id, body) -> web.Response:
    """Updates contacts of a given task.

    Updates contacts of a given task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str
    :param body: Updated contacts of given task.
    :type body: dict | bytes

    """
    body = ContactsDTO.from_dict(body)
    return web.Response(status=200)


async def update_custom_fields5(request: web.Request, task_id, body) -> web.Response:
    """Updates custom fields of a given task.

    Updates custom fields of a given task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str
    :param body: Updated custom fields

    """
    return web.Response(status=200)


async def update_dates2(request: web.Request, task_id, body) -> web.Response:
    """Updates dates of a given task.

    Updates dates of a given task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str
    :param body: Updated dates of a given task.
    :type body: dict | bytes

    """
    body = ProjectDatesDTO.from_dict(body)
    return web.Response(status=200)


async def update_instructions3(request: web.Request, task_id, body) -> web.Response:
    """Updates instructions of a given task.

    Updates instructions of a given task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str
    :param body: Updated instructions of a given task.
    :type body: dict | bytes

    """
    body = InstructionsDTO.from_dict(body)
    return web.Response(status=200)


async def update_name(request: web.Request, task_id, body) -> web.Response:
    """Updates name of a given task.

    Updates name of a given task.

    :param task_id: task&#39;s internal identifier
    :type task_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = StringDTO.from_dict(body)
    return web.Response(status=200)
