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
from openapi_server.models.task_counts import TaskCounts
from openapi_server import util


async def job_add(request: web.Request, api_version, job, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Adds a job to the specified account.

    The Batch service supports two ways to control the work done as part of a job. In the first approach, the user specifies a Job Manager task. The Batch service launches this task when it is ready to start the job. The Job Manager task controls all other tasks that run under this job, by using the Task APIs. In the second approach, the user directly controls the execution of tasks under an active job, by using the Task APIs. Also note: when naming jobs, avoid including sensitive information such as user names or secret project names. This information may appear in telemetry logs accessible to Microsoft Support engineers.

    :param api_version: Client API Version.
    :type api_version: str
    :param job: The job to be added.
    :type job: dict | bytes
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
    job = JobAddParameter.from_dict(job)
    return web.Response(status=200)


async def job_delete(request: web.Request, job_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Deletes a job.

    Deleting a job also deletes all tasks that are part of that job, and all job statistics. This also overrides the retention period for task data; that is, if the job contains tasks which are still retained on compute nodes, the Batch services deletes those tasks&#39; working directories and all their contents.  When a Delete Job request is received, the Batch service sets the job to the deleting state. All update operations on a job that is in deleting state will fail with status code 409 (Conflict), with additional information indicating that the job is being deleted.

    :param job_id: The ID of the job to delete.
    :type job_id: str
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
    :param if_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client.
    :type if_match: str
    :param if_none_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client.
    :type if_none_match: str
    :param if_modified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    :type if_modified_since: str
    :param if_unmodified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def job_disable(request: web.Request, job_id, api_version, job_disable_parameter, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Disables the specified job, preventing new tasks from running.

    The Batch Service immediately moves the job to the disabling state. Batch then uses the disableTasks parameter to determine what to do with the currently running tasks of the job. The job remains in the disabling state until the disable operation is completed and all tasks have been dealt with according to the disableTasks option; the job then moves to the disabled state. No new tasks are started under the job until it moves back to active state. If you try to disable a job that is in any state other than active, disabling, or disabled, the request fails with status code 409.

    :param job_id: The ID of the job to disable.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param job_disable_parameter: The parameters for the request.
    :type job_disable_parameter: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str
    :param if_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client.
    :type if_match: str
    :param if_none_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client.
    :type if_none_match: str
    :param if_modified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    :type if_modified_since: str
    :param if_unmodified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    :type if_unmodified_since: str

    """
    job_disable_parameter = JobDisableParameter.from_dict(job_disable_parameter)
    return web.Response(status=200)


async def job_enable(request: web.Request, job_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Enables the specified job, allowing new tasks to run.

    When you call this API, the Batch service sets a disabled job to the enabling state. After the this operation is completed, the job moves to the active state, and scheduling of new tasks under the job resumes. The Batch service does not allow a task to remain in the active state for more than 180 days. Therefore, if you enable a job containing active tasks which were added more than 180 days ago, those tasks will not run.

    :param job_id: The ID of the job to enable.
    :type job_id: str
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
    :param if_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client.
    :type if_match: str
    :param if_none_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client.
    :type if_none_match: str
    :param if_modified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    :type if_modified_since: str
    :param if_unmodified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def job_get(request: web.Request, job_id, api_version, select=None, expand=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Gets information about the specified job.

    

    :param job_id: The ID of the job.
    :type job_id: str
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
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str
    :param if_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client.
    :type if_match: str
    :param if_none_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client.
    :type if_none_match: str
    :param if_modified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    :type if_modified_since: str
    :param if_unmodified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def job_get_all_lifetime_statistics(request: web.Request, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Gets lifetime summary statistics for all of the jobs in the specified account.

    Statistics are aggregated across all jobs that have ever existed in the account, from account creation to the last update time of the statistics. The statistics may not be immediately available. The Batch service performs periodic roll-up of statistics. The typical delay is about 30 minutes.

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

    """
    return web.Response(status=200)


async def job_get_task_counts(request: web.Request, job_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Gets the task counts for the specified job.

    Task counts provide a count of the tasks by active, running or completed task state, and a count of tasks which succeeded or failed. Tasks in the preparing state are counted as running.

    :param job_id: The ID of the job.
    :type job_id: str
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

    """
    return web.Response(status=200)


async def job_list(request: web.Request, api_version, filter=None, select=None, expand=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists all of the jobs in the specified account.

    

    :param api_version: Client API Version.
    :type api_version: str
    :param filter: An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-jobs.
    :type filter: str
    :param select: An OData $select clause.
    :type select: str
    :param expand: An OData $expand clause.
    :type expand: str
    :param maxresults: The maximum number of items to return in the response. A maximum of 1000 jobs can be returned.
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


async def job_list_from_job_schedule(request: web.Request, job_schedule_id, api_version, filter=None, select=None, expand=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists the jobs that have been created under the specified job schedule.

    

    :param job_schedule_id: The ID of the job schedule from which you want to get a list of jobs.
    :type job_schedule_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-jobs-in-a-job-schedule.
    :type filter: str
    :param select: An OData $select clause.
    :type select: str
    :param expand: An OData $expand clause.
    :type expand: str
    :param maxresults: The maximum number of items to return in the response. A maximum of 1000 jobs can be returned.
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


async def job_list_preparation_and_release_task_status(request: web.Request, job_id, api_version, filter=None, select=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists the execution status of the Job Preparation and Job Release task for the specified job across the compute nodes where the job has run.

    This API returns the Job Preparation and Job Release task status on all compute nodes that have run the Job Preparation or Job Release task. This includes nodes which have since been removed from the pool. If this API is invoked on a job which has no Job Preparation or Job Release task, the Batch service returns HTTP status code 409 (Conflict) with an error code of JobPreparationTaskNotSpecified.

    :param job_id: The ID of the job.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-job-preparation-and-release-status.
    :type filter: str
    :param select: An OData $select clause.
    :type select: str
    :param maxresults: The maximum number of items to return in the response. A maximum of 1000 tasks can be returned.
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


async def job_patch(request: web.Request, job_id, api_version, job_patch_parameter, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Updates the properties of the specified job.

    This replaces only the job properties specified in the request. For example, if the job has constraints, and a request does not specify the constraints element, then the job keeps the existing constraints.

    :param job_id: The ID of the job whose properties you want to update.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param job_patch_parameter: The parameters for the request.
    :type job_patch_parameter: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str
    :param if_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client.
    :type if_match: str
    :param if_none_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client.
    :type if_none_match: str
    :param if_modified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    :type if_modified_since: str
    :param if_unmodified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    :type if_unmodified_since: str

    """
    job_patch_parameter = JobPatchParameter.from_dict(job_patch_parameter)
    return web.Response(status=200)


async def job_terminate(request: web.Request, job_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, job_terminate_parameter=None) -> web.Response:
    """Terminates the specified job, marking it as completed.

    When a Terminate Job request is received, the Batch service sets the job to the terminating state. The Batch service then terminates any running tasks associated with the job and runs any required job release tasks. Then the job moves into the completed state. If there are any tasks in the job in the active state, they will remain in the active state. Once a job is terminated, new tasks cannot be added and any remaining active tasks will not be scheduled.

    :param job_id: The ID of the job to terminate.
    :type job_id: str
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
    :param if_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client.
    :type if_match: str
    :param if_none_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client.
    :type if_none_match: str
    :param if_modified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    :type if_modified_since: str
    :param if_unmodified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    :type if_unmodified_since: str
    :param job_terminate_parameter: The parameters for the request.
    :type job_terminate_parameter: dict | bytes

    """
    job_terminate_parameter = JobTerminateParameter.from_dict(job_terminate_parameter)
    return web.Response(status=200)


async def job_update(request: web.Request, job_id, api_version, job_update_parameter, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Updates the properties of the specified job.

    This fully replaces all the updatable properties of the job. For example, if the job has constraints associated with it and if constraints is not specified with this request, then the Batch service will remove the existing constraints.

    :param job_id: The ID of the job whose properties you want to update.
    :type job_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param job_update_parameter: The parameters for the request.
    :type job_update_parameter: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str
    :param if_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client.
    :type if_match: str
    :param if_none_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client.
    :type if_none_match: str
    :param if_modified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    :type if_modified_since: str
    :param if_unmodified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    :type if_unmodified_since: str

    """
    job_update_parameter = JobUpdateParameter.from_dict(job_update_parameter)
    return web.Response(status=200)
