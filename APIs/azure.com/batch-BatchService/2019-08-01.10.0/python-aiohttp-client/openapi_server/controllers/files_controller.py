from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.node_file_list_result import NodeFileListResult
from openapi_server import util


async def file_delete_from_compute_node(request: web.Request, pool_id, node_id, file_path, api_version, recursive=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Deletes the specified file from the Compute Node.

    

    :param pool_id: The ID of the Pool that contains the Compute Node.
    :type pool_id: str
    :param node_id: The ID of the Compute Node from which you want to delete the file.
    :type node_id: str
    :param file_path: The path to the file or directory that you want to delete.
    :type file_path: str
    :param api_version: Client API Version.
    :type api_version: str
    :param recursive: Whether to delete children of a directory. If the filePath parameter represents a directory instead of a file, you can set recursive to true to delete the directory and all of the files and subdirectories in it. If recursive is false then the directory must be empty or deletion will fail.
    :type recursive: bool
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def file_delete_from_task(request: web.Request, job_id, task_id, file_path, api_version, recursive=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Deletes the specified Task file from the Compute Node where the Task ran.

    

    :param job_id: The ID of the Job that contains the Task.
    :type job_id: str
    :param task_id: The ID of the Task whose file you want to delete.
    :type task_id: str
    :param file_path: The path to the Task file or directory that you want to delete.
    :type file_path: str
    :param api_version: Client API Version.
    :type api_version: str
    :param recursive: Whether to delete children of a directory. If the filePath parameter represents a directory instead of a file, you can set recursive to true to delete the directory and all of the files and subdirectories in it. If recursive is false then the directory must be empty or deletion will fail.
    :type recursive: bool
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def file_get_from_compute_node(request: web.Request, pool_id, node_id, file_path, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, ocp_range=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """file_get_from_compute_node

    Returns the content of the specified Compute Node file.

    :param pool_id: The ID of the Pool that contains the Compute Node.
    :type pool_id: str
    :param node_id: The ID of the Compute Node that contains the file.
    :type node_id: str
    :param file_path: The path to the Compute Node file that you want to get the content of.
    :type file_path: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str
    :param ocp_range: The byte range to be retrieved. The default is to retrieve the entire file. The format is bytes&#x3D;startRange-endRange.
    :type ocp_range: str
    :param if_modified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    :type if_modified_since: str
    :param if_unmodified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def file_get_from_task(request: web.Request, job_id, task_id, file_path, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, ocp_range=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """file_get_from_task

    Returns the content of the specified Task file.

    :param job_id: The ID of the Job that contains the Task.
    :type job_id: str
    :param task_id: The ID of the Task whose file you want to retrieve.
    :type task_id: str
    :param file_path: The path to the Task file that you want to get the content of.
    :type file_path: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str
    :param ocp_range: The byte range to be retrieved. The default is to retrieve the entire file. The format is bytes&#x3D;startRange-endRange.
    :type ocp_range: str
    :param if_modified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    :type if_modified_since: str
    :param if_unmodified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def file_get_properties_from_compute_node(request: web.Request, pool_id, node_id, file_path, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """file_get_properties_from_compute_node

    Gets the properties of the specified Compute Node file.

    :param pool_id: The ID of the Pool that contains the Compute Node.
    :type pool_id: str
    :param node_id: The ID of the Compute Node that contains the file.
    :type node_id: str
    :param file_path: The path to the Compute Node file that you want to get the properties of.
    :type file_path: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str
    :param if_modified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    :type if_modified_since: str
    :param if_unmodified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def file_get_properties_from_task(request: web.Request, job_id, task_id, file_path, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """file_get_properties_from_task

    Gets the properties of the specified Task file.

    :param job_id: The ID of the Job that contains the Task.
    :type job_id: str
    :param task_id: The ID of the Task whose file you want to get the properties of.
    :type task_id: str
    :param file_path: The path to the Task file that you want to get the properties of.
    :type file_path: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str
    :param if_modified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    :type if_modified_since: str
    :param if_unmodified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def file_list_from_compute_node(request: web.Request, pool_id, node_id, api_version, filter=None, recursive=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists all of the files in Task directories on the specified Compute Node.

    

    :param pool_id: The ID of the Pool that contains the Compute Node.
    :type pool_id: str
    :param node_id: The ID of the Compute Node whose files you want to list.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-compute-node-files.
    :type filter: str
    :param recursive: Whether to list children of a directory.
    :type recursive: bool
    :param maxresults: The maximum number of items to return in the response. A maximum of 1000 files can be returned.
    :type maxresults: int
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def file_list_from_task(request: web.Request, job_id, task_id, api_version, filter=None, recursive=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists the files in a Task&#39;s directory on its Compute Node.

    

    :param job_id: The ID of the Job that contains the Task.
    :type job_id: str
    :param task_id: The ID of the Task whose files you want to list.
    :type task_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-task-files.
    :type filter: str
    :param recursive: Whether to list children of the Task directory. This parameter can be used in combination with the filter parameter to list specific type of files.
    :type recursive: bool
    :param maxresults: The maximum number of items to return in the response. A maximum of 1000 files can be returned.
    :type maxresults: int
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    return web.Response(status=200)
