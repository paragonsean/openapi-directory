from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.cloud_job import CloudJob
from openapi_server.models.cloud_job_list_preparation_and_release_task_status_result import CloudJobListPreparationAndReleaseTaskStatusResult
from openapi_server.models.cloud_job_list_result import CloudJobListResult
from openapi_server.models.job_add_parameter import JobAddParameter
from openapi_server.models.job_disable_parameter import JobDisableParameter
from openapi_server.models.job_patch_parameter import JobPatchParameter
from openapi_server.models.job_statistics import JobStatistics
from openapi_server.models.job_terminate_parameter import JobTerminateParameter
from openapi_server.models.job_update_parameter import JobUpdateParameter
from openapi_server import util


async def job_add(request: web.Request, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """job_add

    Adds a job to the specified account.

    :param api_version: Client API Version.
    :type api_version: str
    :param body: Specifies the job to be added.
    :type body: dict | bytes
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    body = JobAddParameter.from_dict(body)
    return web.Response(status=200)


async def job_delete(request: web.Request, job_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_delete

    Deletes a job.

    :param job_id: The id of the job to delete.
    :type job_id: str
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


async def job_disable(request: web.Request, job_id, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_disable

    Disables the specified job, preventing new tasks from running.

    :param job_id: The id of the job to disable.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param body: The parameters for the request.
    :type body: dict | bytes
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
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
    body = JobDisableParameter.from_dict(body)
    return web.Response(status=200)


async def job_enable(request: web.Request, job_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_enable

    Enables the specified job, allowing new tasks to run.

    :param job_id: The id of the job to enable.
    :type job_id: str
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


async def job_get(request: web.Request, job_id, api_version, select=None, expand=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """job_get

    Gets information about the specified job.

    :param job_id: The id of the job.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param select: Sets an OData $select clause.
    :type select: str
    :param expand: Sets an OData $expand clause.
    :type expand: str
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


async def job_get_all_jobs_lifetime_statistics(request: web.Request, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """job_get_all_jobs_lifetime_statistics

    Gets lifetime summary statistics for all of the jobs in the specified account. Statistics are aggregated across all jobs that have ever existed in the account, from account creation to the last update time of the statistics.

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

    """
    return web.Response(status=200)


async def job_list(request: web.Request, api_version, filter=None, select=None, expand=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """job_list

    Lists all of the jobs in the specified account.

    :param api_version: Client API Version.
    :type api_version: str
    :param filter: Sets an OData $filter clause.
    :type filter: str
    :param select: Sets an OData $select clause.
    :type select: str
    :param expand: Sets an OData $expand clause.
    :type expand: str
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


async def job_list_from_job_schedule(request: web.Request, job_schedule_id, api_version, filter=None, select=None, expand=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """job_list_from_job_schedule

    Lists the jobs that have been created under the specified job schedule.

    :param job_schedule_id: The id of the job schedule from which you want to get a list of jobs.
    :type job_schedule_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: Sets an OData $filter clause.
    :type filter: str
    :param select: Sets an OData $select clause.
    :type select: str
    :param expand: Sets an OData $expand clause.
    :type expand: str
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


async def job_list_preparation_and_release_task_status(request: web.Request, job_id, api_version, filter=None, select=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """job_list_preparation_and_release_task_status

    Lists the execution status of the Job Preparation and Job Release task for the specified job across the compute nodes where the job has run.

    :param job_id: The id of the job.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: Sets an OData $filter clause.
    :type filter: str
    :param select: Sets an OData $select clause.
    :type select: str
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


async def job_patch(request: web.Request, job_id, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_patch

    Updates the properties of a job.

    :param job_id: The id of the job whose properties you want to update.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param body: The parameters for the request.
    :type body: dict | bytes
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
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
    body = JobPatchParameter.from_dict(body)
    return web.Response(status=200)


async def job_terminate(request: web.Request, job_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, body=None) -> web.Response:
    """job_terminate

    Terminates the specified job, marking it as completed.

    :param job_id: The id of the job to terminate.
    :type job_id: str
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
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str
    :param body: The parameters for the request.
    :type body: dict | bytes

    """
    body = JobTerminateParameter.from_dict(body)
    return web.Response(status=200)


async def job_update(request: web.Request, job_id, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_update

    Updates the properties of a job.

    :param job_id: The id of the job whose properties you want to update.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param body: The parameters for the request.
    :type body: dict | bytes
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
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
    body = JobUpdateParameter.from_dict(body)
    return web.Response(status=200)
