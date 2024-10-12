from typing import List, Dict
from aiohttp import web

from openapi_server.models.doctor_message import DoctorMessage
from openapi_server.models.inventory_categories_list200_response import InventoryCategoriesList200Response
from openapi_server.models.inventory_category import InventoryCategory
from openapi_server.models.inventory_vaccine import InventoryVaccine
from openapi_server.models.inventory_vaccines_list200_response import InventoryVaccinesList200Response
from openapi_server.models.messages_list200_response import MessagesList200Response
from openapi_server.models.office import Office
from openapi_server.models.offices_list200_response import OfficesList200Response
from openapi_server.models.task import Task
from openapi_server.models.task_categories_list200_response import TaskCategoriesList200Response
from openapi_server.models.task_category import TaskCategory
from openapi_server.models.task_note import TaskNote
from openapi_server.models.task_notes_list200_response import TaskNotesList200Response
from openapi_server.models.task_status import TaskStatus
from openapi_server.models.task_statuses_list200_response import TaskStatusesList200Response
from openapi_server.models.task_template import TaskTemplate
from openapi_server.models.task_templates_list200_response import TaskTemplatesList200Response
from openapi_server.models.tasks_list200_response import TasksList200Response
from openapi_server import util


async def inventory_categories_list(request: web.Request, cursor=None, page_size=None, since=None, doctor=None) -> web.Response:
    """inventory_categories_list

    Retrieve or search inventory categories

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def inventory_categories_read(request: web.Request, id, since=None, doctor=None) -> web.Response:
    """inventory_categories_read

    Retrieve an existing inventory category

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def inventory_vaccines_create(request: web.Request, status=None, cvx_code=None, since=None, doctor=None) -> web.Response:
    """inventory_vaccines_create

    Create vaccine inventory

    :param status: 
    :type status: str
    :param cvx_code: 
    :type cvx_code: str
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def inventory_vaccines_list(request: web.Request, cursor=None, page_size=None, status=None, cvx_code=None, since=None, doctor=None) -> web.Response:
    """inventory_vaccines_list

    Retrieve or search vaccine inventories

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param status: 
    :type status: str
    :param cvx_code: 
    :type cvx_code: str
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def inventory_vaccines_read(request: web.Request, id, status=None, cvx_code=None, since=None, doctor=None) -> web.Response:
    """inventory_vaccines_read

    Retrieve an existing vaccine inventory

    :param id: 
    :type id: str
    :param status: 
    :type status: str
    :param cvx_code: 
    :type cvx_code: str
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def messages_create(request: web.Request, patient=None, doctor=None, responsible_user=None, updated_since=None, received_since=None, owner=None, type=None) -> web.Response:
    """messages_create

    Create messages in doctor&#39;s message center

    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int
    :param responsible_user: 
    :type responsible_user: int
    :param updated_since: 
    :type updated_since: str
    :param received_since: 
    :type received_since: str
    :param owner: 
    :type owner: int
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def messages_delete(request: web.Request, id, patient=None, doctor=None, responsible_user=None, updated_since=None, received_since=None, owner=None, type=None) -> web.Response:
    """messages_delete

    Delete an existing message in doctor&#39;s message center

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int
    :param responsible_user: 
    :type responsible_user: int
    :param updated_since: 
    :type updated_since: str
    :param received_since: 
    :type received_since: str
    :param owner: 
    :type owner: int
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def messages_list(request: web.Request, cursor=None, page_size=None, patient=None, doctor=None, responsible_user=None, updated_since=None, received_since=None, owner=None, type=None) -> web.Response:
    """messages_list

    Retrieve or search messages in doctor&#39;s message center

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int
    :param responsible_user: 
    :type responsible_user: int
    :param updated_since: 
    :type updated_since: str
    :param received_since: 
    :type received_since: str
    :param owner: 
    :type owner: int
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def messages_partial_update(request: web.Request, id, patient=None, doctor=None, responsible_user=None, updated_since=None, received_since=None, owner=None, type=None) -> web.Response:
    """messages_partial_update

    Update an existing message in doctor&#39;s message center

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int
    :param responsible_user: 
    :type responsible_user: int
    :param updated_since: 
    :type updated_since: str
    :param received_since: 
    :type received_since: str
    :param owner: 
    :type owner: int
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def messages_read(request: web.Request, id, patient=None, doctor=None, responsible_user=None, updated_since=None, received_since=None, owner=None, type=None) -> web.Response:
    """messages_read

    Retrieve an existing message in doctor&#39;s message center

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int
    :param responsible_user: 
    :type responsible_user: int
    :param updated_since: 
    :type updated_since: str
    :param received_since: 
    :type received_since: str
    :param owner: 
    :type owner: int
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def messages_update(request: web.Request, id, patient=None, doctor=None, responsible_user=None, updated_since=None, received_since=None, owner=None, type=None) -> web.Response:
    """messages_update

    Update an existing message in doctor&#39;s message center

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int
    :param responsible_user: 
    :type responsible_user: int
    :param updated_since: 
    :type updated_since: str
    :param received_since: 
    :type received_since: str
    :param owner: 
    :type owner: int
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def offices_add_exam_room(request: web.Request, id, doctor=None) -> web.Response:
    """offices_add_exam_room

    Add an exam room to the office

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def offices_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """offices_list

    Retrieve or search offices

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def offices_partial_update(request: web.Request, id, doctor=None) -> web.Response:
    """offices_partial_update

    Update an existing office

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def offices_read(request: web.Request, id, doctor=None) -> web.Response:
    """offices_read

    Retrieve an existing office

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def offices_update(request: web.Request, id, doctor=None) -> web.Response:
    """offices_update

    Update an existing office

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def task_categories_create(request: web.Request, since=None) -> web.Response:
    """task_categories_create

    Create a task category

    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_categories_list(request: web.Request, cursor=None, page_size=None, since=None) -> web.Response:
    """task_categories_list

    Retrieve or search task categories

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_categories_partial_update(request: web.Request, id, since=None) -> web.Response:
    """task_categories_partial_update

    Update an existing task category

    :param id: 
    :type id: str
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_categories_read(request: web.Request, id, since=None) -> web.Response:
    """task_categories_read

    Retrieve an existing task category

    :param id: 
    :type id: str
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_categories_update(request: web.Request, id, since=None) -> web.Response:
    """task_categories_update

    Update an existing task category

    :param id: 
    :type id: str
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_notes_create(request: web.Request, task=None, since=None) -> web.Response:
    """task_notes_create

    Create a task note

    :param task: 
    :type task: int
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_notes_list(request: web.Request, cursor=None, page_size=None, task=None, since=None) -> web.Response:
    """task_notes_list

    Retrieve or search task notes

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param task: 
    :type task: int
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_notes_partial_update(request: web.Request, id, task=None, since=None) -> web.Response:
    """task_notes_partial_update

    Update an existing task note

    :param id: 
    :type id: str
    :param task: 
    :type task: int
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_notes_read(request: web.Request, id, task=None, since=None) -> web.Response:
    """task_notes_read

    Retrieve an existing task note

    :param id: 
    :type id: str
    :param task: 
    :type task: int
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_notes_update(request: web.Request, id, task=None, since=None) -> web.Response:
    """task_notes_update

    Update an existing task note

    :param id: 
    :type id: str
    :param task: 
    :type task: int
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_statuses_create(request: web.Request, since=None) -> web.Response:
    """task_statuses_create

    Create a task status

    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_statuses_list(request: web.Request, cursor=None, page_size=None, since=None) -> web.Response:
    """task_statuses_list

    Retrieve or search task statuses

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_statuses_partial_update(request: web.Request, id, since=None) -> web.Response:
    """task_statuses_partial_update

    Update an existing task status

    :param id: 
    :type id: str
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_statuses_read(request: web.Request, id, since=None) -> web.Response:
    """task_statuses_read

    Retrieve an existing task status

    :param id: 
    :type id: str
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_statuses_update(request: web.Request, id, since=None) -> web.Response:
    """task_statuses_update

    Update an existing task status

    :param id: 
    :type id: str
    :param since: 
    :type since: str

    """
    return web.Response(status=200)


