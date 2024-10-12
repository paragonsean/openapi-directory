from typing import List, Dict
from aiohttp import web

from openapi_server.models.analyze_iam_policy_response import AnalyzeIamPolicyResponse
from openapi_server.models.export_iam_policy_analysis_request import ExportIamPolicyAnalysisRequest
from openapi_server.models.operation import Operation
from openapi_server import util


async def cloudasset_analyze_iam_policy(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, analysis_query_access_selector_permissions=None, analysis_query_access_selector_roles=None, analysis_query_identity_selector_identity=None, analysis_query_resource_selector_full_resource_name=None, options_analyze_service_account_impersonation=None, options_execution_timeout=None, options_expand_groups=None, options_expand_resources=None, options_expand_roles=None, options_output_group_edges=None, options_output_resource_edges=None) -> web.Response:
    """cloudasset_analyze_iam_policy

    Analyzes IAM policies to answer which identities have what accesses on which resources.

    :param parent: Required. The relative name of the root asset. Only resources and IAM policies within the parent will be analyzed. This can only be an organization number (such as \&quot;organizations/123\&quot;), a folder number (such as \&quot;folders/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;). To know how to get organization id, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). To know how to get folder or project id, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects).
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
    :param analysis_query_access_selector_permissions: Optional. The permissions to appear in result.
    :type analysis_query_access_selector_permissions: List[str]
    :param analysis_query_access_selector_roles: Optional. The roles to appear in result.
    :type analysis_query_access_selector_roles: List[str]
    :param analysis_query_identity_selector_identity: Required. The identity appear in the form of members in [IAM policy binding](https://cloud.google.com/iam/reference/rest/v1/Binding). The examples of supported forms are: \&quot;user:mike@example.com\&quot;, \&quot;group:admins@example.com\&quot;, \&quot;domain:google.com\&quot;, \&quot;serviceAccount:my-project-id@appspot.gserviceaccount.com\&quot;. Notice that wildcard characters (such as * and ?) are not supported. You must give a specific identity.
    :type analysis_query_identity_selector_identity: str
    :param analysis_query_resource_selector_full_resource_name: Required. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of a resource of [supported resource types](https://cloud.google.com/asset-inventory/docs/supported-asset-types#analyzable_asset_types).
    :type analysis_query_resource_selector_full_resource_name: str
    :param options_analyze_service_account_impersonation: Optional. If true, the response will include access analysis from identities to resources via service account impersonation. This is a very expensive operation, because many derived queries will be executed. We highly recommend you use AssetService.ExportIamPolicyAnalysis rpc instead. For example, if the request analyzes for which resources user A has permission P, and there&#39;s an IAM policy states user A has iam.serviceAccounts.getAccessToken permission to a service account SA, and there&#39;s another IAM policy states service account SA has permission P to a GCP folder F, then user A potentially has access to the GCP folder F. And those advanced analysis results will be included in AnalyzeIamPolicyResponse.service_account_impersonation_analysis. Another example, if the request analyzes for who has permission P to a GCP folder F, and there&#39;s an IAM policy states user A has iam.serviceAccounts.actAs permission to a service account SA, and there&#39;s another IAM policy states service account SA has permission P to the GCP folder F, then user A potentially has access to the GCP folder F. And those advanced analysis results will be included in AnalyzeIamPolicyResponse.service_account_impersonation_analysis. Default is false.
    :type options_analyze_service_account_impersonation: bool
    :param options_execution_timeout: Optional. Amount of time executable has to complete. See JSON representation of [Duration](https://developers.google.com/protocol-buffers/docs/proto3#json). If this field is set with a value less than the RPC deadline, and the execution of your query hasn&#39;t finished in the specified execution timeout, you will get a response with partial result. Otherwise, your query&#39;s execution will continue until the RPC deadline. If it&#39;s not finished until then, you will get a DEADLINE_EXCEEDED error. Default is empty.
    :type options_execution_timeout: str
    :param options_expand_groups: Optional. If true, the identities section of the result will expand any Google groups appearing in an IAM policy binding. If identity_selector is specified, the identity in the result will be determined by the selector, and this flag will have no effect. Default is false.
    :type options_expand_groups: bool
    :param options_expand_resources: Optional. If true, the resource section of the result will expand any resource attached to an IAM policy to include resources lower in the resource hierarchy. For example, if the request analyzes for which resources user A has permission P, and the results include an IAM policy with P on a GCP folder, the results will also include resources in that folder with permission P. If resource_selector is specified, the resource section of the result will be determined by the selector, and this flag will have no effect. Default is false.
    :type options_expand_resources: bool
    :param options_expand_roles: Optional. If true, the access section of result will expand any roles appearing in IAM policy bindings to include their permissions. If access_selector is specified, the access section of the result will be determined by the selector, and this flag will have no effect. Default is false.
    :type options_expand_roles: bool
    :param options_output_group_edges: Optional. If true, the result will output group identity edges, starting from the binding&#39;s group members, to any expanded identities. Default is false.
    :type options_output_group_edges: bool
    :param options_output_resource_edges: Optional. If true, the result will output resource edges, starting from the policy attached resource, to any expanded resources. Default is false.
    :type options_output_resource_edges: bool

    """
    return web.Response(status=200)


async def cloudasset_export_iam_policy_analysis(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudasset_export_iam_policy_analysis

    Exports the answers of which identities have what accesses on which resources to a Google Cloud Storage destination. The output format is the JSON format that represents a AnalyzeIamPolicyResponse in the JSON format. This method implements the google.longrunning.Operation, which allows you to keep track of the export. We recommend intervals of at least 2 seconds with exponential retry to poll the export operation result. The metadata contains the request to help callers to map responses to requests.

    :param parent: Required. The relative name of the root asset. Only resources and IAM policies within the parent will be analyzed. This can only be an organization number (such as \&quot;organizations/123\&quot;), a folder number (such as \&quot;folders/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;). To know how to get organization id, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). To know how to get folder or project id, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects).
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
    body = ExportIamPolicyAnalysisRequest.from_dict(body)
    return web.Response(status=200)
