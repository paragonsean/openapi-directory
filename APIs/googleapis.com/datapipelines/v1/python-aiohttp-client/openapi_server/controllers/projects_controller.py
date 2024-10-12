from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_datapipelines_v1_list_jobs_response import GoogleCloudDatapipelinesV1ListJobsResponse
from openapi_server.models.google_cloud_datapipelines_v1_list_pipelines_response import GoogleCloudDatapipelinesV1ListPipelinesResponse
from openapi_server.models.google_cloud_datapipelines_v1_pipeline import GoogleCloudDatapipelinesV1Pipeline
from openapi_server.models.google_cloud_datapipelines_v1_run_pipeline_response import GoogleCloudDatapipelinesV1RunPipelineResponse
from openapi_server import util


async def datapipelines_projects_locations_pipelines_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """datapipelines_projects_locations_pipelines_create

    Creates a pipeline. For a batch pipeline, you can pass scheduler information. Data Pipelines uses the scheduler information to create an internal scheduler that runs jobs periodically. If the internal scheduler is not configured, you can use RunPipeline to run jobs.

    :param parent: Required. The location name. For example: &#x60;projects/PROJECT_ID/locations/LOCATION_ID&#x60;.
    :type parent: str
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
    body = GoogleCloudDatapipelinesV1Pipeline.from_dict(body)
    return web.Response(status=200)


async def datapipelines_projects_locations_pipelines_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """datapipelines_projects_locations_pipelines_delete

    Deletes a pipeline. If a scheduler job is attached to the pipeline, it will be deleted.

    :param name: Required. The pipeline name. For example: &#x60;projects/PROJECT_ID/locations/LOCATION_ID/pipelines/PIPELINE_ID&#x60;.
    :type name: str
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


async def datapipelines_projects_locations_pipelines_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """datapipelines_projects_locations_pipelines_get

    Looks up a single pipeline. Returns a \&quot;NOT_FOUND\&quot; error if no such pipeline exists. Returns a \&quot;FORBIDDEN\&quot; error if the caller doesn&#39;t have permission to access it.

    :param name: Required. The pipeline name. For example: &#x60;projects/PROJECT_ID/locations/LOCATION_ID/pipelines/PIPELINE_ID&#x60;.
    :type name: str
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


async def datapipelines_projects_locations_pipelines_jobs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """datapipelines_projects_locations_pipelines_jobs_list

    Lists jobs for a given pipeline. Throws a \&quot;FORBIDDEN\&quot; error if the caller doesn&#39;t have permission to access it.

    :param parent: Required. The pipeline name. For example: &#x60;projects/PROJECT_ID/locations/LOCATION_ID/pipelines/PIPELINE_ID&#x60;.
    :type parent: str
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
    :param page_size: The maximum number of entities to return. The service may return fewer than this value, even if there are additional pages. If unspecified, the max limit will be determined by the backend implementation.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListJobs&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListJobs&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def datapipelines_projects_locations_pipelines_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """datapipelines_projects_locations_pipelines_list

    Lists pipelines. Returns a \&quot;FORBIDDEN\&quot; error if the caller doesn&#39;t have permission to access it.

    :param parent: Required. The location name. For example: &#x60;projects/PROJECT_ID/locations/LOCATION_ID&#x60;.
    :type parent: str
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
    :param filter: An expression for filtering the results of the request. If unspecified, all pipelines will be returned. Multiple filters can be applied and must be comma separated. Fields eligible for filtering are: + &#x60;type&#x60;: The type of the pipeline (streaming or batch). Allowed values are &#x60;ALL&#x60;, &#x60;BATCH&#x60;, and &#x60;STREAMING&#x60;. + &#x60;status&#x60;: The activity status of the pipeline. Allowed values are &#x60;ALL&#x60;, &#x60;ACTIVE&#x60;, &#x60;ARCHIVED&#x60;, and &#x60;PAUSED&#x60;. For example, to limit results to active batch processing pipelines: type:BATCH,status:ACTIVE
    :type filter: str
    :param page_size: The maximum number of entities to return. The service may return fewer than this value, even if there are additional pages. If unspecified, the max limit is yet to be determined by the backend implementation.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListPipelines&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListPipelines&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def datapipelines_projects_locations_pipelines_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """datapipelines_projects_locations_pipelines_patch

    Updates a pipeline. If successful, the updated Pipeline is returned. Returns &#x60;NOT_FOUND&#x60; if the pipeline doesn&#39;t exist. If UpdatePipeline does not return successfully, you can retry the UpdatePipeline request until you receive a successful response.

    :param name: The pipeline name. For example: &#x60;projects/PROJECT_ID/locations/LOCATION_ID/pipelines/PIPELINE_ID&#x60;. * &#x60;PROJECT_ID&#x60; can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), and periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). * &#x60;LOCATION_ID&#x60; is the canonical ID for the pipeline&#39;s location. The list of available locations can be obtained by calling &#x60;google.cloud.location.Locations.ListLocations&#x60;. Note that the Data Pipelines service is not available in all regions. It depends on Cloud Scheduler, an App Engine application, so it&#39;s only available in [App Engine regions](https://cloud.google.com/about/locations#region). * &#x60;PIPELINE_ID&#x60; is the ID of the pipeline. Must be unique for the selected project and location.
    :type name: str
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
    :param update_mask: The list of fields to be updated.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudDatapipelinesV1Pipeline.from_dict(body)
    return web.Response(status=200)


async def datapipelines_projects_locations_pipelines_run(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """datapipelines_projects_locations_pipelines_run

    Creates a job for the specified pipeline directly. You can use this method when the internal scheduler is not configured and you want to trigger the job directly or through an external system. Returns a \&quot;NOT_FOUND\&quot; error if the pipeline doesn&#39;t exist. Returns a \&quot;FORBIDDEN\&quot; error if the user doesn&#39;t have permission to access the pipeline or run jobs for the pipeline.

    :param name: Required. The pipeline name. For example: &#x60;projects/PROJECT_ID/locations/LOCATION_ID/pipelines/PIPELINE_ID&#x60;.
    :type name: str
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
    :type body: 

    """
    return web.Response(status=200)


async def datapipelines_projects_locations_pipelines_stop(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """datapipelines_projects_locations_pipelines_stop

    Freezes pipeline execution permanently. If there&#39;s a corresponding scheduler entry, it&#39;s deleted, and the pipeline state is changed to \&quot;ARCHIVED\&quot;. However, pipeline metadata is retained.

    :param name: Required. The pipeline name. For example: &#x60;projects/PROJECT_ID/locations/LOCATION_ID/pipelines/PIPELINE_ID&#x60;.
    :type name: str
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
    :type body: 

    """
    return web.Response(status=200)
