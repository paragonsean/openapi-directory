# ChainsApi

All URIs are relative to *https://mybusinessbusinessinformation.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mybusinessbusinessinformationChainsSearch**](ChainsApi.md#mybusinessbusinessinformationChainsSearch) | **GET** /v1/chains:search |  |


<a id="mybusinessbusinessinformationChainsSearch"></a>
# **mybusinessbusinessinformationChainsSearch**
> SearchChainsResponse mybusinessbusinessinformationChainsSearch($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, chainName, pageSize)



Searches the chain based on chain name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mybusinessbusinessinformation.googleapis.com");

    ChainsApi apiInstance = new ChainsApi(defaultClient);
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
    String chainName = "chainName_example"; // String | Required. Search for a chain by its name. Exact/partial/fuzzy/related queries are supported. Examples: \"walmart\", \"wal-mart\", \"walmmmart\", \"沃尔玛\"
    Integer pageSize = 56; // Integer | The maximum number of matched chains to return from this query. The default is 10. The maximum possible value is 500.
    try {
      SearchChainsResponse result = apiInstance.mybusinessbusinessinformationChainsSearch($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, chainName, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChainsApi#mybusinessbusinessinformationChainsSearch");
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
| **chainName** | **String**| Required. Search for a chain by its name. Exact/partial/fuzzy/related queries are supported. Examples: \&quot;walmart\&quot;, \&quot;wal-mart\&quot;, \&quot;walmmmart\&quot;, \&quot;沃尔玛\&quot; | [optional] |
| **pageSize** | **Integer**| The maximum number of matched chains to return from this query. The default is 10. The maximum possible value is 500. | [optional] |

### Return type

[**SearchChainsResponse**](SearchChainsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

