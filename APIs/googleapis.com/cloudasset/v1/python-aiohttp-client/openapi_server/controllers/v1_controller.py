from typing import List, Dict
from aiohttp import web

from openapi_server.models.analyze_iam_policy_longrunning_request import AnalyzeIamPolicyLongrunningRequest
from openapi_server.models.analyze_iam_policy_response import AnalyzeIamPolicyResponse
from openapi_server.models.analyze_move_response import AnalyzeMoveResponse
from openapi_server.models.analyze_org_policies_response import AnalyzeOrgPoliciesResponse
from openapi_server.models.analyze_org_policy_governed_assets_response import AnalyzeOrgPolicyGovernedAssetsResponse
from openapi_server.models.analyze_org_policy_governed_containers_response import AnalyzeOrgPolicyGovernedContainersResponse
from openapi_server.models.batch_get_assets_history_response import BatchGetAssetsHistoryResponse
from openapi_server.models.export_assets_request import ExportAssetsRequest
from openapi_server.models.operation import Operation
from openapi_server.models.query_assets_request import QueryAssetsRequest
from openapi_server.models.query_assets_response import QueryAssetsResponse
from openapi_server.models.search_all_iam_policies_response import SearchAllIamPoliciesResponse
from openapi_server.models.search_all_resources_response import SearchAllResourcesResponse
from openapi_server import util


