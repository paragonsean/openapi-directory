from typing import List, Dict
from aiohttp import web

from openapi_server.models.clear_task_instances import ClearTaskInstances
from openapi_server.models.dag import DAG
from openapi_server.models.dag_collection import DAGCollection
from openapi_server.models.dag_detail import DAGDetail
from openapi_server.models.error import Error
from openapi_server.models.get_dag_source200_response import GetDagSource200Response
from openapi_server.models.task import Task
from openapi_server.models.task_collection import TaskCollection
from openapi_server.models.task_instance_reference_collection import TaskInstanceReferenceCollection
from openapi_server.models.update_task_instances_state import UpdateTaskInstancesState
from openapi_server import util


async def delete_dag(request: web.Request, dag_id) -> web.Response:
    """Delete a DAG

    Deletes all metadata related to the DAG, including finished DAG Runs and Tasks. Logs are not deleted. This action cannot be undone.  *New in version 2.2.0* 

    :param dag_id: The DAG ID.
    :type dag_id: str

    """
    return web.Response(status=200)


async def get_dag(request: web.Request, dag_id) -> web.Response:
    """Get basic information about a DAG

    Presents only information available in database (DAGModel). If you need detailed information, consider using GET /dags/{dag_id}/details. 

    :param dag_id: The DAG ID.
    :type dag_id: str

    """
    return web.Response(status=200)


async def get_dag_details(request: web.Request, dag_id) -> web.Response:
    """Get a simplified representation of DAG

    The response contains many DAG attributes, so the response can be large. If possible, consider using GET /dags/{dag_id}. 

    :param dag_id: The DAG ID.
    :type dag_id: str

    """
    return web.Response(status=200)


async def get_dag_source(request: web.Request, file_token) -> web.Response:
    """Get a source code

    Get a source code using file token. 

    :param file_token: The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change. 
    :type file_token: str

    """
    return web.Response(status=200)


async def get_dags(request: web.Request, limit=None, offset=None, order_by=None, tags=None, only_active=None, dag_id_pattern=None) -> web.Response:
    """List DAGs

    List DAGs in the database. &#x60;dag_id_pattern&#x60; can be set to match dags of a specific pattern 

    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param order_by: The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0* 
    :type order_by: str
    :param tags: List of tags to filter results.  *New in version 2.2.0* 
    :type tags: List[str]
    :param only_active: Only filter active DAGs.  *New in version 2.1.1* 
    :type only_active: bool
    :param dag_id_pattern: If set, only return DAGs with dag_ids matching this pattern. 
    :type dag_id_pattern: str

    """
    return web.Response(status=200)


async def get_task(request: web.Request, dag_id, task_id) -> web.Response:
    """Get simplified representation of a task

    

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param task_id: The task ID.
    :type task_id: str

    """
    return web.Response(status=200)


async def get_tasks(request: web.Request, dag_id, order_by=None) -> web.Response:
    """Get tasks for DAG

    

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param order_by: The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0* 
    :type order_by: str

    """
    return web.Response(status=200)


async def patch_dag(request: web.Request, dag_id, body, update_mask=None) -> web.Response:
    """Update a DAG

    

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param body: 
    :type body: dict | bytes
    :param update_mask: The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
    :type update_mask: List[str]

    """
    body = DAG.from_dict(body)
    return web.Response(status=200)


async def patch_dags(request: web.Request, dag_id_pattern, body, limit=None, offset=None, tags=None, update_mask=None, only_active=None) -> web.Response:
    """Update DAGs

    Update DAGs of a given dag_id_pattern using UpdateMask. This endpoint allows specifying &#x60;~&#x60; as the dag_id_pattern to update all DAGs. *New in version 2.3.0* 

    :param dag_id_pattern: If set, only update DAGs with dag_ids matching this pattern. 
    :type dag_id_pattern: str
    :param body: 
    :type body: dict | bytes
    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param tags: List of tags to filter results.  *New in version 2.2.0* 
    :type tags: List[str]
    :param update_mask: The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
    :type update_mask: List[str]
    :param only_active: Only filter active DAGs.  *New in version 2.1.1* 
    :type only_active: bool

    """
    body = DAG.from_dict(body)
    return web.Response(status=200)


async def post_clear_task_instances(request: web.Request, dag_id, body) -> web.Response:
    """Clear a set of task instances

    Clears a set of task instances associated with the DAG for a specified date range. 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param body: Parameters of action
    :type body: dict | bytes

    """
    body = ClearTaskInstances.from_dict(body)
    return web.Response(status=200)


async def post_set_task_instances_state(request: web.Request, dag_id, body) -> web.Response:
    """Set a state of task instances

    Updates the state for multiple task instances simultaneously. 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param body: Parameters of action
    :type body: dict | bytes

    """
    body = UpdateTaskInstancesState.from_dict(body)
    return web.Response(status=200)
