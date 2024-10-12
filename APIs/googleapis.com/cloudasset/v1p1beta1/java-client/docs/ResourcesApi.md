# ResourcesApi

All URIs are relative to *https://cloudasset.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudassetResourcesSearchAll**](ResourcesApi.md#cloudassetResourcesSearchAll) | **GET** /v1p1beta1/{scope}/resources:searchAll |  |


<a id="cloudassetResourcesSearchAll"></a>
# **cloudassetResourcesSearchAll**
> SearchAllResourcesResponse cloudassetResourcesSearchAll(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, assetTypes, orderBy, pageSize, pageToken, query)



Searches all the resources within a given accessible Resource Manager scope (project/folder/organization). This RPC gives callers especially administrators the ability to search all the resources within a scope, even if they don&#39;t have &#x60;.get&#x60; permission of all the resources. Callers should have &#x60;cloud.assets.SearchAllResources&#x60; permission on the requested scope, otherwise the request will be rejected.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

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

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String scope = "scope_example"; // String | Required. The relative name of an asset. The search is limited to the resources within the `scope`. The allowed value must be: * Organization number (such as \"organizations/123\") * Folder number (such as \"folders/1234\") * Project number (such as \"projects/12345\") * Project ID (such as \"projects/abc\")
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
    List<String> assetTypes = Arrays.asList(); // List<String> | Optional. A list of asset types that this request searches for. If empty, it will search all the supported asset types.
    String orderBy = "orderBy_example"; // String | Optional. A comma separated list of fields specifying the sorting order of the results. The default order is ascending. Add ` DESC` after the field name to indicate descending order. Redundant space characters are ignored. For example, ` location DESC , name `.
    Integer pageSize = 56; // Integer | Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `next_page_token` is returned.
    String pageToken = "pageToken_example"; // String | Optional. If present, then retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters, must be identical to those in the previous call.
    String query = "query_example"; // String | Optional. The query statement.
    try {
      SearchAllResourcesResponse result = apiInstance.cloudassetResourcesSearchAll(scope, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, assetTypes, orderBy, pageSize, pageToken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#cloudassetResourcesSearchAll");
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
| **scope** | **String**| Required. The relative name of an asset. The search is limited to the resources within the &#x60;scope&#x60;. The allowed value must be: * Organization number (such as \&quot;organizations/123\&quot;) * Folder number (such as \&quot;folders/1234\&quot;) * Project number (such as \&quot;projects/12345\&quot;) * Project ID (such as \&quot;projects/abc\&quot;) | |
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
| **assetTypes** | [**List&lt;String&gt;**](String.md)| Optional. A list of asset types that this request searches for. If empty, it will search all the supported asset types. | [optional] |
| **orderBy** | **String**| Optional. A comma separated list of fields specifying the sorting order of the results. The default order is ascending. Add &#x60; DESC&#x60; after the field name to indicate descending order. Redundant space characters are ignored. For example, &#x60; location DESC , name &#x60;. | [optional] |
| **pageSize** | **Integer**| Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as &#x60;next_page_token&#x60; is returned. | [optional] |
| **pageToken** | **String**| Optional. If present, then retrieve the next batch of results from the preceding call to this method. &#x60;page_token&#x60; must be the value of &#x60;next_page_token&#x60; from the previous response. The values of all other method parameters, must be identical to those in the previous call. | [optional] |
| **query** | **String**| Optional. The query statement. | [optional] |

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

