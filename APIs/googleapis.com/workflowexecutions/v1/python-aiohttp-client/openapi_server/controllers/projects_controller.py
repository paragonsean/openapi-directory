from typing import List, Dict
from aiohttp import web

from openapi_server.models.execution import Execution
from openapi_server.models.export_data_response import ExportDataResponse
from openapi_server.models.list_callbacks_response import ListCallbacksResponse
from openapi_server.models.list_executions_response import ListExecutionsResponse
from openapi_server.models.list_step_entries_response import ListStepEntriesResponse
from openapi_server.models.step_entry import StepEntry
from openapi_server.models.trigger_pubsub_execution_request import TriggerPubsubExecutionRequest
from openapi_server import util


async def workflowexecutions_projects_locations_workflows_executions_callbacks_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """workflowexecutions_projects_locations_workflows_executions_callbacks_list

    Returns a list of active callbacks that belong to the execution with the given name. The returned callbacks are ordered by callback ID.

    :param parent: Required. Name of the execution for which the callbacks should be listed. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}
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
    :param page_size: Maximum number of callbacks to return per call. The default value is 100 and is also the maximum value.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListCallbacks&#x60; call. Provide this to retrieve the subsequent page. Note that pagination is applied to dynamic data. The list of callbacks returned can change between page requests if callbacks are created or deleted.
    :type page_token: str

    """
    return web.Response(status=200)


async def workflowexecutions_projects_locations_workflows_executions_cancel(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """workflowexecutions_projects_locations_workflows_executions_cancel

    Cancels an execution of the given name.

    :param name: Required. Name of the execution to be cancelled. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}
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


async def workflowexecutions_projects_locations_workflows_executions_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """workflowexecutions_projects_locations_workflows_executions_create

    Creates a new execution using the latest revision of the given workflow. For more information, see Execute a workflow.

    :param parent: Required. Name of the workflow for which an execution should be created. Format: projects/{project}/locations/{location}/workflows/{workflow} The latest revision of the workflow will be used.
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
    body = Execution.from_dict(body)
    return web.Response(status=200)


async def workflowexecutions_projects_locations_workflows_executions_export_data(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """workflowexecutions_projects_locations_workflows_executions_export_data

    Returns all metadata stored about an execution, excluding most data that is already accessible using other API methods.

    :param name: Required. Name of the execution for which data is to be exported. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}
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


async def workflowexecutions_projects_locations_workflows_executions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, view=None) -> web.Response:
    """workflowexecutions_projects_locations_workflows_executions_list

    Returns a list of executions which belong to the workflow with the given name. The method returns executions of all workflow revisions. Returned executions are ordered by their start time (newest first).

    :param parent: Required. Name of the workflow for which the executions should be listed. Format: projects/{project}/locations/{location}/workflows/{workflow}
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
    :param filter: Optional. Filters applied to the &#x60;[Executions.ListExecutions]&#x60; results. The following fields are supported for filtering: &#x60;executionId&#x60;, &#x60;state&#x60;, &#x60;createTime&#x60;, &#x60;startTime&#x60;, &#x60;endTime&#x60;, &#x60;duration&#x60;, &#x60;workflowRevisionId&#x60;, &#x60;stepName&#x60;, and &#x60;label&#x60;. For details, see AIP-160. For example, if you are using the Google APIs Explorer: &#x60;state&#x3D;\&quot;SUCCEEDED\&quot;&#x60; or &#x60;startTime&gt;\&quot;2023-08-01\&quot; AND state&#x3D;\&quot;FAILED\&quot;&#x60;
    :type filter: str
    :param order_by: Optional. Comma-separated list of fields that specify the ordering applied to the &#x60;[Executions.ListExecutions]&#x60; results. By default the ordering is based on descending &#x60;createTime&#x60;. The following fields are supported for ordering: &#x60;executionId&#x60;, &#x60;state&#x60;, &#x60;createTime&#x60;, &#x60;startTime&#x60;, &#x60;endTime&#x60;, &#x60;duration&#x60;, and &#x60;workflowRevisionId&#x60;. For details, see AIP-132.
    :type order_by: str
    :param page_size: Maximum number of executions to return per call. Max supported value depends on the selected Execution view: it&#39;s 1000 for BASIC and 100 for FULL. The default value used if the field is not specified is 100, regardless of the selected view. Values greater than the max value will be coerced down to it.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListExecutions&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListExecutions&#x60; must match the call that provided the page token. Note that pagination is applied to dynamic data. The list of executions returned can change between page requests.
    :type page_token: str
    :param view: Optional. A view defining which fields should be filled in the returned executions. The API will default to the BASIC view.
    :type view: str

    """
    return web.Response(status=200)


async def workflowexecutions_projects_locations_workflows_executions_step_entries_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, view=None) -> web.Response:
    """workflowexecutions_projects_locations_workflows_executions_step_entries_get

    Gets a step entry.

    :param name: Required. The name of the step entry to retrieve. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}/stepEntries/{step_entry}
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
    :param view: Optional. A view defining which fields should be filled in the returned execution. The API will default to the FULL view.
    :type view: str

    """
    return web.Response(status=200)


async def workflowexecutions_projects_locations_workflows_executions_step_entries_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, skip=None) -> web.Response:
    """workflowexecutions_projects_locations_workflows_executions_step_entries_list

    Lists step entries for the corresponding workflow execution. Returned entries are ordered by their create_time.

    :param parent: Required. Name of the workflow execution to list entries for. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}/stepEntries/
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
    :param filter: Optional. Filters applied to the &#x60;[StepEntries.ListStepEntries]&#x60; results. The following fields are supported for filtering: &#x60;entryId&#x60;, &#x60;createTime&#x60;, &#x60;updateTime&#x60;, &#x60;routine&#x60;, &#x60;step&#x60;, &#x60;stepType&#x60;, &#x60;state&#x60;. For details, see AIP-160. For example, if you are using the Google APIs Explorer: &#x60;state&#x3D;\&quot;SUCCEEDED\&quot;&#x60; or &#x60;createTime&gt;\&quot;2023-08-01\&quot; AND state&#x3D;\&quot;FAILED\&quot;&#x60;
    :type filter: str
    :param order_by: Optional. Comma-separated list of fields that specify the ordering applied to the &#x60;[StepEntries.ListStepEntries]&#x60; results. By default the ordering is based on ascending &#x60;entryId&#x60;. The following fields are supported for ordering: &#x60;entryId&#x60;, &#x60;createTime&#x60;, &#x60;updateTime&#x60;, &#x60;routine&#x60;, &#x60;step&#x60;, &#x60;stepType&#x60;, &#x60;state&#x60;. For details, see AIP-132.
    :type order_by: str
    :param page_size: Optional. Number of step entries to return per call. The default max is 1000.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListStepEntries&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListStepEntries&#x60; must match the call that provided the page token.
    :type page_token: str
    :param skip: Optional. The number of step entries to skip. It can be used with or without a pageToken. If used with a pageToken, then it indicates the number of step entries to skip starting from the requested page.
    :type skip: int

    """
    return web.Response(status=200)


async def workflowexecutions_projects_locations_workflows_trigger_pubsub_execution(request: web.Request, workflow, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """workflowexecutions_projects_locations_workflows_trigger_pubsub_execution

    Triggers a new execution using the latest revision of the given workflow by a Pub/Sub push notification.

    :param workflow: Required. Name of the workflow for which an execution should be created. Format: projects/{project}/locations/{location}/workflows/{workflow}
    :type workflow: str
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
    body = TriggerPubsubExecutionRequest.from_dict(body)
    return web.Response(status=200)
