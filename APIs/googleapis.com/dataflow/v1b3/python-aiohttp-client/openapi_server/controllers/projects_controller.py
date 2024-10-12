from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_job_from_template_request import CreateJobFromTemplateRequest
from openapi_server.models.get_debug_config_request import GetDebugConfigRequest
from openapi_server.models.get_debug_config_response import GetDebugConfigResponse
from openapi_server.models.get_template_response import GetTemplateResponse
from openapi_server.models.job import Job
from openapi_server.models.job_execution_details import JobExecutionDetails
from openapi_server.models.job_metrics import JobMetrics
from openapi_server.models.launch_flex_template_request import LaunchFlexTemplateRequest
from openapi_server.models.launch_flex_template_response import LaunchFlexTemplateResponse
from openapi_server.models.launch_template_parameters import LaunchTemplateParameters
from openapi_server.models.launch_template_response import LaunchTemplateResponse
from openapi_server.models.lease_work_item_request import LeaseWorkItemRequest
from openapi_server.models.lease_work_item_response import LeaseWorkItemResponse
from openapi_server.models.list_job_messages_response import ListJobMessagesResponse
from openapi_server.models.list_jobs_response import ListJobsResponse
from openapi_server.models.list_snapshots_response import ListSnapshotsResponse
from openapi_server.models.report_work_item_status_request import ReportWorkItemStatusRequest
from openapi_server.models.report_work_item_status_response import ReportWorkItemStatusResponse
from openapi_server.models.send_debug_capture_request import SendDebugCaptureRequest
from openapi_server.models.send_worker_messages_request import SendWorkerMessagesRequest
from openapi_server.models.send_worker_messages_response import SendWorkerMessagesResponse
from openapi_server.models.snapshot import Snapshot
from openapi_server.models.snapshot_job_request import SnapshotJobRequest
from openapi_server.models.stage_execution_details import StageExecutionDetails
from openapi_server import util


async def dataflow_projects_delete_snapshots(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, location=None, snapshot_id=None) -> web.Response:
    """dataflow_projects_delete_snapshots

    Deletes a snapshot.

    :param project_id: The ID of the Cloud Platform project that the snapshot belongs to.
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
    :param location: The location that contains this snapshot.
    :type location: str
    :param snapshot_id: The ID of the snapshot.
    :type snapshot_id: str

    """
    return web.Response(status=200)


async def dataflow_projects_jobs_aggregated(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, location=None, name=None, page_size=None, page_token=None, view=None) -> web.Response:
    """dataflow_projects_jobs_aggregated

    List the jobs of a project across all regions. **Note:** This method doesn&#39;t support filtering the list of jobs by name.

    :param project_id: The project which owns the jobs.
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
    :param filter: The kind of filter to use.
    :type filter: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.
    :type location: str
    :param name: Optional. The job name.
    :type name: str
    :param page_size: If there are many jobs, limit response to at most this many. The actual number of jobs returned will be the lesser of max_responses and an unspecified server-defined limit.
    :type page_size: int
    :param page_token: Set this to the &#39;next_page_token&#39; field of a previous response to request additional results in a long list.
    :type page_token: str
    :param view: Deprecated. ListJobs always returns summaries now. Use GetJob for other JobViews.
    :type view: str

    """
    return web.Response(status=200)