async def cloudasset_analyze_iam_policy(request: web.Request, scope, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, analysis_query_access_selector_permissions=None, analysis_query_access_selector_roles=None, analysis_query_condition_context_access_time=None, analysis_query_identity_selector_identity=None, analysis_query_options_analyze_service_account_impersonation=None, analysis_query_options_expand_groups=None, analysis_query_options_expand_resources=None, analysis_query_options_expand_roles=None, analysis_query_options_output_group_edges=None, analysis_query_options_output_resource_edges=None, analysis_query_resource_selector_full_resource_name=None, execution_timeout=None, saved_analysis_query=None) -> web.Response:
    """cloudasset_analyze_iam_policy

    Analyzes IAM policies to answer which identities have what accesses on which resources.

    :param scope: Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed. This can only be an organization number (such as \&quot;organizations/123\&quot;), a folder number (such as \&quot;folders/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;). To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects).
    :type scope: str
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
    :param analysis_query_access_selector_permissions: Optional. The permissions to appear in result.
    :type analysis_query_access_selector_permissions: List[str]
    :param analysis_query_access_selector_roles: Optional. The roles to appear in result.
    :type analysis_query_access_selector_roles: List[str]
    :param analysis_query_condition_context_access_time: The hypothetical access timestamp to evaluate IAM conditions. Note that this value must not be earlier than the current time; otherwise, an INVALID_ARGUMENT error will be returned.
    :type analysis_query_condition_context_access_time: str
    :param analysis_query_identity_selector_identity: Required. The identity appear in the form of principals in [IAM policy binding](https://cloud.google.com/iam/reference/rest/v1/Binding). The examples of supported forms are: \&quot;user:mike@example.com\&quot;, \&quot;group:admins@example.com\&quot;, \&quot;domain:google.com\&quot;, \&quot;serviceAccount:my-project-id@appspot.gserviceaccount.com\&quot;. Notice that wildcard characters (such as * and ?) are not supported. You must give a specific identity.
    :type analysis_query_identity_selector_identity: str
    :param analysis_query_options_analyze_service_account_impersonation: Optional. If true, the response will include access analysis from identities to resources via service account impersonation. This is a very expensive operation, because many derived queries will be executed. We highly recommend you use AssetService.AnalyzeIamPolicyLongrunning RPC instead. For example, if the request analyzes for which resources user A has permission P, and there&#39;s an IAM policy states user A has iam.serviceAccounts.getAccessToken permission to a service account SA, and there&#39;s another IAM policy states service account SA has permission P to a Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in AnalyzeIamPolicyResponse.service_account_impersonation_analysis. Another example, if the request analyzes for who has permission P to a Google Cloud folder F, and there&#39;s an IAM policy states user A has iam.serviceAccounts.actAs permission to a service account SA, and there&#39;s another IAM policy states service account SA has permission P to the Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in AnalyzeIamPolicyResponse.service_account_impersonation_analysis. Only the following permissions are considered in this analysis: * &#x60;iam.serviceAccounts.actAs&#x60; * &#x60;iam.serviceAccounts.signBlob&#x60; * &#x60;iam.serviceAccounts.signJwt&#x60; * &#x60;iam.serviceAccounts.getAccessToken&#x60; * &#x60;iam.serviceAccounts.getOpenIdToken&#x60; * &#x60;iam.serviceAccounts.implicitDelegation&#x60; Default is false.
    :type analysis_query_options_analyze_service_account_impersonation: bool
    :param analysis_query_options_expand_groups: Optional. If true, the identities section of the result will expand any Google groups appearing in an IAM policy binding. If IamPolicyAnalysisQuery.identity_selector is specified, the identity in the result will be determined by the selector, and this flag is not allowed to set. If true, the default max expansion per group is 1000 for AssetService.AnalyzeIamPolicy][]. Default is false.
    :type analysis_query_options_expand_groups: bool
    :param analysis_query_options_expand_resources: Optional. If true and IamPolicyAnalysisQuery.resource_selector is not specified, the resource section of the result will expand any resource attached to an IAM policy to include resources lower in the resource hierarchy. For example, if the request analyzes for which resources user A has permission P, and the results include an IAM policy with P on a Google Cloud folder, the results will also include resources in that folder with permission P. If true and IamPolicyAnalysisQuery.resource_selector is specified, the resource section of the result will expand the specified resource to include resources lower in the resource hierarchy. Only project or lower resources are supported. Folder and organization resources cannot be used together with this option. For example, if the request analyzes for which users have permission P on a Google Cloud project with this option enabled, the results will include all users who have permission P on that project or any lower resource. If true, the default max expansion per resource is 1000 for AssetService.AnalyzeIamPolicy][] and 100000 for AssetService.AnalyzeIamPolicyLongrunning][]. Default is false.
    :type analysis_query_options_expand_resources: bool
    :param analysis_query_options_expand_roles: Optional. If true, the access section of result will expand any roles appearing in IAM policy bindings to include their permissions. If IamPolicyAnalysisQuery.access_selector is specified, the access section of the result will be determined by the selector, and this flag is not allowed to set. Default is false.
    :type analysis_query_options_expand_roles: bool
    :param analysis_query_options_output_group_edges: Optional. If true, the result will output the relevant membership relationships between groups and other groups, and between groups and principals. Default is false.
    :type analysis_query_options_output_group_edges: bool
    :param analysis_query_options_output_resource_edges: Optional. If true, the result will output the relevant parent/child relationships between resources. Default is false.
    :type analysis_query_options_output_resource_edges: bool
    :param analysis_query_resource_selector_full_resource_name: Required. The [full resource name] (https://cloud.google.com/asset-inventory/docs/resource-name-format) of a resource of [supported resource types](https://cloud.google.com/asset-inventory/docs/supported-asset-types#analyzable_asset_types).
    :type analysis_query_resource_selector_full_resource_name: str
    :param execution_timeout: Optional. Amount of time executable has to complete. See JSON representation of [Duration](https://developers.google.com/protocol-buffers/docs/proto3#json). If this field is set with a value less than the RPC deadline, and the execution of your query hasn&#39;t finished in the specified execution timeout, you will get a response with partial result. Otherwise, your query&#39;s execution will continue until the RPC deadline. If it&#39;s not finished until then, you will get a DEADLINE_EXCEEDED error. Default is empty.
    :type execution_timeout: str
    :param saved_analysis_query: Optional. The name of a saved query, which must be in the format of: * projects/project_number/savedQueries/saved_query_id * folders/folder_number/savedQueries/saved_query_id * organizations/organization_number/savedQueries/saved_query_id If both &#x60;analysis_query&#x60; and &#x60;saved_analysis_query&#x60; are provided, they will be merged together with the &#x60;saved_analysis_query&#x60; as base and the &#x60;analysis_query&#x60; as overrides. For more details of the merge behavior, refer to the [MergeFrom](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details) page. Note that you cannot override primitive fields with default value, such as 0 or empty string, etc., because we use proto3, which doesn&#39;t support field presence yet.
    :type saved_analysis_query: str

    """
    return web.Response(status=200)


async def cloudasset_analyze_iam_policy_longrunning(request: web.Request, scope, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudasset_analyze_iam_policy_longrunning

    Analyzes IAM policies asynchronously to answer which identities have what accesses on which resources, and writes the analysis results to a Google Cloud Storage or a BigQuery destination. For Cloud Storage destination, the output format is the JSON format that represents a AnalyzeIamPolicyResponse. This method implements the google.longrunning.Operation, which allows you to track the operation status. We recommend intervals of at least 2 seconds with exponential backoff retry to poll the operation result. The metadata contains the metadata for the long-running operation.

    :param scope: Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed. This can only be an organization number (such as \&quot;organizations/123\&quot;), a folder number (such as \&quot;folders/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;). To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects).
    :type scope: str
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
    body = AnalyzeIamPolicyLongrunningRequest.from_dict(body)
    return web.Response(status=200)


