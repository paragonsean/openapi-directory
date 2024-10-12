# IdeasApi

All URIs are relative to *https://ideahub.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ideahubIdeasList**](IdeasApi.md#ideahubIdeasList) | **GET** /v1alpha/ideas |  |


<a id="ideahubIdeasList"></a>
# **ideahubIdeasList**
> GoogleSearchIdeahubV1alphaListIdeasResponse ideahubIdeasList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, orderBy, pageSize, pageToken, parent)



List ideas for a given Creator and filter and sort options.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdeasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ideahub.googleapis.com");

    IdeasApi apiInstance = new IdeasApi(defaultClient);
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
    String filter = "filter_example"; // String | Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions are implicitly combined, as if the `AND` operator was always used. The `OR` operator is currently unsupported. * Supported functions: - `saved(bool)`: If set to true, fetches only saved ideas. If set to false, fetches all except saved ideas. Can't be simultaneously used with `dismissed(bool)`. - `dismissed(bool)`: If set to true, fetches only dismissed ideas. Can't be simultaneously used with `saved(bool)`. The `false` value is currently unsupported. Examples: * `saved(true)` * `saved(false)` * `dismissed(true)` The length of this field should be no more than 500 characters.
    String orderBy = "orderBy_example"; // String | Order semantics described below.
    Integer pageSize = 56; // Integer | The maximum number of ideas per page. If unspecified, at most 10 ideas will be returned. The maximum value is 2000; values above 2000 will be coerced to 2000.
    String pageToken = "pageToken_example"; // String | Used to fetch next page.
    String parent = "parent_example"; // String | If defined, specifies the creator for which to filter by. Format: publishers/{publisher}/properties/{property}
    try {
      GoogleSearchIdeahubV1alphaListIdeasResponse result = apiInstance.ideahubIdeasList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, orderBy, pageSize, pageToken, parent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdeasApi#ideahubIdeasList");
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
| **filter** | **String**| Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions are implicitly combined, as if the &#x60;AND&#x60; operator was always used. The &#x60;OR&#x60; operator is currently unsupported. * Supported functions: - &#x60;saved(bool)&#x60;: If set to true, fetches only saved ideas. If set to false, fetches all except saved ideas. Can&#39;t be simultaneously used with &#x60;dismissed(bool)&#x60;. - &#x60;dismissed(bool)&#x60;: If set to true, fetches only dismissed ideas. Can&#39;t be simultaneously used with &#x60;saved(bool)&#x60;. The &#x60;false&#x60; value is currently unsupported. Examples: * &#x60;saved(true)&#x60; * &#x60;saved(false)&#x60; * &#x60;dismissed(true)&#x60; The length of this field should be no more than 500 characters. | [optional] |
| **orderBy** | **String**| Order semantics described below. | [optional] |
| **pageSize** | **Integer**| The maximum number of ideas per page. If unspecified, at most 10 ideas will be returned. The maximum value is 2000; values above 2000 will be coerced to 2000. | [optional] |
| **pageToken** | **String**| Used to fetch next page. | [optional] |
| **parent** | **String**| If defined, specifies the creator for which to filter by. Format: publishers/{publisher}/properties/{property} | [optional] |

### Return type

[**GoogleSearchIdeahubV1alphaListIdeasResponse**](GoogleSearchIdeahubV1alphaListIdeasResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

