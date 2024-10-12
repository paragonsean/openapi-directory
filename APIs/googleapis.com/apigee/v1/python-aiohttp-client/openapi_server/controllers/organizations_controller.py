from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_api_http_body import GoogleApiHttpBody
from openapi_server.models.google_cloud_apigee_v1_adjust_developer_balance_request import GoogleCloudApigeeV1AdjustDeveloperBalanceRequest
from openapi_server.models.google_cloud_apigee_v1_alias import GoogleCloudApigeeV1Alias
from openapi_server.models.google_cloud_apigee_v1_api_category import GoogleCloudApigeeV1ApiCategory
from openapi_server.models.google_cloud_apigee_v1_api_category_response import GoogleCloudApigeeV1ApiCategoryResponse
from openapi_server.models.google_cloud_apigee_v1_api_doc import GoogleCloudApigeeV1ApiDoc
from openapi_server.models.google_cloud_apigee_v1_api_doc_documentation import GoogleCloudApigeeV1ApiDocDocumentation
from openapi_server.models.google_cloud_apigee_v1_api_doc_documentation_response import GoogleCloudApigeeV1ApiDocDocumentationResponse
from openapi_server.models.google_cloud_apigee_v1_api_doc_response import GoogleCloudApigeeV1ApiDocResponse
from openapi_server.models.google_cloud_apigee_v1_api_product import GoogleCloudApigeeV1ApiProduct
from openapi_server.models.google_cloud_apigee_v1_api_proxy_revision import GoogleCloudApigeeV1ApiProxyRevision
from openapi_server.models.google_cloud_apigee_v1_app_group import GoogleCloudApigeeV1AppGroup
from openapi_server.models.google_cloud_apigee_v1_archive_deployment import GoogleCloudApigeeV1ArchiveDeployment
from openapi_server.models.google_cloud_apigee_v1_async_query import GoogleCloudApigeeV1AsyncQuery
from openapi_server.models.google_cloud_apigee_v1_attributes import GoogleCloudApigeeV1Attributes
from openapi_server.models.google_cloud_apigee_v1_batch_update_security_incidents_request import GoogleCloudApigeeV1BatchUpdateSecurityIncidentsRequest
from openapi_server.models.google_cloud_apigee_v1_batch_update_security_incidents_response import GoogleCloudApigeeV1BatchUpdateSecurityIncidentsResponse
from openapi_server.models.google_cloud_apigee_v1_canary_evaluation import GoogleCloudApigeeV1CanaryEvaluation
from openapi_server.models.google_cloud_apigee_v1_compute_environment_scores_request import GoogleCloudApigeeV1ComputeEnvironmentScoresRequest
from openapi_server.models.google_cloud_apigee_v1_compute_environment_scores_response import GoogleCloudApigeeV1ComputeEnvironmentScoresResponse
from openapi_server.models.google_cloud_apigee_v1_credit_developer_balance_request import GoogleCloudApigeeV1CreditDeveloperBalanceRequest
from openapi_server.models.google_cloud_apigee_v1_custom_report import GoogleCloudApigeeV1CustomReport
from openapi_server.models.google_cloud_apigee_v1_data_collector import GoogleCloudApigeeV1DataCollector
from openapi_server.models.google_cloud_apigee_v1_datastore import GoogleCloudApigeeV1Datastore
from openapi_server.models.google_cloud_apigee_v1_debug_session import GoogleCloudApigeeV1DebugSession
from openapi_server.models.google_cloud_apigee_v1_delete_response import GoogleCloudApigeeV1DeleteResponse
from openapi_server.models.google_cloud_apigee_v1_deployment import GoogleCloudApigeeV1Deployment
from openapi_server.models.google_cloud_apigee_v1_deployment_change_report import GoogleCloudApigeeV1DeploymentChangeReport
from openapi_server.models.google_cloud_apigee_v1_developer import GoogleCloudApigeeV1Developer
from openapi_server.models.google_cloud_apigee_v1_developer_app import GoogleCloudApigeeV1DeveloperApp
from openapi_server.models.google_cloud_apigee_v1_developer_app_key import GoogleCloudApigeeV1DeveloperAppKey
from openapi_server.models.google_cloud_apigee_v1_developer_balance import GoogleCloudApigeeV1DeveloperBalance
from openapi_server.models.google_cloud_apigee_v1_developer_subscription import GoogleCloudApigeeV1DeveloperSubscription
from openapi_server.models.google_cloud_apigee_v1_endpoint_attachment import GoogleCloudApigeeV1EndpointAttachment
from openapi_server.models.google_cloud_apigee_v1_environment_group import GoogleCloudApigeeV1EnvironmentGroup
from openapi_server.models.google_cloud_apigee_v1_export import GoogleCloudApigeeV1Export
from openapi_server.models.google_cloud_apigee_v1_export_request import GoogleCloudApigeeV1ExportRequest
from openapi_server.models.google_cloud_apigee_v1_generate_download_url_response import GoogleCloudApigeeV1GenerateDownloadUrlResponse
from openapi_server.models.google_cloud_apigee_v1_generate_upload_url_response import GoogleCloudApigeeV1GenerateUploadUrlResponse
from openapi_server.models.google_cloud_apigee_v1_instance import GoogleCloudApigeeV1Instance
from openapi_server.models.google_cloud_apigee_v1_instance_attachment import GoogleCloudApigeeV1InstanceAttachment
from openapi_server.models.google_cloud_apigee_v1_key_value_entry import GoogleCloudApigeeV1KeyValueEntry
from openapi_server.models.google_cloud_apigee_v1_key_value_map import GoogleCloudApigeeV1KeyValueMap
from openapi_server.models.google_cloud_apigee_v1_keystore import GoogleCloudApigeeV1Keystore
from openapi_server.models.google_cloud_apigee_v1_list_api_categories_response import GoogleCloudApigeeV1ListApiCategoriesResponse
from openapi_server.models.google_cloud_apigee_v1_list_api_docs_response import GoogleCloudApigeeV1ListApiDocsResponse
from openapi_server.models.google_cloud_apigee_v1_list_api_products_response import GoogleCloudApigeeV1ListApiProductsResponse
from openapi_server.models.google_cloud_apigee_v1_list_api_proxies_response import GoogleCloudApigeeV1ListApiProxiesResponse
from openapi_server.models.google_cloud_apigee_v1_list_app_groups_response import GoogleCloudApigeeV1ListAppGroupsResponse
from openapi_server.models.google_cloud_apigee_v1_list_archive_deployments_response import GoogleCloudApigeeV1ListArchiveDeploymentsResponse
from openapi_server.models.google_cloud_apigee_v1_list_async_queries_response import GoogleCloudApigeeV1ListAsyncQueriesResponse
from openapi_server.models.google_cloud_apigee_v1_list_custom_reports_response import GoogleCloudApigeeV1ListCustomReportsResponse
from openapi_server.models.google_cloud_apigee_v1_list_data_collectors_response import GoogleCloudApigeeV1ListDataCollectorsResponse
from openapi_server.models.google_cloud_apigee_v1_list_datastores_response import GoogleCloudApigeeV1ListDatastoresResponse
from openapi_server.models.google_cloud_apigee_v1_list_debug_sessions_response import GoogleCloudApigeeV1ListDebugSessionsResponse
from openapi_server.models.google_cloud_apigee_v1_list_deployments_response import GoogleCloudApigeeV1ListDeploymentsResponse
from openapi_server.models.google_cloud_apigee_v1_list_developer_apps_response import GoogleCloudApigeeV1ListDeveloperAppsResponse
from openapi_server.models.google_cloud_apigee_v1_list_developer_subscriptions_response import GoogleCloudApigeeV1ListDeveloperSubscriptionsResponse
from openapi_server.models.google_cloud_apigee_v1_list_endpoint_attachments_response import GoogleCloudApigeeV1ListEndpointAttachmentsResponse
from openapi_server.models.google_cloud_apigee_v1_list_environment_groups_response import GoogleCloudApigeeV1ListEnvironmentGroupsResponse
from openapi_server.models.google_cloud_apigee_v1_list_environment_resources_response import GoogleCloudApigeeV1ListEnvironmentResourcesResponse
from openapi_server.models.google_cloud_apigee_v1_list_exports_response import GoogleCloudApigeeV1ListExportsResponse
from openapi_server.models.google_cloud_apigee_v1_list_instance_attachments_response import GoogleCloudApigeeV1ListInstanceAttachmentsResponse
from openapi_server.models.google_cloud_apigee_v1_list_instances_response import GoogleCloudApigeeV1ListInstancesResponse
from openapi_server.models.google_cloud_apigee_v1_list_key_value_entries_response import GoogleCloudApigeeV1ListKeyValueEntriesResponse
from openapi_server.models.google_cloud_apigee_v1_list_nat_addresses_response import GoogleCloudApigeeV1ListNatAddressesResponse
from openapi_server.models.google_cloud_apigee_v1_list_of_developers_response import GoogleCloudApigeeV1ListOfDevelopersResponse
from openapi_server.models.google_cloud_apigee_v1_list_organizations_response import GoogleCloudApigeeV1ListOrganizationsResponse
from openapi_server.models.google_cloud_apigee_v1_list_rate_plans_response import GoogleCloudApigeeV1ListRatePlansResponse
from openapi_server.models.google_cloud_apigee_v1_list_security_actions_response import GoogleCloudApigeeV1ListSecurityActionsResponse
from openapi_server.models.google_cloud_apigee_v1_list_security_incidents_response import GoogleCloudApigeeV1ListSecurityIncidentsResponse
from openapi_server.models.google_cloud_apigee_v1_list_security_profile_revisions_response import GoogleCloudApigeeV1ListSecurityProfileRevisionsResponse
from openapi_server.models.google_cloud_apigee_v1_list_security_profiles_response import GoogleCloudApigeeV1ListSecurityProfilesResponse
from openapi_server.models.google_cloud_apigee_v1_list_security_reports_response import GoogleCloudApigeeV1ListSecurityReportsResponse
from openapi_server.models.google_cloud_apigee_v1_list_shared_flows_response import GoogleCloudApigeeV1ListSharedFlowsResponse
from openapi_server.models.google_cloud_apigee_v1_list_trace_config_overrides_response import GoogleCloudApigeeV1ListTraceConfigOverridesResponse
from openapi_server.models.google_cloud_apigee_v1_nat_address import GoogleCloudApigeeV1NatAddress
from openapi_server.models.google_cloud_apigee_v1_organization import GoogleCloudApigeeV1Organization
from openapi_server.models.google_cloud_apigee_v1_organization_project_mapping import GoogleCloudApigeeV1OrganizationProjectMapping
from openapi_server.models.google_cloud_apigee_v1_query import GoogleCloudApigeeV1Query
from openapi_server.models.google_cloud_apigee_v1_query_tabular_stats_request import GoogleCloudApigeeV1QueryTabularStatsRequest
from openapi_server.models.google_cloud_apigee_v1_query_tabular_stats_response import GoogleCloudApigeeV1QueryTabularStatsResponse
from openapi_server.models.google_cloud_apigee_v1_query_time_series_stats_request import GoogleCloudApigeeV1QueryTimeSeriesStatsRequest
from openapi_server.models.google_cloud_apigee_v1_query_time_series_stats_response import GoogleCloudApigeeV1QueryTimeSeriesStatsResponse
from openapi_server.models.google_cloud_apigee_v1_rate_plan import GoogleCloudApigeeV1RatePlan
from openapi_server.models.google_cloud_apigee_v1_reference import GoogleCloudApigeeV1Reference
from openapi_server.models.google_cloud_apigee_v1_report_instance_status_request import GoogleCloudApigeeV1ReportInstanceStatusRequest
from openapi_server.models.google_cloud_apigee_v1_resource_file import GoogleCloudApigeeV1ResourceFile
from openapi_server.models.google_cloud_apigee_v1_security_action import GoogleCloudApigeeV1SecurityAction
from openapi_server.models.google_cloud_apigee_v1_security_profile import GoogleCloudApigeeV1SecurityProfile
from openapi_server.models.google_cloud_apigee_v1_security_profile_environment_association import GoogleCloudApigeeV1SecurityProfileEnvironmentAssociation
from openapi_server.models.google_cloud_apigee_v1_security_report import GoogleCloudApigeeV1SecurityReport
from openapi_server.models.google_cloud_apigee_v1_security_report_query import GoogleCloudApigeeV1SecurityReportQuery
from openapi_server.models.google_cloud_apigee_v1_set_addon_enablement_request import GoogleCloudApigeeV1SetAddonEnablementRequest
from openapi_server.models.google_cloud_apigee_v1_set_addons_request import GoogleCloudApigeeV1SetAddonsRequest
from openapi_server.models.google_cloud_apigee_v1_shared_flow_revision import GoogleCloudApigeeV1SharedFlowRevision
from openapi_server.models.google_cloud_apigee_v1_subscription import GoogleCloudApigeeV1Subscription
from openapi_server.models.google_cloud_apigee_v1_sync_authorization import GoogleCloudApigeeV1SyncAuthorization
from openapi_server.models.google_cloud_apigee_v1_target_server import GoogleCloudApigeeV1TargetServer
from openapi_server.models.google_cloud_apigee_v1_test_datastore_response import GoogleCloudApigeeV1TestDatastoreResponse
from openapi_server.models.google_cloud_apigee_v1_trace_config_override import GoogleCloudApigeeV1TraceConfigOverride
from openapi_server.models.google_iam_v1_policy import GoogleIamV1Policy
from openapi_server.models.google_iam_v1_set_iam_policy_request import GoogleIamV1SetIamPolicyRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_request import GoogleIamV1TestIamPermissionsRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server import util


