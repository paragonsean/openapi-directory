from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain_mapping import DomainMapping
from openapi_server.models.execution import Execution
from openapi_server.models.job import Job
from openapi_server.models.list_authorized_domains_response import ListAuthorizedDomainsResponse
from openapi_server.models.list_configurations_response import ListConfigurationsResponse
from openapi_server.models.list_domain_mappings_response import ListDomainMappingsResponse
from openapi_server.models.list_executions_response import ListExecutionsResponse
from openapi_server.models.list_jobs_response import ListJobsResponse
from openapi_server.models.list_revisions_response import ListRevisionsResponse
from openapi_server.models.list_routes_response import ListRoutesResponse
from openapi_server.models.list_services_response import ListServicesResponse
from openapi_server.models.list_tasks_response import ListTasksResponse
from openapi_server.models.run_job_request import RunJobRequest
from openapi_server.models.service import Service
from openapi_server.models.status import Status
from openapi_server.models.task import Task
from openapi_server import util


async def run_namespaces_authorizeddomains_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """run_namespaces_authorizeddomains_list

    List authorized domains.

    :param parent: Name of the parent Project resource. Example: &#x60;projects/myproject&#x60;.
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
    :param page_size: Maximum results to return per page.
    :type page_size: int
    :param page_token: Continuation token for fetching the next page of results.
    :type page_token: str

    """
    return web.Response(status=200)


async def run_namespaces_configurations_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, _continue=None, field_selector=None, include_uninitialized=None, label_selector=None, limit=None, resource_version=None, watch=None) -> web.Response:
    """run_namespaces_configurations_list

    List configurations.

    :param parent: The namespace from which the configurations should be listed. For Cloud Run, replace {namespace_id} with the project ID or number.
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
    :param _continue: Optional. Encoded string to continue paging.
    :type _continue: str
    :param field_selector: Not supported by Cloud Run.
    :type field_selector: str
    :param include_uninitialized: Not supported by Cloud Run.
    :type include_uninitialized: bool
    :param label_selector: Allows to filter resources based on a label. Supported operations are &#x3D;, !&#x3D;, exists, in, and notIn.
    :type label_selector: str
    :param limit: Optional. The maximum number of the records that should be returned.
    :type limit: int
    :param resource_version: Not supported by Cloud Run.
    :type resource_version: str
    :param watch: Not supported by Cloud Run.
    :type watch: bool

    """
    return web.Response(status=200)


async def run_namespaces_domainmappings_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, dry_run=None, body=None) -> web.Response:
    """run_namespaces_domainmappings_create

    Create a new domain mapping.

    :param parent: Required. The namespace in which the domain mapping should be created. For Cloud Run (fully managed), replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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
    :param dry_run: Indicates that the server should validate the request and populate default values without persisting the request. Supported values: &#x60;all&#x60;
    :type dry_run: str
    :param body: 
    :type body: dict | bytes

    """
    body = DomainMapping.from_dict(body)
    return web.Response(status=200)


async def run_namespaces_domainmappings_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, api_version=None, dry_run=None, kind=None, propagation_policy=None) -> web.Response:
    """run_namespaces_domainmappings_delete

    Delete a domain mapping.

    :param name: Required. The name of the domain mapping to delete. For Cloud Run (fully managed), replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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
    :param api_version: Cloud Run currently ignores this parameter.
    :type api_version: str
    :param dry_run: Indicates that the server should validate the request and populate default values without persisting the request. Supported values: &#x60;all&#x60;
    :type dry_run: str
    :param kind: Cloud Run currently ignores this parameter.
    :type kind: str
    :param propagation_policy: Specifies the propagation policy of delete. Cloud Run currently ignores this setting, and deletes in the background. Please see kubernetes.io/docs/concepts/architecture/garbage-collection/ for more information.
    :type propagation_policy: str

    """
    return web.Response(status=200)


async def run_namespaces_domainmappings_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """run_namespaces_domainmappings_get

    Get information about a domain mapping.

    :param name: Required. The name of the domain mapping to retrieve. For Cloud Run (fully managed), replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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


async def run_namespaces_domainmappings_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, _continue=None, field_selector=None, include_uninitialized=None, label_selector=None, limit=None, resource_version=None, watch=None) -> web.Response:
    """run_namespaces_domainmappings_list

    List all domain mappings.

    :param parent: Required. The namespace from which the domain mappings should be listed. For Cloud Run (fully managed), replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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
    :param _continue: Optional. Encoded string to continue paging.
    :type _continue: str
    :param field_selector: Allows to filter resources based on a specific value for a field name. Send this in a query string format. i.e. &#39;metadata.name%3Dlorem&#39;. Not currently used by Cloud Run.
    :type field_selector: str
    :param include_uninitialized: Not currently used by Cloud Run.
    :type include_uninitialized: bool
    :param label_selector: Allows to filter resources based on a label. Supported operations are &#x3D;, !&#x3D;, exists, in, and notIn.
    :type label_selector: str
    :param limit: Optional. The maximum number of records that should be returned.
    :type limit: int
    :param resource_version: The baseline resource version from which the list or watch operation should start. Not currently used by Cloud Run.
    :type resource_version: str
    :param watch: Flag that indicates that the client expects to watch this resource as well. Not currently used by Cloud Run.
    :type watch: bool

    """
    return web.Response(status=200)


async def run_namespaces_executions_cancel(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """run_namespaces_executions_cancel

    Cancel an execution.

    :param name: Required. The name of the execution to cancel. Replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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


