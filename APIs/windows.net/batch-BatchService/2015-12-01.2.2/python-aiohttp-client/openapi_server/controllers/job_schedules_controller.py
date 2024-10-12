from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.cloud_job_schedule import CloudJobSchedule
from openapi_server.models.cloud_job_schedule_list_result import CloudJobScheduleListResult
from openapi_server.models.job_schedule_add_parameter import JobScheduleAddParameter
from openapi_server.models.job_schedule_patch_parameter import JobSchedulePatchParameter
from openapi_server.models.job_schedule_update_parameter import JobScheduleUpdateParameter
from openapi_server import util


async def job_schedule_add(request: web.Request, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """job_schedule_add

    Adds a job schedule to the specified account.

    :param api_version: Client API Version.
    :type api_version: str
    :param body: Specifies the job schedule to be added.
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
    body = JobScheduleAddParameter.from_dict(body)
    return web.Response(status=200)


async def job_schedule_delete(request: web.Request, job_schedule_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_schedule_delete

    Deletes a job schedule from the specified account.

    :param job_schedule_id: The id of the job schedule to delete.
    :type job_schedule_id: str
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


async def job_schedule_disable(request: web.Request, job_schedule_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_schedule_disable

    Disables a job schedule.

    :param job_schedule_id: The id of the job schedule to disable.
    :type job_schedule_id: str
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


async def job_schedule_enable(request: web.Request, job_schedule_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_schedule_enable

    Enables a job schedule.

    :param job_schedule_id: The id of the job schedule to enable.
    :type job_schedule_id: str
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


async def job_schedule_exists(request: web.Request, job_schedule_id, api_version, select=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_schedule_exists

    Checks the specified job schedule exists.

    :param job_schedule_id: The id of the job schedule which you want to check.
    :type job_schedule_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param select: Sets an OData $select clause.
    :type select: str
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


async def job_schedule_get(request: web.Request, job_schedule_id, api_version, select=None, expand=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_schedule_get

    Gets information about the specified job schedule.

    :param job_schedule_id: The id of the job schedule to get.
    :type job_schedule_id: str
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


async def job_schedule_list(request: web.Request, api_version, filter=None, select=None, expand=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """job_schedule_list

    Lists all of the job schedules in the specified account.

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


async def job_schedule_patch(request: web.Request, job_schedule_id, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_schedule_patch

    Updates the properties of the specified job schedule.

    :param job_schedule_id: The id of the job schedule to update.
    :type job_schedule_id: str
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
    body = JobSchedulePatchParameter.from_dict(body)
    return web.Response(status=200)


async def job_schedule_terminate(request: web.Request, job_schedule_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_schedule_terminate

    Terminates a job schedule.

    :param job_schedule_id: The id of the job schedule to terminates.
    :type job_schedule_id: str
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


async def job_schedule_update(request: web.Request, job_schedule_id, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """job_schedule_update

    Updates the properties of the specified job schedule.

    :param job_schedule_id: The id of the job schedule to update.
    :type job_schedule_id: str
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
    body = JobScheduleUpdateParameter.from_dict(body)
    return web.Response(status=200)