async def apigee_organizations_analytics_datastores_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_analytics_datastores_create

    Create a Datastore for an org

    :param parent: Required. The parent organization name. Must be of the form &#x60;organizations/{org}&#x60;.
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
    body = GoogleCloudApigeeV1Datastore.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_analytics_datastores_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, target_type=None) -> web.Response:
    """apigee_organizations_analytics_datastores_list

    List Datastores

    :param parent: Required. The parent organization name. Must be of the form &#x60;organizations/{org}&#x60;.
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
    :param target_type: Optional. TargetType is used to fetch all Datastores that match the type
    :type target_type: str

    """
    return web.Response(status=200)


async def apigee_organizations_analytics_datastores_test(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_analytics_datastores_test

    Test if Datastore configuration is correct. This includes checking if credentials provided by customer have required permissions in target destination storage

    :param parent: Required. The parent organization name Must be of the form &#x60;organizations/{org}&#x60;
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
    body = GoogleCloudApigeeV1Datastore.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_apiproducts_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_apiproducts_create

    Creates an API product in an organization. You create API products after you have proxied backend services using API proxies. An API product is a collection of API resources combined with quota settings and metadata that you can use to deliver customized and productized API bundles to your developer community. This metadata can include: - Scope - Environments - API proxies - Extensible profile API products enable you repackage APIs on the fly, without having to do any additional coding or configuration. Apigee recommends that you start with a simple API product including only required elements. You then provision credentials to apps to enable them to start testing your APIs. After you have authentication and authorization working against a simple API product, you can iterate to create finer-grained API products, defining different sets of API resources for each API product. **WARNING:** - If you don&#39;t specify an API proxy in the request body, *any* app associated with the product can make calls to *any* API in your entire organization. - If you don&#39;t specify an environment in the request body, the product allows access to all environments. For more information, see What is an API product?

    :param parent: Required. Name of the organization in which the API product will be created. Use the following structure in your request: &#x60;organizations/{org}&#x60;
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
    body = GoogleCloudApigeeV1ApiProduct.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_apiproducts_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, attributename=None, attributevalue=None, count=None, expand=None, start_key=None) -> web.Response:
    """apigee_organizations_apiproducts_list

    Lists all API product names for an organization. Filter the list by passing an &#x60;attributename&#x60; and &#x60;attibutevalue&#x60;. The maximum number of API products returned is 1000. You can paginate the list of API products returned using the &#x60;startKey&#x60; and &#x60;count&#x60; query parameters.

    :param parent: Required. Name of the organization. Use the following structure in your request: &#x60;organizations/{org}&#x60;
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
    :param attributename: Name of the attribute used to filter the search.
    :type attributename: str
    :param attributevalue: Value of the attribute used to filter the search.
    :type attributevalue: str
    :param count: Enter the number of API products you want returned in the API call. The limit is 1000.
    :type count: str
    :param expand: Flag that specifies whether to expand the results. Set to &#x60;true&#x60; to get expanded details about each API.
    :type expand: bool
    :param start_key: Gets a list of API products starting with a specific API product in the list. For example, if you&#39;re returning 50 API products at a time (using the &#x60;count&#x60; query parameter), you can view products 50-99 by entering the name of the 50th API product in the first API (without using &#x60;startKey&#x60;). Product name is case sensitive.
    :type start_key: str

    """
    return web.Response(status=200)


async def apigee_organizations_apiproducts_rateplans_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_apiproducts_rateplans_create

    Create a rate plan that is associated with an API product in an organization. Using rate plans, API product owners can monetize their API products by configuring one or more of the following: - Billing frequency - Initial setup fees for using an API product - Payment funding model (postpaid only) - Fixed recurring or consumption-based charges for using an API product - Revenue sharing with developer partners An API product can have multiple rate plans associated with it but *only one* rate plan can be active at any point of time. **Note: From the developer&#39;s perspective, they purchase API products not rate plans.

    :param parent: Required. Name of the API product that is associated with the rate plan. Use the following structure in your request: &#x60;organizations/{org}/apiproducts/{apiproduct}&#x60;
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
    body = GoogleCloudApigeeV1RatePlan.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_apiproducts_rateplans_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, count=None, expand=None, order_by=None, start_key=None, state=None) -> web.Response:
    """apigee_organizations_apiproducts_rateplans_list

    Lists all the rate plans for an API product.

    :param parent: Required. Name of the API product. Use the following structure in your request: &#x60;organizations/{org}/apiproducts/{apiproduct}&#x60; Use &#x60;organizations/{org}/apiproducts/-&#x60; to return rate plans for all API products within the organization.
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
    :param count: Number of rate plans to return in the API call. Use with the &#x60;startKey&#x60; parameter to provide more targeted filtering. The maximum limit is 1000. Defaults to 100.
    :type count: int
    :param expand: Flag that specifies whether to expand the results. Set to &#x60;true&#x60; to get expanded details about each API. Defaults to &#x60;false&#x60;.
    :type expand: bool
    :param order_by: Name of the attribute used for sorting. Valid values include: * &#x60;name&#x60;: Name of the rate plan. * &#x60;state&#x60;: State of the rate plan (&#x60;DRAFT&#x60;, &#x60;PUBLISHED&#x60;). * &#x60;startTime&#x60;: Time when the rate plan becomes active. * &#x60;endTime&#x60;: Time when the rate plan expires. **Note**: Not supported by Apigee at this time.
    :type order_by: str
    :param start_key: Name of the rate plan from which to start displaying the list of rate plans. If omitted, the list starts from the first item. For example, to view the rate plans from 51-150, set the value of &#x60;startKey&#x60; to the name of the 51st rate plan and set the value of &#x60;count&#x60; to 100.
    :type start_key: str
    :param state: State of the rate plans (&#x60;DRAFT&#x60;, &#x60;PUBLISHED&#x60;) that you want to display.
    :type state: str

    """
    return web.Response(status=200)