async def run_namespaces_executions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, _continue=None, field_selector=None, include_uninitialized=None, label_selector=None, limit=None, resource_version=None, watch=None) -> web.Response:
    """run_namespaces_executions_list

    List executions.

    :param parent: Required. The namespace from which the executions should be listed. Replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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
    :param _continue: Optional. Optional encoded string to continue paging.
    :type _continue: str
    :param field_selector: Optional. Not supported by Cloud Run.
    :type field_selector: str
    :param include_uninitialized: Optional. Not supported by Cloud Run.
    :type include_uninitialized: bool
    :param label_selector: Optional. Allows to filter resources based on a label. Supported operations are &#x3D;, !&#x3D;, exists, in, and notIn.
    :type label_selector: str
    :param limit: Optional. The maximum number of the records that should be returned.
    :type limit: int
    :param resource_version: Optional. Not supported by Cloud Run.
    :type resource_version: str
    :param watch: Optional. Not supported by Cloud Run.
    :type watch: bool

    """
    return web.Response(status=200)


async def run_namespaces_jobs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """run_namespaces_jobs_create

    Create a job.

    :param parent: Required. The namespace in which the job should be created. Replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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
    body = Job.from_dict(body)
    return web.Response(status=200)


async def run_namespaces_jobs_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, api_version=None, kind=None, propagation_policy=None) -> web.Response:
    """run_namespaces_jobs_delete

    Delete a job.

    :param name: Required. The name of the job to delete. Replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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
    :param api_version: Optional. Cloud Run currently ignores this parameter.
    :type api_version: str
    :param kind: Optional. Cloud Run currently ignores this parameter.
    :type kind: str
    :param propagation_policy: Optional. Specifies the propagation policy of delete. Cloud Run currently ignores this setting, and deletes in the background. Please see kubernetes.io/docs/concepts/workloads/controllers/garbage-collection/ for more information.
    :type propagation_policy: str

    """
    return web.Response(status=200)


async def run_namespaces_jobs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, _continue=None, field_selector=None, include_uninitialized=None, label_selector=None, limit=None, resource_version=None, watch=None) -> web.Response:
    """run_namespaces_jobs_list

    List jobs.

    :param parent: Required. The namespace from which the jobs should be listed. Replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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
    :param _continue: Optional. Optional encoded string to continue paging.
    :type _continue: str
    :param field_selector: Optional. Not supported by Cloud Run.
    :type field_selector: str
    :param include_uninitialized: Optional. Not supported by Cloud Run.
    :type include_uninitialized: bool
    :param label_selector: Optional. Allows to filter resources based on a label. Supported operations are &#x3D;, !&#x3D;, exists, in, and notIn.
    :type label_selector: str
    :param limit: Optional. The maximum number of records that should be returned.
    :type limit: int
    :param resource_version: Optional. Not supported by Cloud Run.
    :type resource_version: str
    :param watch: Optional. Not supported by Cloud Run.
    :type watch: bool

    """
    return web.Response(status=200)


async def run_namespaces_jobs_replace_job(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """run_namespaces_jobs_replace_job

    Replace a job. Only the spec and metadata labels and annotations are modifiable. After the Replace request, Cloud Run will work to make the &#39;status&#39; match the requested &#39;spec&#39;. May provide metadata.resourceVersion to enforce update from last read for optimistic concurrency control.

    :param name: Required. The name of the job being replaced. Replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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
    :type body: dict | bytes

    """
    body = Job.from_dict(body)
    return web.Response(status=200)


async def run_namespaces_jobs_run(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """run_namespaces_jobs_run

    Trigger creation of a new execution of this job.

    :param name: Required. The name of the job to run. Replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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
    :type body: dict | bytes

    """
    body = RunJobRequest.from_dict(body)
    return web.Response(status=200)


async def run_namespaces_revisions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, _continue=None, field_selector=None, include_uninitialized=None, label_selector=None, limit=None, resource_version=None, watch=None) -> web.Response:
    """run_namespaces_revisions_list

    List revisions.

    :param parent: The namespace from which the revisions should be listed. For Cloud Run (fully managed), replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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
    :param _continue: Optional. Encoded string to continue paging.
    :type _continue: str
    :param field_selector: Allows to filter resources based on a specific value for a field name. Send this in a query string format. i.e. &#39;metadata.name%3Dlorem&#39;. Not currently used by Cloud Run.
    :type field_selector: str
    :param include_uninitialized: Not currently used by Cloud Run.
    :type include_uninitialized: bool
    :param label_selector: Allows to filter resources based on a label. Supported operations are &#x3D;, !&#x3D;, exists, in, and notIn.
    :type label_selector: str
    :param limit: Optional. The maximum number of records that should be returned.
    :type limit: int
    :param resource_version: The baseline resource version from which the list or watch operation should start. Not currently used by Cloud Run.
    :type resource_version: str
    :param watch: Flag that indicates that the client expects to watch this resource as well. Not currently used by Cloud Run.
    :type watch: bool

    """
    return web.Response(status=200)


async def run_namespaces_routes_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, _continue=None, field_selector=None, include_uninitialized=None, label_selector=None, limit=None, resource_version=None, watch=None) -> web.Response:
    """run_namespaces_routes_list

    List routes.

    :param parent: The namespace from which the routes should be listed. For Cloud Run (fully managed), replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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
    :param _continue: Optional. Encoded string to continue paging.
    :type _continue: str
    :param field_selector: Allows to filter resources based on a specific value for a field name. Send this in a query string format. i.e. &#39;metadata.name%3Dlorem&#39;. Not currently used by Cloud Run.
    :type field_selector: str
    :param include_uninitialized: Not currently used by Cloud Run.
    :type include_uninitialized: bool
    :param label_selector: Allows to filter resources based on a label. Supported operations are &#x3D;, !&#x3D;, exists, in, and notIn.
    :type label_selector: str
    :param limit: Optional. The maximum number of records that should be returned.
    :type limit: int
    :param resource_version: The baseline resource version from which the list or watch operation should start. Not currently used by Cloud Run.
    :type resource_version: str
    :param watch: Flag that indicates that the client expects to watch this resource as well. Not currently used by Cloud Run.
    :type watch: bool

    """
    return web.Response(status=200)


async def run_namespaces_services_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, dry_run=None, body=None) -> web.Response:
    """run_namespaces_services_create

    Creates a new Service. Service creation will trigger a new deployment. Use GetService, and check service.status to determine if the Service is ready.

    :param parent: Required. The resource&#39;s parent. In Cloud Run, it may be one of the following: * &#x60;{project_id_or_number}&#x60; * &#x60;namespaces/{project_id_or_number}&#x60; * &#x60;namespaces/{project_id_or_number}/services&#x60; * &#x60;projects/{project_id_or_number}/locations/{region}&#x60; * &#x60;projects/{project_id_or_number}/regions/{region}&#x60;
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
    :param dry_run: Indicates that the server should validate the request and populate default values without persisting the request. Supported values: &#x60;all&#x60;
    :type dry_run: str
    :param body: 
    :type body: dict | bytes

    """
    body = Service.from_dict(body)
    return web.Response(status=200)


async def run_namespaces_services_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, api_version=None, dry_run=None, kind=None, propagation_policy=None) -> web.Response:
    """run_namespaces_services_delete

    Deletes the provided service. This will cause the Service to stop serving traffic and will delete all associated Revisions.

    :param name: Required. The fully qualified name of the service to delete. It can be any of the following forms: * &#x60;namespaces/{project_id_or_number}/services/{service_name}&#x60; (only when the &#x60;endpoint&#x60; is regional) * &#x60;projects/{project_id_or_number}/locations/{region}/services/{service_name}&#x60; * &#x60;projects/{project_id_or_number}/regions/{region}/services/{service_name}&#x60;
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
    :param api_version: Not supported, and ignored by Cloud Run.
    :type api_version: str
    :param dry_run: Indicates that the server should validate the request and populate default values without persisting the request. Supported values: &#x60;all&#x60;
    :type dry_run: str
    :param kind: Not supported, and ignored by Cloud Run.
    :type kind: str
    :param propagation_policy: Not supported, and ignored by Cloud Run.
    :type propagation_policy: str

    """
    return web.Response(status=200)


async def run_namespaces_services_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """run_namespaces_services_get

    Gets information about a service.

    :param name: Required. The fully qualified name of the service to retrieve. It can be any of the following forms: * &#x60;namespaces/{project_id_or_number}/services/{service_name}&#x60; (only when the &#x60;endpoint&#x60; is regional) * &#x60;projects/{project_id_or_number}/locations/{region}/services/{service_name}&#x60; * &#x60;projects/{project_id_or_number}/regions/{region}/services/{service_name}&#x60;
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


