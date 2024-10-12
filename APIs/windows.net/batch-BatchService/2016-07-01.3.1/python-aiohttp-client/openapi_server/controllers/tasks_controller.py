from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.cloud_task import CloudTask
from openapi_server.models.cloud_task_list_result import CloudTaskListResult
from openapi_server.models.cloud_task_list_subtasks_result import CloudTaskListSubtasksResult
from openapi_server.models.task_add_collection_parameter import TaskAddCollectionParameter
from openapi_server.models.task_add_collection_result import TaskAddCollectionResult
from openapi_server.models.task_add_parameter import TaskAddParameter
from openapi_server.models.task_update_parameter import TaskUpdateParameter
from openapi_server import util


async def task_add(request: web.Request, job_id, api_version, task, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Adds a task to the specified job.

    

    :param job_id: The ID of the job to which the task is to be added.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param task: The task to be added.
    :type task: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    task = TaskAddParameter.from_dict(task)
    return web.Response(status=200)


async def task_add_collection(request: web.Request, job_id, api_version, task_collection, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Adds a collection of tasks to the specified job.

    Note that each task must have a unique ID. The Batch service may not return the results for each task in the same order the tasks were submitted in this request. If the server times out or the connection is closed during the request, the request may have been partially or fully processed, or not at all. In such cases, the user should re-issue the request. Note that it is up to the user to correctly handle failures when re-issuing a request. For example, you should use the same task ids during a retry so that if the prior operation succeeded, the retry will not create extra tasks unexpectedly.

    :param job_id: The ID of the job to which the task collection is to be added.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param task_collection: The tasks to be added.
    :type task_collection: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    task_collection = TaskAddCollectionParameter.from_dict(task_collection)
    return web.Response(status=200)


async def task_delete(request: web.Request, job_id, task_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Deletes a task from the specified job.

    When a task is deleted, all of the files in its directory on the compute node where it ran are also deleted (regardless of the retention time). For multi-instance tasks, the delete task operation applies synchronously to the primary task; subtasks and their files are then deleted asynchronously in the background.

    :param job_id: The ID of the job from which to delete the task.
    :type job_id: str
    :param task_id: The ID of the task to delete.
    :type task_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def task_get(request: web.Request, job_id, task_id, api_version, select=None, expand=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Gets information about the specified task.

    For multi-instance tasks, information such as affinityId, executionInfo and nodeInfo refer to the primary task. Use the list subtasks API to retrieve information about subtasks.

    :param job_id: The ID of the job that contains the task.
    :type job_id: str
    :param task_id: The ID of the task to get information about.
    :type task_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param select: An OData $select clause.
    :type select: str
    :param expand: An OData $expand clause.
    :type expand: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def task_list(request: web.Request, job_id, api_version, filter=None, select=None, expand=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists all of the tasks that are associated with the specified job.

    For multi-instance tasks, information such as affinityId, executionInfo and nodeInfo refer to the primary task. Use the list subtasks API to retrieve information about subtasks.

    :param job_id: The ID of the job.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: An OData $filter clause.
    :type filter: str
    :param select: An OData $select clause.
    :type select: str
    :param expand: An OData $expand clause.
    :type expand: str
    :param maxresults: The maximum number of items to return in the response. A maximum of 1000 tasks can be returned.
    :type maxresults: int
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def task_list_subtasks(request: web.Request, job_id, task_id, api_version, select=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists all of the subtasks that are associated with the specified multi-instance task.

    If the task is not a multi-instance task then this returns an empty collection.

    :param job_id: The ID of the job.
    :type job_id: str
    :param task_id: The ID of the task.
    :type task_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param select: An OData $select clause.
    :type select: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def task_reactivate(request: web.Request, job_id, task_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Reactivates the specified task.

    Reactivation makes a task eligible to be retried again up to its maximum retry count. The task&#39;s state is changed to active. As the task is no longer in the completed state, any previous exit code or scheduling error is no longer available after reactivation. This will fail for tasks that are not completed or that previously completed successfully (with an exit code of 0). Additionally, this will fail if the job has completed (or is terminating or deleting).

    :param job_id: The ID of the job containing the task.
    :type job_id: str
    :param task_id: The ID of the task to reactivate.
    :type task_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def task_terminate(request: web.Request, job_id, task_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Terminates the specified task.

    When the task has been terminated, it moves to the completed state. For multi-instance tasks, the terminate task operation applies synchronously to the primary task; subtasks are then terminated asynchronously in the background.

    :param job_id: The ID of the job containing the task.
    :type job_id: str
    :param task_id: The ID of the task to terminate.
    :type task_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def task_update(request: web.Request, job_id, task_id, api_version, task_update_parameter, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """task_update

    Updates the properties of the specified task.

    :param job_id: The ID of the job containing the task.
    :type job_id: str
    :param task_id: The ID of the task to update.
    :type task_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param task_update_parameter: The parameters for the request.
    :type task_update_parameter: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    task_update_parameter = TaskUpdateParameter.from_dict(task_update_parameter)
    return web.Response(status=200)
