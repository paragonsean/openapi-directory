from typing import List, Dict
from aiohttp import web

from openapi_server.models.job import Job
from openapi_server.models.list_jobs_response import ListJobsResponse
from openapi_server.models.list_reports_response import ListReportsResponse
from openapi_server.models.report import Report
from openapi_server import util


async def youtubereporting_jobs_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, on_behalf_of_content_owner=None, body=None) -> web.Response:
    """youtubereporting_jobs_create

    Creates a job and returns it.

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
    :param on_behalf_of_content_owner: The content owner&#39;s external ID on which behalf the user is acting on. If not set, the user is acting for himself (his own channel).
    :type on_behalf_of_content_owner: str
    :param body: 
    :type body: dict | bytes

    """
    body = Job.from_dict(body)
    return web.Response(status=200)


async def youtubereporting_jobs_delete(request: web.Request, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, on_behalf_of_content_owner=None) -> web.Response:
    """youtubereporting_jobs_delete

    Deletes a job.

    :param job_id: The ID of the job to delete.
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
    :param on_behalf_of_content_owner: The content owner&#39;s external ID on which behalf the user is acting on. If not set, the user is acting for himself (his own channel).
    :type on_behalf_of_content_owner: str

    """
    return web.Response(status=200)


async def youtubereporting_jobs_get(request: web.Request, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, on_behalf_of_content_owner=None) -> web.Response:
    """youtubereporting_jobs_get

    Gets a job.

    :param job_id: The ID of the job to retrieve.
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
    :param on_behalf_of_content_owner: The content owner&#39;s external ID on which behalf the user is acting on. If not set, the user is acting for himself (his own channel).
    :type on_behalf_of_content_owner: str

    """
    return web.Response(status=200)


async def youtubereporting_jobs_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_system_managed=None, on_behalf_of_content_owner=None, page_size=None, page_token=None) -> web.Response:
    """youtubereporting_jobs_list

    Lists jobs.

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
    :param include_system_managed: If set to true, also system-managed jobs will be returned; otherwise only user-created jobs will be returned. System-managed jobs can neither be modified nor deleted.
    :type include_system_managed: bool
    :param on_behalf_of_content_owner: The content owner&#39;s external ID on which behalf the user is acting on. If not set, the user is acting for himself (his own channel).
    :type on_behalf_of_content_owner: str
    :param page_size: Requested page size. Server may return fewer jobs than requested. If unspecified, server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListReportTypesResponse.next_page_token returned in response to the previous call to the &#x60;ListJobs&#x60; method.
    :type page_token: str

    """
    return web.Response(status=200)


async def youtubereporting_jobs_reports_get(request: web.Request, job_id, report_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, on_behalf_of_content_owner=None) -> web.Response:
    """youtubereporting_jobs_reports_get

    Gets the metadata of a specific report.

    :param job_id: The ID of the job.
    :type job_id: str
    :param report_id: The ID of the report to retrieve.
    :type report_id: str
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
    :param on_behalf_of_content_owner: The content owner&#39;s external ID on which behalf the user is acting on. If not set, the user is acting for himself (his own channel).
    :type on_behalf_of_content_owner: str

    """
    return web.Response(status=200)


async def youtubereporting_jobs_reports_list(request: web.Request, job_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, created_after=None, on_behalf_of_content_owner=None, page_size=None, page_token=None, start_time_at_or_after=None, start_time_before=None) -> web.Response:
    """youtubereporting_jobs_reports_list

    Lists reports created by a specific job. Returns NOT_FOUND if the job does not exist.

    :param job_id: The ID of the job.
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
    :param created_after: If set, only reports created after the specified date/time are returned.
    :type created_after: str
    :param on_behalf_of_content_owner: The content owner&#39;s external ID on which behalf the user is acting on. If not set, the user is acting for himself (his own channel).
    :type on_behalf_of_content_owner: str
    :param page_size: Requested page size. Server may return fewer report types than requested. If unspecified, server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListReportsResponse.next_page_token returned in response to the previous call to the &#x60;ListReports&#x60; method.
    :type page_token: str
    :param start_time_at_or_after: If set, only reports whose start time is greater than or equal the specified date/time are returned.
    :type start_time_at_or_after: str
    :param start_time_before: If set, only reports whose start time is smaller than the specified date/time are returned.
    :type start_time_before: str

    """
    return web.Response(status=200)