async def run_namespaces_services_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, _continue=None, field_selector=None, include_uninitialized=None, label_selector=None, limit=None, resource_version=None, watch=None) -> web.Response:
    """run_namespaces_services_list

    Lists services for the given project and region.

    :param parent: Required. The parent from where the resources should be listed. In Cloud Run, it may be one of the following: * &#x60;{project_id_or_number}&#x60; * &#x60;namespaces/{project_id_or_number}&#x60; * &#x60;namespaces/{project_id_or_number}/services&#x60; * &#x60;projects/{project_id_or_number}/locations/{region}&#x60; * &#x60;projects/{project_id_or_number}/regions/{region}&#x60;
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
    :param _continue: Encoded string to continue paging.
    :type _continue: str
    :param field_selector: Not supported, and ignored by Cloud Run.
    :type field_selector: str
    :param include_uninitialized: Not supported, and ignored by Cloud Run.
    :type include_uninitialized: bool
    :param label_selector: Allows to filter resources based on a label. Supported operations are &#x3D;, !&#x3D;, exists, in, and notIn.
    :type label_selector: str
    :param limit: The maximum number of records that should be returned.
    :type limit: int
    :param resource_version: Not supported, and ignored by Cloud Run.
    :type resource_version: str
    :param watch: Not supported, and ignored by Cloud Run.
    :type watch: bool

    """
    return web.Response(status=200)