async def apigee_organizations_apis_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, action=None, name=None, validate=None, body=None) -> web.Response:
    """apigee_organizations_apis_create

    Creates an API proxy. The API proxy created will not be accessible at runtime until it is deployed to an environment. Create a new API proxy by setting the &#x60;name&#x60; query parameter to the name of the API proxy. Import an API proxy configuration bundle stored in zip format on your local machine to your organization by doing the following: * Set the &#x60;name&#x60; query parameter to the name of the API proxy. * Set the &#x60;action&#x60; query parameter to &#x60;import&#x60;. * Set the &#x60;Content-Type&#x60; header to &#x60;multipart/form-data&#x60;. * Pass as a file the name of API proxy configuration bundle stored in zip format on your local machine using the &#x60;file&#x60; form field. **Note**: To validate the API proxy configuration bundle only without importing it, set the &#x60;action&#x60; query parameter to &#x60;validate&#x60;. When importing an API proxy configuration bundle, if the API proxy does not exist, it will be created. If the API proxy exists, then a new revision is created. Invalid API proxy configurations are rejected, and a list of validation errors is returned to the client.

    :param parent: Required. Name of the organization in the following format: &#x60;organizations/{org}&#x60;
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
    :param action: Action to perform when importing an API proxy configuration bundle. Set this parameter to one of the following values: * &#x60;import&#x60; to import the API proxy configuration bundle. * &#x60;validate&#x60; to validate the API proxy configuration bundle without importing it.
    :type action: str
    :param name: Name of the API proxy. Restrict the characters used to: A-Za-z0-9._-
    :type name: str
    :param validate: Ignored. All uploads are validated regardless of the value of this field. Maintained for compatibility with Apigee Edge API.
    :type validate: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleApiHttpBody.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_apis_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_meta_data=None, include_revisions=None) -> web.Response:
    """apigee_organizations_apis_list

    Lists the names of all API proxies in an organization. The names returned correspond to the names defined in the configuration files for each API proxy.

    :param parent: Required. Name of the organization in the following format: &#x60;organizations/{org}&#x60;
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
    :param include_meta_data: Flag that specifies whether to include API proxy metadata in the response.
    :type include_meta_data: bool
    :param include_revisions: Flag that specifies whether to include a list of revisions in the response.
    :type include_revisions: bool

    """
    return web.Response(status=200)


async def apigee_organizations_appgroups_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_appgroups_create

    Creates an AppGroup. Once created, user can register apps under the AppGroup to obtain secret key and password. At creation time, the AppGroup&#39;s state is set as &#x60;active&#x60;.

    :param parent: Required. Name of the Apigee organization in which the AppGroup is created. Use the following structure in your request: &#x60;organizations/{org}&#x60;.
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
    body = GoogleCloudApigeeV1AppGroup.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_appgroups_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_appgroups_list

    Lists all AppGroups in an organization. A maximum of 1000 AppGroups are returned in the response if PageSize is not specified, or if the PageSize is greater than 1000.

    :param parent: Required. Name of the Apigee organization. Use the following structure in your request: &#x60;organizations/{org}&#x60;.
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
    :param filter: The filter expression to be used to get the list of AppGroups, where filtering can be done on status, channelId or channelUri of the app group. Examples: filter&#x3D;status&#x3D;active\&quot;, filter&#x3D;channelId&#x3D;, filter&#x3D;channelUri&#x3D;
    :type filter: str
    :param page_size: Count of AppGroups a single page can have in the response. If unspecified, at most 1000 AppGroups will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: The starting index record for listing the AppGroups.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, parent=None, body=None) -> web.Response:
    """apigee_organizations_create

    Creates an Apigee organization. See [Create an Apigee organization](https://cloud.google.com/apigee/docs/api-platform/get-started/create-org).

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
    :param parent: Required. Name of the Google Cloud project in which to associate the Apigee organization. Pass the information as a query parameter using the following structure in your request: &#x60;projects/&#x60;
    :type parent: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudApigeeV1Organization.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_datacollectors_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, data_collector_id=None, body=None) -> web.Response:
    """apigee_organizations_datacollectors_create

    Creates a new data collector.

    :param parent: Required. Name of the organization in which to create the data collector in the following format: &#x60;organizations/{org}&#x60;.
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
    :param data_collector_id: ID of the data collector. Overrides any ID in the data collector resource. Must be a string beginning with &#x60;dc_&#x60; that contains only letters, numbers, and underscores.
    :type data_collector_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudApigeeV1DataCollector.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_datacollectors_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_datacollectors_list

    Lists all data collectors.

    :param parent: Required. Name of the organization for which to list data collectors in the following format: &#x60;organizations/{org}&#x60;.
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
    :param page_size: Maximum number of data collectors to return. The page size defaults to 25.
    :type page_size: int
    :param page_token: Page token, returned from a previous ListDataCollectors call, that you can use to retrieve the next page.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_developers_apps_attributes(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_developers_apps_attributes

    Updates attributes for a developer app. This API replaces the current attributes with those specified in the request.

    :param name: Required. Name of the developer app. Use the following structure in your request: &#x60;organizations/{org}/developers/{developer_email}/apps/{app}&#x60;
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
    body = GoogleCloudApigeeV1Attributes.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_developers_apps_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_developers_apps_create

    Creates an app associated with a developer. This API associates the developer app with the specified API product and auto-generates an API key for the app to use in calls to API proxies inside that API product. The &#x60;name&#x60; is the unique ID of the app that you can use in API calls. The &#x60;DisplayName&#x60; (set as an attribute) appears in the UI. If you don&#39;t set the &#x60;DisplayName&#x60; attribute, the &#x60;name&#x60; appears in the UI.

    :param parent: Required. Name of the developer. Use the following structure in your request: &#x60;organizations/{org}/developers/{developer_email}&#x60;
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
    body = GoogleCloudApigeeV1DeveloperApp.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_developers_apps_keys_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_developers_apps_keys_create

    Creates a custom consumer key and secret for a developer app. This is particularly useful if you want to migrate existing consumer keys and secrets to Apigee from another system. Consumer keys and secrets can contain letters, numbers, underscores, and hyphens. No other special characters are allowed. To avoid service disruptions, a consumer key and secret should not exceed 2 KBs each. **Note**: When creating the consumer key and secret, an association to API products will not be made. Therefore, you should not specify the associated API products in your request. Instead, use the UpdateDeveloperAppKey API to make the association after the consumer key and secret are created. If a consumer key and secret already exist, you can keep them or delete them using the DeleteDeveloperAppKey API. **Note**: All keys start out with status&#x3D;approved, even if status&#x3D;revoked is passed when the key is created. To revoke a key, use the UpdateDeveloperAppKey API.

    :param parent: Parent of the developer app key. Use the following structure in your request: &#39;organizations/{org}/developers/{developerEmail}/apps/{appName}&#39;
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
    body = GoogleCloudApigeeV1DeveloperAppKey.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_developers_apps_keys_create_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_developers_apps_keys_create_create

    Creates a custom consumer key and secret for a developer app. This is particularly useful if you want to migrate existing consumer keys and secrets to Apigee from another system. Consumer keys and secrets can contain letters, numbers, underscores, and hyphens. No other special characters are allowed. To avoid service disruptions, a consumer key and secret should not exceed 2 KBs each. **Note**: When creating the consumer key and secret, an association to API products will not be made. Therefore, you should not specify the associated API products in your request. Instead, use the UpdateDeveloperAppKey API to make the association after the consumer key and secret are created. If a consumer key and secret already exist, you can keep them or delete them using the DeleteDeveloperAppKey API. **Note**: All keys start out with status&#x3D;approved, even if status&#x3D;revoked is passed when the key is created. To revoke a key, use the UpdateDeveloperAppKey API.

    :param parent: Parent of the developer app key. Use the following structure in your request: &#39;organizations/{org}/developers/{developerEmail}/apps/{appName}&#39;
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
    body = GoogleCloudApigeeV1DeveloperAppKey.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_developers_apps_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, count=None, expand=None, shallow_expand=None, start_key=None, ids=None, include_cred=None, key_status=None, page_size=None, page_token=None, rows=None, status=None) -> web.Response:
    """apigee_organizations_developers_apps_list

    Lists all apps created by a developer in an Apigee organization. Optionally, you can request an expanded view of the developer apps. A maximum of 100 developer apps are returned per API call. You can paginate the list of deveoper apps returned using the &#x60;startKey&#x60; and &#x60;count&#x60; query parameters.

    :param parent: Required. Name of the developer. Use the following structure in your request: &#x60;organizations/{org}/developers/{developer_email}&#x60;
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
    :param count: Number of developer apps to return in the API call. Use with the &#x60;startKey&#x60; parameter to provide more targeted filtering. The limit is 1000.
    :type count: str
    :param expand: Optional. Specifies whether to expand the results. Set to &#x60;true&#x60; to expand the results. This query parameter is not valid if you use the &#x60;count&#x60; or &#x60;startKey&#x60; query parameters.
    :type expand: bool
    :param shallow_expand: Optional. Specifies whether to expand the results in shallow mode. Set to &#x60;true&#x60; to expand the results in shallow mode.
    :type shallow_expand: bool
    :param start_key: **Note**: Must be used in conjunction with the &#x60;count&#x60; parameter. Name of the developer app from which to start displaying the list of developer apps. For example, if you&#39;re returning 50 developer apps at a time (using the &#x60;count&#x60; query parameter), you can view developer apps 50-99 by entering the name of the 50th developer app. The developer app name is case sensitive.
    :type start_key: str
    :param ids: Optional. Comma-separated list of app IDs on which to filter.
    :type ids: str
    :param include_cred: Optional. Flag that specifies whether to include credentials in the response.
    :type include_cred: bool
    :param key_status: Optional. Key status of the app. Valid values include &#x60;approved&#x60; or &#x60;revoked&#x60;. Defaults to &#x60;approved&#x60;.
    :type key_status: str
    :param page_size: Optional. Count of apps a single page can have in the response. If unspecified, at most 100 apps will be returned. The maximum value is 100; values above 100 will be coerced to 100. \&quot;page_size\&quot; is supported from ver 1.10.0 and above.
    :type page_size: int
    :param page_token: Optional. The starting index record for listing the developers. \&quot;page_token\&quot; is supported from ver 1.10.0 and above.
    :type page_token: str
    :param rows: Optional. Maximum number of app IDs to return. Defaults to 10000.
    :type rows: str
    :param status: Optional. Filter by the status of the app. Valid values are &#x60;approved&#x60; or &#x60;revoked&#x60;. Defaults to &#x60;approved&#x60;.
    :type status: str

    """
    return web.Response(status=200)


async def apigee_organizations_developers_attributes(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_developers_attributes

    Updates developer attributes. This API replaces the existing attributes with those specified in the request. Add new attributes, and include or exclude any existing attributes that you want to retain or remove, respectively. The custom attribute limit is 18. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (default). Any custom attributes associated with these entities are cached for at least 180 seconds after the entity is accessed at runtime. Therefore, an &#x60;ExpiresIn&#x60; element on the OAuthV2 policy won&#39;t be able to expire an access token in less than 180 seconds.

    :param parent: Required. Email address of the developer for which attributes are being updated. Use the following structure in your request: &#x60;organizations/{org}/developers/{developer_email}&#x60;
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
    body = GoogleCloudApigeeV1Attributes.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_developers_attributes_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_developers_attributes_list

    Returns a list of all developer attributes.

    :param parent: Required. Email address of the developer for which attributes are being listed. Use the following structure in your request: &#x60;organizations/{org}/developers/{developer_email}&#x60;
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


async def apigee_organizations_developers_balance_adjust(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_developers_balance_adjust

    Adjust the prepaid balance for the developer. This API will be used in scenarios where the developer has been under-charged or over-charged.

    :param name: Required. Account balance for the developer. Use the following structure in your request: &#x60;organizations/{org}/developers/{developer}/balance&#x60;
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
    body = GoogleCloudApigeeV1AdjustDeveloperBalanceRequest.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_developers_balance_credit(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_developers_balance_credit

    Credits the account balance for the developer.

    :param name: Required. Account balance for the developer. Use the following structure in your request: &#x60;organizations/{org}/developers/{developer}/balance&#x60;
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
    body = GoogleCloudApigeeV1CreditDeveloperBalanceRequest.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_developers_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_developers_create

    Creates a developer. Once created, the developer can register an app and obtain an API key. At creation time, a developer is set as &#x60;active&#x60;. To change the developer status, use the SetDeveloperStatus API.

    :param parent: Required. Name of the Apigee organization in which the developer is created. Use the following structure in your request: &#x60;organizations/{org}&#x60;.
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
    body = GoogleCloudApigeeV1Developer.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_developers_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, app=None, count=None, expand=None, ids=None, include_company=None, start_key=None) -> web.Response:
    """apigee_organizations_developers_list

    Lists all developers in an organization by email address. By default, the response does not include company developers. Set the &#x60;includeCompany&#x60; query parameter to &#x60;true&#x60; to include company developers. **Note**: A maximum of 1000 developers are returned in the response. You paginate the list of developers returned using the &#x60;startKey&#x60; and &#x60;count&#x60; query parameters.

    :param parent: Required. Name of the Apigee organization. Use the following structure in your request: &#x60;organizations/{org}&#x60;.
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
    :param app: Optional. List only Developers that are associated with the app. Note that start_key, count are not applicable for this filter criteria.
    :type app: str
    :param count: Optional. Number of developers to return in the API call. Use with the &#x60;startKey&#x60; parameter to provide more targeted filtering. The limit is 1000.
    :type count: str
    :param expand: Specifies whether to expand the results. Set to &#x60;true&#x60; to expand the results. This query parameter is not valid if you use the &#x60;count&#x60; or &#x60;startKey&#x60; query parameters.
    :type expand: bool
    :param ids: Optional. List of IDs to include, separated by commas.
    :type ids: str
    :param include_company: Flag that specifies whether to include company details in the response.
    :type include_company: bool
    :param start_key: **Note**: Must be used in conjunction with the &#x60;count&#x60; parameter. Email address of the developer from which to start displaying the list of developers. For example, if the an unfiltered list returns: &#x60;&#x60;&#x60; westley@example.com fezzik@example.com buttercup@example.com &#x60;&#x60;&#x60; and your &#x60;startKey&#x60; is &#x60;fezzik@example.com&#x60;, the list returned will be &#x60;&#x60;&#x60; fezzik@example.com buttercup@example.com &#x60;&#x60;&#x60;
    :type start_key: str

    """
    return web.Response(status=200)


async def apigee_organizations_developers_subscriptions_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_developers_subscriptions_create

    Creates a subscription to an API product. 

    :param parent: Required. Email address of the developer that is purchasing a subscription to the API product. Use the following structure in your request: &#x60;organizations/{org}/developers/{developer_email}&#x60;
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
    body = GoogleCloudApigeeV1DeveloperSubscription.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_developers_subscriptions_expire(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_developers_subscriptions_expire

    Expires an API product subscription immediately.

    :param name: Required. Name of the API product subscription. Use the following structure in your request: &#x60;organizations/{org}/developers/{developer_email}/subscriptions/{subscription}&#x60;
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


async def apigee_organizations_developers_subscriptions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, count=None, start_key=None) -> web.Response:
    """apigee_organizations_developers_subscriptions_list

    Lists all API product subscriptions for a developer.

    :param parent: Required. Email address of the developer. Use the following structure in your request: &#x60;organizations/{org}/developers/{developer_email}&#x60;
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
    :param count: Number of API product subscriptions to return in the API call. Use with &#x60;startKey&#x60; to provide more targeted filtering. Defaults to 100. The maximum limit is 1000.
    :type count: int
    :param start_key: Name of the API product subscription from which to start displaying the list of subscriptions. If omitted, the list starts from the first item. For example, to view the API product subscriptions from 51-150, set the value of &#x60;startKey&#x60; to the name of the 51st subscription and set the value of &#x60;count&#x60; to 100.
    :type start_key: str

    """
    return web.Response(status=200)


async def apigee_organizations_endpoint_attachments_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, endpoint_attachment_id=None, body=None) -> web.Response:
    """apigee_organizations_endpoint_attachments_create

    Creates an endpoint attachment. **Note:** Not supported for Apigee hybrid.

    :param parent: Required. Organization the endpoint attachment will be created in.
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
    :param endpoint_attachment_id: ID to use for the endpoint attachment. ID must start with a lowercase letter followed by up to 31 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. The minimum length is 2.
    :type endpoint_attachment_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudApigeeV1EndpointAttachment.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_endpoint_attachments_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_endpoint_attachments_list

    Lists the endpoint attachments in an organization.

    :param parent: Required. Name of the organization for which to list endpoint attachments. Use the following structure in your request: &#x60;organizations/{org}&#x60;
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
    :param page_size: Optional. Maximum number of endpoint attachments to return. If unspecified, at most 25 attachments will be returned.
    :type page_size: int
    :param page_token: Optional. Page token, returned from a previous &#x60;ListEndpointAttachments&#x60; call, that you can use to retrieve the next page.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_envgroups_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, name=None, body=None) -> web.Response:
    """apigee_organizations_envgroups_create

    Creates a new environment group.

    :param parent: Required. Name of the organization in which to create the environment group in the following format: &#x60;organizations/{org}&#x60;.
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
    :param name: Optional. ID of the environment group. Overrides any ID in the environment_group resource.
    :type name: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudApigeeV1EnvironmentGroup.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_envgroups_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_envgroups_list

    Lists all environment groups.

    :param parent: Required. Name of the organization for which to list environment groups in the following format: &#x60;organizations/{org}&#x60;.
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
    :param page_size: Maximum number of environment groups to return. The page size defaults to 25.
    :type page_size: int
    :param page_token: Page token, returned from a previous ListEnvironmentGroups call, that you can use to retrieve the next page.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_environments_addons_config_set_addon_enablement(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_addons_config_set_addon_enablement

    Updates an add-on enablement status of an environment.

    :param name: Required. Name of the add-ons config. Must be in the format of &#x60;/organizations/{org}/environments/{env}/addonsConfig&#x60;
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
    body = GoogleCloudApigeeV1SetAddonEnablementRequest.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_analytics_exports_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_analytics_exports_create

    Submit a data export job to be processed in the background. If the request is successful, the API returns a 201 status, a URI that can be used to retrieve the status of the export job, and the &#x60;state&#x60; value of \&quot;enqueued\&quot;.

    :param parent: Required. Names of the parent organization and environment. Must be of the form &#x60;organizations/{org}/environments/{env}&#x60;.
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
    body = GoogleCloudApigeeV1ExportRequest.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_analytics_exports_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_environments_analytics_exports_list

    Lists the details and status of all analytics export jobs belonging to the parent organization and environment.

    :param parent: Required. Names of the parent organization and environment. Must be of the form &#x60;organizations/{org}/environments/{env}&#x60;.
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


async def apigee_organizations_environments_apis_revisions_debugsessions_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, timeout=None, body=None) -> web.Response:
    """apigee_organizations_environments_apis_revisions_debugsessions_create

    Creates a debug session for a deployed API Proxy revision.

    :param parent: Required. The resource name of the API Proxy revision deployment for which to create the DebugSession. Must be of the form &#x60;organizations/{organization}/environments/{environment}/apis/{api}/revisions/{revision}&#x60;.
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
    :param timeout: Optional. The time in seconds after which this DebugSession should end. A timeout specified in DebugSession will overwrite this value.
    :type timeout: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudApigeeV1DebugSession.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_apis_revisions_debugsessions_delete_data(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_environments_apis_revisions_debugsessions_delete_data

    Deletes the data from a debug session. This does not cancel the debug session or prevent further data from being collected if the session is still active in runtime pods.

    :param name: Required. The name of the debug session to delete. Must be of the form: &#x60;organizations/{organization}/environments/{environment}/apis/{api}/revisions/{revision}/debugsessions/{debugsession}&#x60;.
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


async def apigee_organizations_environments_apis_revisions_debugsessions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_environments_apis_revisions_debugsessions_list

    Lists debug sessions that are currently active in the given API Proxy revision.

    :param parent: Required. The name of the API Proxy revision deployment for which to list debug sessions. Must be of the form: &#x60;organizations/{organization}/environments/{environment}/apis/{api}/revisions/{revision}&#x60;.
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
    :param page_size: Maximum number of debug sessions to return. The page size defaults to 25.
    :type page_size: int
    :param page_token: Page token, returned from a previous ListDebugSessions call, that you can use to retrieve the next page.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_environments_apis_revisions_deployments_generate_deploy_change_report(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, override=None) -> web.Response:
    """apigee_organizations_environments_apis_revisions_deployments_generate_deploy_change_report

    Generates a report for a dry run analysis of a DeployApiProxy request without committing the deployment. In addition to the standard validations performed when adding deployments, additional analysis will be done to detect possible traffic routing changes that would result from this deployment being created. Any potential routing conflicts or unsafe changes will be reported in the response. This routing analysis is not performed for a non-dry-run DeployApiProxy request. For a request path &#x60;organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/deployments:generateDeployChangeReport&#x60;, two permissions are required: * &#x60;apigee.deployments.create&#x60; on the resource &#x60;organizations/{org}/environments/{env}&#x60; * &#x60;apigee.proxyrevisions.deploy&#x60; on the resource &#x60;organizations/{org}/apis/{api}/revisions/{rev}&#x60;

    :param name: Name of the API proxy revision deployment in the following format: &#x60;organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}&#x60;
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
    :param override: Flag that specifies whether to force the deployment of the new revision over the currently deployed revision by overriding conflict checks.
    :type override: bool

    """
    return web.Response(status=200)


async def apigee_organizations_environments_apis_revisions_deployments_generate_undeploy_change_report(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_environments_apis_revisions_deployments_generate_undeploy_change_report

    Generates a report for a dry run analysis of an UndeployApiProxy request without committing the undeploy. In addition to the standard validations performed when removing deployments, additional analysis will be done to detect possible traffic routing changes that would result from this deployment being removed. Any potential routing conflicts or unsafe changes will be reported in the response. This routing analysis is not performed for a non-dry-run UndeployApiProxy request. For a request path &#x60;organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/deployments:generateUndeployChangeReport&#x60;, two permissions are required: * &#x60;apigee.deployments.delete&#x60; on the resource &#x60;organizations/{org}/environments/{env}&#x60; * &#x60;apigee.proxyrevisions.undeploy&#x60; on the resource &#x60;organizations/{org}/apis/{api}/revisions/{rev}&#x60;

    :param name: Name of the API proxy revision deployment in the following format: &#x60;organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}&#x60;
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


async def apigee_organizations_environments_archive_deployments_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_archive_deployments_create

    Creates a new ArchiveDeployment.

    :param parent: Required. The Environment this Archive Deployment will be created in.
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
    body = GoogleCloudApigeeV1ArchiveDeployment.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_archive_deployments_generate_download_url(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_archive_deployments_generate_download_url

    Generates a signed URL for downloading the original zip file used to create an Archive Deployment. The URL is only valid for a limited period and should be used within minutes after generation. Each call returns a new upload URL.

    :param name: Required. The name of the Archive Deployment you want to download.
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


async def apigee_organizations_environments_archive_deployments_generate_upload_url(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_archive_deployments_generate_upload_url

    Generates a signed URL for uploading an Archive zip file to Google Cloud Storage. Once the upload is complete, the signed URL should be passed to CreateArchiveDeployment. When uploading to the generated signed URL, please follow these restrictions: * Source file type should be a zip file. * Source file size should not exceed 1GB limit. * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL. When making a HTTP PUT request, these two headers need to be specified: * &#x60;content-type: application/zip&#x60; * &#x60;x-goog-content-length-range: 0,1073741824&#x60; And this header SHOULD NOT be specified: * &#x60;Authorization: Bearer YOUR_TOKEN&#x60;

    :param parent: Required. The organization and environment to upload to.
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
    :type body: 

    """
    return web.Response(status=200)


async def apigee_organizations_environments_archive_deployments_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_environments_archive_deployments_list

    Lists the ArchiveDeployments in the specified Environment.

    :param parent: Required. Name of the Environment for which to list Archive Deployments in the format: &#x60;organizations/{org}/environments/{env}&#x60;.
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
    :param filter: Optional. An optional query used to return a subset of Archive Deployments using the semantics defined in https://google.aip.dev/160.
    :type filter: str
    :param page_size: Optional. Maximum number of Archive Deployments to return. If unspecified, at most 25 deployments will be returned.
    :type page_size: int
    :param page_token: Optional. Page token, returned from a previous ListArchiveDeployments call, that you can use to retrieve the next page.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_environments_get_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, options_requested_policy_version=None) -> web.Response:
    """apigee_organizations_environments_get_iam_policy

    Gets the IAM policy on an environment. For more information, see [Manage users, roles, and permissions using the API](https://cloud.google.com/apigee/docs/api-platform/system-administration/manage-users-roles). You must have the &#x60;apigee.environments.getIamPolicy&#x60; permission to call this API.

    :param resource: REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
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
    :param options_requested_policy_version: Optional. The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).
    :type options_requested_policy_version: int

    """
    return web.Response(status=200)


async def apigee_organizations_environments_keystores_aliases_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, password=None, alias=None, format=None, ignore_expiry_validation=None, ignore_newline_validation=None, body=None) -> web.Response:
    """apigee_organizations_environments_keystores_aliases_create

    Creates an alias from a key/certificate pair. The structure of the request is controlled by the &#x60;format&#x60; query parameter: - &#x60;keycertfile&#x60; - Separate PEM-encoded key and certificate files are uploaded. Set &#x60;Content-Type: multipart/form-data&#x60; and include the &#x60;keyFile&#x60;, &#x60;certFile&#x60;, and &#x60;password&#x60; (if keys are encrypted) fields in the request body. If uploading to a truststore, omit &#x60;keyFile&#x60;. - &#x60;pkcs12&#x60; - A PKCS12 file is uploaded. Set &#x60;Content-Type: multipart/form-data&#x60;, provide the file in the &#x60;file&#x60; field, and include the &#x60;password&#x60; field if the file is encrypted in the request body. - &#x60;selfsignedcert&#x60; - A new private key and certificate are generated. Set &#x60;Content-Type: application/json&#x60; and include CertificateGenerationSpec in the request body.

    :param parent: Required. Name of the keystore. Use the following format in your request: &#x60;organizations/{org}/environments/{env}/keystores/{keystore}&#x60;.
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
    :param password: DEPRECATED: For improved security, specify the password in the request body instead of using the query parameter. To specify the password in the request body, set &#x60;Content-type: multipart/form-data&#x60; part with name &#x60;password&#x60;. Password for the private key file, if required.
    :type password: str
    :param alias: Alias for the key/certificate pair. Values must match the regular expression &#x60;[\\w\\s-.]{1,255}&#x60;. This must be provided for all formats except &#x60;selfsignedcert&#x60;; self-signed certs may specify the alias in either this parameter or the JSON body.
    :type alias: str
    :param format: Required. Format of the data. Valid values include: &#x60;selfsignedcert&#x60;, &#x60;keycertfile&#x60;, or &#x60;pkcs12&#x60;
    :type format: str
    :param ignore_expiry_validation: Flag that specifies whether to ignore expiry validation. If set to &#x60;true&#x60;, no expiry validation will be performed.
    :type ignore_expiry_validation: bool
    :param ignore_newline_validation: Flag that specifies whether to ignore newline validation. If set to &#x60;true&#x60;, no error is thrown when the file contains a certificate chain with no newline between each certificate. Defaults to &#x60;false&#x60;.
    :type ignore_newline_validation: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleApiHttpBody.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_keystores_aliases_csr(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_environments_keystores_aliases_csr

    Generates a PKCS #10 Certificate Signing Request for the private key in an alias.

    :param name: Required. Name of the alias. Use the following format in your request: &#x60;organizations/{org}/environments/{env}/keystores/{keystore}/aliases/{alias}&#x60;.
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


async def apigee_organizations_environments_keystores_aliases_get_certificate(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_environments_keystores_aliases_get_certificate

    Gets the certificate from an alias in PEM-encoded form.

    :param name: Required. Name of the alias. Use the following format in your request: &#x60;organizations/{org}/environments/{env}/keystores/{keystore}/aliases/{alias}&#x60;.
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


async def apigee_organizations_environments_keystores_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, name=None, body=None) -> web.Response:
    """apigee_organizations_environments_keystores_create

    Creates a keystore or truststore. - Keystore: Contains certificates and their associated keys. - Truststore: Contains trusted certificates used to validate a server&#39;s certificate. These certificates are typically self-signed certificates or certificates that are not signed by a trusted CA.

    :param parent: Required. Name of the environment in which to create the keystore. Use the following format in your request: &#x60;organizations/{org}/environments/{env}&#x60;
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
    :param name: Optional. Name of the keystore. Overrides the value in Keystore.
    :type name: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudApigeeV1Keystore.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_queries_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_queries_create

    Submit a query to be processed in the background. If the submission of the query succeeds, the API returns a 201 status and an ID that refer to the query. In addition to the HTTP status 201, the &#x60;state&#x60; of \&quot;enqueued\&quot; means that the request succeeded.

    :param parent: Required. The parent resource name. Must be of the form &#x60;organizations/{org}/environments/{env}&#x60;.
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
    body = GoogleCloudApigeeV1Query.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_queries_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, dataset=None, _from=None, incl_queries_without_report=None, status=None, submitted_by=None, to=None) -> web.Response:
    """apigee_organizations_environments_queries_list

    Return a list of Asynchronous Queries

    :param parent: Required. The parent resource name. Must be of the form &#x60;organizations/{org}/environments/{env}&#x60;.
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
    :param dataset: Filter response list by dataset. Example: &#x60;api&#x60;, &#x60;mint&#x60;
    :type dataset: str
    :param _from: Filter response list by returning asynchronous queries that created after this date time. Time must be in ISO date-time format like &#39;2011-12-03T10:15:30Z&#39;.
    :type _from: str
    :param incl_queries_without_report: Flag to include asynchronous queries that don&#39;t have a report denifition.
    :type incl_queries_without_report: str
    :param status: Filter response list by asynchronous query status.
    :type status: str
    :param submitted_by: Filter response list by user who submitted queries.
    :type submitted_by: str
    :param to: Filter response list by returning asynchronous queries that created before this date time. Time must be in ISO date-time format like &#39;2011-12-03T10:16:30Z&#39;.
    :type to: str

    """
    return web.Response(status=200)


async def apigee_organizations_environments_references_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_references_create

    Creates a Reference in the specified environment.

    :param parent: Required. The parent environment name under which the Reference will be created. Must be of the form &#x60;organizations/{org}/environments/{env}&#x60;.
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
    body = GoogleCloudApigeeV1Reference.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_resourcefiles_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, name=None, type=None, body=None) -> web.Response:
    """apigee_organizations_environments_resourcefiles_create

    Creates a resource file. Specify the &#x60;Content-Type&#x60; as &#x60;application/octet-stream&#x60; or &#x60;multipart/form-data&#x60;. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files).

    :param parent: Required. Name of the environment in which to create the resource file in the following format: &#x60;organizations/{org}/environments/{env}&#x60;.
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
    :param name: Required. Name of the resource file. Must match the regular expression: [a-zA-Z0-9:/\\\\!@#$%^&amp;{}\\[\\]()+\\-&#x3D;,.~&#39;&#x60; ]{1,255}
    :type name: str
    :param type: Required. Resource file type. {{ resource_file_type }}
    :type type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleApiHttpBody.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_resourcefiles_delete(request: web.Request, parent, type, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_environments_resourcefiles_delete

    Deletes a resource file. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files).

    :param parent: Required. Name of the environment in the following format: &#x60;organizations/{org}/environments/{env}&#x60;.
    :type parent: str
    :param type: Required. Resource file type. {{ resource_file_type }}
    :type type: str
    :param name: Required. ID of the resource file to delete. Must match the regular expression: [a-zA-Z0-9:/\\\\!@#$%^&amp;{}\\[\\]()+\\-&#x3D;,.~&#39;&#x60; ]{1,255}
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


async def apigee_organizations_environments_resourcefiles_get(request: web.Request, parent, type, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_environments_resourcefiles_get

    Gets the contents of a resource file. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files).

    :param parent: Required. Name of the environment in the following format: &#x60;organizations/{org}/environments/{env}&#x60;.
    :type parent: str
    :param type: Required. Resource file type. {{ resource_file_type }}
    :type type: str
    :param name: Required. ID of the resource file. Must match the regular expression: [a-zA-Z0-9:/\\\\!@#$%^&amp;{}\\[\\]()+\\-&#x3D;,.~&#39;&#x60; ]{1,255}
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


async def apigee_organizations_environments_resourcefiles_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, type=None) -> web.Response:
    """apigee_organizations_environments_resourcefiles_list

    Lists all resource files, optionally filtering by type. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files).

    :param parent: Required. Name of the environment in which to list resource files in the following format: &#x60;organizations/{org}/environments/{env}&#x60;.
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
    :param type: Optional. Type of resource files to list. {{ resource_file_type }}
    :type type: str

    """
    return web.Response(status=200)


async def apigee_organizations_environments_resourcefiles_list_environment_resources(request: web.Request, parent, type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_environments_resourcefiles_list_environment_resources

    Lists all resource files, optionally filtering by type. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files).

    :param parent: Required. Name of the environment in which to list resource files in the following format: &#x60;organizations/{org}/environments/{env}&#x60;.
    :type parent: str
    :param type: Optional. Type of resource files to list. {{ resource_file_type }}
    :type type: str
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


async def apigee_organizations_environments_resourcefiles_update(request: web.Request, parent, type, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_resourcefiles_update

    Updates a resource file. Specify the &#x60;Content-Type&#x60; as &#x60;application/octet-stream&#x60; or &#x60;multipart/form-data&#x60;. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files).

    :param parent: Required. Name of the environment in the following format: &#x60;organizations/{org}/environments/{env}&#x60;.
    :type parent: str
    :param type: Required. Resource file type. {{ resource_file_type }}
    :type type: str
    :param name: Required. ID of the resource file to update. Must match the regular expression: [a-zA-Z0-9:/\\\\!@#$%^&amp;{}\\[\\]()+\\-&#x3D;,.~&#39;&#x60; ]{1,255}
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
    body = GoogleApiHttpBody.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_security_actions_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, security_action_id=None, body=None) -> web.Response:
    """apigee_organizations_environments_security_actions_create

    CreateSecurityAction creates a SecurityAction.

    :param parent: Required. The organization and environment that this SecurityAction applies to. Format: organizations/{org}/environments/{env}
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
    :param security_action_id: Required. The ID to use for the SecurityAction, which will become the final component of the action&#39;s resource name. This value should be 0-61 characters, and valid format is (^[a-z]([a-z0-9-]{​0,61}[a-z0-9])?$).
    :type security_action_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudApigeeV1SecurityAction.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_security_actions_disable(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_security_actions_disable

    Disable a SecurityAction. The &#x60;state&#x60; of the SecurityAction after disabling is &#x60;DISABLED&#x60;. &#x60;DisableSecurityAction&#x60; can be called on SecurityActions in the state &#x60;ENABLED&#x60;; SecurityActions in a different state (including &#x60;DISABLED&#x60;) return an error.

    :param name: Required. The name of the SecurityAction to disable. Format: organizations/{org}/environments/{env}/securityActions/{security_action}
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


async def apigee_organizations_environments_security_actions_enable(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_security_actions_enable

    Enable a SecurityAction. The &#x60;state&#x60; of the SecurityAction after enabling is &#x60;ENABLED&#x60;. &#x60;EnableSecurityAction&#x60; can be called on SecurityActions in the state &#x60;DISABLED&#x60;; SecurityActions in a different state (including &#x60;ENABLED) return an error.

    :param name: Required. The name of the SecurityAction to enable. Format: organizations/{org}/environments/{env}/securityActions/{security_action}
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


async def apigee_organizations_environments_security_actions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_environments_security_actions_list

    Returns a list of SecurityActions. This returns both enabled and disabled actions.

    :param parent: Required. The parent, which owns this collection of SecurityActions. Format: organizations/{org}/environments/{env}
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
    :param filter: The filter expression to filter List results. https://google.aip.dev/160. Allows for filtering over: state and api_proxies. E.g.: state &#x3D; ACTIVE AND apiProxies:foo. Filtering by action is not supported https://github.com/aip-dev/google.aip.dev/issues/624
    :type filter: str
    :param page_size: The maximum number of SecurityActions to return. If unspecified, at most 50 SecurityActions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListSecurityActions&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListSecurityActions&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_environments_security_incidents_batch_update(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_security_incidents_batch_update

    BatchUpdateSecurityIncident updates multiple existing security incidents.

    :param parent: Optional. The parent resource shared by all security incidents being updated. If this is set, the parent field in the UpdateSecurityIncidentRequest messages must either be empty or match this field.
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
    body = GoogleCloudApigeeV1BatchUpdateSecurityIncidentsRequest.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_security_incidents_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_environments_security_incidents_list

    ListSecurityIncidents lists all the security incident associated with the environment.

    :param parent: Required. For a specific organization, list of all the security incidents. Format: &#x60;organizations/{org}/environments/{environment}&#x60;
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
    :param filter: The filter expression to be used to get the list of security incidents, where filtering can be done on API Proxies. Example: filter &#x3D; \&quot;api_proxy &#x3D; /\&quot;, \&quot;first_detected_time &gt;\&quot;, \&quot;last_detected_time &lt;\&quot;
    :type filter: str
    :param page_size: Optional. The maximum number of incidents to return. The service may return fewer than this value. If unspecified, at most 50 incidents will be returned.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListSecurityIncident&#x60; call. Provide this to retrieve the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_environments_security_reports_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_security_reports_create

    Submit a report request to be processed in the background. If the submission succeeds, the API returns a 200 status and an ID that refer to the report request. In addition to the HTTP status 200, the &#x60;state&#x60; of \&quot;enqueued\&quot; means that the request succeeded.

    :param parent: Required. The parent resource name. Must be of the form &#x60;organizations/{org}/environments/{env}&#x60;.
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
    body = GoogleCloudApigeeV1SecurityReportQuery.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_security_reports_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, dataset=None, _from=None, page_size=None, page_token=None, status=None, submitted_by=None, to=None) -> web.Response:
    """apigee_organizations_environments_security_reports_list

    Return a list of Security Reports

    :param parent: Required. The parent resource name. Must be of the form &#x60;organizations/{org}/environments/{env}&#x60;.
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
    :param dataset: Filter response list by dataset. Example: &#x60;api&#x60;, &#x60;mint&#x60;
    :type dataset: str
    :param _from: Filter response list by returning security reports that created after this date time. Time must be in ISO date-time format like &#39;2011-12-03T10:15:30Z&#39;.
    :type _from: str
    :param page_size: The maximum number of security report to return in the list response.
    :type page_size: int
    :param page_token: Token returned from the previous list response to fetch the next page.
    :type page_token: str
    :param status: Filter response list by security reports status.
    :type status: str
    :param submitted_by: Filter response list by user who submitted queries.
    :type submitted_by: str
    :param to: Filter response list by returning security reports that created before this date time. Time must be in ISO date-time format like &#39;2011-12-03T10:16:30Z&#39;.
    :type to: str

    """
    return web.Response(status=200)


async def apigee_organizations_environments_security_stats_query_tabular_stats(request: web.Request, orgenv, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_security_stats_query_tabular_stats

    Retrieve security statistics as tabular rows.

    :param orgenv: Required. Should be of the form organizations//environments/.
    :type orgenv: str
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
    body = GoogleCloudApigeeV1QueryTabularStatsRequest.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_security_stats_query_time_series_stats(request: web.Request, orgenv, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_security_stats_query_time_series_stats

    Retrieve security statistics as a collection of time series.

    :param orgenv: Required. Should be of the form organizations//environments/.
    :type orgenv: str
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
    body = GoogleCloudApigeeV1QueryTimeSeriesStatsRequest.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_set_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_set_iam_policy

    Sets the IAM policy on an environment, if the policy already exists it will be replaced. For more information, see [Manage users, roles, and permissions using the API](https://cloud.google.com/apigee/docs/api-platform/system-administration/manage-users-roles). You must have the &#x60;apigee.environments.setIamPolicy&#x60; permission to call this API.

    :param resource: REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
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
    body = GoogleIamV1SetIamPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_sharedflows_revisions_deploy(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, override=None, service_account=None) -> web.Response:
    """apigee_organizations_environments_sharedflows_revisions_deploy

    Deploys a revision of a shared flow. If another revision of the same shared flow is currently deployed, set the &#x60;override&#x60; parameter to &#x60;true&#x60; to have this revision replace the currently deployed revision. You cannot use a shared flow until it has been deployed to an environment. For a request path &#x60;organizations/{org}/environments/{env}/sharedflows/{sf}/revisions/{rev}/deployments&#x60;, two permissions are required: * &#x60;apigee.deployments.create&#x60; on the resource &#x60;organizations/{org}/environments/{env}&#x60; * &#x60;apigee.sharedflowrevisions.deploy&#x60; on the resource &#x60;organizations/{org}/sharedflows/{sf}/revisions/{rev}&#x60;

    :param name: Required. Name of the shared flow revision to deploy in the following format: &#x60;organizations/{org}/environments/{env}/sharedflows/{sharedflow}/revisions/{rev}&#x60;
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
    :param override: Flag that specifies whether the new deployment replaces other deployed revisions of the shared flow in the environment. Set &#x60;override&#x60; to &#x60;true&#x60; to replace other deployed revisions. By default, &#x60;override&#x60; is &#x60;false&#x60; and the deployment is rejected if other revisions of the shared flow are deployed in the environment.
    :type override: bool
    :param service_account: Google Cloud IAM service account. The service account represents the identity of the deployed proxy, and determines what permissions it has. The format must be &#x60;{ACCOUNT_ID}@{PROJECT}.iam.gserviceaccount.com&#x60;.
    :type service_account: str

    """
    return web.Response(status=200)


async def apigee_organizations_environments_sharedflows_revisions_get_deployments(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_environments_sharedflows_revisions_get_deployments

    Gets the deployment of a shared flow revision and actual state reported by runtime pods.

    :param name: Required. Name representing a shared flow in an environment in the following format: &#x60;organizations/{org}/environments/{env}/sharedflows/{sharedflow}/revisions/{rev}&#x60;
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


async def apigee_organizations_environments_sharedflows_revisions_undeploy(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, sequenced_rollout=None) -> web.Response:
    """apigee_organizations_environments_sharedflows_revisions_undeploy

    Undeploys a shared flow revision from an environment. For a request path &#x60;organizations/{org}/environments/{env}/sharedflows/{sf}/revisions/{rev}/deployments&#x60;, two permissions are required: * &#x60;apigee.deployments.delete&#x60; on the resource &#x60;organizations/{org}/environments/{env}&#x60; * &#x60;apigee.sharedflowrevisions.undeploy&#x60; on the resource &#x60;organizations/{org}/sharedflows/{sf}/revisions/{rev}&#x60;

    :param name: Required. Name of the shared flow revision to undeploy in the following format: &#x60;organizations/{org}/environments/{env}/sharedflows/{sharedflow}/revisions/{rev}&#x60;
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
    :param sequenced_rollout: Flag that specifies whether to enable sequenced rollout. If set to &#x60;true&#x60;, the environment group routing rules corresponding to this deployment will be removed before removing the deployment from the runtime. This is likely to be a rare use case; it is only needed when the intended effect of undeploying this proxy is to cause the traffic it currently handles to be rerouted to some other existing proxy in the environment group. The GenerateUndeployChangeReport API may be used to examine routing changes before issuing the undeployment request, and its response will indicate if a sequenced rollout is recommended for the undeployment.
    :type sequenced_rollout: bool

    """
    return web.Response(status=200)


async def apigee_organizations_environments_subscribe(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_environments_subscribe

    Creates a subscription for the environment&#39;s Pub/Sub topic. The server will assign a random name for this subscription. The \&quot;name\&quot; and \&quot;push_config\&quot; must *not* be specified.

    :param parent: Required. Name of the environment. Use the following structure in your request: &#x60;organizations/{org}/environments/{env}&#x60;
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


async def apigee_organizations_environments_targetservers_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, name=None, body=None) -> web.Response:
    """apigee_organizations_environments_targetservers_create

    Creates a TargetServer in the specified environment.

    :param parent: Required. The parent environment name under which the TargetServer will be created. Must be of the form &#x60;organizations/{org}/environments/{env}&#x60;.
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
    :param name: Optional. The ID to give the TargetServer. This will overwrite the value in TargetServer.
    :type name: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudApigeeV1TargetServer.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_test_iam_permissions(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_test_iam_permissions

    Tests the permissions of a user on an environment, and returns a subset of permissions that the user has on the environment. If the environment does not exist, an empty permission set is returned (a NOT_FOUND error is not returned).

    :param resource: REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
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
    body = GoogleIamV1TestIamPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_trace_config_overrides_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_trace_config_overrides_create

    Creates a trace configuration override. The response contains a system-generated UUID, that can be used to view, update, or delete the configuration override. Use the List API to view the existing trace configuration overrides.

    :param parent: Required. Parent resource of the trace configuration override. Use the following structure in your request. \&quot;organizations/*/environments/*/traceConfig\&quot;.
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
    body = GoogleCloudApigeeV1TraceConfigOverride.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_environments_trace_config_overrides_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_environments_trace_config_overrides_list

    Lists all of the distributed trace configuration overrides in an environment.

    :param parent: Required. Parent resource of the trace configuration override. Use the following structure in your request: \&quot;organizations/*/environments/*/traceConfig\&quot;.
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
    :param page_size: Maximum number of trace configuration overrides to return. If not specified, the maximum number returned is 25. The maximum number cannot exceed 100.
    :type page_size: int
    :param page_token: A page token, returned from a previous &#x60;ListTraceConfigOverrides&#x60; call. Token value that can be used to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListTraceConfigOverrides&#x60; must match those specified in the call to obtain the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_environments_unsubscribe(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_environments_unsubscribe

    Deletes a subscription for the environment&#39;s Pub/Sub topic.

    :param parent: Required. Name of the environment. Use the following structure in your request: &#x60;organizations/{org}/environments/{env}&#x60;
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
    body = GoogleCloudApigeeV1Subscription.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_get_project_mapping(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_get_project_mapping

    Gets the project ID and region for an Apigee organization.

    :param name: Required. Apigee organization name in the following format: &#x60;organizations/{org}&#x60;
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


async def apigee_organizations_get_sync_authorization(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_get_sync_authorization

    Lists the service accounts with the permissions required to allow the Synchronizer to download environment data from the control plane. An ETag is returned in the response to &#x60;getSyncAuthorization&#x60;. Pass that ETag when calling [setSyncAuthorization](setSyncAuthorization) to ensure that you are updating the correct version. If you don&#39;t pass the ETag in the call to &#x60;setSyncAuthorization&#x60;, then the existing authorization is overwritten indiscriminately. For more information, see [Configure the Synchronizer](https://cloud.google.com/apigee/docs/hybrid/latest/synchronizer-access). **Note**: Available to Apigee hybrid only.

    :param name: Required. Name of the Apigee organization. Use the following structure in your request: &#x60;organizations/{org}&#x60;
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


async def apigee_organizations_host_queries_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_host_queries_create

    Submit a query at host level to be processed in the background. If the submission of the query succeeds, the API returns a 201 status and an ID that refer to the query. In addition to the HTTP status 201, the &#x60;state&#x60; of \&quot;enqueued\&quot; means that the request succeeded.

    :param parent: Required. The parent resource name. Must be of the form &#x60;organizations/{org}&#x60;.
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
    body = GoogleCloudApigeeV1Query.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_host_queries_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, dataset=None, envgroup_hostname=None, _from=None, incl_queries_without_report=None, status=None, submitted_by=None, to=None) -> web.Response:
    """apigee_organizations_host_queries_list

    Return a list of Asynchronous Queries at host level.

    :param parent: Required. The parent resource name. Must be of the form &#x60;organizations/{org}&#x60;.
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
    :param dataset: Filter response list by dataset. Example: &#x60;api&#x60;, &#x60;mint&#x60;
    :type dataset: str
    :param envgroup_hostname: Required. Filter response list by hostname.
    :type envgroup_hostname: str
    :param _from: Filter response list by returning asynchronous queries that created after this date time. Time must be in ISO date-time format like &#39;2011-12-03T10:15:30Z&#39;.
    :type _from: str
    :param incl_queries_without_report: Flag to include asynchronous queries that don&#39;t have a report denifition.
    :type incl_queries_without_report: str
    :param status: Filter response list by asynchronous query status.
    :type status: str
    :param submitted_by: Filter response list by user who submitted queries.
    :type submitted_by: str
    :param to: Filter response list by returning asynchronous queries that created before this date time. Time must be in ISO date-time format like &#39;2011-12-03T10:16:30Z&#39;.
    :type to: str

    """
    return web.Response(status=200)


async def apigee_organizations_host_security_reports_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_host_security_reports_create

    Submit a query at host level to be processed in the background. If the submission of the query succeeds, the API returns a 201 status and an ID that refer to the query. In addition to the HTTP status 201, the &#x60;state&#x60; of \&quot;enqueued\&quot; means that the request succeeded.

    :param parent: Required. The parent resource name. Must be of the form &#x60;organizations/{org}&#x60;.
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
    body = GoogleCloudApigeeV1SecurityReportQuery.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_host_security_reports_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, dataset=None, envgroup_hostname=None, _from=None, page_size=None, page_token=None, status=None, submitted_by=None, to=None) -> web.Response:
    """apigee_organizations_host_security_reports_list

    Return a list of Security Reports at host level.

    :param parent: Required. The parent resource name. Must be of the form &#x60;organizations/{org}&#x60;.
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
    :param dataset: Filter response list by dataset. Example: &#x60;api&#x60;, &#x60;mint&#x60;
    :type dataset: str
    :param envgroup_hostname: Required. Filter response list by hostname.
    :type envgroup_hostname: str
    :param _from: Filter response list by returning security reports that created after this date time. Time must be in ISO date-time format like &#39;2011-12-03T10:15:30Z&#39;.
    :type _from: str
    :param page_size: The maximum number of security report to return in the list response.
    :type page_size: int
    :param page_token: Token returned from the previous list response to fetch the next page.
    :type page_token: str
    :param status: Filter response list by security report status.
    :type status: str
    :param submitted_by: Filter response list by user who submitted queries.
    :type submitted_by: str
    :param to: Filter response list by returning security reports that created before this date time. Time must be in ISO date-time format like &#39;2011-12-03T10:16:30Z&#39;.
    :type to: str

    """
    return web.Response(status=200)


async def apigee_organizations_instances_attachments_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_instances_attachments_create

    Creates a new attachment of an environment to an instance. **Note:** Not supported for Apigee hybrid.

    :param parent: Required. Name of the instance. Use the following structure in your request: &#x60;organizations/{org}/instances/{instance}&#x60;.
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
    body = GoogleCloudApigeeV1InstanceAttachment.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_instances_attachments_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_instances_attachments_list

    Lists all attachments to an instance. **Note:** Not supported for Apigee hybrid.

    :param parent: Required. Name of the organization. Use the following structure in your request: &#x60;organizations/{org}/instances/{instance}&#x60;
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
    :param page_size: Maximum number of instance attachments to return. Defaults to 25.
    :type page_size: int
    :param page_token: Page token, returned by a previous ListInstanceAttachments call, that you can use to retrieve the next page of content.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_instances_canaryevaluations_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_instances_canaryevaluations_create

    Creates a new canary evaluation for an organization.

    :param parent: Required. Name of the organization. Use the following structure in your request: &#x60;organizations/{org}/instances/{instance}&#x60;.
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
    body = GoogleCloudApigeeV1CanaryEvaluation.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_instances_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_instances_create

    Creates an Apigee runtime instance. The instance is accessible from the authorized network configured on the organization. **Note:** Not supported for Apigee hybrid.

    :param parent: Required. Name of the organization. Use the following structure in your request: &#x60;organizations/{org}&#x60;.
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
    body = GoogleCloudApigeeV1Instance.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_instances_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_instances_list

    Lists all Apigee runtime instances for the organization. **Note:** Not supported for Apigee hybrid.

    :param parent: Required. Name of the organization. Use the following structure in your request: &#x60;organizations/{org}&#x60;.
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
    :param page_size: Maximum number of instances to return. Defaults to 25.
    :type page_size: int
    :param page_token: Page token, returned from a previous ListInstances call, that you can use to retrieve the next page of content.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_instances_nat_addresses_activate(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_instances_nat_addresses_activate

    Activates the NAT address. The Apigee instance can now use this for Internet egress traffic. **Note:** Not supported for Apigee hybrid.

    :param name: Required. Name of the nat address. Use the following structure in your request: &#x60;organizations/{org}/instances/{instances}/natAddresses/{nataddress}&#x60;&#x60;
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


async def apigee_organizations_instances_nat_addresses_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_instances_nat_addresses_create

    Creates a NAT address. The address is created in the RESERVED state and a static external IP address will be provisioned. At this time, the instance will not use this IP address for Internet egress traffic. The address can be activated for use once any required firewall IP whitelisting has been completed. **Note:** Not supported for Apigee hybrid.

    :param parent: Required. Name of the instance. Use the following structure in your request: &#x60;organizations/{org}/instances/{instance}&#x60;
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
    body = GoogleCloudApigeeV1NatAddress.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_instances_nat_addresses_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_instances_nat_addresses_list

    Lists the NAT addresses for an Apigee instance. **Note:** Not supported for Apigee hybrid.

    :param parent: Required. Name of the instance. Use the following structure in your request: &#x60;organizations/{org}/instances/{instance}&#x60;
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
    :param page_size: Maximum number of natAddresses to return. Defaults to 25.
    :type page_size: int
    :param page_token: Page token, returned from a previous ListNatAddresses call, that you can use to retrieve the next page of content.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_instances_report_status(request: web.Request, instance, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_instances_report_status

    Reports the latest status for a runtime instance.

    :param instance: The name of the instance reporting this status. For SaaS the request will be rejected if no instance exists under this name. Format is organizations/{org}/instances/{instance}
    :type instance: str
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
    body = GoogleCloudApigeeV1ReportInstanceStatusRequest.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_keyvaluemaps_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_keyvaluemaps_create

    Creates a key value map in an organization.

    :param parent: Required. Name of the organization in which to create the key value map file. Use the following structure in your request: &#x60;organizations/{org}&#x60;
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
    body = GoogleCloudApigeeV1KeyValueMap.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_keyvaluemaps_entries_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_keyvaluemaps_entries_create

    Creates key value entries in a key value map scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher.

    :param parent: Required. Scope as indicated by the URI in which to create the key value map entry. Use **one** of the following structures in your request: * &#x60;organizations/{organization}/apis/{api}/keyvaluemaps/{keyvaluemap}&#x60;. * &#x60;organizations/{organization}/environments/{environment}/keyvaluemaps/{keyvaluemap}&#x60; * &#x60;organizations/{organization}/keyvaluemaps/{keyvaluemap}&#x60;.
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
    body = GoogleCloudApigeeV1KeyValueEntry.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_keyvaluemaps_entries_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_keyvaluemaps_entries_list

    Lists key value entries for key values maps scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher.

    :param parent: Required. Scope as indicated by the URI in which to list key value maps. Use **one** of the following structures in your request: * &#x60;organizations/{organization}/apis/{api}/keyvaluemaps/{keyvaluemap}&#x60;. * &#x60;organizations/{organization}/environments/{environment}/keyvaluemaps/{keyvaluemap}&#x60; * &#x60;organizations/{organization}/keyvaluemaps/{keyvaluemap}&#x60;.
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
    :param page_size: Optional. Maximum number of key value entries to return. If unspecified, at most 100 entries will be returned.
    :type page_size: int
    :param page_token: Optional. Page token. If provides, must be a valid key value entry returned from a previous call that can be used to retrieve the next page.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_list

    Lists the Apigee organizations and associated Google Cloud projects that you have permission to access. See [Understanding organizations](https://cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure).

    :param parent: Required. Use the following structure in your request: &#x60;organizations&#x60;
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


async def apigee_organizations_operations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_operations_list

    Lists operations that match the specified filter in the request. If the server doesn&#39;t support this method, it returns &#x60;UNIMPLEMENTED&#x60;.

    :param name: The name of the operation&#39;s parent resource.
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
    :param filter: The standard list filter.
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_reports_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_reports_create

    Creates a Custom Report for an Organization. A Custom Report provides Apigee Customers to create custom dashboards in addition to the standard dashboards which are provided. The Custom Report in its simplest form contains specifications about metrics, dimensions and filters. It is important to note that the custom report by itself does not provide an executable entity. The Edge UI converts the custom report definition into an analytics query and displays the result in a chart.

    :param parent: Required. The parent organization name under which the Custom Report will be created. Must be of the form: &#x60;organizations/{organization_id}/reports&#x60;
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
    body = GoogleCloudApigeeV1CustomReport.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_reports_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, expand=None) -> web.Response:
    """apigee_organizations_reports_list

    Return a list of Custom Reports

    :param parent: Required. The parent organization name under which the API product will be listed &#x60;organizations/{organization_id}/reports&#x60;
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
    :param expand: Set to &#39;true&#39; to get expanded details about each custom report.
    :type expand: bool

    """
    return web.Response(status=200)


async def apigee_organizations_security_profiles_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, security_profile_id=None, body=None) -> web.Response:
    """apigee_organizations_security_profiles_create

    CreateSecurityProfile create a new custom security profile.

    :param parent: Required. Name of organization. Format: organizations/{org}
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
    :param security_profile_id: Required. The ID to use for the SecurityProfile, which will become the final component of the action&#39;s resource name. This value should be 1-63 characters and validated by \&quot;(^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$)\&quot;.
    :type security_profile_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudApigeeV1SecurityProfile.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_security_profiles_environments_compute_environment_scores(request: web.Request, profile_environment, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_security_profiles_environments_compute_environment_scores

    ComputeEnvironmentScores calculates scores for requested time range for the specified security profile and environment.

    :param profile_environment: Required. Name of organization and environment and profile id for which score needs to be computed. Format: organizations/{org}/securityProfiles/{profile}/environments/{env}
    :type profile_environment: str
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
    body = GoogleCloudApigeeV1ComputeEnvironmentScoresRequest.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_security_profiles_environments_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, name=None, body=None) -> web.Response:
    """apigee_organizations_security_profiles_environments_create

    CreateSecurityProfileEnvironmentAssociation creates profile environment association i.e. attaches environment to security profile.

    :param parent: Required. Name of organization and security profile ID. Format: organizations/{org}/securityProfiles/{profile}
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
    :param name: Optional. Name of the environment.
    :type name: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudApigeeV1SecurityProfileEnvironmentAssociation.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_security_profiles_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_security_profiles_list

    ListSecurityProfiles lists all the security profiles associated with the org including attached and unattached profiles.

    :param parent: Required. For a specific organization, list of all the security profiles. Format: &#x60;organizations/{org}&#x60;
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
    :param page_size: The maximum number of profiles to return. The service may return fewer than this value. If unspecified, at most 50 profiles will be returned.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListSecurityProfiles&#x60; call. Provide this to retrieve the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_security_profiles_list_revisions(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_security_profiles_list_revisions

    ListSecurityProfileRevisions lists all the revisions of the security profile.

    :param name: Required. For a specific profile, list all the revisions. Format: &#x60;organizations/{org}/securityProfiles/{profile}&#x60;
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
    :param page_size: The maximum number of profile revisions to return. The service may return fewer than this value. If unspecified, at most 50 revisions will be returned.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListSecurityProfileRevisions&#x60; call. Provide this to retrieve the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_set_addons(request: web.Request, org, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_set_addons

    Configures the add-ons for the Apigee organization. The existing add-on configuration will be fully replaced.

    :param org: Required. Name of the organization. Use the following structure in your request: &#x60;organizations/{org}&#x60;
    :type org: str
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
    body = GoogleCloudApigeeV1SetAddonsRequest.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_set_sync_authorization(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_set_sync_authorization

    Sets the permissions required to allow the Synchronizer to download environment data from the control plane. You must call this API to enable proper functioning of hybrid. Pass the ETag when calling &#x60;setSyncAuthorization&#x60; to ensure that you are updating the correct version. To get an ETag, call [getSyncAuthorization](getSyncAuthorization). If you don&#39;t pass the ETag in the call to &#x60;setSyncAuthorization&#x60;, then the existing authorization is overwritten indiscriminately. For more information, see [Configure the Synchronizer](https://cloud.google.com/apigee/docs/hybrid/latest/synchronizer-access). **Note**: Available to Apigee hybrid only.

    :param name: Required. Name of the Apigee organization. Use the following structure in your request: &#x60;organizations/{org}&#x60;
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
    body = GoogleCloudApigeeV1SyncAuthorization.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_sharedflows_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, action=None, name=None, body=None) -> web.Response:
    """apigee_organizations_sharedflows_create

    Uploads a ZIP-formatted shared flow configuration bundle to an organization. If the shared flow already exists, this creates a new revision of it. If the shared flow does not exist, this creates it. Once imported, the shared flow revision must be deployed before it can be accessed at runtime. The size limit of a shared flow bundle is 15 MB.

    :param parent: Required. The name of the parent organization under which to create the shared flow. Must be of the form: &#x60;organizations/{organization_id}&#x60;
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
    :param action: Required. Must be set to either &#x60;import&#x60; or &#x60;validate&#x60;.
    :type action: str
    :param name: Required. The name to give the shared flow
    :type name: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleApiHttpBody.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_sharedflows_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_meta_data=None, include_revisions=None) -> web.Response:
    """apigee_organizations_sharedflows_list

    Lists all shared flows in the organization.

    :param parent: Required. The name of the parent organization under which to get shared flows. Must be of the form: &#x60;organizations/{organization_id}&#x60;
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
    :param include_meta_data: Indicates whether to include shared flow metadata in the response.
    :type include_meta_data: bool
    :param include_revisions: Indicates whether to include a list of revisions in the response.
    :type include_revisions: bool

    """
    return web.Response(status=200)


async def apigee_organizations_sharedflows_revisions_deployments_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, shared_flows=None) -> web.Response:
    """apigee_organizations_sharedflows_revisions_deployments_list

    Lists all deployments of a shared flow revision.

    :param parent: Required. Name of the API proxy revision for which to return deployment information in the following format: &#x60;organizations/{org}/sharedflows/{sharedflow}/revisions/{rev}&#x60;.
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
    :param shared_flows: Optional. Flag that specifies whether to return shared flow or API proxy deployments. Set to &#x60;true&#x60; to return shared flow deployments; set to &#x60;false&#x60; to return API proxy deployments. Defaults to &#x60;false&#x60;.
    :type shared_flows: bool

    """
    return web.Response(status=200)


async def apigee_organizations_sharedflows_revisions_update_shared_flow_revision(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, validate=None, body=None) -> web.Response:
    """apigee_organizations_sharedflows_revisions_update_shared_flow_revision

    Updates a shared flow revision. This operation is only allowed on revisions which have never been deployed. After deployment a revision becomes immutable, even if it becomes undeployed. The payload is a ZIP-formatted shared flow. Content type must be either multipart/form-data or application/octet-stream.

    :param name: Required. The name of the shared flow revision to update. Must be of the form: &#x60;organizations/{organization_id}/sharedflows/{shared_flow_id}/revisions/{revision_id}&#x60;
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
    :param validate: Ignored. All uploads are validated regardless of the value of this field. It is kept for compatibility with existing APIs. Must be &#x60;true&#x60; or &#x60;false&#x60; if provided.
    :type validate: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleApiHttpBody.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_sites_apicategories_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_sites_apicategories_create

    Creates a new API category.

    :param parent: Required. Name of the portal. Use the following structure in your request: &#x60;organizations/{org}/sites/{site}&#x60;
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
    body = GoogleCloudApigeeV1ApiCategory.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_sites_apicategories_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """apigee_organizations_sites_apicategories_list

    Returns the API categories associated with a portal.

    :param parent: Required. Name of the portal. Use the following structure in your request: &#x60;organizations/{org}/sites/{site}&#x60;
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


async def apigee_organizations_sites_apidocs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """apigee_organizations_sites_apidocs_create

    Creates a new catalog item.

    :param parent: Required. Name of the portal. Use the following structure in your request: &#x60;organizations/{org}/sites/{site}&#x60;
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
    body = GoogleCloudApigeeV1ApiDoc.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_sites_apidocs_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, retention=None) -> web.Response:
    """apigee_organizations_sites_apidocs_delete

    Deletes a catalog item.

    :param name: Required. Name of the catalog item. Use the following structure in your request: &#x60;organizations/{org}/sites/{site}/apidocs/{apidoc}&#x60;
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
    :param retention: Optional. This setting is applicable only for organizations that are soft-deleted (i.e., BillingType is not EVALUATION). It controls how long Organization data will be retained after the initial delete operation completes. During this period, the Organization may be restored to its last known state. After this period, the Organization will no longer be able to be restored. **Note: During the data retention period specified using this field, the Apigee organization cannot be recreated in the same GCP project.**
    :type retention: str

    """
    return web.Response(status=200)


async def apigee_organizations_sites_apidocs_get_documentation(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, format=None, envgroup_hostname=None, filter=None, limit=None, offset=None, realtime=None, select=None, sort=None, sortby=None, time_range=None, time_unit=None, topk=None, ts_ascending=None, tzo=None) -> web.Response:
    """apigee_organizations_sites_apidocs_get_documentation

    Gets the documentation for the specified catalog item.

    :param name: Required. Resource name of the catalog item documentation. Use the following structure in your request: &#x60;organizations/{org}/sites/{site}/apidocs/{apidoc}/documentation&#x60;
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
    :param format: Specify &#x60;bundle&#x60; to export the contents of the shared flow bundle. Otherwise, the bundle metadata is returned.
    :type format: str
    :param envgroup_hostname: Required. Hostname for which the interactive query will be executed.
    :type envgroup_hostname: str
    :param filter: Filter that enables you to drill-down on specific dimension values.
    :type filter: str
    :param limit: Maximum number of result items to return. The default and maximum value that can be returned is 14400.
    :type limit: str
    :param offset: Offset value. Use &#x60;offset&#x60; with &#x60;limit&#x60; to enable pagination of results. For example, to display results 11-20, set limit to &#x60;10&#x60; and offset to &#x60;10&#x60;.
    :type offset: str
    :param realtime: No longer used by Apigee. Supported for backwards compatibility.
    :type realtime: bool
    :param select: Required. Comma-separated list of metrics. For example: &#x60;sum(message_count),sum(error_count)&#x60;
    :type select: str
    :param sort: Flag that specifies whether the sort order should be ascending or descending. Valid values include &#x60;DESC&#x60; and &#x60;ASC&#x60;.
    :type sort: str
    :param sortby: Comma-separated list of columns used to sort the final result.
    :type sortby: str
    :param time_range: Required. Time interval for the interactive query. Time range is specified in GMT as &#x60;start~end&#x60;. For example: &#x60;04/15/2017 00:00~05/15/2017 23:59&#x60;.
    :type time_range: str
    :param time_unit: Granularity of metrics returned. Valid values include: &#x60;second&#x60;, &#x60;minute&#x60;, &#x60;hour&#x60;, &#x60;day&#x60;, &#x60;week&#x60;, or &#x60;month&#x60;.
    :type time_unit: str
    :param topk: Top number of results to return. For example, to return the top 5 results, set &#x60;topk&#x3D;5&#x60;.
    :type topk: str
    :param ts_ascending: Flag that specifies whether to list timestamps in ascending (&#x60;true&#x60;) or descending (&#x60;false&#x60;) order. Apigee recommends that you set this value to &#x60;true&#x60; if you are using &#x60;sortby&#x60; with &#x60;sort&#x3D;DESC&#x60;.
    :type ts_ascending: bool
    :param tzo: Timezone offset value.
    :type tzo: str

    """
    return web.Response(status=200)


async def apigee_organizations_sites_apidocs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """apigee_organizations_sites_apidocs_list

    Returns the catalog items associated with a portal.

    :param parent: Required. Name of the portal. Use the following structure in your request: &#x60;organizations/{org}/sites/{site}&#x60;
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
    :param page_size: Optional. The maximum number of items to return. The service may return fewer than this value. If unspecified, at most 25 books will be returned. The maximum value is 100; values above 100 will be coerced to 100.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListApiDocs&#x60; call. Provide this to retrieve the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def apigee_organizations_sites_apidocs_update(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, ignore_expiry_validation=None, ignore_newline_validation=None, body=None) -> web.Response:
    """apigee_organizations_sites_apidocs_update

    Updates a catalog item.

    :param name: Required. Name of the catalog item. Use the following structure in your request: &#x60;organizations/{org}/sites/{site}/apidocs/{apidoc}&#x60;
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
    :param ignore_expiry_validation: Required. Flag that specifies whether to ignore expiry validation. If set to &#x60;true&#x60;, no expiry validation will be performed.
    :type ignore_expiry_validation: bool
    :param ignore_newline_validation: Flag that specifies whether to ignore newline validation. If set to &#x60;true&#x60;, no error is thrown when the file contains a certificate chain with no newline between each certificate. Defaults to &#x60;false&#x60;.
    :type ignore_newline_validation: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudApigeeV1ApiDoc.from_dict(body)
    return web.Response(status=200)


async def apigee_organizations_sites_apidocs_update_documentation(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """apigee_organizations_sites_apidocs_update_documentation

    Updates the documentation for the specified catalog item. Note that the documentation file contents will not be populated in the return message.

    :param name: Required. Resource name of the catalog item documentation. Use the following structure in your request: &#x60;organizations/{org}/sites/{site}/apidocs/{apidoc}/documentation&#x60;
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
    :param update_mask: Required. The list of fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudApigeeV1ApiDocDocumentation.from_dict(body)
    return web.Response(status=200)
