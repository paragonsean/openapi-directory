# OrganizationsApi

All URIs are relative to *https://kmsinventory.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**kmsinventoryOrganizationsProtectedResourcesSearch**](OrganizationsApi.md#kmsinventoryOrganizationsProtectedResourcesSearch) | **GET** /v1/{scope}/protectedResources:search |  |


<a id="kmsinventoryOrganizationsProtectedResourcesSearch"></a>
# **kmsinventoryOrganizationsProtectedResourcesSearch**
> GoogleCloudKmsInventoryV1SearchProtectedResourcesResponse kmsinventoryOrganizationsProtectedResourcesSearch(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, cryptoKey, pageSize, pageToken, resourceTypes)



Returns metadata about the resources protected by the given Cloud KMS CryptoKey in the given Cloud organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kmsinventory.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String scope = "scope_example"; // String | Required. Resource name of the organization. Example: organizations/123
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
    String cryptoKey = "cryptoKey_example"; // String | Required. The resource name of the CryptoKey.
    Integer pageSize = 56; // Integer | The maximum number of resources to return. The service may return fewer than this value. If unspecified, at most 500 resources will be returned. The maximum value is 500; values above 500 will be coerced to 500.
    String pageToken = "pageToken_example"; // String | A page token, received from a previous KeyTrackingService.SearchProtectedResources call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to KeyTrackingService.SearchProtectedResources must match the call that provided the page token.
    List<String> resourceTypes = Arrays.asList(); // List<String> | Optional. A list of resource types that this request searches for. If empty, it will search all the [trackable resource types](https://cloud.google.com/kms/docs/view-key-usage#tracked-resource-types). Regular expressions are also supported. For example: * `compute.googleapis.com.*` snapshots resources whose type starts with `compute.googleapis.com`. * `.*Image` snapshots resources whose type ends with `Image`. * `.*Image.*` snapshots resources whose type contains `Image`. See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported resource type, an INVALID_ARGUMENT error will be returned.
    try {
      GoogleCloudKmsInventoryV1SearchProtectedResourcesResponse result = apiInstance.kmsinventoryOrganizationsProtectedResourcesSearch(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, cryptoKey, pageSize, pageToken, resourceTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#kmsinventoryOrganizationsProtectedResourcesSearch");
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
| **scope** | **String**| Required. Resource name of the organization. Example: organizations/123 | |
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
| **cryptoKey** | **String**| Required. The resource name of the CryptoKey. | [optional] |
| **pageSize** | **Integer**| The maximum number of resources to return. The service may return fewer than this value. If unspecified, at most 500 resources will be returned. The maximum value is 500; values above 500 will be coerced to 500. | [optional] |
| **pageToken** | **String**| A page token, received from a previous KeyTrackingService.SearchProtectedResources call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to KeyTrackingService.SearchProtectedResources must match the call that provided the page token. | [optional] |
| **resourceTypes** | [**List&lt;String&gt;**](String.md)| Optional. A list of resource types that this request searches for. If empty, it will search all the [trackable resource types](https://cloud.google.com/kms/docs/view-key-usage#tracked-resource-types). Regular expressions are also supported. For example: * &#x60;compute.googleapis.com.*&#x60; snapshots resources whose type starts with &#x60;compute.googleapis.com&#x60;. * &#x60;.*Image&#x60; snapshots resources whose type ends with &#x60;Image&#x60;. * &#x60;.*Image.*&#x60; snapshots resources whose type contains &#x60;Image&#x60;. See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported resource type, an INVALID_ARGUMENT error will be returned. | [optional] |

### Return type

[**GoogleCloudKmsInventoryV1SearchProtectedResourcesResponse**](GoogleCloudKmsInventoryV1SearchProtectedResourcesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

