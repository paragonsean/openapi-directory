from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.extra_link_collection import ExtraLinkCollection
from openapi_server.models.get_log200_response import GetLog200Response
from openapi_server.models.list_task_instance_form import ListTaskInstanceForm
from openapi_server.models.set_task_instance_note import SetTaskInstanceNote
from openapi_server.models.task_instance import TaskInstance
from openapi_server.models.task_instance_collection import TaskInstanceCollection
from openapi_server.models.task_instance_reference import TaskInstanceReference
from openapi_server.models.update_task_instance import UpdateTaskInstance
from openapi_server import util


async def get_extra_links(request: web.Request, dag_id, dag_run_id, task_id) -> web.Response:
    """List extra links

    List extra links for task instance. 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param task_id: The task ID.
    :type task_id: str

    """
    return web.Response(status=200)


async def get_log(request: web.Request, dag_id, dag_run_id, task_id, task_try_number, full_content=None, map_index=None, token=None) -> web.Response:
    """Get logs

    Get logs for a specific task instance and its try number.

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param task_id: The task ID.
    :type task_id: str
    :param task_try_number: The task try number.
    :type task_try_number: int
    :param full_content: A full content will be returned. By default, only the first fragment will be returned. 
    :type full_content: bool
    :param map_index: Filter on map index for mapped task.
    :type map_index: int
    :param token: A token that allows you to continue fetching logs. If passed, it will specify the location from which the download should be continued. 
    :type token: str

    """
    return web.Response(status=200)


async def get_mapped_task_instance(request: web.Request, dag_id, dag_run_id, task_id, map_index) -> web.Response:
    """Get a mapped task instance

    Get details of a mapped task instance.  *New in version 2.3.0* 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param task_id: The task ID.
    :type task_id: str
    :param map_index: The map index.
    :type map_index: int

    """
    return web.Response(status=200)


async def get_mapped_task_instances(request: web.Request, dag_id, dag_run_id, task_id, limit=None, offset=None, execution_date_gte=None, execution_date_lte=None, start_date_gte=None, start_date_lte=None, end_date_gte=None, end_date_lte=None, duration_gte=None, duration_lte=None, state=None, pool=None, queue=None, order_by=None) -> web.Response:
    """List mapped task instances

    Get details of all mapped task instances.  *New in version 2.3.0* 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param task_id: The task ID.
    :type task_id: str
    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param execution_date_gte: Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period. 
    :type execution_date_gte: str
    :param execution_date_lte: Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period. 
    :type execution_date_lte: str
    :param start_date_gte: Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
    :type start_date_gte: str
    :param start_date_lte: Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
    :type start_date_lte: str
    :param end_date_gte: Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
    :type end_date_gte: str
    :param end_date_lte: Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
    :type end_date_lte: str
    :param duration_gte: Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period. 
    :type duration_gte: 
    :param duration_lte: Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range. 
    :type duration_lte: 
    :param state: The value can be repeated to retrieve multiple matching values (OR condition).
    :type state: List[str]
    :param pool: The value can be repeated to retrieve multiple matching values (OR condition).
    :type pool: List[str]
    :param queue: The value can be repeated to retrieve multiple matching values (OR condition).
    :type queue: List[str]
    :param order_by: The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0* 
    :type order_by: str

    """
    execution_date_gte = util.deserialize_datetime(execution_date_gte)
    execution_date_lte = util.deserialize_datetime(execution_date_lte)
    start_date_gte = util.deserialize_datetime(start_date_gte)
    start_date_lte = util.deserialize_datetime(start_date_lte)
    end_date_gte = util.deserialize_datetime(end_date_gte)
    end_date_lte = util.deserialize_datetime(end_date_lte)
    return web.Response(status=200)


async def get_task_instance(request: web.Request, dag_id, dag_run_id, task_id) -> web.Response:
    """Get a task instance

    

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param task_id: The task ID.
    :type task_id: str

    """
    return web.Response(status=200)


