# V1Api

All URIs are relative to *https://cloudasset.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudassetAnalyzeIamPolicy**](V1Api.md#cloudassetAnalyzeIamPolicy) | **GET** /v1/{scope}:analyzeIamPolicy |  |
| [**cloudassetAnalyzeIamPolicyLongrunning**](V1Api.md#cloudassetAnalyzeIamPolicyLongrunning) | **POST** /v1/{scope}:analyzeIamPolicyLongrunning |  |
| [**cloudassetAnalyzeMove**](V1Api.md#cloudassetAnalyzeMove) | **GET** /v1/{resource}:analyzeMove |  |
| [**cloudassetAnalyzeOrgPolicies**](V1Api.md#cloudassetAnalyzeOrgPolicies) | **GET** /v1/{scope}:analyzeOrgPolicies |  |
| [**cloudassetAnalyzeOrgPolicyGovernedAssets**](V1Api.md#cloudassetAnalyzeOrgPolicyGovernedAssets) | **GET** /v1/{scope}:analyzeOrgPolicyGovernedAssets |  |
| [**cloudassetAnalyzeOrgPolicyGovernedContainers**](V1Api.md#cloudassetAnalyzeOrgPolicyGovernedContainers) | **GET** /v1/{scope}:analyzeOrgPolicyGovernedContainers |  |
| [**cloudassetBatchGetAssetsHistory**](V1Api.md#cloudassetBatchGetAssetsHistory) | **GET** /v1/{parent}:batchGetAssetsHistory |  |
| [**cloudassetExportAssets**](V1Api.md#cloudassetExportAssets) | **POST** /v1/{parent}:exportAssets |  |
| [**cloudassetQueryAssets**](V1Api.md#cloudassetQueryAssets) | **POST** /v1/{parent}:queryAssets |  |
| [**cloudassetSearchAllIamPolicies**](V1Api.md#cloudassetSearchAllIamPolicies) | **GET** /v1/{scope}:searchAllIamPolicies |  |
| [**cloudassetSearchAllResources**](V1Api.md#cloudassetSearchAllResources) | **GET** /v1/{scope}:searchAllResources |  |


<a id="cloudassetAnalyzeIamPolicy"></a>
# **cloudassetAnalyzeIamPolicy**
> AnalyzeIamPolicyResponse cloudassetAnalyzeIamPolicy(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, analysisQueryAccessSelectorPermissions, analysisQueryAccessSelectorRoles, analysisQueryConditionContextAccessTime, analysisQueryIdentitySelectorIdentity, analysisQueryOptionsAnalyzeServiceAccountImpersonation, analysisQueryOptionsExpandGroups, analysisQueryOptionsExpandResources, analysisQueryOptionsExpandRoles, analysisQueryOptionsOutputGroupEdges, analysisQueryOptionsOutputResourceEdges, analysisQueryResourceSelectorFullResourceName, executionTimeout, savedAnalysisQuery)



Analyzes IAM policies to answer which identities have what accesses on which resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudasset.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String scope = "scope_example"; // String | Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed. This can only be an organization number (such as \"organizations/123\"), a folder number (such as \"folders/123\"), a project ID (such as \"projects/my-project-id\"), or a project number (such as \"projects/12345\"). To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects).
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    List<String> analysisQueryAccessSelectorPermissions = Arrays.asList(); // List<String> | Optional. The permissions to appear in result.
    List<String> analysisQueryAccessSelectorRoles = Arrays.asList(); // List<String> | Optional. The roles to appear in result.
    String analysisQueryConditionContextAccessTime = "analysisQueryConditionContextAccessTime_example"; // String | The hypothetical access timestamp to evaluate IAM conditions. Note that this value must not be earlier than the current time; otherwise, an INVALID_ARGUMENT error will be returned.
    String analysisQueryIdentitySelectorIdentity = "analysisQueryIdentitySelectorIdentity_example"; // String | Required. The identity appear in the form of principals in [IAM policy binding](https://cloud.google.com/iam/reference/rest/v1/Binding). The examples of supported forms are: \"user:mike@example.com\", \"group:admins@example.com\", \"domain:google.com\", \"serviceAccount:my-project-id@appspot.gserviceaccount.com\". Notice that wildcard characters (such as * and ?) are not supported. You must give a specific identity.
    Boolean analysisQueryOptionsAnalyzeServiceAccountImpersonation = true; // Boolean | Optional. If true, the response will include access analysis from identities to resources via service account impersonation. This is a very expensive operation, because many derived queries will be executed. We highly recommend you use AssetService.AnalyzeIamPolicyLongrunning RPC instead. For example, if the request analyzes for which resources user A has permission P, and there's an IAM policy states user A has iam.serviceAccounts.getAccessToken permission to a service account SA, and there's another IAM policy states service account SA has permission P to a Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in AnalyzeIamPolicyResponse.service_account_impersonation_analysis. Another example, if the request analyzes for who has permission P to a Google Cloud folder F, and there's an IAM policy states user A has iam.serviceAccounts.actAs permission to a service account SA, and there's another IAM policy states service account SA has permission P to the Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in AnalyzeIamPolicyResponse.service_account_impersonation_analysis. Only the following permissions are considered in this analysis: * `iam.serviceAccounts.actAs` * `iam.serviceAccounts.signBlob` * `iam.serviceAccounts.signJwt` * `iam.serviceAccounts.getAccessToken` * `iam.serviceAccounts.getOpenIdToken` * `iam.serviceAccounts.implicitDelegation` Default is false.
    Boolean analysisQueryOptionsExpandGroups = true; // Boolean | Optional. If true, the identities section of the result will expand any Google groups appearing in an IAM policy binding. If IamPolicyAnalysisQuery.identity_selector is specified, the identity in the result will be determined by the selector, and this flag is not allowed to set. If true, the default max expansion per group is 1000 for AssetService.AnalyzeIamPolicy][]. Default is false.
    Boolean analysisQueryOptionsExpandResources = true; // Boolean | Optional. If true and IamPolicyAnalysisQuery.resource_selector is not specified, the resource section of the result will expand any resource attached to an IAM policy to include resources lower in the resource hierarchy. For example, if the request analyzes for which resources user A has permission P, and the results include an IAM policy with P on a Google Cloud folder, the results will also include resources in that folder with permission P. If true and IamPolicyAnalysisQuery.resource_selector is specified, the resource section of the result will expand the specified resource to include resources lower in the resource hierarchy. Only project or lower resources are supported. Folder and organization resources cannot be used together with this option. For example, if the request analyzes for which users have permission P on a Google Cloud project with this option enabled, the results will include all users who have permission P on that project or any lower resource. If true, the default max expansion per resource is 1000 for AssetService.AnalyzeIamPolicy][] and 100000 for AssetService.AnalyzeIamPolicyLongrunning][]. Default is false.
    Boolean analysisQueryOptionsExpandRoles = true; // Boolean | Optional. If true, the access section of result will expand any roles appearing in IAM policy bindings to include their permissions. If IamPolicyAnalysisQuery.access_selector is specified, the access section of the result will be determined by the selector, and this flag is not allowed to set. Default is false.
    Boolean analysisQueryOptionsOutputGroupEdges = true; // Boolean | Optional. If true, the result will output the relevant membership relationships between groups and other groups, and between groups and principals. Default is false.
    Boolean analysisQueryOptionsOutputResourceEdges = true; // Boolean | Optional. If true, the result will output the relevant parent/child relationships between resources. Default is false.
    String analysisQueryResourceSelectorFullResourceName = "analysisQueryResourceSelectorFullResourceName_example"; // String | Required. The [full resource name] (https://cloud.google.com/asset-inventory/docs/resource-name-format) of a resource of [supported resource types](https://cloud.google.com/asset-inventory/docs/supported-asset-types#analyzable_asset_types).
    String executionTimeout = "executionTimeout_example"; // String | Optional. Amount of time executable has to complete. See JSON representation of [Duration](https://developers.google.com/protocol-buffers/docs/proto3#json). If this field is set with a value less than the RPC deadline, and the execution of your query hasn't finished in the specified execution timeout, you will get a response with partial result. Otherwise, your query's execution will continue until the RPC deadline. If it's not finished until then, you will get a DEADLINE_EXCEEDED error. Default is empty.
    String savedAnalysisQuery = "savedAnalysisQuery_example"; // String | Optional. The name of a saved query, which must be in the format of: * projects/project_number/savedQueries/saved_query_id * folders/folder_number/savedQueries/saved_query_id * organizations/organization_number/savedQueries/saved_query_id If both `analysis_query` and `saved_analysis_query` are provided, they will be merged together with the `saved_analysis_query` as base and the `analysis_query` as overrides. For more details of the merge behavior, refer to the [MergeFrom](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details) page. Note that you cannot override primitive fields with default value, such as 0 or empty string, etc., because we use proto3, which doesn't support field presence yet.
    try {
      AnalyzeIamPolicyResponse result = apiInstance.cloudassetAnalyzeIamPolicy(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, analysisQueryAccessSelectorPermissions, analysisQueryAccessSelectorRoles, analysisQueryConditionContextAccessTime, analysisQueryIdentitySelectorIdentity, analysisQueryOptionsAnalyzeServiceAccountImpersonation, analysisQueryOptionsExpandGroups, analysisQueryOptionsExpandResources, analysisQueryOptionsExpandRoles, analysisQueryOptionsOutputGroupEdges, analysisQueryOptionsOutputResourceEdges, analysisQueryResourceSelectorFullResourceName, executionTimeout, savedAnalysisQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#cloudassetAnalyzeIamPolicy");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scope** | **String**| Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed. This can only be an organization number (such as \&quot;organizations/123\&quot;), a folder number (such as \&quot;folders/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;). To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **analysisQueryAccessSelectorPermissions** | [**List&lt;String&gt;**](String.md)| Optional. The permissions to appear in result. | [optional] |
| **analysisQueryAccessSelectorRoles** | [**List&lt;String&gt;**](String.md)| Optional. The roles to appear in result. | [optional] |
| **analysisQueryConditionContextAccessTime** | **String**| The hypothetical access timestamp to evaluate IAM conditions. Note that this value must not be earlier than the current time; otherwise, an INVALID_ARGUMENT error will be returned. | [optional] |
| **analysisQueryIdentitySelectorIdentity** | **String**| Required. The identity appear in the form of principals in [IAM policy binding](https://cloud.google.com/iam/reference/rest/v1/Binding). The examples of supported forms are: \&quot;user:mike@example.com\&quot;, \&quot;group:admins@example.com\&quot;, \&quot;domain:google.com\&quot;, \&quot;serviceAccount:my-project-id@appspot.gserviceaccount.com\&quot;. Notice that wildcard characters (such as * and ?) are not supported. You must give a specific identity. | [optional] |
| **analysisQueryOptionsAnalyzeServiceAccountImpersonation** | **Boolean**| Optional. If true, the response will include access analysis from identities to resources via service account impersonation. This is a very expensive operation, because many derived queries will be executed. We highly recommend you use AssetService.AnalyzeIamPolicyLongrunning RPC instead. For example, if the request analyzes for which resources user A has permission P, and there&#39;s an IAM policy states user A has iam.serviceAccounts.getAccessToken permission to a service account SA, and there&#39;s another IAM policy states service account SA has permission P to a Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in AnalyzeIamPolicyResponse.service_account_impersonation_analysis. Another example, if the request analyzes for who has permission P to a Google Cloud folder F, and there&#39;s an IAM policy states user A has iam.serviceAccounts.actAs permission to a service account SA, and there&#39;s another IAM policy states service account SA has permission P to the Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in AnalyzeIamPolicyResponse.service_account_impersonation_analysis. Only the following permissions are considered in this analysis: * &#x60;iam.serviceAccounts.actAs&#x60; * &#x60;iam.serviceAccounts.signBlob&#x60; * &#x60;iam.serviceAccounts.signJwt&#x60; * &#x60;iam.serviceAccounts.getAccessToken&#x60; * &#x60;iam.serviceAccounts.getOpenIdToken&#x60; * &#x60;iam.serviceAccounts.implicitDelegation&#x60; Default is false. | [optional] |
| **analysisQueryOptionsExpandGroups** | **Boolean**| Optional. If true, the identities section of the result will expand any Google groups appearing in an IAM policy binding. If IamPolicyAnalysisQuery.identity_selector is specified, the identity in the result will be determined by the selector, and this flag is not allowed to set. If true, the default max expansion per group is 1000 for AssetService.AnalyzeIamPolicy][]. Default is false. | [optional] |
| **analysisQueryOptionsExpandResources** | **Boolean**| Optional. If true and IamPolicyAnalysisQuery.resource_selector is not specified, the resource section of the result will expand any resource attached to an IAM policy to include resources lower in the resource hierarchy. For example, if the request analyzes for which resources user A has permission P, and the results include an IAM policy with P on a Google Cloud folder, the results will also include resources in that folder with permission P. If true and IamPolicyAnalysisQuery.resource_selector is specified, the resource section of the result will expand the specified resource to include resources lower in the resource hierarchy. Only project or lower resources are supported. Folder and organization resources cannot be used together with this option. For example, if the request analyzes for which users have permission P on a Google Cloud project with this option enabled, the results will include all users who have permission P on that project or any lower resource. If true, the default max expansion per resource is 1000 for AssetService.AnalyzeIamPolicy][] and 100000 for AssetService.AnalyzeIamPolicyLongrunning][]. Default is false. | [optional] |
| **analysisQueryOptionsExpandRoles** | **Boolean**| Optional. If true, the access section of result will expand any roles appearing in IAM policy bindings to include their permissions. If IamPolicyAnalysisQuery.access_selector is specified, the access section of the result will be determined by the selector, and this flag is not allowed to set. Default is false. | [optional] |
| **analysisQueryOptionsOutputGroupEdges** | **Boolean**| Optional. If true, the result will output the relevant membership relationships between groups and other groups, and between groups and principals. Default is false. | [optional] |
| **analysisQueryOptionsOutputResourceEdges** | **Boolean**| Optional. If true, the result will output the relevant parent/child relationships between resources. Default is false. | [optional] |
| **analysisQueryResourceSelectorFullResourceName** | **String**| Required. The [full resource name] (https://cloud.google.com/asset-inventory/docs/resource-name-format) of a resource of [supported resource types](https://cloud.google.com/asset-inventory/docs/supported-asset-types#analyzable_asset_types). | [optional] |
| **executionTimeout** | **String**| Optional. Amount of time executable has to complete. See JSON representation of [Duration](https://developers.google.com/protocol-buffers/docs/proto3#json). If this field is set with a value less than the RPC deadline, and the execution of your query hasn&#39;t finished in the specified execution timeout, you will get a response with partial result. Otherwise, your query&#39;s execution will continue until the RPC deadline. If it&#39;s not finished until then, you will get a DEADLINE_EXCEEDED error. Default is empty. | [optional] |
| **savedAnalysisQuery** | **String**| Optional. The name of a saved query, which must be in the format of: * projects/project_number/savedQueries/saved_query_id * folders/folder_number/savedQueries/saved_query_id * organizations/organization_number/savedQueries/saved_query_id If both &#x60;analysis_query&#x60; and &#x60;saved_analysis_query&#x60; are provided, they will be merged together with the &#x60;saved_analysis_query&#x60; as base and the &#x60;analysis_query&#x60; as overrides. For more details of the merge behavior, refer to the [MergeFrom](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details) page. Note that you cannot override primitive fields with default value, such as 0 or empty string, etc., because we use proto3, which doesn&#39;t support field presence yet. | [optional] |

### Return type

[**AnalyzeIamPolicyResponse**](AnalyzeIamPolicyResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudassetAnalyzeIamPolicyLongrunning"></a>
# **cloudassetAnalyzeIamPolicyLongrunning**
> Operation cloudassetAnalyzeIamPolicyLongrunning(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, analyzeIamPolicyLongrunningRequest)



Analyzes IAM policies asynchronously to answer which identities have what accesses on which resources, and writes the analysis results to a Google Cloud Storage or a BigQuery destination. For Cloud Storage destination, the output format is the JSON format that represents a AnalyzeIamPolicyResponse. This method implements the google.longrunning.Operation, which allows you to track the operation status. We recommend intervals of at least 2 seconds with exponential backoff retry to poll the operation result. The metadata contains the metadata for the long-running operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudasset.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String scope = "scope_example"; // String | Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed. This can only be an organization number (such as \"organizations/123\"), a folder number (such as \"folders/123\"), a project ID (such as \"projects/my-project-id\"), or a project number (such as \"projects/12345\"). To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects).
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    AnalyzeIamPolicyLongrunningRequest analyzeIamPolicyLongrunningRequest = new AnalyzeIamPolicyLongrunningRequest(); // AnalyzeIamPolicyLongrunningRequest | 
    try {
      Operation result = apiInstance.cloudassetAnalyzeIamPolicyLongrunning(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, analyzeIamPolicyLongrunningRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#cloudassetAnalyzeIamPolicyLongrunning");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scope** | **String**| Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed. This can only be an organization number (such as \&quot;organizations/123\&quot;), a folder number (such as \&quot;folders/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;). To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **analyzeIamPolicyLongrunningRequest** | [**AnalyzeIamPolicyLongrunningRequest**](AnalyzeIamPolicyLongrunningRequest.md)|  | [optional] |

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudassetAnalyzeMove"></a>
# **cloudassetAnalyzeMove**
> AnalyzeMoveResponse cloudassetAnalyzeMove(resource, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, destinationParent, view)



Analyze moving a resource to a specified destination without kicking off the actual move. The analysis is best effort depending on the user&#39;s permissions of viewing different hierarchical policies and configurations. The policies and configuration are subject to change before the actual resource migration takes place.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudasset.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String resource = "resource_example"; // String | Required. Name of the resource to perform the analysis against. Only Google Cloud projects are supported as of today. Hence, this can only be a project ID (such as \"projects/my-project-id\") or a project number (such as \"projects/12345\").
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String destinationParent = "destinationParent_example"; // String | Required. Name of the Google Cloud folder or organization to reparent the target resource. The analysis will be performed against hypothetically moving the resource to this specified desitination parent. This can only be a folder number (such as \"folders/123\") or an organization number (such as \"organizations/123\").
    String view = "ANALYSIS_VIEW_UNSPECIFIED"; // String | Analysis view indicating what information should be included in the analysis response. If unspecified, the default view is FULL.
    try {
      AnalyzeMoveResponse result = apiInstance.cloudassetAnalyzeMove(resource, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, destinationParent, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#cloudassetAnalyzeMove");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource** | **String**| Required. Name of the resource to perform the analysis against. Only Google Cloud projects are supported as of today. Hence, this can only be a project ID (such as \&quot;projects/my-project-id\&quot;) or a project number (such as \&quot;projects/12345\&quot;). | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **destinationParent** | **String**| Required. Name of the Google Cloud folder or organization to reparent the target resource. The analysis will be performed against hypothetically moving the resource to this specified desitination parent. This can only be a folder number (such as \&quot;folders/123\&quot;) or an organization number (such as \&quot;organizations/123\&quot;). | [optional] |
| **view** | **String**| Analysis view indicating what information should be included in the analysis response. If unspecified, the default view is FULL. | [optional] [enum: ANALYSIS_VIEW_UNSPECIFIED, FULL, BASIC] |

### Return type

[**AnalyzeMoveResponse**](AnalyzeMoveResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudassetAnalyzeOrgPolicies"></a>
# **cloudassetAnalyzeOrgPolicies**
> AnalyzeOrgPoliciesResponse cloudassetAnalyzeOrgPolicies(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, constraint, filter, pageSize, pageToken)



Analyzes organization policies under a scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudasset.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String scope = "scope_example"; // String | Required. The organization to scope the request. Only organization policies within the scope will be analyzed. * organizations/{ORGANIZATION_NUMBER} (e.g., \"organizations/123456\")
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String constraint = "constraint_example"; // String | Required. The name of the constraint to analyze organization policies for. The response only contains analyzed organization policies for the provided constraint.
    String filter = "filter_example"; // String | The expression to filter AnalyzeOrgPoliciesResponse.org_policy_results. Filtering is currently available for bare literal values and the following fields: * consolidated_policy.attached_resource * consolidated_policy.rules.enforce When filtering by a specific field, the only supported operator is `=`. For example, filtering by consolidated_policy.attached_resource=\"//cloudresourcemanager.googleapis.com/folders/001\" will return all the Organization Policy results attached to \"folders/001\".
    Integer pageSize = 56; // Integer | The maximum number of items to return per page. If unspecified, AnalyzeOrgPoliciesResponse.org_policy_results will contain 20 items with a maximum of 200.
    String pageToken = "pageToken_example"; // String | The pagination token to retrieve the next page.
    try {
      AnalyzeOrgPoliciesResponse result = apiInstance.cloudassetAnalyzeOrgPolicies(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, constraint, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#cloudassetAnalyzeOrgPolicies");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scope** | **String**| Required. The organization to scope the request. Only organization policies within the scope will be analyzed. * organizations/{ORGANIZATION_NUMBER} (e.g., \&quot;organizations/123456\&quot;) | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **constraint** | **String**| Required. The name of the constraint to analyze organization policies for. The response only contains analyzed organization policies for the provided constraint. | [optional] |
| **filter** | **String**| The expression to filter AnalyzeOrgPoliciesResponse.org_policy_results. Filtering is currently available for bare literal values and the following fields: * consolidated_policy.attached_resource * consolidated_policy.rules.enforce When filtering by a specific field, the only supported operator is &#x60;&#x3D;&#x60;. For example, filtering by consolidated_policy.attached_resource&#x3D;\&quot;//cloudresourcemanager.googleapis.com/folders/001\&quot; will return all the Organization Policy results attached to \&quot;folders/001\&quot;. | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return per page. If unspecified, AnalyzeOrgPoliciesResponse.org_policy_results will contain 20 items with a maximum of 200. | [optional] |
| **pageToken** | **String**| The pagination token to retrieve the next page. | [optional] |

### Return type

[**AnalyzeOrgPoliciesResponse**](AnalyzeOrgPoliciesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudassetAnalyzeOrgPolicyGovernedAssets"></a>
# **cloudassetAnalyzeOrgPolicyGovernedAssets**
> AnalyzeOrgPolicyGovernedAssetsResponse cloudassetAnalyzeOrgPolicyGovernedAssets(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, constraint, filter, pageSize, pageToken)



Analyzes organization policies governed assets (Google Cloud resources or policies) under a scope. This RPC supports custom constraints and the following canned constraints: * constraints/ainotebooks.accessMode * constraints/ainotebooks.disableFileDownloads * constraints/ainotebooks.disableRootAccess * constraints/ainotebooks.disableTerminal * constraints/ainotebooks.environmentOptions * constraints/ainotebooks.requireAutoUpgradeSchedule * constraints/ainotebooks.restrictVpcNetworks * constraints/compute.disableGuestAttributesAccess * constraints/compute.disableInstanceDataAccessApis * constraints/compute.disableNestedVirtualization * constraints/compute.disableSerialPortAccess * constraints/compute.disableSerialPortLogging * constraints/compute.disableVpcExternalIpv6 * constraints/compute.requireOsLogin * constraints/compute.requireShieldedVm * constraints/compute.restrictLoadBalancerCreationForTypes * constraints/compute.restrictProtocolForwardingCreationForTypes * constraints/compute.restrictXpnProjectLienRemoval * constraints/compute.setNewProjectDefaultToZonalDNSOnly * constraints/compute.skipDefaultNetworkCreation * constraints/compute.trustedImageProjects * constraints/compute.vmCanIpForward * constraints/compute.vmExternalIpAccess * constraints/gcp.detailedAuditLoggingMode * constraints/gcp.resourceLocations * constraints/iam.allowedPolicyMemberDomains * constraints/iam.automaticIamGrantsForDefaultServiceAccounts * constraints/iam.disableServiceAccountCreation * constraints/iam.disableServiceAccountKeyCreation * constraints/iam.disableServiceAccountKeyUpload * constraints/iam.restrictCrossProjectServiceAccountLienRemoval * constraints/iam.serviceAccountKeyExpiryHours * constraints/resourcemanager.accessBoundaries * constraints/resourcemanager.allowedExportDestinations * constraints/sql.restrictAuthorizedNetworks * constraints/sql.restrictNoncompliantDiagnosticDataAccess * constraints/sql.restrictNoncompliantResourceCreation * constraints/sql.restrictPublicIp * constraints/storage.publicAccessPrevention * constraints/storage.restrictAuthTypes * constraints/storage.uniformBucketLevelAccess This RPC only returns either resources of types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types) or IAM policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudasset.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String scope = "scope_example"; // String | Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output assets will also be limited to the ones governed by those in-scope organization policies. * organizations/{ORGANIZATION_NUMBER} (e.g., \"organizations/123456\")
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String constraint = "constraint_example"; // String | Required. The name of the constraint to analyze governed assets for. The analysis only contains analyzed organization policies for the provided constraint.
    String filter = "filter_example"; // String | The expression to filter AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets. For governed resources, filtering is currently available for bare literal values and the following fields: * governed_resource.project * governed_resource.folders * consolidated_policy.rules.enforce When filtering by `governed_resource.project` or `consolidated_policy.rules.enforce`, the only supported operator is `=`. When filtering by `governed_resource.folders`, the supported operators are `=` and `:`. For example, filtering by `governed_resource.project=\"projects/12345678\"` will return all the governed resources under \"projects/12345678\", including the project itself if applicable. For governed IAM policies, filtering is currently available for bare literal values and the following fields: * governed_iam_policy.project * governed_iam_policy.folders * consolidated_policy.rules.enforce When filtering by `governed_iam_policy.project` or `consolidated_policy.rules.enforce`, the only supported operator is `=`. When filtering by `governed_iam_policy.folders`, the supported operators are `=` and `:`. For example, filtering by `governed_iam_policy.folders:\"folders/12345678\"` will return all the governed IAM policies under \"folders/001\".
    Integer pageSize = 56; // Integer | The maximum number of items to return per page. If unspecified, AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets will contain 100 items with a maximum of 200.
    String pageToken = "pageToken_example"; // String | The pagination token to retrieve the next page.
    try {
      AnalyzeOrgPolicyGovernedAssetsResponse result = apiInstance.cloudassetAnalyzeOrgPolicyGovernedAssets(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, constraint, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#cloudassetAnalyzeOrgPolicyGovernedAssets");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scope** | **String**| Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output assets will also be limited to the ones governed by those in-scope organization policies. * organizations/{ORGANIZATION_NUMBER} (e.g., \&quot;organizations/123456\&quot;) | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **constraint** | **String**| Required. The name of the constraint to analyze governed assets for. The analysis only contains analyzed organization policies for the provided constraint. | [optional] |
| **filter** | **String**| The expression to filter AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets. For governed resources, filtering is currently available for bare literal values and the following fields: * governed_resource.project * governed_resource.folders * consolidated_policy.rules.enforce When filtering by &#x60;governed_resource.project&#x60; or &#x60;consolidated_policy.rules.enforce&#x60;, the only supported operator is &#x60;&#x3D;&#x60;. When filtering by &#x60;governed_resource.folders&#x60;, the supported operators are &#x60;&#x3D;&#x60; and &#x60;:&#x60;. For example, filtering by &#x60;governed_resource.project&#x3D;\&quot;projects/12345678\&quot;&#x60; will return all the governed resources under \&quot;projects/12345678\&quot;, including the project itself if applicable. For governed IAM policies, filtering is currently available for bare literal values and the following fields: * governed_iam_policy.project * governed_iam_policy.folders * consolidated_policy.rules.enforce When filtering by &#x60;governed_iam_policy.project&#x60; or &#x60;consolidated_policy.rules.enforce&#x60;, the only supported operator is &#x60;&#x3D;&#x60;. When filtering by &#x60;governed_iam_policy.folders&#x60;, the supported operators are &#x60;&#x3D;&#x60; and &#x60;:&#x60;. For example, filtering by &#x60;governed_iam_policy.folders:\&quot;folders/12345678\&quot;&#x60; will return all the governed IAM policies under \&quot;folders/001\&quot;. | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return per page. If unspecified, AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets will contain 100 items with a maximum of 200. | [optional] |
| **pageToken** | **String**| The pagination token to retrieve the next page. | [optional] |

### Return type

[**AnalyzeOrgPolicyGovernedAssetsResponse**](AnalyzeOrgPolicyGovernedAssetsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudassetAnalyzeOrgPolicyGovernedContainers"></a>
# **cloudassetAnalyzeOrgPolicyGovernedContainers**
> AnalyzeOrgPolicyGovernedContainersResponse cloudassetAnalyzeOrgPolicyGovernedContainers(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, constraint, filter, pageSize, pageToken)



Analyzes organization policies governed containers (projects, folders or organization) under a scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudasset.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String scope = "scope_example"; // String | Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output containers will also be limited to the ones governed by those in-scope organization policies. * organizations/{ORGANIZATION_NUMBER} (e.g., \"organizations/123456\")
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String constraint = "constraint_example"; // String | Required. The name of the constraint to analyze governed containers for. The analysis only contains organization policies for the provided constraint.
    String filter = "filter_example"; // String | The expression to filter AnalyzeOrgPolicyGovernedContainersResponse.governed_containers. Filtering is currently available for bare literal values and the following fields: * parent * consolidated_policy.rules.enforce When filtering by a specific field, the only supported operator is `=`. For example, filtering by parent=\"//cloudresourcemanager.googleapis.com/folders/001\" will return all the containers under \"folders/001\".
    Integer pageSize = 56; // Integer | The maximum number of items to return per page. If unspecified, AnalyzeOrgPolicyGovernedContainersResponse.governed_containers will contain 100 items with a maximum of 200.
    String pageToken = "pageToken_example"; // String | The pagination token to retrieve the next page.
    try {
      AnalyzeOrgPolicyGovernedContainersResponse result = apiInstance.cloudassetAnalyzeOrgPolicyGovernedContainers(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, constraint, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#cloudassetAnalyzeOrgPolicyGovernedContainers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scope** | **String**| Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output containers will also be limited to the ones governed by those in-scope organization policies. * organizations/{ORGANIZATION_NUMBER} (e.g., \&quot;organizations/123456\&quot;) | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **constraint** | **String**| Required. The name of the constraint to analyze governed containers for. The analysis only contains organization policies for the provided constraint. | [optional] |
| **filter** | **String**| The expression to filter AnalyzeOrgPolicyGovernedContainersResponse.governed_containers. Filtering is currently available for bare literal values and the following fields: * parent * consolidated_policy.rules.enforce When filtering by a specific field, the only supported operator is &#x60;&#x3D;&#x60;. For example, filtering by parent&#x3D;\&quot;//cloudresourcemanager.googleapis.com/folders/001\&quot; will return all the containers under \&quot;folders/001\&quot;. | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return per page. If unspecified, AnalyzeOrgPolicyGovernedContainersResponse.governed_containers will contain 100 items with a maximum of 200. | [optional] |
| **pageToken** | **String**| The pagination token to retrieve the next page. | [optional] |

### Return type

[**AnalyzeOrgPolicyGovernedContainersResponse**](AnalyzeOrgPolicyGovernedContainersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudassetBatchGetAssetsHistory"></a>
# **cloudassetBatchGetAssetsHistory**
> BatchGetAssetsHistoryResponse cloudassetBatchGetAssetsHistory(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, assetNames, contentType, readTimeWindowEndTime, readTimeWindowStartTime, relationshipTypes)



Batch gets the update history of assets that overlap a time window. For IAM_POLICY content, this API outputs history when the asset and its attached IAM POLICY both exist. This can create gaps in the output history. Otherwise, this API outputs history with asset in both non-delete or deleted status. If a specified asset does not exist, this API returns an INVALID_ARGUMENT error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudasset.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String parent = "parent_example"; // String | Required. The relative name of the root asset. It can only be an organization number (such as \"organizations/123\"), a project ID (such as \"projects/my-project-id\")\", or a project number (such as \"projects/12345\").
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    List<String> assetNames = Arrays.asList(); // List<String> | A list of the full names of the assets. See: https://cloud.google.com/asset-inventory/docs/resource-name-format Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. The request becomes a no-op if the asset name list is empty, and the max size of the asset name list is 100 in one request.
    String contentType = "CONTENT_TYPE_UNSPECIFIED"; // String | Optional. The content type.
    String readTimeWindowEndTime = "readTimeWindowEndTime_example"; // String | End time of the time window (inclusive). If not specified, the current timestamp is used instead.
    String readTimeWindowStartTime = "readTimeWindowStartTime_example"; // String | Start time of the time window (exclusive).
    List<String> relationshipTypes = Arrays.asList(); // List<String> | Optional. A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP. * If specified: it outputs specified relationships' history on the [asset_names]. It returns an error if any of the [relationship_types] doesn't belong to the supported relationship types of the [asset_names] or if any of the [asset_names]'s types doesn't belong to the source types of the [relationship_types]. * Otherwise: it outputs the supported relationships' history on the [asset_names] or returns an error if any of the [asset_names]'s types has no relationship support. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.
    try {
      BatchGetAssetsHistoryResponse result = apiInstance.cloudassetBatchGetAssetsHistory(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, assetNames, contentType, readTimeWindowEndTime, readTimeWindowStartTime, relationshipTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#cloudassetBatchGetAssetsHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The relative name of the root asset. It can only be an organization number (such as \&quot;organizations/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;)\&quot;, or a project number (such as \&quot;projects/12345\&quot;). | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **assetNames** | [**List&lt;String&gt;**](String.md)| A list of the full names of the assets. See: https://cloud.google.com/asset-inventory/docs/resource-name-format Example: &#x60;//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1&#x60;. The request becomes a no-op if the asset name list is empty, and the max size of the asset name list is 100 in one request. | [optional] |
| **contentType** | **String**| Optional. The content type. | [optional] [enum: CONTENT_TYPE_UNSPECIFIED, RESOURCE, IAM_POLICY, ORG_POLICY, ACCESS_POLICY, OS_INVENTORY, RELATIONSHIP] |
| **readTimeWindowEndTime** | **String**| End time of the time window (inclusive). If not specified, the current timestamp is used instead. | [optional] |
| **readTimeWindowStartTime** | **String**| Start time of the time window (exclusive). | [optional] |
| **relationshipTypes** | [**List&lt;String&gt;**](String.md)| Optional. A list of relationship types to output, for example: &#x60;INSTANCE_TO_INSTANCEGROUP&#x60;. This field should only be specified if content_type&#x3D;RELATIONSHIP. * If specified: it outputs specified relationships&#39; history on the [asset_names]. It returns an error if any of the [relationship_types] doesn&#39;t belong to the supported relationship types of the [asset_names] or if any of the [asset_names]&#39;s types doesn&#39;t belong to the source types of the [relationship_types]. * Otherwise: it outputs the supported relationships&#39; history on the [asset_names] or returns an error if any of the [asset_names]&#39;s types has no relationship support. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types. | [optional] |

### Return type

[**BatchGetAssetsHistoryResponse**](BatchGetAssetsHistoryResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudassetExportAssets"></a>
# **cloudassetExportAssets**
> Operation cloudassetExportAssets(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, exportAssetsRequest)



Exports assets with time and resource types to a given Cloud Storage location/BigQuery table. For Cloud Storage location destinations, the output format is newline-delimited JSON. Each line represents a google.cloud.asset.v1.Asset in the JSON format; for BigQuery table destinations, the output table stores the fields in asset Protobuf as columns. This API implements the google.longrunning.Operation API, which allows you to keep track of the export. We recommend intervals of at least 2 seconds with exponential retry to poll the export operation result. For regular-size resource parent, the export operation usually finishes within 5 minutes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudasset.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String parent = "parent_example"; // String | Required. The relative name of the root asset. This can only be an organization number (such as \"organizations/123\"), a project ID (such as \"projects/my-project-id\"), or a project number (such as \"projects/12345\"), or a folder number (such as \"folders/123\").
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    ExportAssetsRequest exportAssetsRequest = new ExportAssetsRequest(); // ExportAssetsRequest | 
    try {
      Operation result = apiInstance.cloudassetExportAssets(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, exportAssetsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#cloudassetExportAssets");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The relative name of the root asset. This can only be an organization number (such as \&quot;organizations/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;), or a folder number (such as \&quot;folders/123\&quot;). | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **exportAssetsRequest** | [**ExportAssetsRequest**](ExportAssetsRequest.md)|  | [optional] |

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudassetQueryAssets"></a>
# **cloudassetQueryAssets**
> QueryAssetsResponse cloudassetQueryAssets(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, queryAssetsRequest)



Issue a job that queries assets using a SQL statement compatible with [BigQuery SQL](https://cloud.google.com/bigquery/docs/introduction-sql). If the query execution finishes within timeout and there&#39;s no pagination, the full query results will be returned in the &#x60;QueryAssetsResponse&#x60;. Otherwise, full query results can be obtained by issuing extra requests with the &#x60;job_reference&#x60; from the a previous &#x60;QueryAssets&#x60; call. Note, the query result has approximately 10 GB limitation enforced by [BigQuery](https://cloud.google.com/bigquery/docs/best-practices-performance-output). Queries return larger results will result in errors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudasset.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String parent = "parent_example"; // String | Required. The relative name of the root asset. This can only be an organization number (such as \"organizations/123\"), a project ID (such as \"projects/my-project-id\"), or a project number (such as \"projects/12345\"), or a folder number (such as \"folders/123\"). Only assets belonging to the `parent` will be returned.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    QueryAssetsRequest queryAssetsRequest = new QueryAssetsRequest(); // QueryAssetsRequest | 
    try {
      QueryAssetsResponse result = apiInstance.cloudassetQueryAssets(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, queryAssetsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#cloudassetQueryAssets");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The relative name of the root asset. This can only be an organization number (such as \&quot;organizations/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;), or a folder number (such as \&quot;folders/123\&quot;). Only assets belonging to the &#x60;parent&#x60; will be returned. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **queryAssetsRequest** | [**QueryAssetsRequest**](QueryAssetsRequest.md)|  | [optional] |

### Return type

[**QueryAssetsResponse**](QueryAssetsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudassetSearchAllIamPolicies"></a>
# **cloudassetSearchAllIamPolicies**
> SearchAllIamPoliciesResponse cloudassetSearchAllIamPolicies(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, assetTypes, orderBy, pageSize, pageToken, query)



Searches all IAM policies within the specified scope, such as a project, folder, or organization. The caller must be granted the &#x60;cloudasset.assets.searchAllIamPolicies&#x60; permission on the desired scope, otherwise the request will be rejected.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudasset.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String scope = "scope_example"; // String | Required. A scope can be a project, a folder, or an organization. The search is limited to the IAM policies within the `scope`. The caller must be granted the [`cloudasset.assets.searchAllIamPolicies`](https://cloud.google.com/asset-inventory/docs/access-control#required_permissions) permission on the desired scope. The allowed values are: * projects/{PROJECT_ID} (e.g., \"projects/foo-bar\") * projects/{PROJECT_NUMBER} (e.g., \"projects/12345678\") * folders/{FOLDER_NUMBER} (e.g., \"folders/1234567\") * organizations/{ORGANIZATION_NUMBER} (e.g., \"organizations/123456\")
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    List<String> assetTypes = Arrays.asList(); // List<String> | Optional. A list of asset types that the IAM policies are attached to. If empty, it will search the IAM policies that are attached to all the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types) Regular expressions are also supported. For example: * \"compute.googleapis.com.*\" snapshots IAM policies attached to asset type starts with \"compute.googleapis.com\". * \".*Instance\" snapshots IAM policies attached to asset type ends with \"Instance\". * \".*Instance.*\" snapshots IAM policies attached to asset type contains \"Instance\". See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.
    String orderBy = "orderBy_example"; // String | Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add \" DESC\" after the field name to indicate descending order. Redundant space characters are ignored. Example: \"assetType DESC, resource\". Only singular primitive fields in the response are sortable: * resource * assetType * project All the other fields such as repeated fields (e.g., `folders`) and non-primitive fields (e.g., `policy`) are not supported.
    Integer pageSize = 56; // Integer | Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `next_page_token` is returned.
    String pageToken = "pageToken_example"; // String | Optional. If present, retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters must be identical to those in the previous call.
    String query = "query_example"; // String | Optional. The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-iam-policies#how_to_construct_a_query) for more information. If not specified or empty, it will search all the IAM policies within the specified `scope`. Note that the query string is compared against each IAM policy binding, including its principals, roles, and IAM conditions. The returned IAM policies will only contain the bindings that match your query. To learn more about the IAM policy structure, see the [IAM policy documentation](https://cloud.google.com/iam/help/allow-policies/structure). Examples: * `policy:amy@gmail.com` to find IAM policy bindings that specify user \"amy@gmail.com\". * `policy:roles/compute.admin` to find IAM policy bindings that specify the Compute Admin role. * `policy:comp*` to find IAM policy bindings that contain \"comp\" as a prefix of any word in the binding. * `policy.role.permissions:storage.buckets.update` to find IAM policy bindings that specify a role containing \"storage.buckets.update\" permission. Note that if callers don't have `iam.roles.get` access to a role's included permissions, policy bindings that specify this role will be dropped from the search results. * `policy.role.permissions:upd*` to find IAM policy bindings that specify a role containing \"upd\" as a prefix of any word in the role permission. Note that if callers don't have `iam.roles.get` access to a role's included permissions, policy bindings that specify this role will be dropped from the search results. * `resource:organizations/123456` to find IAM policy bindings that are set on \"organizations/123456\". * `resource=//cloudresourcemanager.googleapis.com/projects/myproject` to find IAM policy bindings that are set on the project named \"myproject\". * `Important` to find IAM policy bindings that contain \"Important\" as a word in any of the searchable fields (except for the included permissions). * `resource:(instance1 OR instance2) policy:amy` to find IAM policy bindings that are set on resources \"instance1\" or \"instance2\" and also specify user \"amy\". * `roles:roles/compute.admin` to find IAM policy bindings that specify the Compute Admin role. * `memberTypes:user` to find IAM policy bindings that contain the principal type \"user\".
    try {
      SearchAllIamPoliciesResponse result = apiInstance.cloudassetSearchAllIamPolicies(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, assetTypes, orderBy, pageSize, pageToken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#cloudassetSearchAllIamPolicies");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scope** | **String**| Required. A scope can be a project, a folder, or an organization. The search is limited to the IAM policies within the &#x60;scope&#x60;. The caller must be granted the [&#x60;cloudasset.assets.searchAllIamPolicies&#x60;](https://cloud.google.com/asset-inventory/docs/access-control#required_permissions) permission on the desired scope. The allowed values are: * projects/{PROJECT_ID} (e.g., \&quot;projects/foo-bar\&quot;) * projects/{PROJECT_NUMBER} (e.g., \&quot;projects/12345678\&quot;) * folders/{FOLDER_NUMBER} (e.g., \&quot;folders/1234567\&quot;) * organizations/{ORGANIZATION_NUMBER} (e.g., \&quot;organizations/123456\&quot;) | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **assetTypes** | [**List&lt;String&gt;**](String.md)| Optional. A list of asset types that the IAM policies are attached to. If empty, it will search the IAM policies that are attached to all the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types) Regular expressions are also supported. For example: * \&quot;compute.googleapis.com.*\&quot; snapshots IAM policies attached to asset type starts with \&quot;compute.googleapis.com\&quot;. * \&quot;.*Instance\&quot; snapshots IAM policies attached to asset type ends with \&quot;Instance\&quot;. * \&quot;.*Instance.*\&quot; snapshots IAM policies attached to asset type contains \&quot;Instance\&quot;. See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned. | [optional] |
| **orderBy** | **String**| Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add \&quot; DESC\&quot; after the field name to indicate descending order. Redundant space characters are ignored. Example: \&quot;assetType DESC, resource\&quot;. Only singular primitive fields in the response are sortable: * resource * assetType * project All the other fields such as repeated fields (e.g., &#x60;folders&#x60;) and non-primitive fields (e.g., &#x60;policy&#x60;) are not supported. | [optional] |
| **pageSize** | **Integer**| Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as &#x60;next_page_token&#x60; is returned. | [optional] |
| **pageToken** | **String**| Optional. If present, retrieve the next batch of results from the preceding call to this method. &#x60;page_token&#x60; must be the value of &#x60;next_page_token&#x60; from the previous response. The values of all other method parameters must be identical to those in the previous call. | [optional] |
| **query** | **String**| Optional. The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-iam-policies#how_to_construct_a_query) for more information. If not specified or empty, it will search all the IAM policies within the specified &#x60;scope&#x60;. Note that the query string is compared against each IAM policy binding, including its principals, roles, and IAM conditions. The returned IAM policies will only contain the bindings that match your query. To learn more about the IAM policy structure, see the [IAM policy documentation](https://cloud.google.com/iam/help/allow-policies/structure). Examples: * &#x60;policy:amy@gmail.com&#x60; to find IAM policy bindings that specify user \&quot;amy@gmail.com\&quot;. * &#x60;policy:roles/compute.admin&#x60; to find IAM policy bindings that specify the Compute Admin role. * &#x60;policy:comp*&#x60; to find IAM policy bindings that contain \&quot;comp\&quot; as a prefix of any word in the binding. * &#x60;policy.role.permissions:storage.buckets.update&#x60; to find IAM policy bindings that specify a role containing \&quot;storage.buckets.update\&quot; permission. Note that if callers don&#39;t have &#x60;iam.roles.get&#x60; access to a role&#39;s included permissions, policy bindings that specify this role will be dropped from the search results. * &#x60;policy.role.permissions:upd*&#x60; to find IAM policy bindings that specify a role containing \&quot;upd\&quot; as a prefix of any word in the role permission. Note that if callers don&#39;t have &#x60;iam.roles.get&#x60; access to a role&#39;s included permissions, policy bindings that specify this role will be dropped from the search results. * &#x60;resource:organizations/123456&#x60; to find IAM policy bindings that are set on \&quot;organizations/123456\&quot;. * &#x60;resource&#x3D;//cloudresourcemanager.googleapis.com/projects/myproject&#x60; to find IAM policy bindings that are set on the project named \&quot;myproject\&quot;. * &#x60;Important&#x60; to find IAM policy bindings that contain \&quot;Important\&quot; as a word in any of the searchable fields (except for the included permissions). * &#x60;resource:(instance1 OR instance2) policy:amy&#x60; to find IAM policy bindings that are set on resources \&quot;instance1\&quot; or \&quot;instance2\&quot; and also specify user \&quot;amy\&quot;. * &#x60;roles:roles/compute.admin&#x60; to find IAM policy bindings that specify the Compute Admin role. * &#x60;memberTypes:user&#x60; to find IAM policy bindings that contain the principal type \&quot;user\&quot;. | [optional] |

### Return type

[**SearchAllIamPoliciesResponse**](SearchAllIamPoliciesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudassetSearchAllResources"></a>
# **cloudassetSearchAllResources**
> SearchAllResourcesResponse cloudassetSearchAllResources(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, assetTypes, orderBy, pageSize, pageToken, query, readMask)



Searches all Google Cloud resources within the specified scope, such as a project, folder, or organization. The caller must be granted the &#x60;cloudasset.assets.searchAllResources&#x60; permission on the desired scope, otherwise the request will be rejected.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudasset.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String scope = "scope_example"; // String | Required. A scope can be a project, a folder, or an organization. The search is limited to the resources within the `scope`. The caller must be granted the [`cloudasset.assets.searchAllResources`](https://cloud.google.com/asset-inventory/docs/access-control#required_permissions) permission on the desired scope. The allowed values are: * projects/{PROJECT_ID} (e.g., \"projects/foo-bar\") * projects/{PROJECT_NUMBER} (e.g., \"projects/12345678\") * folders/{FOLDER_NUMBER} (e.g., \"folders/1234567\") * organizations/{ORGANIZATION_NUMBER} (e.g., \"organizations/123456\")
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    List<String> assetTypes = Arrays.asList(); // List<String> | Optional. A list of asset types that this request searches for. If empty, it will search all the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types). Regular expressions are also supported. For example: * \"compute.googleapis.com.*\" snapshots resources whose asset type starts with \"compute.googleapis.com\". * \".*Instance\" snapshots resources whose asset type ends with \"Instance\". * \".*Instance.*\" snapshots resources whose asset type contains \"Instance\". See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.
    String orderBy = "orderBy_example"; // String | Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add \" DESC\" after the field name to indicate descending order. Redundant space characters are ignored. Example: \"location DESC, name\". Only the following fields in the response are sortable: * name * assetType * project * displayName * description * location * createTime * updateTime * state * parentFullResourceName * parentAssetType
    Integer pageSize = 56; // Integer | Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `next_page_token` is returned.
    String pageToken = "pageToken_example"; // String | Optional. If present, then retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters, must be identical to those in the previous call.
    String query = "query_example"; // String | Optional. The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-resources#how_to_construct_a_query) for more information. If not specified or empty, it will search all the resources within the specified `scope`. Examples: * `name:Important` to find Google Cloud resources whose name contains `Important` as a word. * `name=Important` to find the Google Cloud resource whose name is exactly `Important`. * `displayName:Impor*` to find Google Cloud resources whose display name contains `Impor` as a prefix of any word in the field. * `location:us-west*` to find Google Cloud resources whose location contains both `us` and `west` as prefixes. * `labels:prod` to find Google Cloud resources whose labels contain `prod` as a key or value. * `labels.env:prod` to find Google Cloud resources that have a label `env` and its value is `prod`. * `labels.env:*` to find Google Cloud resources that have a label `env`. * `tagKeys:env` to find Google Cloud resources that have directly attached tags where the [`TagKey.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey) contains `env`. * `tagValues:prod*` to find Google Cloud resources that have directly attached tags where the [`TagValue.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) contains a word prefixed by `prod`. * `tagValueIds=tagValues/123` to find Google Cloud resources that have directly attached tags where the [`TagValue.name`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) is exactly `tagValues/123`. * `effectiveTagKeys:env` to find Google Cloud resources that have directly attached or inherited tags where the [`TagKey.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey) contains `env`. * `effectiveTagValues:prod*` to find Google Cloud resources that have directly attached or inherited tags where the [`TagValue.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) contains a word prefixed by `prod`. * `effectiveTagValueIds=tagValues/123` to find Google Cloud resources that have directly attached or inherited tags where the [`TagValue.name`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) is exactly `tagValues/123`. * `kmsKey:key` to find Google Cloud resources encrypted with a customer-managed encryption key whose name contains `key` as a word. This field is deprecated. Use the `kmsKeys` field to retrieve Cloud KMS key information. * `kmsKeys:key` to find Google Cloud resources encrypted with customer-managed encryption keys whose name contains the word `key`. * `relationships:instance-group-1` to find Google Cloud resources that have relationships with `instance-group-1` in the related resource name. * `relationships:INSTANCE_TO_INSTANCEGROUP` to find Compute Engine instances that have relationships of type `INSTANCE_TO_INSTANCEGROUP`. * `relationships.INSTANCE_TO_INSTANCEGROUP:instance-group-1` to find Compute Engine instances that have relationships with `instance-group-1` in the Compute Engine instance group resource name, for relationship type `INSTANCE_TO_INSTANCEGROUP`. * `sccSecurityMarks.key=value` to find Cloud resources that are attached with security marks whose key is `key` and value is `value`. * `sccSecurityMarks.key:*` to find Cloud resources that are attached with security marks whose key is `key`. * `state:ACTIVE` to find Google Cloud resources whose state contains `ACTIVE` as a word. * `NOT state:ACTIVE` to find Google Cloud resources whose state doesn't contain `ACTIVE` as a word. * `createTime<1609459200` to find Google Cloud resources that were created before `2021-01-01 00:00:00 UTC`. `1609459200` is the epoch timestamp of `2021-01-01 00:00:00 UTC` in seconds. * `updateTime>1609459200` to find Google Cloud resources that were updated after `2021-01-01 00:00:00 UTC`. `1609459200` is the epoch timestamp of `2021-01-01 00:00:00 UTC` in seconds. * `Important` to find Google Cloud resources that contain `Important` as a word in any of the searchable fields. * `Impor*` to find Google Cloud resources that contain `Impor` as a prefix of any word in any of the searchable fields. * `Important location:(us-west1 OR global)` to find Google Cloud resources that contain `Important` as a word in any of the searchable fields and are also located in the `us-west1` region or the `global` location.
    String readMask = "readMask_example"; // String | Optional. A comma-separated list of fields that you want returned in the results. The following fields are returned by default if not specified: * `name` * `assetType` * `project` * `folders` * `organization` * `displayName` * `description` * `location` * `labels` * `tags` * `effectiveTags` * `networkTags` * `kmsKeys` * `createTime` * `updateTime` * `state` * `additionalAttributes` * `parentFullResourceName` * `parentAssetType` Some fields of large size, such as `versionedResources`, `attachedResources`, `effectiveTags` etc., are not returned by default, but you can specify them in the `read_mask` parameter if you want to include them. If `\"*\"` is specified, all [available fields](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#resourcesearchresult) are returned. Examples: `\"name,location\"`, `\"name,versionedResources\"`, `\"*\"`. Any invalid field path will trigger INVALID_ARGUMENT error.
    try {
      SearchAllResourcesResponse result = apiInstance.cloudassetSearchAllResources(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, assetTypes, orderBy, pageSize, pageToken, query, readMask);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#cloudassetSearchAllResources");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scope** | **String**| Required. A scope can be a project, a folder, or an organization. The search is limited to the resources within the &#x60;scope&#x60;. The caller must be granted the [&#x60;cloudasset.assets.searchAllResources&#x60;](https://cloud.google.com/asset-inventory/docs/access-control#required_permissions) permission on the desired scope. The allowed values are: * projects/{PROJECT_ID} (e.g., \&quot;projects/foo-bar\&quot;) * projects/{PROJECT_NUMBER} (e.g., \&quot;projects/12345678\&quot;) * folders/{FOLDER_NUMBER} (e.g., \&quot;folders/1234567\&quot;) * organizations/{ORGANIZATION_NUMBER} (e.g., \&quot;organizations/123456\&quot;) | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **assetTypes** | [**List&lt;String&gt;**](String.md)| Optional. A list of asset types that this request searches for. If empty, it will search all the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types). Regular expressions are also supported. For example: * \&quot;compute.googleapis.com.*\&quot; snapshots resources whose asset type starts with \&quot;compute.googleapis.com\&quot;. * \&quot;.*Instance\&quot; snapshots resources whose asset type ends with \&quot;Instance\&quot;. * \&quot;.*Instance.*\&quot; snapshots resources whose asset type contains \&quot;Instance\&quot;. See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned. | [optional] |
| **orderBy** | **String**| Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add \&quot; DESC\&quot; after the field name to indicate descending order. Redundant space characters are ignored. Example: \&quot;location DESC, name\&quot;. Only the following fields in the response are sortable: * name * assetType * project * displayName * description * location * createTime * updateTime * state * parentFullResourceName * parentAssetType | [optional] |
| **pageSize** | **Integer**| Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as &#x60;next_page_token&#x60; is returned. | [optional] |
| **pageToken** | **String**| Optional. If present, then retrieve the next batch of results from the preceding call to this method. &#x60;page_token&#x60; must be the value of &#x60;next_page_token&#x60; from the previous response. The values of all other method parameters, must be identical to those in the previous call. | [optional] |
| **query** | **String**| Optional. The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-resources#how_to_construct_a_query) for more information. If not specified or empty, it will search all the resources within the specified &#x60;scope&#x60;. Examples: * &#x60;name:Important&#x60; to find Google Cloud resources whose name contains &#x60;Important&#x60; as a word. * &#x60;name&#x3D;Important&#x60; to find the Google Cloud resource whose name is exactly &#x60;Important&#x60;. * &#x60;displayName:Impor*&#x60; to find Google Cloud resources whose display name contains &#x60;Impor&#x60; as a prefix of any word in the field. * &#x60;location:us-west*&#x60; to find Google Cloud resources whose location contains both &#x60;us&#x60; and &#x60;west&#x60; as prefixes. * &#x60;labels:prod&#x60; to find Google Cloud resources whose labels contain &#x60;prod&#x60; as a key or value. * &#x60;labels.env:prod&#x60; to find Google Cloud resources that have a label &#x60;env&#x60; and its value is &#x60;prod&#x60;. * &#x60;labels.env:*&#x60; to find Google Cloud resources that have a label &#x60;env&#x60;. * &#x60;tagKeys:env&#x60; to find Google Cloud resources that have directly attached tags where the [&#x60;TagKey.namespacedName&#x60;](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey) contains &#x60;env&#x60;. * &#x60;tagValues:prod*&#x60; to find Google Cloud resources that have directly attached tags where the [&#x60;TagValue.namespacedName&#x60;](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) contains a word prefixed by &#x60;prod&#x60;. * &#x60;tagValueIds&#x3D;tagValues/123&#x60; to find Google Cloud resources that have directly attached tags where the [&#x60;TagValue.name&#x60;](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) is exactly &#x60;tagValues/123&#x60;. * &#x60;effectiveTagKeys:env&#x60; to find Google Cloud resources that have directly attached or inherited tags where the [&#x60;TagKey.namespacedName&#x60;](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey) contains &#x60;env&#x60;. * &#x60;effectiveTagValues:prod*&#x60; to find Google Cloud resources that have directly attached or inherited tags where the [&#x60;TagValue.namespacedName&#x60;](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) contains a word prefixed by &#x60;prod&#x60;. * &#x60;effectiveTagValueIds&#x3D;tagValues/123&#x60; to find Google Cloud resources that have directly attached or inherited tags where the [&#x60;TagValue.name&#x60;](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) is exactly &#x60;tagValues/123&#x60;. * &#x60;kmsKey:key&#x60; to find Google Cloud resources encrypted with a customer-managed encryption key whose name contains &#x60;key&#x60; as a word. This field is deprecated. Use the &#x60;kmsKeys&#x60; field to retrieve Cloud KMS key information. * &#x60;kmsKeys:key&#x60; to find Google Cloud resources encrypted with customer-managed encryption keys whose name contains the word &#x60;key&#x60;. * &#x60;relationships:instance-group-1&#x60; to find Google Cloud resources that have relationships with &#x60;instance-group-1&#x60; in the related resource name. * &#x60;relationships:INSTANCE_TO_INSTANCEGROUP&#x60; to find Compute Engine instances that have relationships of type &#x60;INSTANCE_TO_INSTANCEGROUP&#x60;. * &#x60;relationships.INSTANCE_TO_INSTANCEGROUP:instance-group-1&#x60; to find Compute Engine instances that have relationships with &#x60;instance-group-1&#x60; in the Compute Engine instance group resource name, for relationship type &#x60;INSTANCE_TO_INSTANCEGROUP&#x60;. * &#x60;sccSecurityMarks.key&#x3D;value&#x60; to find Cloud resources that are attached with security marks whose key is &#x60;key&#x60; and value is &#x60;value&#x60;. * &#x60;sccSecurityMarks.key:*&#x60; to find Cloud resources that are attached with security marks whose key is &#x60;key&#x60;. * &#x60;state:ACTIVE&#x60; to find Google Cloud resources whose state contains &#x60;ACTIVE&#x60; as a word. * &#x60;NOT state:ACTIVE&#x60; to find Google Cloud resources whose state doesn&#39;t contain &#x60;ACTIVE&#x60; as a word. * &#x60;createTime&lt;1609459200&#x60; to find Google Cloud resources that were created before &#x60;2021-01-01 00:00:00 UTC&#x60;. &#x60;1609459200&#x60; is the epoch timestamp of &#x60;2021-01-01 00:00:00 UTC&#x60; in seconds. * &#x60;updateTime&gt;1609459200&#x60; to find Google Cloud resources that were updated after &#x60;2021-01-01 00:00:00 UTC&#x60;. &#x60;1609459200&#x60; is the epoch timestamp of &#x60;2021-01-01 00:00:00 UTC&#x60; in seconds. * &#x60;Important&#x60; to find Google Cloud resources that contain &#x60;Important&#x60; as a word in any of the searchable fields. * &#x60;Impor*&#x60; to find Google Cloud resources that contain &#x60;Impor&#x60; as a prefix of any word in any of the searchable fields. * &#x60;Important location:(us-west1 OR global)&#x60; to find Google Cloud resources that contain &#x60;Important&#x60; as a word in any of the searchable fields and are also located in the &#x60;us-west1&#x60; region or the &#x60;global&#x60; location. | [optional] |
| **readMask** | **String**| Optional. A comma-separated list of fields that you want returned in the results. The following fields are returned by default if not specified: * &#x60;name&#x60; * &#x60;assetType&#x60; * &#x60;project&#x60; * &#x60;folders&#x60; * &#x60;organization&#x60; * &#x60;displayName&#x60; * &#x60;description&#x60; * &#x60;location&#x60; * &#x60;labels&#x60; * &#x60;tags&#x60; * &#x60;effectiveTags&#x60; * &#x60;networkTags&#x60; * &#x60;kmsKeys&#x60; * &#x60;createTime&#x60; * &#x60;updateTime&#x60; * &#x60;state&#x60; * &#x60;additionalAttributes&#x60; * &#x60;parentFullResourceName&#x60; * &#x60;parentAssetType&#x60; Some fields of large size, such as &#x60;versionedResources&#x60;, &#x60;attachedResources&#x60;, &#x60;effectiveTags&#x60; etc., are not returned by default, but you can specify them in the &#x60;read_mask&#x60; parameter if you want to include them. If &#x60;\&quot;*\&quot;&#x60; is specified, all [available fields](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#resourcesearchresult) are returned. Examples: &#x60;\&quot;name,location\&quot;&#x60;, &#x60;\&quot;name,versionedResources\&quot;&#x60;, &#x60;\&quot;*\&quot;&#x60;. Any invalid field path will trigger INVALID_ARGUMENT error. | [optional] |

### Return type

[**SearchAllResourcesResponse**](SearchAllResourcesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

