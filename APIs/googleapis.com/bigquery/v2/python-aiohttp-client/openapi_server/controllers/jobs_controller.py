from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_query_results_response import GetQueryResultsResponse
from openapi_server.models.job import Job
from openapi_server.models.job_cancel_response import JobCancelResponse
from openapi_server.models.job_list import JobList
from openapi_server.models.query_request import QueryRequest
from openapi_server.models.query_response import QueryResponse
from openapi_server import util


async def bigquery_jobs_cancel(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, location=None) -> web.Response:
    """bigquery_jobs_cancel

    Requests that a job be cancelled. This call will return immediately, and the client will need to poll for the job status to see if the cancel completed successfully. Cancelled jobs may still incur costs.

    :param project_id: Required. Project ID of the job to cancel
    :type project_id: str
    :param job_id: Required. Job ID of the job to cancel
    :type job_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param location: The geographic location of the job. You must specify the location to run the job for the following scenarios: - If the location to run a job is not in the &#x60;us&#x60; or the &#x60;eu&#x60; multi-regional location - If the job&#39;s location is in a single region (for example, &#x60;us-central1&#x60;) For more information, see https://cloud.google.com/bigquery/docs/locations#specifying_your_location.
    :type location: str

    """
    return web.Response(status=200)


async def bigquery_jobs_delete(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, location=None) -> web.Response:
    """bigquery_jobs_delete

    Requests the deletion of the metadata of a job. This call returns when the job&#39;s metadata is deleted.

    :param project_id: Required. Project ID of the job for which metadata is to be deleted.
    :type project_id: str
    :param job_id: Required. Job ID of the job for which metadata is to be deleted. If this is a parent job which has child jobs, the metadata from all child jobs will be deleted as well. Direct deletion of the metadata of child jobs is not allowed.
    :type job_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param location: The geographic location of the job. Required. See details at: https://cloud.google.com/bigquery/docs/locations#specifying_your_location.
    :type location: str

    """
    return web.Response(status=200)


async def bigquery_jobs_get(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, location=None) -> web.Response:
    """bigquery_jobs_get

    Returns information about a specific job. Job information is available for a six month period after creation. Requires that you&#39;re the person who ran the job, or have the Is Owner project role.

    :param project_id: Required. Project ID of the requested job.
    :type project_id: str
    :param job_id: Required. Job ID of the requested job.
    :type job_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param location: The geographic location of the job. You must specify the location to run the job for the following scenarios: - If the location to run a job is not in the &#x60;us&#x60; or the &#x60;eu&#x60; multi-regional location - If the job&#39;s location is in a single region (for example, &#x60;us-central1&#x60;) For more information, see https://cloud.google.com/bigquery/docs/locations#specifying_your_location.
    :type location: str

    """
    return web.Response(status=200)


async def bigquery_jobs_get_query_results(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, format_options_use_int64_timestamp=None, location=None, max_results=None, page_token=None, start_index=None, timeout_ms=None) -> web.Response:
    """bigquery_jobs_get_query_results

    RPC to get the results of a query job.

    :param project_id: Required. Project ID of the query job.
    :type project_id: str
    :param job_id: Required. Job ID of the query job.
    :type job_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param format_options_use_int64_timestamp: Optional. Output timestamp as usec int64. Default is false.
    :type format_options_use_int64_timestamp: bool
    :param location: The geographic location of the job. You must specify the location to run the job for the following scenarios: - If the location to run a job is not in the &#x60;us&#x60; or the &#x60;eu&#x60; multi-regional location - If the job&#39;s location is in a single region (for example, &#x60;us-central1&#x60;) For more information, see https://cloud.google.com/bigquery/docs/locations#specifying_your_location.
    :type location: str
    :param max_results: Maximum number of results to read.
    :type max_results: int
    :param page_token: Page token, returned by a previous call, to request the next page of results.
    :type page_token: str
    :param start_index: Zero-based index of the starting row.
    :type start_index: str
    :param timeout_ms: Optional: Specifies the maximum amount of time, in milliseconds, that the client is willing to wait for the query to complete. By default, this limit is 10 seconds (10,000 milliseconds). If the query is complete, the jobComplete field in the response is true. If the query has not yet completed, jobComplete is false. You can request a longer timeout period in the timeoutMs field. However, the call is not guaranteed to wait for the specified timeout; it typically returns after around 200 seconds (200,000 milliseconds), even if the query is not complete. If jobComplete is false, you can continue to wait for the query to complete by calling the getQueryResults method until the jobComplete field in the getQueryResults response is true.
    :type timeout_ms: int

    """
    return web.Response(status=200)


async def bigquery_jobs_insert(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """bigquery_jobs_insert

    Starts a new asynchronous job. This API has two different kinds of endpoint URIs, as this method supports a variety of use cases. * The *Metadata* URI is used for most interactions, as it accepts the job configuration directly. * The *Upload* URI is ONLY for the case when you&#39;re sending both a load job configuration and a data stream together. In this case, the Upload URI accepts the job configuration and the data as two distinct multipart MIME parts.

    :param project_id: Project ID of project that will be billed for the job.
    :type project_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = Job.from_dict(body)
    return web.Response(status=200)


async def bigquery_jobs_list(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, all_users=None, max_creation_time=None, max_results=None, min_creation_time=None, page_token=None, parent_job_id=None, projection=None, state_filter=None) -> web.Response:
    """bigquery_jobs_list

    Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property.

    :param project_id: Project ID of the jobs to list.
    :type project_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param all_users: Whether to display jobs owned by all users in the project. Default False.
    :type all_users: bool
    :param max_creation_time: Max value for job creation time, in milliseconds since the POSIX epoch. If set, only jobs created before or at this timestamp are returned.
    :type max_creation_time: str
    :param max_results: The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection.
    :type max_results: int
    :param min_creation_time: Min value for job creation time, in milliseconds since the POSIX epoch. If set, only jobs created after or at this timestamp are returned.
    :type min_creation_time: str
    :param page_token: Page token, returned by a previous call, to request the next page of results.
    :type page_token: str
    :param parent_job_id: If set, show only child jobs of the specified parent. Otherwise, show all top-level jobs.
    :type parent_job_id: str
    :param projection: Restrict information returned to a set of selected fields
    :type projection: str
    :param state_filter: Filter for job state
    :type state_filter: List[str]

    """
    return web.Response(status=200)


async def bigquery_jobs_query(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """bigquery_jobs_query

    Runs a BigQuery SQL query synchronously and returns query results if the query completes within a specified timeout.

    :param project_id: Required. Project ID of the query request.
    :type project_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = QueryRequest.from_dict(body)
    return web.Response(status=200)