async def get_task_instances(request: web.Request, dag_id, dag_run_id, execution_date_gte=None, execution_date_lte=None, start_date_gte=None, start_date_lte=None, end_date_gte=None, end_date_lte=None, duration_gte=None, duration_lte=None, state=None, pool=None, queue=None, limit=None, offset=None) -> web.Response:
    """List task instances

    This endpoint allows specifying &#x60;~&#x60; as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and DAG runs. 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param execution_date_gte: Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period. 
    :type execution_date_gte: str
    :param execution_date_lte: Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period. 
    :type execution_date_lte: str
    :param start_date_gte: Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
    :type start_date_gte: str
    :param start_date_lte: Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
    :type start_date_lte: str
    :param end_date_gte: Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
    :type end_date_gte: str
    :param end_date_lte: Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
    :type end_date_lte: str
    :param duration_gte: Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period. 
    :type duration_gte: 
    :param duration_lte: Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range. 
    :type duration_lte: 
    :param state: The value can be repeated to retrieve multiple matching values (OR condition).
    :type state: List[str]
    :param pool: The value can be repeated to retrieve multiple matching values (OR condition).
    :type pool: List[str]
    :param queue: The value can be repeated to retrieve multiple matching values (OR condition).
    :type queue: List[str]
    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int

    """
    execution_date_gte = util.deserialize_datetime(execution_date_gte)
    execution_date_lte = util.deserialize_datetime(execution_date_lte)
    start_date_gte = util.deserialize_datetime(start_date_gte)
    start_date_lte = util.deserialize_datetime(start_date_lte)
    end_date_gte = util.deserialize_datetime(end_date_gte)
    end_date_lte = util.deserialize_datetime(end_date_lte)
    return web.Response(status=200)


async def get_task_instances_batch(request: web.Request, body) -> web.Response:
    """List task instances (batch)

    List task instances from all DAGs and DAG runs. This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limits. 

    :param body: 
    :type body: dict | bytes

    """
    body = ListTaskInstanceForm.from_dict(body)
    return web.Response(status=200)


async def patch_mapped_task_instance(request: web.Request, dag_id, dag_run_id, task_id, map_index, body=None) -> web.Response:
    """Updates the state of a mapped task instance

    Updates the state for single mapped task instance. *New in version 2.5.0* 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param task_id: The task ID.
    :type task_id: str
    :param map_index: The map index.
    :type map_index: int
    :param body: Parameters of action
    :type body: dict | bytes

    """
    body = UpdateTaskInstance.from_dict(body)
    return web.Response(status=200)


async def patch_task_instance(request: web.Request, dag_id, dag_run_id, task_id, body) -> web.Response:
    """Updates the state of a task instance

    Updates the state for single task instance. *New in version 2.5.0* 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param task_id: The task ID.
    :type task_id: str
    :param body: Parameters of action
    :type body: dict | bytes

    """
    body = UpdateTaskInstance.from_dict(body)
    return web.Response(status=200)


async def set_mapped_task_instance_note(request: web.Request, dag_id, dag_run_id, task_id, map_index, body) -> web.Response:
    """Update the TaskInstance note.

    Update the manual user note of a mapped Task Instance.  *New in version 2.5.0* 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param task_id: The task ID.
    :type task_id: str
    :param map_index: The map index.
    :type map_index: int
    :param body: Parameters of set Task Instance note.
    :type body: dict | bytes

    """
    body = SetTaskInstanceNote.from_dict(body)
    return web.Response(status=200)


async def set_task_instance_note(request: web.Request, dag_id, dag_run_id, task_id, body) -> web.Response:
    """Update the TaskInstance note.

    Update the manual user note of a non-mapped Task Instance.  *New in version 2.5.0* 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param task_id: The task ID.
    :type task_id: str
    :param body: Parameters of set Task Instance note.
    :type body: dict | bytes

    """
    body = SetTaskInstanceNote.from_dict(body)
    return web.Response(status=200)