async def run_namespaces_services_replace_service(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, dry_run=None, body=None) -> web.Response:
    """run_namespaces_services_replace_service

    Replaces a service. Only the spec and metadata labels and annotations are modifiable. After the Update request, Cloud Run will work to make the &#39;status&#39; match the requested &#39;spec&#39;. May provide metadata.resourceVersion to enforce update from last read for optimistic concurrency control.

    :param name: Required. The fully qualified name of the service to replace. It can be any of the following forms: * &#x60;namespaces/{project_id_or_number}/services/{service_name}&#x60; (only when the &#x60;endpoint&#x60; is regional) * &#x60;projects/{project_id_or_number}/locations/{region}/services/{service_name}&#x60; * &#x60;projects/{project_id_or_number}/regions/{region}/services/{service_name}&#x60;
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
    :param dry_run: Indicates that the server should validate the request and populate default values without persisting the request. Supported values: &#x60;all&#x60;
    :type dry_run: str
    :param body: 
    :type body: dict | bytes

    """
    body = Service.from_dict(body)
    return web.Response(status=200)


async def run_namespaces_tasks_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """run_namespaces_tasks_get

    Get information about a task.

    :param name: Required. The name of the task to retrieve. Replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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


async def run_namespaces_tasks_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, _continue=None, field_selector=None, include_uninitialized=None, label_selector=None, limit=None, resource_version=None, watch=None) -> web.Response:
    """run_namespaces_tasks_list

    List tasks.

    :param parent: Required. The namespace from which the tasks should be listed. Replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID
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
    :param _continue: Optional. Optional encoded string to continue paging.
    :type _continue: str
    :param field_selector: Optional. Not supported by Cloud Run.
    :type field_selector: str
    :param include_uninitialized: Optional. Not supported by Cloud Run.
    :type include_uninitialized: bool
    :param label_selector: Optional. Allows to filter resources based on a label. Supported operations are &#x3D;, !&#x3D;, exists, in, and notIn. For example, to list all tasks of execution \&quot;foo\&quot; in succeeded state: &#x60;run.googleapis.com/execution&#x3D;foo,run.googleapis.com/runningState&#x3D;Succeeded&#x60;. Supported states are: * &#x60;Pending&#x60;: Initial state of all tasks. The task has not yet started but eventually will. * &#x60;Running&#x60;: Container instances for this task are running or will be running shortly. * &#x60;Succeeded&#x60;: No more container instances to run for the task, and the last attempt succeeded. * &#x60;Failed&#x60;: No more container instances to run for the task, and the last attempt failed. This task has run out of retry attempts. * &#x60;Cancelled&#x60;: Task was running but got stopped because its parent execution has been aborted. * &#x60;Abandoned&#x60;: The task has not yet started and never will because its parent execution has been aborted.
    :type label_selector: str
    :param limit: Optional. The maximum number of records that should be returned.
    :type limit: int
    :param resource_version: Optional. Not supported by Cloud Run.
    :type resource_version: str
    :param watch: Optional. Not supported by Cloud Run.
    :type watch: bool

    """
    return web.Response(status=200)