async def cloudasset_analyze_move(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, destination_parent=None, view=None) -> web.Response:
    """cloudasset_analyze_move

    Analyze moving a resource to a specified destination without kicking off the actual move. The analysis is best effort depending on the user&#39;s permissions of viewing different hierarchical policies and configurations. The policies and configuration are subject to change before the actual resource migration takes place.

    :param resource: Required. Name of the resource to perform the analysis against. Only Google Cloud projects are supported as of today. Hence, this can only be a project ID (such as \&quot;projects/my-project-id\&quot;) or a project number (such as \&quot;projects/12345\&quot;).
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
    :param destination_parent: Required. Name of the Google Cloud folder or organization to reparent the target resource. The analysis will be performed against hypothetically moving the resource to this specified desitination parent. This can only be a folder number (such as \&quot;folders/123\&quot;) or an organization number (such as \&quot;organizations/123\&quot;).
    :type destination_parent: str
    :param view: Analysis view indicating what information should be included in the analysis response. If unspecified, the default view is FULL.
    :type view: str

    """
    return web.Response(status=200)


async def cloudasset_analyze_org_policies(request: web.Request, scope, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, constraint=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """cloudasset_analyze_org_policies

    Analyzes organization policies under a scope.

    :param scope: Required. The organization to scope the request. Only organization policies within the scope will be analyzed. * organizations/{ORGANIZATION_NUMBER} (e.g., \&quot;organizations/123456\&quot;)
    :type scope: str
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
    :param constraint: Required. The name of the constraint to analyze organization policies for. The response only contains analyzed organization policies for the provided constraint.
    :type constraint: str
    :param filter: The expression to filter AnalyzeOrgPoliciesResponse.org_policy_results. Filtering is currently available for bare literal values and the following fields: * consolidated_policy.attached_resource * consolidated_policy.rules.enforce When filtering by a specific field, the only supported operator is &#x60;&#x3D;&#x60;. For example, filtering by consolidated_policy.attached_resource&#x3D;\&quot;//cloudresourcemanager.googleapis.com/folders/001\&quot; will return all the Organization Policy results attached to \&quot;folders/001\&quot;.
    :type filter: str
    :param page_size: The maximum number of items to return per page. If unspecified, AnalyzeOrgPoliciesResponse.org_policy_results will contain 20 items with a maximum of 200.
    :type page_size: int
    :param page_token: The pagination token to retrieve the next page.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudasset_analyze_org_policy_governed_assets(request: web.Request, scope, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, constraint=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """cloudasset_analyze_org_policy_governed_assets

    Analyzes organization policies governed assets (Google Cloud resources or policies) under a scope. This RPC supports custom constraints and the following canned constraints: * constraints/ainotebooks.accessMode * constraints/ainotebooks.disableFileDownloads * constraints/ainotebooks.disableRootAccess * constraints/ainotebooks.disableTerminal * constraints/ainotebooks.environmentOptions * constraints/ainotebooks.requireAutoUpgradeSchedule * constraints/ainotebooks.restrictVpcNetworks * constraints/compute.disableGuestAttributesAccess * constraints/compute.disableInstanceDataAccessApis * constraints/compute.disableNestedVirtualization * constraints/compute.disableSerialPortAccess * constraints/compute.disableSerialPortLogging * constraints/compute.disableVpcExternalIpv6 * constraints/compute.requireOsLogin * constraints/compute.requireShieldedVm * constraints/compute.restrictLoadBalancerCreationForTypes * constraints/compute.restrictProtocolForwardingCreationForTypes * constraints/compute.restrictXpnProjectLienRemoval * constraints/compute.setNewProjectDefaultToZonalDNSOnly * constraints/compute.skipDefaultNetworkCreation * constraints/compute.trustedImageProjects * constraints/compute.vmCanIpForward * constraints/compute.vmExternalIpAccess * constraints/gcp.detailedAuditLoggingMode * constraints/gcp.resourceLocations * constraints/iam.allowedPolicyMemberDomains * constraints/iam.automaticIamGrantsForDefaultServiceAccounts * constraints/iam.disableServiceAccountCreation * constraints/iam.disableServiceAccountKeyCreation * constraints/iam.disableServiceAccountKeyUpload * constraints/iam.restrictCrossProjectServiceAccountLienRemoval * constraints/iam.serviceAccountKeyExpiryHours * constraints/resourcemanager.accessBoundaries * constraints/resourcemanager.allowedExportDestinations * constraints/sql.restrictAuthorizedNetworks * constraints/sql.restrictNoncompliantDiagnosticDataAccess * constraints/sql.restrictNoncompliantResourceCreation * constraints/sql.restrictPublicIp * constraints/storage.publicAccessPrevention * constraints/storage.restrictAuthTypes * constraints/storage.uniformBucketLevelAccess This RPC only returns either resources of types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types) or IAM policies.

    :param scope: Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output assets will also be limited to the ones governed by those in-scope organization policies. * organizations/{ORGANIZATION_NUMBER} (e.g., \&quot;organizations/123456\&quot;)
    :type scope: str
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
    :param constraint: Required. The name of the constraint to analyze governed assets for. The analysis only contains analyzed organization policies for the provided constraint.
    :type constraint: str
    :param filter: The expression to filter AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets. For governed resources, filtering is currently available for bare literal values and the following fields: * governed_resource.project * governed_resource.folders * consolidated_policy.rules.enforce When filtering by &#x60;governed_resource.project&#x60; or &#x60;consolidated_policy.rules.enforce&#x60;, the only supported operator is &#x60;&#x3D;&#x60;. When filtering by &#x60;governed_resource.folders&#x60;, the supported operators are &#x60;&#x3D;&#x60; and &#x60;:&#x60;. For example, filtering by &#x60;governed_resource.project&#x3D;\&quot;projects/12345678\&quot;&#x60; will return all the governed resources under \&quot;projects/12345678\&quot;, including the project itself if applicable. For governed IAM policies, filtering is currently available for bare literal values and the following fields: * governed_iam_policy.project * governed_iam_policy.folders * consolidated_policy.rules.enforce When filtering by &#x60;governed_iam_policy.project&#x60; or &#x60;consolidated_policy.rules.enforce&#x60;, the only supported operator is &#x60;&#x3D;&#x60;. When filtering by &#x60;governed_iam_policy.folders&#x60;, the supported operators are &#x60;&#x3D;&#x60; and &#x60;:&#x60;. For example, filtering by &#x60;governed_iam_policy.folders:\&quot;folders/12345678\&quot;&#x60; will return all the governed IAM policies under \&quot;folders/001\&quot;.
    :type filter: str
    :param page_size: The maximum number of items to return per page. If unspecified, AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets will contain 100 items with a maximum of 200.
    :type page_size: int
    :param page_token: The pagination token to retrieve the next page.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudasset_analyze_org_policy_governed_containers(request: web.Request, scope, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, constraint=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """cloudasset_analyze_org_policy_governed_containers

    Analyzes organization policies governed containers (projects, folders or organization) under a scope.

    :param scope: Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output containers will also be limited to the ones governed by those in-scope organization policies. * organizations/{ORGANIZATION_NUMBER} (e.g., \&quot;organizations/123456\&quot;)
    :type scope: str
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
    :param constraint: Required. The name of the constraint to analyze governed containers for. The analysis only contains organization policies for the provided constraint.
    :type constraint: str
    :param filter: The expression to filter AnalyzeOrgPolicyGovernedContainersResponse.governed_containers. Filtering is currently available for bare literal values and the following fields: * parent * consolidated_policy.rules.enforce When filtering by a specific field, the only supported operator is &#x60;&#x3D;&#x60;. For example, filtering by parent&#x3D;\&quot;//cloudresourcemanager.googleapis.com/folders/001\&quot; will return all the containers under \&quot;folders/001\&quot;.
    :type filter: str
    :param page_size: The maximum number of items to return per page. If unspecified, AnalyzeOrgPolicyGovernedContainersResponse.governed_containers will contain 100 items with a maximum of 200.
    :type page_size: int
    :param page_token: The pagination token to retrieve the next page.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudasset_batch_get_assets_history(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, asset_names=None, content_type=None, read_time_window_end_time=None, read_time_window_start_time=None, relationship_types=None) -> web.Response:
    """cloudasset_batch_get_assets_history

    Batch gets the update history of assets that overlap a time window. For IAM_POLICY content, this API outputs history when the asset and its attached IAM POLICY both exist. This can create gaps in the output history. Otherwise, this API outputs history with asset in both non-delete or deleted status. If a specified asset does not exist, this API returns an INVALID_ARGUMENT error.

    :param parent: Required. The relative name of the root asset. It can only be an organization number (such as \&quot;organizations/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;)\&quot;, or a project number (such as \&quot;projects/12345\&quot;).
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
    :param asset_names: A list of the full names of the assets. See: https://cloud.google.com/asset-inventory/docs/resource-name-format Example: &#x60;//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1&#x60;. The request becomes a no-op if the asset name list is empty, and the max size of the asset name list is 100 in one request.
    :type asset_names: List[str]
    :param content_type: Optional. The content type.
    :type content_type: str
    :param read_time_window_end_time: End time of the time window (inclusive). If not specified, the current timestamp is used instead.
    :type read_time_window_end_time: str
    :param read_time_window_start_time: Start time of the time window (exclusive).
    :type read_time_window_start_time: str
    :param relationship_types: Optional. A list of relationship types to output, for example: &#x60;INSTANCE_TO_INSTANCEGROUP&#x60;. This field should only be specified if content_type&#x3D;RELATIONSHIP. * If specified: it outputs specified relationships&#39; history on the [asset_names]. It returns an error if any of the [relationship_types] doesn&#39;t belong to the supported relationship types of the [asset_names] or if any of the [asset_names]&#39;s types doesn&#39;t belong to the source types of the [relationship_types]. * Otherwise: it outputs the supported relationships&#39; history on the [asset_names] or returns an error if any of the [asset_names]&#39;s types has no relationship support. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.
    :type relationship_types: List[str]

    """
    return web.Response(status=200)


async def cloudasset_export_assets(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudasset_export_assets

    Exports assets with time and resource types to a given Cloud Storage location/BigQuery table. For Cloud Storage location destinations, the output format is newline-delimited JSON. Each line represents a google.cloud.asset.v1.Asset in the JSON format; for BigQuery table destinations, the output table stores the fields in asset Protobuf as columns. This API implements the google.longrunning.Operation API, which allows you to keep track of the export. We recommend intervals of at least 2 seconds with exponential retry to poll the export operation result. For regular-size resource parent, the export operation usually finishes within 5 minutes.

    :param parent: Required. The relative name of the root asset. This can only be an organization number (such as \&quot;organizations/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;), or a folder number (such as \&quot;folders/123\&quot;).
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
    body = ExportAssetsRequest.from_dict(body)
    return web.Response(status=200)


async def cloudasset_query_assets(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudasset_query_assets

    Issue a job that queries assets using a SQL statement compatible with [BigQuery SQL](https://cloud.google.com/bigquery/docs/introduction-sql). If the query execution finishes within timeout and there&#39;s no pagination, the full query results will be returned in the &#x60;QueryAssetsResponse&#x60;. Otherwise, full query results can be obtained by issuing extra requests with the &#x60;job_reference&#x60; from the a previous &#x60;QueryAssets&#x60; call. Note, the query result has approximately 10 GB limitation enforced by [BigQuery](https://cloud.google.com/bigquery/docs/best-practices-performance-output). Queries return larger results will result in errors.

    :param parent: Required. The relative name of the root asset. This can only be an organization number (such as \&quot;organizations/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;), or a folder number (such as \&quot;folders/123\&quot;). Only assets belonging to the &#x60;parent&#x60; will be returned.
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
    body = QueryAssetsRequest.from_dict(body)
    return web.Response(status=200)


async def cloudasset_search_all_iam_policies(request: web.Request, scope, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, asset_types=None, order_by=None, page_size=None, page_token=None, query=None) -> web.Response:
    """cloudasset_search_all_iam_policies

    Searches all IAM policies within the specified scope, such as a project, folder, or organization. The caller must be granted the &#x60;cloudasset.assets.searchAllIamPolicies&#x60; permission on the desired scope, otherwise the request will be rejected.

    :param scope: Required. A scope can be a project, a folder, or an organization. The search is limited to the IAM policies within the &#x60;scope&#x60;. The caller must be granted the [&#x60;cloudasset.assets.searchAllIamPolicies&#x60;](https://cloud.google.com/asset-inventory/docs/access-control#required_permissions) permission on the desired scope. The allowed values are: * projects/{PROJECT_ID} (e.g., \&quot;projects/foo-bar\&quot;) * projects/{PROJECT_NUMBER} (e.g., \&quot;projects/12345678\&quot;) * folders/{FOLDER_NUMBER} (e.g., \&quot;folders/1234567\&quot;) * organizations/{ORGANIZATION_NUMBER} (e.g., \&quot;organizations/123456\&quot;)
    :type scope: str
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
    :param asset_types: Optional. A list of asset types that the IAM policies are attached to. If empty, it will search the IAM policies that are attached to all the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types) Regular expressions are also supported. For example: * \&quot;compute.googleapis.com.*\&quot; snapshots IAM policies attached to asset type starts with \&quot;compute.googleapis.com\&quot;. * \&quot;.*Instance\&quot; snapshots IAM policies attached to asset type ends with \&quot;Instance\&quot;. * \&quot;.*Instance.*\&quot; snapshots IAM policies attached to asset type contains \&quot;Instance\&quot;. See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.
    :type asset_types: List[str]
    :param order_by: Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add \&quot; DESC\&quot; after the field name to indicate descending order. Redundant space characters are ignored. Example: \&quot;assetType DESC, resource\&quot;. Only singular primitive fields in the response are sortable: * resource * assetType * project All the other fields such as repeated fields (e.g., &#x60;folders&#x60;) and non-primitive fields (e.g., &#x60;policy&#x60;) are not supported.
    :type order_by: str
    :param page_size: Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as &#x60;next_page_token&#x60; is returned.
    :type page_size: int
    :param page_token: Optional. If present, retrieve the next batch of results from the preceding call to this method. &#x60;page_token&#x60; must be the value of &#x60;next_page_token&#x60; from the previous response. The values of all other method parameters must be identical to those in the previous call.
    :type page_token: str
    :param query: Optional. The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-iam-policies#how_to_construct_a_query) for more information. If not specified or empty, it will search all the IAM policies within the specified &#x60;scope&#x60;. Note that the query string is compared against each IAM policy binding, including its principals, roles, and IAM conditions. The returned IAM policies will only contain the bindings that match your query. To learn more about the IAM policy structure, see the [IAM policy documentation](https://cloud.google.com/iam/help/allow-policies/structure). Examples: * &#x60;policy:amy@gmail.com&#x60; to find IAM policy bindings that specify user \&quot;amy@gmail.com\&quot;. * &#x60;policy:roles/compute.admin&#x60; to find IAM policy bindings that specify the Compute Admin role. * &#x60;policy:comp*&#x60; to find IAM policy bindings that contain \&quot;comp\&quot; as a prefix of any word in the binding. * &#x60;policy.role.permissions:storage.buckets.update&#x60; to find IAM policy bindings that specify a role containing \&quot;storage.buckets.update\&quot; permission. Note that if callers don&#39;t have &#x60;iam.roles.get&#x60; access to a role&#39;s included permissions, policy bindings that specify this role will be dropped from the search results. * &#x60;policy.role.permissions:upd*&#x60; to find IAM policy bindings that specify a role containing \&quot;upd\&quot; as a prefix of any word in the role permission. Note that if callers don&#39;t have &#x60;iam.roles.get&#x60; access to a role&#39;s included permissions, policy bindings that specify this role will be dropped from the search results. * &#x60;resource:organizations/123456&#x60; to find IAM policy bindings that are set on \&quot;organizations/123456\&quot;. * &#x60;resource&#x3D;//cloudresourcemanager.googleapis.com/projects/myproject&#x60; to find IAM policy bindings that are set on the project named \&quot;myproject\&quot;. * &#x60;Important&#x60; to find IAM policy bindings that contain \&quot;Important\&quot; as a word in any of the searchable fields (except for the included permissions). * &#x60;resource:(instance1 OR instance2) policy:amy&#x60; to find IAM policy bindings that are set on resources \&quot;instance1\&quot; or \&quot;instance2\&quot; and also specify user \&quot;amy\&quot;. * &#x60;roles:roles/compute.admin&#x60; to find IAM policy bindings that specify the Compute Admin role. * &#x60;memberTypes:user&#x60; to find IAM policy bindings that contain the principal type \&quot;user\&quot;.
    :type query: str

    """
    return web.Response(status=200)


async def cloudasset_search_all_resources(request: web.Request, scope, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, asset_types=None, order_by=None, page_size=None, page_token=None, query=None, read_mask=None) -> web.Response:
    """cloudasset_search_all_resources

    Searches all Google Cloud resources within the specified scope, such as a project, folder, or organization. The caller must be granted the &#x60;cloudasset.assets.searchAllResources&#x60; permission on the desired scope, otherwise the request will be rejected.

    :param scope: Required. A scope can be a project, a folder, or an organization. The search is limited to the resources within the &#x60;scope&#x60;. The caller must be granted the [&#x60;cloudasset.assets.searchAllResources&#x60;](https://cloud.google.com/asset-inventory/docs/access-control#required_permissions) permission on the desired scope. The allowed values are: * projects/{PROJECT_ID} (e.g., \&quot;projects/foo-bar\&quot;) * projects/{PROJECT_NUMBER} (e.g., \&quot;projects/12345678\&quot;) * folders/{FOLDER_NUMBER} (e.g., \&quot;folders/1234567\&quot;) * organizations/{ORGANIZATION_NUMBER} (e.g., \&quot;organizations/123456\&quot;)
    :type scope: str
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
    :param asset_types: Optional. A list of asset types that this request searches for. If empty, it will search all the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types). Regular expressions are also supported. For example: * \&quot;compute.googleapis.com.*\&quot; snapshots resources whose asset type starts with \&quot;compute.googleapis.com\&quot;. * \&quot;.*Instance\&quot; snapshots resources whose asset type ends with \&quot;Instance\&quot;. * \&quot;.*Instance.*\&quot; snapshots resources whose asset type contains \&quot;Instance\&quot;. See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.
    :type asset_types: List[str]
    :param order_by: Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add \&quot; DESC\&quot; after the field name to indicate descending order. Redundant space characters are ignored. Example: \&quot;location DESC, name\&quot;. Only the following fields in the response are sortable: * name * assetType * project * displayName * description * location * createTime * updateTime * state * parentFullResourceName * parentAssetType
    :type order_by: str
    :param page_size: Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as &#x60;next_page_token&#x60; is returned.
    :type page_size: int
    :param page_token: Optional. If present, then retrieve the next batch of results from the preceding call to this method. &#x60;page_token&#x60; must be the value of &#x60;next_page_token&#x60; from the previous response. The values of all other method parameters, must be identical to those in the previous call.
    :type page_token: str
    :param query: Optional. The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-resources#how_to_construct_a_query) for more information. If not specified or empty, it will search all the resources within the specified &#x60;scope&#x60;. Examples: * &#x60;name:Important&#x60; to find Google Cloud resources whose name contains &#x60;Important&#x60; as a word. * &#x60;name&#x3D;Important&#x60; to find the Google Cloud resource whose name is exactly &#x60;Important&#x60;. * &#x60;displayName:Impor*&#x60; to find Google Cloud resources whose display name contains &#x60;Impor&#x60; as a prefix of any word in the field. * &#x60;location:us-west*&#x60; to find Google Cloud resources whose location contains both &#x60;us&#x60; and &#x60;west&#x60; as prefixes. * &#x60;labels:prod&#x60; to find Google Cloud resources whose labels contain &#x60;prod&#x60; as a key or value. * &#x60;labels.env:prod&#x60; to find Google Cloud resources that have a label &#x60;env&#x60; and its value is &#x60;prod&#x60;. * &#x60;labels.env:*&#x60; to find Google Cloud resources that have a label &#x60;env&#x60;. * &#x60;tagKeys:env&#x60; to find Google Cloud resources that have directly attached tags where the [&#x60;TagKey.namespacedName&#x60;](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey) contains &#x60;env&#x60;. * &#x60;tagValues:prod*&#x60; to find Google Cloud resources that have directly attached tags where the [&#x60;TagValue.namespacedName&#x60;](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) contains a word prefixed by &#x60;prod&#x60;. * &#x60;tagValueIds&#x3D;tagValues/123&#x60; to find Google Cloud resources that have directly attached tags where the [&#x60;TagValue.name&#x60;](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) is exactly &#x60;tagValues/123&#x60;. * &#x60;effectiveTagKeys:env&#x60; to find Google Cloud resources that have directly attached or inherited tags where the [&#x60;TagKey.namespacedName&#x60;](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey) contains &#x60;env&#x60;. * &#x60;effectiveTagValues:prod*&#x60; to find Google Cloud resources that have directly attached or inherited tags where the [&#x60;TagValue.namespacedName&#x60;](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) contains a word prefixed by &#x60;prod&#x60;. * &#x60;effectiveTagValueIds&#x3D;tagValues/123&#x60; to find Google Cloud resources that have directly attached or inherited tags where the [&#x60;TagValue.name&#x60;](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) is exactly &#x60;tagValues/123&#x60;. * &#x60;kmsKey:key&#x60; to find Google Cloud resources encrypted with a customer-managed encryption key whose name contains &#x60;key&#x60; as a word. This field is deprecated. Use the &#x60;kmsKeys&#x60; field to retrieve Cloud KMS key information. * &#x60;kmsKeys:key&#x60; to find Google Cloud resources encrypted with customer-managed encryption keys whose name contains the word &#x60;key&#x60;. * &#x60;relationships:instance-group-1&#x60; to find Google Cloud resources that have relationships with &#x60;instance-group-1&#x60; in the related resource name. * &#x60;relationships:INSTANCE_TO_INSTANCEGROUP&#x60; to find Compute Engine instances that have relationships of type &#x60;INSTANCE_TO_INSTANCEGROUP&#x60;. * &#x60;relationships.INSTANCE_TO_INSTANCEGROUP:instance-group-1&#x60; to find Compute Engine instances that have relationships with &#x60;instance-group-1&#x60; in the Compute Engine instance group resource name, for relationship type &#x60;INSTANCE_TO_INSTANCEGROUP&#x60;. * &#x60;sccSecurityMarks.key&#x3D;value&#x60; to find Cloud resources that are attached with security marks whose key is &#x60;key&#x60; and value is &#x60;value&#x60;. * &#x60;sccSecurityMarks.key:*&#x60; to find Cloud resources that are attached with security marks whose key is &#x60;key&#x60;. * &#x60;state:ACTIVE&#x60; to find Google Cloud resources whose state contains &#x60;ACTIVE&#x60; as a word. * &#x60;NOT state:ACTIVE&#x60; to find Google Cloud resources whose state doesn&#39;t contain &#x60;ACTIVE&#x60; as a word. * &#x60;createTime&lt;1609459200&#x60; to find Google Cloud resources that were created before &#x60;2021-01-01 00:00:00 UTC&#x60;. &#x60;1609459200&#x60; is the epoch timestamp of &#x60;2021-01-01 00:00:00 UTC&#x60; in seconds. * &#x60;updateTime&gt;1609459200&#x60; to find Google Cloud resources that were updated after &#x60;2021-01-01 00:00:00 UTC&#x60;. &#x60;1609459200&#x60; is the epoch timestamp of &#x60;2021-01-01 00:00:00 UTC&#x60; in seconds. * &#x60;Important&#x60; to find Google Cloud resources that contain &#x60;Important&#x60; as a word in any of the searchable fields. * &#x60;Impor*&#x60; to find Google Cloud resources that contain &#x60;Impor&#x60; as a prefix of any word in any of the searchable fields. * &#x60;Important location:(us-west1 OR global)&#x60; to find Google Cloud resources that contain &#x60;Important&#x60; as a word in any of the searchable fields and are also located in the &#x60;us-west1&#x60; region or the &#x60;global&#x60; location.
    :type query: str
    :param read_mask: Optional. A comma-separated list of fields that you want returned in the results. The following fields are returned by default if not specified: * &#x60;name&#x60; * &#x60;assetType&#x60; * &#x60;project&#x60; * &#x60;folders&#x60; * &#x60;organization&#x60; * &#x60;displayName&#x60; * &#x60;description&#x60; * &#x60;location&#x60; * &#x60;labels&#x60; * &#x60;tags&#x60; * &#x60;effectiveTags&#x60; * &#x60;networkTags&#x60; * &#x60;kmsKeys&#x60; * &#x60;createTime&#x60; * &#x60;updateTime&#x60; * &#x60;state&#x60; * &#x60;additionalAttributes&#x60; * &#x60;parentFullResourceName&#x60; * &#x60;parentAssetType&#x60; Some fields of large size, such as &#x60;versionedResources&#x60;, &#x60;attachedResources&#x60;, &#x60;effectiveTags&#x60; etc., are not returned by default, but you can specify them in the &#x60;read_mask&#x60; parameter if you want to include them. If &#x60;\&quot;*\&quot;&#x60; is specified, all [available fields](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#resourcesearchresult) are returned. Examples: &#x60;\&quot;name,location\&quot;&#x60;, &#x60;\&quot;name,versionedResources\&quot;&#x60;, &#x60;\&quot;*\&quot;&#x60;. Any invalid field path will trigger INVALID_ARGUMENT error.
    :type read_mask: str

    """
    return web.Response(status=200)
