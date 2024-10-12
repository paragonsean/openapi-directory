from typing import List, Dict
from aiohttp import web

from openapi_server.models.step import Step
from openapi_server.models.task import Task
from openapi_server import util


async def v2_tasks_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch a task

    Fetches a task, by ID only. 

    :param id: Task ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_tasks_id_json_put(request: web.Request, id, current_state=None, description=None, due_date=None, is_logged=None, remind_at=None, subject=None) -> web.Response:
    """Update a Task

    Updates a task. 

    :param id: Task ID
    :type id: str
    :param current_state: Current state of the task, valid options are: completed
    :type current_state: str
    :param description: A description of the task recorded for person at completion time
    :type description: str
    :param due_date: Date of when the Task is due, ISO-8601 date format required
    :type due_date: str
    :param is_logged: A flag to indicate that the task should only be logged
    :type is_logged: bool
    :param remind_at: Datetime of when the user will be reminded of the task, ISO-8601 datetime format required
    :type remind_at: str
    :param subject: Subject line of the task
    :type subject: str

    """
    return web.Response(status=200)


async def v2_tasks_json_get(request: web.Request, ids=None, user_id=None, person_id=None, account_id=None, current_state=None, task_type=None, time_interval_filter=None, idempotency_key=None, locale=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List tasks

    Fetches multiple task records. The records can be filtered, paged, and sorted according to the respective parameters. 

    :param ids: IDs of tasks to fetch.
    :type ids: List[int]
    :param user_id: Filters tasks by the user to which they are assigned.
    :type user_id: List[int]
    :param person_id: Filters tasks by the person to which they are associated.
    :type person_id: List[int]
    :param account_id: Filters tasks by the account to which they are associated.
    :type account_id: List[int]
    :param current_state: Filters tasks by their current state. Valid current_states include: [&#39;scheduled&#39;, &#39;completed&#39;].
    :type current_state: List[str]
    :param task_type: Filters tasks by their task type. Valid task_types include: [&#39;call&#39;, &#39;email&#39;, &#39;general&#39;].
    :type task_type: List[str]
    :param time_interval_filter: Filters tasks by time interval. Valid time_intervals include: [&#39;overdue&#39;, &#39;today&#39;, &#39;tomorrow&#39;, &#39;this_week&#39;, &#39;next_week&#39;].
    :type time_interval_filter: str
    :param idempotency_key: Filters tasks by idempotency key.
    :type idempotency_key: str
    :param locale: Filters tasks by locale of the person to which they are associated.
    :type locale: List[str]
    :param sort_by: Key to sort on, must be one of: due_date, due_at. Defaults to due_date
    :type sort_by: str
    :param sort_direction: Direction to sort in, must be one of: ASC, DESC. Defaults to ASC
    :type sort_direction: str
    :param per_page: How many records to show per page in the range [1, 100]. Defaults to 25
    :type per_page: int
    :param page: The current page to fetch results from. Defaults to 1
    :type page: int
    :param include_paging_counts: Whether to include total_pages and total_count in the metadata. Defaults to false
    :type include_paging_counts: bool
    :param limit_paging_counts: Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    :type limit_paging_counts: bool

    """
    return web.Response(status=200)


async def v2_tasks_json_post(request: web.Request, current_state, due_date, person_id, subject, task_type, user_id, description=None, idempotency_key=None, remind_at=None) -> web.Response:
    """Create a Task

    Creates a task. 

    :param current_state: Current state of the task, valid options are: scheduled
    :type current_state: str
    :param due_date: Date of when the Task is due, ISO-8601 date format required
    :type due_date: str
    :param person_id: ID of the person to be contacted
    :type person_id: str
    :param subject: Subject line of the task.
    :type subject: str
    :param task_type: Task type, valid options are: call, email, general
    :type task_type: str
    :param user_id: ID of the user linked to the task
    :type user_id: int
    :param description: A description of the task recorded for person at completion time
    :type description: str
    :param idempotency_key: Establishes a unique identifier to prevent duplicates from being created
    :type idempotency_key: str
    :param remind_at: Datetime of when the user will be reminded of the task, ISO-8601 datetime format required
    :type remind_at: str

    """
    return web.Response(status=200)
