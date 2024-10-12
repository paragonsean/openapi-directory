from typing import List, Dict
from aiohttp import web

from openapi_server.models.clear_dag_run import ClearDagRun
from openapi_server.models.clear_dag_run200_response import ClearDagRun200Response
from openapi_server.models.dag_run import DAGRun
from openapi_server.models.dag_run_collection import DAGRunCollection
from openapi_server.models.dataset_event_collection import DatasetEventCollection
from openapi_server.models.error import Error
from openapi_server.models.list_dag_runs_form import ListDagRunsForm
from openapi_server.models.set_dag_run_note import SetDagRunNote
from openapi_server.models.update_dag_run_state import UpdateDagRunState
from openapi_server import util


async def clear_dag_run(request: web.Request, dag_id, dag_run_id, body) -> web.Response:
    """Clear a DAG run

    Clear a DAG run.  *New in version 2.4.0* 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClearDagRun.from_dict(body)
    return web.Response(status=200)


async def delete_dag_run(request: web.Request, dag_id, dag_run_id) -> web.Response:
    """Delete a DAG run

    

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str

    """
    return web.Response(status=200)


async def get_dag_run(request: web.Request, dag_id, dag_run_id) -> web.Response:
    """Get a DAG run

    

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str

    """
    return web.Response(status=200)


async def get_dag_runs(request: web.Request, dag_id, limit=None, offset=None, execution_date_gte=None, execution_date_lte=None, start_date_gte=None, start_date_lte=None, end_date_gte=None, end_date_lte=None, state=None, order_by=None) -> web.Response:
    """List DAG runs

    This endpoint allows specifying &#x60;~&#x60; as the dag_id to retrieve DAG runs for all DAGs. 

    :param dag_id: The DAG ID.
    :type dag_id: str
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
    :param state: The value can be repeated to retrieve multiple matching values (OR condition).
    :type state: List[str]
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


async def get_dag_runs_batch(request: web.Request, body) -> web.Response:
    """List DAG runs (batch)

    This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit. 

    :param body: 
    :type body: dict | bytes

    """
    body = ListDagRunsForm.from_dict(body)
    return web.Response(status=200)


async def get_upstream_dataset_events(request: web.Request, dag_id, dag_run_id) -> web.Response:
    """Get dataset events for a DAG run

    Get datasets for a dag run.  *New in version 2.4.0* 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str

    """
    return web.Response(status=200)


async def post_dag_run(request: web.Request, dag_id, body) -> web.Response:
    """Trigger a new DAG run

    

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DAGRun.from_dict(body)
    return web.Response(status=200)


async def set_dag_run_note(request: web.Request, dag_id, dag_run_id, body) -> web.Response:
    """Update the DagRun note.

    Update the manual user note of a DagRun.  *New in version 2.5.0* 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param body: Parameters of set DagRun note.
    :type body: dict | bytes

    """
    body = SetDagRunNote.from_dict(body)
    return web.Response(status=200)


async def update_dag_run_state(request: web.Request, dag_id, dag_run_id, body) -> web.Response:
    """Modify a DAG run

    Modify a DAG run.  *New in version 2.2.0* 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDagRunState.from_dict(body)
    return web.Response(status=200)
