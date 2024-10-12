from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_devtools_remotebuildexecution_admin_v1alpha_create_instance_request import GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest
from openapi_server.models.google_devtools_remotebuildexecution_admin_v1alpha_create_worker_pool_request import GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest
from openapi_server.models.google_devtools_remotebuildexecution_admin_v1alpha_list_instances_response import GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponse
from openapi_server.models.google_devtools_remotebuildexecution_admin_v1alpha_list_worker_pools_response import GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponse
from openapi_server.models.google_devtools_remotebuildexecution_admin_v1alpha_update_worker_pool_request import GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateWorkerPoolRequest
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server import util


async def remotebuildexecution_projects_instances_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """remotebuildexecution_projects_instances_create

    Creates a new instance in the specified region. Returns a long running operation which contains an instance on completion. While the long running operation is in progress, any call to &#x60;GetInstance&#x60; returns an instance in state &#x60;CREATING&#x60;.

    :param parent: Required. Resource name of the project containing the instance. Format: &#x60;projects/[PROJECT_ID]&#x60;.
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
    body = GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def remotebuildexecution_projects_instances_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """remotebuildexecution_projects_instances_list

    Lists instances in a project.

    :param parent: Required. Resource name of the project. Format: &#x60;projects/[PROJECT_ID]&#x60;.
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

    """
    return web.Response(status=200)


async def remotebuildexecution_projects_instances_test_notify(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """remotebuildexecution_projects_instances_test_notify

    Sends a test notification to the specified instance. Returns a &#x60;google.protobuf.Empty&#x60; on success.

    :param name: Name of the instance for which to send a test notification. Format: &#x60;projects/[PROJECT_ID]/instances/[INSTANCE_ID]&#x60;.
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


async def remotebuildexecution_projects_instances_workerpools_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """remotebuildexecution_projects_instances_workerpools_create

    Creates a new worker pool with a specified size and configuration. Returns a long running operation which contains a worker pool on completion. While the long running operation is in progress, any call to &#x60;GetWorkerPool&#x60; returns a worker pool in state &#x60;CREATING&#x60;.

    :param parent: Resource name of the instance in which to create the new worker pool. Format: &#x60;projects/[PROJECT_ID]/instances/[INSTANCE_ID]&#x60;.
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
    body = GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest.from_dict(body)
    return web.Response(status=200)


async def remotebuildexecution_projects_instances_workerpools_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """remotebuildexecution_projects_instances_workerpools_delete

    Deletes the specified worker pool. Returns a long running operation, which contains a &#x60;google.protobuf.Empty&#x60; response on completion. While the long running operation is in progress, any call to &#x60;GetWorkerPool&#x60; returns a worker pool in state &#x60;DELETING&#x60;.

    :param name: Name of the worker pool to delete. Format: &#x60;projects/[PROJECT_ID]/instances/[INSTANCE_ID]/workerpools/[POOL_ID]&#x60;.
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


async def remotebuildexecution_projects_instances_workerpools_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None) -> web.Response:
    """remotebuildexecution_projects_instances_workerpools_list

    Lists worker pools in an instance.

    :param parent: Resource name of the instance. Format: &#x60;projects/[PROJECT_ID]/instances/[INSTANCE_ID]&#x60;.
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
    :param filter: Optional. A filter expression that filters resources listed in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. String values are case-insensitive. The comparison operator must be either &#x60;:&#x60;, &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;, &#x60;&lt;&#x3D;&#x60; or &#x60;&lt;&#x60;. The &#x60;:&#x60; operator can be used with string fields to match substrings. For non-string fields it is equivalent to the &#x60;&#x3D;&#x60; operator. The &#x60;:*&#x60; comparison can be used to test whether a key has been defined. You can also filter on nested fields. To filter on multiple expressions, you can separate expression using &#x60;AND&#x60; and &#x60;OR&#x60; operators, using parentheses to specify precedence. If neither operator is specified, &#x60;AND&#x60; is assumed. Examples: Include only pools with more than 100 reserved workers: &#x60;(worker_count &gt; 100) (worker_config.reserved &#x3D; true)&#x60; Include only pools with a certain label or machines of the e2-standard family: &#x60;worker_config.labels.key1 : * OR worker_config.machine_type: e2-standard&#x60;
    :type filter: str

    """
    return web.Response(status=200)


async def remotebuildexecution_projects_instances_workerpools_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, logging_enabled=None, name1=None, update_mask=None, body=None) -> web.Response:
    """remotebuildexecution_projects_instances_workerpools_patch

    Updates an existing worker pool with a specified size and/or configuration. Returns a long running operation, which contains a worker pool on completion. While the long running operation is in progress, any call to &#x60;GetWorkerPool&#x60; returns a worker pool in state &#x60;UPDATING&#x60;.

    :param name: WorkerPool resource name formatted as: &#x60;projects/[PROJECT_ID]/instances/[INSTANCE_ID]/workerpools/[POOL_ID]&#x60;. name should not be populated when creating a worker pool since it is provided in the &#x60;poolId&#x60; field.
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
    :param logging_enabled: Deprecated, use instance.logging_enabled instead. Whether to enable Stackdriver logging for this instance.
    :type logging_enabled: bool
    :param name1: Deprecated, use instance.Name instead. Name of the instance to update. Format: &#x60;projects/[PROJECT_ID]/instances/[INSTANCE_ID]&#x60;.
    :type name1: str
    :param update_mask: The update mask applies to instance. For the &#x60;FieldMask&#x60; definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask If an empty update_mask is provided, only the non-default valued field in the worker pool field will be updated. Note that in order to update a field to the default value (zero, false, empty string) an explicit update_mask must be provided.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateWorkerPoolRequest.from_dict(body)
    return web.Response(status=200)


async def remotebuildexecution_projects_operations_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """remotebuildexecution_projects_operations_get

    Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

    :param name: The name of the operation resource.
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
