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


async def task_add(request: web.Request, job_id, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """task_add

    Adds a task to the specified job.

    :param job_id: The id of the job to which the task is to be added.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param body: The task to be added.
    :type body: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    body = TaskAddParameter.from_dict(body)
    return web.Response(status=200)


async def task_add_collection(request: web.Request, job_id, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """task_add_collection

    Adds a collection of tasks to the specified job.

    :param job_id: The id of the job to which the task collection is to be added.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param body: The tasks to be added.
    :type body: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    body = TaskAddCollectionParameter.from_dict(body)
    return web.Response(status=200)


async def task_delete(request: web.Request, job_id, task_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """task_delete

    Deletes a task from the specified job.

    :param job_id: The id of the job from which to delete the task.
    :type job_id: str
    :param task_id: The id of the task to delete.
    :type task_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id identifier in the response.
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
    """task_get

    Gets information about the specified task.

    :param job_id: The id of the job that contains the task.
    :type job_id: str
    :param task_id: The id of the task to get information about.
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
    :param return_client_request_id: Whether the server should return the client-request-id identifier in the response.
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
    """task_list

    Lists all of the tasks that are associated with the specified job.

    :param job_id: The id of the job.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: An OData $filter clause.
    :type filter: str
    :param select: An OData $select clause.
    :type select: str
    :param expand: An OData $expand clause.
    :type expand: str
    :param maxresults: The maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def task_list_subtasks(request: web.Request, job_id, task_id, api_version, select=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """task_list_subtasks

    Lists all of the subtasks that are associated with the specified multi-instance task.

    :param job_id: The id of the job.
    :type job_id: str
    :param task_id: The id of the task.
    :type task_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param select: An OData $select clause.
    :type select: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def task_terminate(request: web.Request, job_id, task_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """task_terminate

    Terminates the specified task.

    :param job_id: The id of the job containing the task.
    :type job_id: str
    :param task_id: The id of the task to terminate.
    :type task_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id identifier in the response.
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


async def task_update(request: web.Request, job_id, task_id, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """task_update

    Updates the properties of the specified task.

    :param job_id: The id of the job containing the task.
    :type job_id: str
    :param task_id: The id of the task to update.
    :type task_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param body: The parameters for the request.
    :type body: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id identifier in the response.
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
    body = TaskUpdateParameter.from_dict(body)
    return web.Response(status=200)
