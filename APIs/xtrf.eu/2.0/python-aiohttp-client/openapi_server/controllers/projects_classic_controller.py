from typing import List, Dict
from aiohttp import web

from openapi_server.models.classic_project_create_dto import ClassicProjectCreateDTO
from openapi_server.models.common_language_combination_dto import CommonLanguageCombinationDTO
from openapi_server.models.contacts_dto import ContactsDTO
from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.finance_dto import FinanceDTO
from openapi_server.models.instructions_dto import InstructionsDTO
from openapi_server.models.payable_create_dto import PayableCreateDTO
from openapi_server.models.payable_dto import PayableDTO
from openapi_server.models.project_dtov1 import ProjectDTOv1
from openapi_server.models.project_dates_dto import ProjectDatesDTO
from openapi_server.models.receivable_create_dto import ReceivableCreateDTO
from openapi_server.models.receivable_dto import ReceivableDTO
from openapi_server.models.task_create_dto import TaskCreateDTO
from openapi_server.models.task_dto import TaskDTO
from openapi_server import util


async def create5(request: web.Request, body) -> web.Response:
    """Creates a new Classic Project.

    Creates a new Classic Project. If the specified service ID refers to Smart Project, 400 Bad Request is returned instead.

    :param body: Created a new Classic Project.
    :type body: dict | bytes

    """
    body = ClassicProjectCreateDTO.from_dict(body)
    return web.Response(status=200)


async def create_language_combination(request: web.Request, project_id, body) -> web.Response:
    """Creates a new language combination for a given project without creating a task.

    Creates a new language combination for a given project without creating a task.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Created language combination for a given project without creating a task.
    :type body: dict | bytes

    """
    body = CommonLanguageCombinationDTO.from_dict(body)
    return web.Response(status=200)


async def create_payable(request: web.Request, project_id, body) -> web.Response:
    """Adds a payable to a project.

    Adds a payable to a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PayableCreateDTO.from_dict(body)
    return web.Response(status=200)


async def create_receivable(request: web.Request, project_id, body) -> web.Response:
    """Adds a receivable to a project.

    Adds a receivable to a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReceivableCreateDTO.from_dict(body)
    return web.Response(status=200)


async def create_task(request: web.Request, project_id, body) -> web.Response:
    """Creates a new task for a given project.

    Creates a new task for a given project.&lt;p&gt;   Required fields:   &lt;ul&gt;     &lt;li&gt;languageCombination&lt;/li&gt;     &lt;li&gt;specializationId&lt;/li&gt;     &lt;li&gt;workflowId&lt;/li&gt;   &lt;/ul&gt; &lt;/p&gt; 

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Created new task for a given project.
    :type body: dict | bytes

    """
    body = TaskCreateDTO.from_dict(body)
    return web.Response(status=200)


async def delete12(request: web.Request, project_id) -> web.Response:
    """Removes a project.

    Removes a project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def delete_payable(request: web.Request, project_id, payable_id) -> web.Response:
    """Deletes a payable.

    Deletes a payable.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param payable_id: payable&#39;s internal identifier
    :type payable_id: int

    """
    return web.Response(status=200)


async def delete_receivable(request: web.Request, project_id, receivable_id) -> web.Response:
    """Deletes a receivable.

    Deletes a receivable.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param receivable_id: receivable&#39;s internal identifier
    :type receivable_id: int

    """
    return web.Response(status=200)


async def get_all_ids6(request: web.Request, updated_since=None) -> web.Response:
    """Returns projects&#39; internal identifiers.

    Returns projects&#39; internal identifiers.

    :param updated_since: only projects modified since this timestamp
    :type updated_since: int

    """
    return web.Response(status=200)


async def get_by_id7(request: web.Request, project_id, embed=None) -> web.Response:
    """Returns project details.

    Returns project details. If the specified project ID refers to Smart Project, 400 Bad Request is returned instead.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param embed: list of additional fields which should be embedded in the response (available options: tasks)
    :type embed: str

    """
    return web.Response(status=200)


async def get_contacts(request: web.Request, project_id) -> web.Response:
    """Returns contacts of a given project.

    Returns contacts of a given project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def get_custom_fields5(request: web.Request, project_id) -> web.Response:
    """Returns custom fields of a given project.

    Returns custom fields of a given project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def get_dates1(request: web.Request, project_id) -> web.Response:
    """Returns dates of a given project.

    Returns dates of a given project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def get_file_by_id(request: web.Request, file_id) -> web.Response:
    """Downloads a file.

    Downloads a file.

    :param file_id: file&#39;s internal identifier
    :type file_id: str

    """
    return web.Response(status=200)


async def get_finance(request: web.Request, project_id) -> web.Response:
    """Returns finance of a given project.

    Returns finance of a given project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def get_instructions(request: web.Request, project_id) -> web.Response:
    """Returns instructions of a given project.

    Returns instructions of a given project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str

    """
    return web.Response(status=200)


async def update_contacts(request: web.Request, project_id, body) -> web.Response:
    """Updates contacts of a given project.

    Updates contacts of a given project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated contacts of a given project.
    :type body: dict | bytes

    """
    body = ContactsDTO.from_dict(body)
    return web.Response(status=200)


async def update_custom_fields3(request: web.Request, project_id, body) -> web.Response:
    """Updates custom fields of a given project.

    Updates custom fields of a given project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated custom fields of a given project.

    """
    return web.Response(status=200)


async def update_dates1(request: web.Request, project_id, body) -> web.Response:
    """Updates dates of a given project.

    Updates dates of a given project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated dates of a given project..
    :type body: dict | bytes

    """
    body = ProjectDatesDTO.from_dict(body)
    return web.Response(status=200)


async def update_instructions1(request: web.Request, project_id, body) -> web.Response:
    """Updates instructions of a given project.

    Updates instructions of a given project.

    :param project_id: project&#39;s internal identifier
    :type project_id: str
    :param body: Updated instructions of a given project.
    :type body: dict | bytes

    """
    body = InstructionsDTO.from_dict(body)
    return web.Response(status=200)


async def update_payable(request: web.Request, project_id, payable_id, body) -> web.Response:
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


async def update_receivable(request: web.Request, project_id, receivable_id, body) -> web.Response:
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