async def task_templates_create(request: web.Request, assignee_user=None, status=None, assignee_group=None, since=None, category=None) -> web.Response:
    """task_templates_create

    Create a task template

    :param assignee_user: 
    :type assignee_user: int
    :param status: 
    :type status: int
    :param assignee_group: 
    :type assignee_group: int
    :param since: 
    :type since: str
    :param category: 
    :type category: int

    """
    return web.Response(status=200)


async def task_templates_list(request: web.Request, cursor=None, page_size=None, assignee_user=None, status=None, assignee_group=None, since=None, category=None) -> web.Response:
    """task_templates_list

    Retrieve or search task templates

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param assignee_user: 
    :type assignee_user: int
    :param status: 
    :type status: int
    :param assignee_group: 
    :type assignee_group: int
    :param since: 
    :type since: str
    :param category: 
    :type category: int

    """
    return web.Response(status=200)


async def task_templates_partial_update(request: web.Request, id, assignee_user=None, status=None, assignee_group=None, since=None, category=None) -> web.Response:
    """task_templates_partial_update

    Update an existing task template

    :param id: 
    :type id: str
    :param assignee_user: 
    :type assignee_user: int
    :param status: 
    :type status: int
    :param assignee_group: 
    :type assignee_group: int
    :param since: 
    :type since: str
    :param category: 
    :type category: int

    """
    return web.Response(status=200)


