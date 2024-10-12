# AssetsApi

All URIs are relative to *https://cloudasset.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudassetAssetsList**](AssetsApi.md#cloudassetAssetsList) | **GET** /v1p5beta1/{parent}/assets |  |


<a id="cloudassetAssetsList"></a>
# **cloudassetAssetsList**
> ListAssetsResponse cloudassetAssetsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, assetTypes, contentType, pageSize, pageToken, readTime)



Lists assets with time and resource types and returns paged results in response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetsApi;

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

    AssetsApi apiInstance = new AssetsApi(defaultClient);
    String parent = "parent_example"; // String | Required. Name of the organization or project the assets belong to. Format: \"organizations/[organization-number]\" (such as \"organizations/123\"), \"projects/[project-id]\" (such as \"projects/my-project-id\"), or \"projects/[project-number]\" (such as \"projects/12345\").
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
    List<String> assetTypes = Arrays.asList(); // List<String> | A list of asset types to take a snapshot for. For example: \"compute.googleapis.com/Disk\". Regular expression is also supported. For example: * \"compute.googleapis.com.*\" snapshots resources whose asset type starts with \"compute.googleapis.com\". * \".*Instance\" snapshots resources whose asset type ends with \"Instance\". * \".*Instance.*\" snapshots resources whose asset type contains \"Instance\". See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned. If specified, only matching assets will be returned, otherwise, it will snapshot all asset types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types.
    String contentType = "CONTENT_TYPE_UNSPECIFIED"; // String | Asset content type. If not specified, no content but the asset name will be returned.
    Integer pageSize = 56; // Integer | The maximum number of assets to be returned in a single response. Default is 100, minimum is 1, and maximum is 1000.
    String pageToken = "pageToken_example"; // String | The `next_page_token` returned from the previous `ListAssetsResponse`, or unspecified for the first `ListAssetsRequest`. It is a continuation of a prior `ListAssets` call, and the API should return the next page of assets.
    String readTime = "readTime_example"; // String | Timestamp to take an asset snapshot. This can only be set to a timestamp between the current time and the current time minus 35 days (inclusive). If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query may get different results.
    try {
      ListAssetsResponse result = apiInstance.cloudassetAssetsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, assetTypes, contentType, pageSize, pageToken, readTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetsApi#cloudassetAssetsList");
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
| **parent** | **String**| Required. Name of the organization or project the assets belong to. Format: \&quot;organizations/[organization-number]\&quot; (such as \&quot;organizations/123\&quot;), \&quot;projects/[project-id]\&quot; (such as \&quot;projects/my-project-id\&quot;), or \&quot;projects/[project-number]\&quot; (such as \&quot;projects/12345\&quot;). | |
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
| **assetTypes** | [**List&lt;String&gt;**](String.md)| A list of asset types to take a snapshot for. For example: \&quot;compute.googleapis.com/Disk\&quot;. Regular expression is also supported. For example: * \&quot;compute.googleapis.com.*\&quot; snapshots resources whose asset type starts with \&quot;compute.googleapis.com\&quot;. * \&quot;.*Instance\&quot; snapshots resources whose asset type ends with \&quot;Instance\&quot;. * \&quot;.*Instance.*\&quot; snapshots resources whose asset type contains \&quot;Instance\&quot;. See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned. If specified, only matching assets will be returned, otherwise, it will snapshot all asset types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types. | [optional] |
| **contentType** | **String**| Asset content type. If not specified, no content but the asset name will be returned. | [optional] [enum: CONTENT_TYPE_UNSPECIFIED, RESOURCE, IAM_POLICY, ORG_POLICY, ACCESS_POLICY] |
| **pageSize** | **Integer**| The maximum number of assets to be returned in a single response. Default is 100, minimum is 1, and maximum is 1000. | [optional] |
| **pageToken** | **String**| The &#x60;next_page_token&#x60; returned from the previous &#x60;ListAssetsResponse&#x60;, or unspecified for the first &#x60;ListAssetsRequest&#x60;. It is a continuation of a prior &#x60;ListAssets&#x60; call, and the API should return the next page of assets. | [optional] |
| **readTime** | **String**| Timestamp to take an asset snapshot. This can only be set to a timestamp between the current time and the current time minus 35 days (inclusive). If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query may get different results. | [optional] |

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