async def dataflow_projects_jobs_create(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, location=None, replace_job_id=None, view=None, body=None) -> web.Response:
    """dataflow_projects_jobs_create

    Creates a Cloud Dataflow job. To create a job, we recommend using &#x60;projects.locations.jobs.create&#x60; with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using &#x60;projects.jobs.create&#x60; is not recommended, as your job will always start in &#x60;us-central1&#x60;. Do not enter confidential information when you supply string values using the API.

    :param project_id: The ID of the Cloud Platform project that the job belongs to.
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
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.
    :type location: str
    :param replace_job_id: Deprecated. This field is now in the Job message.
    :type replace_job_id: str
    :param view: The level of information requested in response.
    :type view: str
    :param body: 
    :type body: dict | bytes

    """
    body = Job.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_jobs_debug_get_config(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_jobs_debug_get_config

    Get encoded debug configuration for component. Not cacheable.

    :param project_id: The project id.
    :type project_id: str
    :param job_id: The job id.
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
    :param body: 
    :type body: dict | bytes

    """
    body = GetDebugConfigRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_jobs_debug_send_capture(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_jobs_debug_send_capture

    Send encoded debug capture data for component.

    :param project_id: The project id.
    :type project_id: str
    :param job_id: The job id.
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
    :param body: 
    :type body: dict | bytes

    """
    body = SendDebugCaptureRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_jobs_get(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, location=None, view=None) -> web.Response:
    """dataflow_projects_jobs_get

    Gets the state of the specified Cloud Dataflow job. To get the state of a job, we recommend using &#x60;projects.locations.jobs.get&#x60; with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using &#x60;projects.jobs.get&#x60; is not recommended, as you can only get the state of jobs that are running in &#x60;us-central1&#x60;.

    :param project_id: The ID of the Cloud Platform project that the job belongs to.
    :type project_id: str
    :param job_id: The job ID.
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
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.
    :type location: str
    :param view: The level of information requested in response.
    :type view: str

    """
    return web.Response(status=200)


async def dataflow_projects_jobs_get_metrics(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, location=None, start_time=None) -> web.Response:
    """dataflow_projects_jobs_get_metrics

    Request the job status. To request the status of a job, we recommend using &#x60;projects.locations.jobs.getMetrics&#x60; with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using &#x60;projects.jobs.getMetrics&#x60; is not recommended, as you can only request the status of jobs that are running in &#x60;us-central1&#x60;.

    :param project_id: A project id.
    :type project_id: str
    :param job_id: The job to get metrics for.
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
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the job specified by job_id.
    :type location: str
    :param start_time: Return only metric data that has changed since this time. Default is to return all information about all metrics for the job.
    :type start_time: str

    """
    return web.Response(status=200)


async def dataflow_projects_jobs_list(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, location=None, name=None, page_size=None, page_token=None, view=None) -> web.Response:
    """dataflow_projects_jobs_list

    List the jobs of a project. To list the jobs of a project in a region, we recommend using &#x60;projects.locations.jobs.list&#x60; with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). To list the all jobs across all regions, use &#x60;projects.jobs.aggregated&#x60;. Using &#x60;projects.jobs.list&#x60; is not recommended, because you can only get the list of jobs that are running in &#x60;us-central1&#x60;. &#x60;projects.locations.jobs.list&#x60; and &#x60;projects.jobs.list&#x60; support filtering the list of jobs by name. Filtering by name isn&#39;t supported by &#x60;projects.jobs.aggregated&#x60;.

    :param project_id: The project which owns the jobs.
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
    :param filter: The kind of filter to use.
    :type filter: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.
    :type location: str
    :param name: Optional. The job name.
    :type name: str
    :param page_size: If there are many jobs, limit response to at most this many. The actual number of jobs returned will be the lesser of max_responses and an unspecified server-defined limit.
    :type page_size: int
    :param page_token: Set this to the &#39;next_page_token&#39; field of a previous response to request additional results in a long list.
    :type page_token: str
    :param view: Deprecated. ListJobs always returns summaries now. Use GetJob for other JobViews.
    :type view: str

    """
    return web.Response(status=200)


async def dataflow_projects_jobs_messages_list(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, end_time=None, location=None, minimum_importance=None, page_size=None, page_token=None, start_time=None) -> web.Response:
    """dataflow_projects_jobs_messages_list

    Request the job status. To request the status of a job, we recommend using &#x60;projects.locations.jobs.messages.list&#x60; with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using &#x60;projects.jobs.messages.list&#x60; is not recommended, as you can only request the status of jobs that are running in &#x60;us-central1&#x60;.

    :param project_id: A project id.
    :type project_id: str
    :param job_id: The job to get messages about.
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
    :param end_time: Return only messages with timestamps &lt; end_time. The default is now (i.e. return up to the latest messages available).
    :type end_time: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the job specified by job_id.
    :type location: str
    :param minimum_importance: Filter to only get messages with importance &gt;&#x3D; level
    :type minimum_importance: str
    :param page_size: If specified, determines the maximum number of messages to return. If unspecified, the service may choose an appropriate default, or may return an arbitrarily large number of results.
    :type page_size: int
    :param page_token: If supplied, this should be the value of next_page_token returned by an earlier call. This will cause the next page of results to be returned.
    :type page_token: str
    :param start_time: If specified, return only messages with timestamps &gt;&#x3D; start_time. The default is the job creation time (i.e. beginning of messages).
    :type start_time: str

    """
    return web.Response(status=200)


async def dataflow_projects_jobs_snapshot(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_jobs_snapshot

    Snapshot the state of a streaming job.

    :param project_id: The project which owns the job to be snapshotted.
    :type project_id: str
    :param job_id: The job to be snapshotted.
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
    :param body: 
    :type body: dict | bytes

    """
    body = SnapshotJobRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_jobs_update(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, location=None, update_mask=None, body=None) -> web.Response:
    """dataflow_projects_jobs_update

    Updates the state of an existing Cloud Dataflow job. To update the state of an existing job, we recommend using &#x60;projects.locations.jobs.update&#x60; with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using &#x60;projects.jobs.update&#x60; is not recommended, as you can only update the state of jobs that are running in &#x60;us-central1&#x60;.

    :param project_id: The ID of the Cloud Platform project that the job belongs to.
    :type project_id: str
    :param job_id: The job ID.
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
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.
    :type location: str
    :param update_mask: The list of fields to update relative to Job. If empty, only RequestedJobState will be considered for update. If the FieldMask is not empty and RequestedJobState is none/empty, The fields specified in the update mask will be the only ones considered for update. If both RequestedJobState and update_mask are specified, an error will be returned as we cannot update both state and mask.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Job.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_jobs_work_items_lease(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_jobs_work_items_lease

    Leases a dataflow WorkItem to run.

    :param project_id: Identifies the project this worker belongs to.
    :type project_id: str
    :param job_id: Identifies the workflow job this worker belongs to.
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
    :param body: 
    :type body: dict | bytes

    """
    body = LeaseWorkItemRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_jobs_work_items_report_status(request: web.Request, project_id, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_jobs_work_items_report_status

    Reports the status of dataflow WorkItems leased by a worker.

    :param project_id: The project which owns the WorkItem&#39;s job.
    :type project_id: str
    :param job_id: The job which the WorkItem is part of.
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
    :param body: 
    :type body: dict | bytes

    """
    body = ReportWorkItemStatusRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_locations_flex_templates_launch(request: web.Request, project_id, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_locations_flex_templates_launch

    Launch a job with a FlexTemplate.

    :param project_id: Required. The ID of the Cloud Platform project that the job belongs to.
    :type project_id: str
    :param location: Required. The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) to which to direct the request. E.g., us-central1, us-west1.
    :type location: str
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
    body = LaunchFlexTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_create(request: web.Request, project_id, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, replace_job_id=None, view=None, body=None) -> web.Response:
    """dataflow_projects_locations_jobs_create

    Creates a Cloud Dataflow job. To create a job, we recommend using &#x60;projects.locations.jobs.create&#x60; with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using &#x60;projects.jobs.create&#x60; is not recommended, as your job will always start in &#x60;us-central1&#x60;. Do not enter confidential information when you supply string values using the API.

    :param project_id: The ID of the Cloud Platform project that the job belongs to.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.
    :type location: str
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
    :param replace_job_id: Deprecated. This field is now in the Job message.
    :type replace_job_id: str
    :param view: The level of information requested in response.
    :type view: str
    :param body: 
    :type body: dict | bytes

    """
    body = Job.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_debug_get_config(request: web.Request, project_id, location, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_locations_jobs_debug_get_config

    Get encoded debug configuration for component. Not cacheable.

    :param project_id: The project id.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the job specified by job_id.
    :type location: str
    :param job_id: The job id.
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
    :param body: 
    :type body: dict | bytes

    """
    body = GetDebugConfigRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_debug_send_capture(request: web.Request, project_id, location, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_locations_jobs_debug_send_capture

    Send encoded debug capture data for component.

    :param project_id: The project id.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the job specified by job_id.
    :type location: str
    :param job_id: The job id.
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
    :param body: 
    :type body: dict | bytes

    """
    body = SendDebugCaptureRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_get(request: web.Request, project_id, location, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, view=None) -> web.Response:
    """dataflow_projects_locations_jobs_get

    Gets the state of the specified Cloud Dataflow job. To get the state of a job, we recommend using &#x60;projects.locations.jobs.get&#x60; with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using &#x60;projects.jobs.get&#x60; is not recommended, as you can only get the state of jobs that are running in &#x60;us-central1&#x60;.

    :param project_id: The ID of the Cloud Platform project that the job belongs to.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.
    :type location: str
    :param job_id: The job ID.
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
    :param view: The level of information requested in response.
    :type view: str

    """
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_get_execution_details(request: web.Request, project_id, location, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """dataflow_projects_locations_jobs_get_execution_details

    Request detailed information about the execution status of the job. EXPERIMENTAL. This API is subject to change or removal without notice.

    :param project_id: A project id.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the job specified by job_id.
    :type location: str
    :param job_id: The job to get execution details for.
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
    :param page_size: If specified, determines the maximum number of stages to return. If unspecified, the service may choose an appropriate default, or may return an arbitrarily large number of results.
    :type page_size: int
    :param page_token: If supplied, this should be the value of next_page_token returned by an earlier call. This will cause the next page of results to be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_get_metrics(request: web.Request, project_id, location, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, start_time=None) -> web.Response:
    """dataflow_projects_locations_jobs_get_metrics

    Request the job status. To request the status of a job, we recommend using &#x60;projects.locations.jobs.getMetrics&#x60; with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using &#x60;projects.jobs.getMetrics&#x60; is not recommended, as you can only request the status of jobs that are running in &#x60;us-central1&#x60;.

    :param project_id: A project id.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the job specified by job_id.
    :type location: str
    :param job_id: The job to get metrics for.
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
    :param start_time: Return only metric data that has changed since this time. Default is to return all information about all metrics for the job.
    :type start_time: str

    """
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_list(request: web.Request, project_id, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, name=None, page_size=None, page_token=None, view=None) -> web.Response:
    """dataflow_projects_locations_jobs_list

    List the jobs of a project. To list the jobs of a project in a region, we recommend using &#x60;projects.locations.jobs.list&#x60; with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). To list the all jobs across all regions, use &#x60;projects.jobs.aggregated&#x60;. Using &#x60;projects.jobs.list&#x60; is not recommended, because you can only get the list of jobs that are running in &#x60;us-central1&#x60;. &#x60;projects.locations.jobs.list&#x60; and &#x60;projects.jobs.list&#x60; support filtering the list of jobs by name. Filtering by name isn&#39;t supported by &#x60;projects.jobs.aggregated&#x60;.

    :param project_id: The project which owns the jobs.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.
    :type location: str
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
    :param filter: The kind of filter to use.
    :type filter: str
    :param name: Optional. The job name.
    :type name: str
    :param page_size: If there are many jobs, limit response to at most this many. The actual number of jobs returned will be the lesser of max_responses and an unspecified server-defined limit.
    :type page_size: int
    :param page_token: Set this to the &#39;next_page_token&#39; field of a previous response to request additional results in a long list.
    :type page_token: str
    :param view: Deprecated. ListJobs always returns summaries now. Use GetJob for other JobViews.
    :type view: str

    """
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_messages_list(request: web.Request, project_id, location, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, end_time=None, minimum_importance=None, page_size=None, page_token=None, start_time=None) -> web.Response:
    """dataflow_projects_locations_jobs_messages_list

    Request the job status. To request the status of a job, we recommend using &#x60;projects.locations.jobs.messages.list&#x60; with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using &#x60;projects.jobs.messages.list&#x60; is not recommended, as you can only request the status of jobs that are running in &#x60;us-central1&#x60;.

    :param project_id: A project id.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the job specified by job_id.
    :type location: str
    :param job_id: The job to get messages about.
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
    :param end_time: Return only messages with timestamps &lt; end_time. The default is now (i.e. return up to the latest messages available).
    :type end_time: str
    :param minimum_importance: Filter to only get messages with importance &gt;&#x3D; level
    :type minimum_importance: str
    :param page_size: If specified, determines the maximum number of messages to return. If unspecified, the service may choose an appropriate default, or may return an arbitrarily large number of results.
    :type page_size: int
    :param page_token: If supplied, this should be the value of next_page_token returned by an earlier call. This will cause the next page of results to be returned.
    :type page_token: str
    :param start_time: If specified, return only messages with timestamps &gt;&#x3D; start_time. The default is the job creation time (i.e. beginning of messages).
    :type start_time: str

    """
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_snapshot(request: web.Request, project_id, location, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_locations_jobs_snapshot

    Snapshot the state of a streaming job.

    :param project_id: The project which owns the job to be snapshotted.
    :type project_id: str
    :param location: The location that contains this job.
    :type location: str
    :param job_id: The job to be snapshotted.
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
    :param body: 
    :type body: dict | bytes

    """
    body = SnapshotJobRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_snapshots_list(request: web.Request, project_id, location, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """dataflow_projects_locations_jobs_snapshots_list

    Lists snapshots.

    :param project_id: The project ID to list snapshots for.
    :type project_id: str
    :param location: The location to list snapshots in.
    :type location: str
    :param job_id: If specified, list snapshots created from this job.
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

    """
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_stages_get_execution_details(request: web.Request, project_id, location, job_id, stage_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, end_time=None, page_size=None, page_token=None, start_time=None) -> web.Response:
    """dataflow_projects_locations_jobs_stages_get_execution_details

    Request detailed information about the execution status of a stage of the job. EXPERIMENTAL. This API is subject to change or removal without notice.

    :param project_id: A project id.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the job specified by job_id.
    :type location: str
    :param job_id: The job to get execution details for.
    :type job_id: str
    :param stage_id: The stage for which to fetch information.
    :type stage_id: str
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
    :param end_time: Upper time bound of work items to include, by start time.
    :type end_time: str
    :param page_size: If specified, determines the maximum number of work items to return. If unspecified, the service may choose an appropriate default, or may return an arbitrarily large number of results.
    :type page_size: int
    :param page_token: If supplied, this should be the value of next_page_token returned by an earlier call. This will cause the next page of results to be returned.
    :type page_token: str
    :param start_time: Lower time bound of work items to include, by start time.
    :type start_time: str

    """
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_update(request: web.Request, project_id, location, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """dataflow_projects_locations_jobs_update

    Updates the state of an existing Cloud Dataflow job. To update the state of an existing job, we recommend using &#x60;projects.locations.jobs.update&#x60; with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using &#x60;projects.jobs.update&#x60; is not recommended, as you can only update the state of jobs that are running in &#x60;us-central1&#x60;.

    :param project_id: The ID of the Cloud Platform project that the job belongs to.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.
    :type location: str
    :param job_id: The job ID.
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
    :param update_mask: The list of fields to update relative to Job. If empty, only RequestedJobState will be considered for update. If the FieldMask is not empty and RequestedJobState is none/empty, The fields specified in the update mask will be the only ones considered for update. If both RequestedJobState and update_mask are specified, an error will be returned as we cannot update both state and mask.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Job.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_work_items_lease(request: web.Request, project_id, location, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_locations_jobs_work_items_lease

    Leases a dataflow WorkItem to run.

    :param project_id: Identifies the project this worker belongs to.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the WorkItem&#39;s job.
    :type location: str
    :param job_id: Identifies the workflow job this worker belongs to.
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
    :param body: 
    :type body: dict | bytes

    """
    body = LeaseWorkItemRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_locations_jobs_work_items_report_status(request: web.Request, project_id, location, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_locations_jobs_work_items_report_status

    Reports the status of dataflow WorkItems leased by a worker.

    :param project_id: The project which owns the WorkItem&#39;s job.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the WorkItem&#39;s job.
    :type location: str
    :param job_id: The job which the WorkItem is part of.
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
    :param body: 
    :type body: dict | bytes

    """
    body = ReportWorkItemStatusRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_locations_snapshots_delete(request: web.Request, project_id, location, snapshot_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """dataflow_projects_locations_snapshots_delete

    Deletes a snapshot.

    :param project_id: The ID of the Cloud Platform project that the snapshot belongs to.
    :type project_id: str
    :param location: The location that contains this snapshot.
    :type location: str
    :param snapshot_id: The ID of the snapshot.
    :type snapshot_id: str
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

    """
    return web.Response(status=200)


async def dataflow_projects_locations_snapshots_get(request: web.Request, project_id, location, snapshot_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """dataflow_projects_locations_snapshots_get

    Gets information about a snapshot.

    :param project_id: The ID of the Cloud Platform project that the snapshot belongs to.
    :type project_id: str
    :param location: The location that contains this snapshot.
    :type location: str
    :param snapshot_id: The ID of the snapshot.
    :type snapshot_id: str
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

    """
    return web.Response(status=200)


async def dataflow_projects_locations_snapshots_list(request: web.Request, project_id, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, job_id=None) -> web.Response:
    """dataflow_projects_locations_snapshots_list

    Lists snapshots.

    :param project_id: The project ID to list snapshots for.
    :type project_id: str
    :param location: The location to list snapshots in.
    :type location: str
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
    :param job_id: If specified, list snapshots created from this job.
    :type job_id: str

    """
    return web.Response(status=200)


async def dataflow_projects_locations_templates_create(request: web.Request, project_id, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_locations_templates_create

    Creates a Cloud Dataflow job from a template. Do not enter confidential information when you supply string values using the API.

    :param project_id: Required. The ID of the Cloud Platform project that the job belongs to.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) to which to direct the request.
    :type location: str
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
    body = CreateJobFromTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_locations_templates_get(request: web.Request, project_id, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, gcs_path=None, view=None) -> web.Response:
    """dataflow_projects_locations_templates_get

    Get the template associated with a template.

    :param project_id: Required. The ID of the Cloud Platform project that the job belongs to.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) to which to direct the request.
    :type location: str
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
    :param gcs_path: Required. A Cloud Storage path to the template from which to create the job. Must be valid Cloud Storage URL, beginning with &#39;gs://&#39;.
    :type gcs_path: str
    :param view: The view to retrieve. Defaults to METADATA_ONLY.
    :type view: str

    """
    return web.Response(status=200)


async def dataflow_projects_locations_templates_launch(request: web.Request, project_id, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, dynamic_template_gcs_path=None, dynamic_template_staging_location=None, gcs_path=None, validate_only=None, body=None) -> web.Response:
    """dataflow_projects_locations_templates_launch

    Launch a template.

    :param project_id: Required. The ID of the Cloud Platform project that the job belongs to.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) to which to direct the request.
    :type location: str
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
    :param dynamic_template_gcs_path: Path to dynamic template spec file on Cloud Storage. The file must be a Json serialized DynamicTemplateFieSpec object.
    :type dynamic_template_gcs_path: str
    :param dynamic_template_staging_location: Cloud Storage path for staging dependencies. Must be a valid Cloud Storage URL, beginning with &#x60;gs://&#x60;.
    :type dynamic_template_staging_location: str
    :param gcs_path: A Cloud Storage path to the template from which to create the job. Must be valid Cloud Storage URL, beginning with &#39;gs://&#39;.
    :type gcs_path: str
    :param validate_only: If true, the request is validated but not actually executed. Defaults to false.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = LaunchTemplateParameters.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_locations_worker_messages(request: web.Request, project_id, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_locations_worker_messages

    Send a worker_message to the service.

    :param project_id: The project to send the WorkerMessages to.
    :type project_id: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the job.
    :type location: str
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
    body = SendWorkerMessagesRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_snapshots_get(request: web.Request, project_id, snapshot_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, location=None) -> web.Response:
    """dataflow_projects_snapshots_get

    Gets information about a snapshot.

    :param project_id: The ID of the Cloud Platform project that the snapshot belongs to.
    :type project_id: str
    :param snapshot_id: The ID of the snapshot.
    :type snapshot_id: str
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
    :param location: The location that contains this snapshot.
    :type location: str

    """
    return web.Response(status=200)


async def dataflow_projects_snapshots_list(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, job_id=None, location=None) -> web.Response:
    """dataflow_projects_snapshots_list

    Lists snapshots.

    :param project_id: The project ID to list snapshots for.
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
    :param job_id: If specified, list snapshots created from this job.
    :type job_id: str
    :param location: The location to list snapshots in.
    :type location: str

    """
    return web.Response(status=200)


async def dataflow_projects_templates_create(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_templates_create

    Creates a Cloud Dataflow job from a template. Do not enter confidential information when you supply string values using the API.

    :param project_id: Required. The ID of the Cloud Platform project that the job belongs to.
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
    body = CreateJobFromTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_templates_get(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, gcs_path=None, location=None, view=None) -> web.Response:
    """dataflow_projects_templates_get

    Get the template associated with a template.

    :param project_id: Required. The ID of the Cloud Platform project that the job belongs to.
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
    :param gcs_path: Required. A Cloud Storage path to the template from which to create the job. Must be valid Cloud Storage URL, beginning with &#39;gs://&#39;.
    :type gcs_path: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) to which to direct the request.
    :type location: str
    :param view: The view to retrieve. Defaults to METADATA_ONLY.
    :type view: str

    """
    return web.Response(status=200)


async def dataflow_projects_templates_launch(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, dynamic_template_gcs_path=None, dynamic_template_staging_location=None, gcs_path=None, location=None, validate_only=None, body=None) -> web.Response:
    """dataflow_projects_templates_launch

    Launch a template.

    :param project_id: Required. The ID of the Cloud Platform project that the job belongs to.
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
    :param dynamic_template_gcs_path: Path to dynamic template spec file on Cloud Storage. The file must be a Json serialized DynamicTemplateFieSpec object.
    :type dynamic_template_gcs_path: str
    :param dynamic_template_staging_location: Cloud Storage path for staging dependencies. Must be a valid Cloud Storage URL, beginning with &#x60;gs://&#x60;.
    :type dynamic_template_staging_location: str
    :param gcs_path: A Cloud Storage path to the template from which to create the job. Must be valid Cloud Storage URL, beginning with &#39;gs://&#39;.
    :type gcs_path: str
    :param location: The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) to which to direct the request.
    :type location: str
    :param validate_only: If true, the request is validated but not actually executed. Defaults to false.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = LaunchTemplateParameters.from_dict(body)
    return web.Response(status=200)


async def dataflow_projects_worker_messages(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dataflow_projects_worker_messages

    Send a worker_message to the service.

    :param project_id: The project to send the WorkerMessages to.
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
    body = SendWorkerMessagesRequest.from_dict(body)
    return web.Response(status=200)
