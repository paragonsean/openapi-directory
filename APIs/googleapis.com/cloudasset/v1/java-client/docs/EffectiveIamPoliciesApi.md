# EffectiveIamPoliciesApi

All URIs are relative to *https://cloudasset.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudassetEffectiveIamPoliciesBatchGet**](EffectiveIamPoliciesApi.md#cloudassetEffectiveIamPoliciesBatchGet) | **GET** /v1/{scope}/effectiveIamPolicies:batchGet |  |


<a id="cloudassetEffectiveIamPoliciesBatchGet"></a>
# **cloudassetEffectiveIamPoliciesBatchGet**
> BatchGetEffectiveIamPoliciesResponse cloudassetEffectiveIamPoliciesBatchGet(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, names)



Gets effective IAM policies for a batch of resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EffectiveIamPoliciesApi;

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

    EffectiveIamPoliciesApi apiInstance = new EffectiveIamPoliciesApi(defaultClient);
    String scope = "scope_example"; // String | Required. Only IAM policies on or below the scope will be returned. This can only be an organization number (such as \"organizations/123\"), a folder number (such as \"folders/123\"), a project ID (such as \"projects/my-project-id\"), or a project number (such as \"projects/12345\"). To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects).
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
    List<String> names = Arrays.asList(); // List<String> | Required. The names refer to the [full_resource_names] (https://cloud.google.com/asset-inventory/docs/resource-name-format) of the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types). A maximum of 20 resources' effective policies can be retrieved in a batch.
    try {
      BatchGetEffectiveIamPoliciesResponse result = apiInstance.cloudassetEffectiveIamPoliciesBatchGet(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, names);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EffectiveIamPoliciesApi#cloudassetEffectiveIamPoliciesBatchGet");
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
| **scope** | **String**| Required. Only IAM policies on or below the scope will be returned. This can only be an organization number (such as \&quot;organizations/123\&quot;), a folder number (such as \&quot;folders/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;). To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). | |
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
| **names** | [**List&lt;String&gt;**](String.md)| Required. The names refer to the [full_resource_names] (https://cloud.google.com/asset-inventory/docs/resource-name-format) of the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types). A maximum of 20 resources&#39; effective policies can be retrieved in a batch. | [optional] |

### Return type

[**BatchGetEffectiveIamPoliciesResponse**](BatchGetEffectiveIamPoliciesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