async def task_templates_read(request: web.Request, id, assignee_user=None, status=None, assignee_group=None, since=None, category=None) -> web.Response:
    """task_templates_read

    Retrieve an existing task template

    :param id: 
    :type id: str
    :param assignee_user: 
    :type assignee_user: int
    :param status: 
    :type status: int
    :param assignee_group: 
    :type assignee_group: int
    :param since: 
    :type since: str
    :param category: 
    :type category: int

    """
    return web.Response(status=200)


async def task_templates_update(request: web.Request, id, assignee_user=None, status=None, assignee_group=None, since=None, category=None) -> web.Response:
    """task_templates_update

    Update an existing task template

    :param id: 
    :type id: str
    :param assignee_user: 
    :type assignee_user: int
    :param status: 
    :type status: int
    :param assignee_group: 
    :type assignee_group: int
    :param since: 
    :type since: str
    :param category: 
    :type category: int

    """
    return web.Response(status=200)


async def tasks_create(request: web.Request, status=None, category=None, due_at_date=None, due_at_unknown=None, since=None, due_at_since=None, assignee_user=None, assignee_group=None, due_at_range=None) -> web.Response:
    """tasks_create

    Create a task

    :param status: 
    :type status: int
    :param category: 
    :type category: int
    :param due_at_date: 
    :type due_at_date: str
    :param due_at_unknown: 
    :type due_at_unknown: str
    :param since: 
    :type since: str
    :param due_at_since: 
    :type due_at_since: str
    :param assignee_user: 
    :type assignee_user: int
    :param assignee_group: 
    :type assignee_group: int
    :param due_at_range: 
    :type due_at_range: str

    """
    return web.Response(status=200)


async def tasks_list(request: web.Request, cursor=None, page_size=None, status=None, category=None, due_at_date=None, due_at_unknown=None, since=None, due_at_since=None, assignee_user=None, assignee_group=None, due_at_range=None) -> web.Response:
    """tasks_list

    Retrieve or search tasks

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param status: 
    :type status: int
    :param category: 
    :type category: int
    :param due_at_date: 
    :type due_at_date: str
    :param due_at_unknown: 
    :type due_at_unknown: str
    :param since: 
    :type since: str
    :param due_at_since: 
    :type due_at_since: str
    :param assignee_user: 
    :type assignee_user: int
    :param assignee_group: 
    :type assignee_group: int
    :param due_at_range: 
    :type due_at_range: str

    """
    return web.Response(status=200)


async def tasks_partial_update(request: web.Request, id, status=None, category=None, due_at_date=None, due_at_unknown=None, since=None, due_at_since=None, assignee_user=None, assignee_group=None, due_at_range=None) -> web.Response:
    """tasks_partial_update

    Update an existing task

    :param id: 
    :type id: str
    :param status: 
    :type status: int
    :param category: 
    :type category: int
    :param due_at_date: 
    :type due_at_date: str
    :param due_at_unknown: 
    :type due_at_unknown: str
    :param since: 
    :type since: str
    :param due_at_since: 
    :type due_at_since: str
    :param assignee_user: 
    :type assignee_user: int
    :param assignee_group: 
    :type assignee_group: int
    :param due_at_range: 
    :type due_at_range: str

    """
    return web.Response(status=200)


async def tasks_read(request: web.Request, id, status=None, category=None, due_at_date=None, due_at_unknown=None, since=None, due_at_since=None, assignee_user=None, assignee_group=None, due_at_range=None) -> web.Response:
    """tasks_read

    Retrieve an existing task

    :param id: 
    :type id: str
    :param status: 
    :type status: int
    :param category: 
    :type category: int
    :param due_at_date: 
    :type due_at_date: str
    :param due_at_unknown: 
    :type due_at_unknown: str
    :param since: 
    :type since: str
    :param due_at_since: 
    :type due_at_since: str
    :param assignee_user: 
    :type assignee_user: int
    :param assignee_group: 
    :type assignee_group: int
    :param due_at_range: 
    :type due_at_range: str

    """
    return web.Response(status=200)


async def tasks_update(request: web.Request, id, status=None, category=None, due_at_date=None, due_at_unknown=None, since=None, due_at_since=None, assignee_user=None, assignee_group=None, due_at_range=None) -> web.Response:
    """tasks_update

    Update an existing task

    :param id: 
    :type id: str
    :param status: 
    :type status: int
    :param category: 
    :type category: int
    :param due_at_date: 
    :type due_at_date: str
    :param due_at_unknown: 
    :type due_at_unknown: str
    :param since: 
    :type since: str
    :param due_at_since: 
    :type due_at_since: str
    :param assignee_user: 
    :type assignee_user: int
    :param assignee_group: 
    :type assignee_group: int
    :param due_at_range: 
    :type due_at_range: str

    """
    return web.Response(status=200)
