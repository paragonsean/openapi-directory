from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.node_file_list_result import NodeFileListResult
from openapi_server import util


async def file_delete_from_compute_node(request: web.Request, pool_id, node_id, file_name, api_version, recursive=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """file_delete_from_compute_node

    Deletes the specified task file from the compute node.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the compute node from which you want to delete the file.
    :type node_id: str
    :param file_name: The path to the file that you want to delete.
    :type file_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param recursive: Sets whether to delete children of a directory. If the fileName parameter represents a directory instead of a file, you can set Recursive to true to delete the directory and all of the files and subdirectories in it. If Recursive is false then the directory must be empty or deletion will fail.
    :type recursive: bool
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def file_delete_from_task(request: web.Request, job_id, task_id, file_name, api_version, recursive=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """file_delete_from_task

    Deletes the specified task file from the compute node where the task ran.

    :param job_id: The id of the job that contains the task.
    :type job_id: str
    :param task_id: The id of the task whose file you want to delete.
    :type task_id: str
    :param file_name: The path to the task file that you want to delete.
    :type file_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param recursive: Sets whether to delete children of a directory. If the fileName parameter represents a directory instead of a file, you can set Recursive to true to delete the directory and all of the files and subdirectories in it. If Recursive is false then the directory must be empty or deletion will fail.
    :type recursive: bool
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def file_get_from_compute_node(request: web.Request, pool_id, node_id, file_name, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, ocp_range=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """file_get_from_compute_node

    Gets the content of the specified task file.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the compute node that contains the file.
    :type node_id: str
    :param file_name: The path to the task file that you want to get the content of.
    :type file_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param ocp_range: Specifies the byte range to be retrieved. The default is to retrieve the entire file.  The format is startRange-endRange.
    :type ocp_range: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def file_get_from_task(request: web.Request, job_id, task_id, file_name, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, ocp_range=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """file_get_from_task

    Gets the content of the specified task file.

    :param job_id: The id of the job that contains the task.
    :type job_id: str
    :param task_id: The id of the task whose file you want to retrieve.
    :type task_id: str
    :param file_name: The path to the task file that you want to get the content of.
    :type file_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param ocp_range: Specifies the byte range to be retrieved. The default is to retrieve the entire file.  The format is startRange-endRange.
    :type ocp_range: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def file_get_node_file_properties_from_compute_node(request: web.Request, pool_id, node_id, file_name, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """file_get_node_file_properties_from_compute_node

    Gets the properties of the specified compute node file.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the compute node that contains the file.
    :type node_id: str
    :param file_name: The path to the compute node file that you want to get the properties of.
    :type file_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def file_get_node_file_properties_from_task(request: web.Request, job_id, task_id, file_name, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """file_get_node_file_properties_from_task

    Gets the properties of the specified task file.

    :param job_id: The id of the job that contains the task.
    :type job_id: str
    :param task_id: The id of the task whose file you want to get the properties of.
    :type task_id: str
    :param file_name: The path to the task file that you want to get the properties of.
    :type file_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def file_list_from_compute_node(request: web.Request, pool_id, node_id, api_version, filter=None, recursive=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """file_list_from_compute_node

    Lists all of the files in task directories on the specified compute node.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the compute node whose files you want to list.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: Sets an OData $filter clause.
    :type filter: str
    :param recursive: Sets whether to list children of a directory.
    :type recursive: bool
    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def file_list_from_task(request: web.Request, job_id, task_id, api_version, filter=None, recursive=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """file_list_from_task

    Lists the files in a task&#39;s directory on its compute node.

    :param job_id: The id of the job that contains the task.
    :type job_id: str
    :param task_id: The id of the task whose files you want to list.
    :type task_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: Sets an OData $filter clause.
    :type filter: str
    :param recursive: Sets whether to list children of a directory.
    :type recursive: bool
    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)
