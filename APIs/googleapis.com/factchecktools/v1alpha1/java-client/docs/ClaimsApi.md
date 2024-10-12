# ClaimsApi

All URIs are relative to *https://factchecktools.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**factchecktoolsClaimsSearch**](ClaimsApi.md#factchecktoolsClaimsSearch) | **GET** /v1alpha1/claims:search |  |


<a id="factchecktoolsClaimsSearch"></a>
# **factchecktoolsClaimsSearch**
> GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse factchecktoolsClaimsSearch($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, maxAgeDays, offset, pageSize, pageToken, query, reviewPublisherSiteFilter)



Search through fact-checked claims.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClaimsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://factchecktools.googleapis.com");

    ClaimsApi apiInstance = new ClaimsApi(defaultClient);
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
    String languageCode = "languageCode_example"; // String | The BCP-47 language code, such as \"en-US\" or \"sr-Latn\". Can be used to restrict results by language, though we do not currently consider the region.
    Integer maxAgeDays = 56; // Integer | The maximum age of the returned search results, in days. Age is determined by either claim date or review date, whichever is newer.
    Integer offset = 56; // Integer | An integer that specifies the current offset (that is, starting result location) in search results. This field is only considered if `page_token` is unset. For example, 0 means to return results starting from the first matching result, and 10 means to return from the 11th result.
    Integer pageSize = 56; // Integer | The pagination size. We will return up to that many results. Defaults to 10 if not set.
    String pageToken = "pageToken_example"; // String | The pagination token. You may provide the `next_page_token` returned from a previous List request, if any, in order to get the next page. All other fields must have the same values as in the previous request.
    String query = "query_example"; // String | Textual query string. Required unless `review_publisher_site_filter` is specified.
    String reviewPublisherSiteFilter = "reviewPublisherSiteFilter_example"; // String | The review publisher site to filter results by, e.g. nytimes.com.
    try {
      GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse result = apiInstance.factchecktoolsClaimsSearch($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, maxAgeDays, offset, pageSize, pageToken, query, reviewPublisherSiteFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClaimsApi#factchecktoolsClaimsSearch");
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
| **languageCode** | **String**| The BCP-47 language code, such as \&quot;en-US\&quot; or \&quot;sr-Latn\&quot;. Can be used to restrict results by language, though we do not currently consider the region. | [optional] |
| **maxAgeDays** | **Integer**| The maximum age of the returned search results, in days. Age is determined by either claim date or review date, whichever is newer. | [optional] |
| **offset** | **Integer**| An integer that specifies the current offset (that is, starting result location) in search results. This field is only considered if &#x60;page_token&#x60; is unset. For example, 0 means to return results starting from the first matching result, and 10 means to return from the 11th result. | [optional] |
| **pageSize** | **Integer**| The pagination size. We will return up to that many results. Defaults to 10 if not set. | [optional] |
| **pageToken** | **String**| The pagination token. You may provide the &#x60;next_page_token&#x60; returned from a previous List request, if any, in order to get the next page. All other fields must have the same values as in the previous request. | [optional] |
| **query** | **String**| Textual query string. Required unless &#x60;review_publisher_site_filter&#x60; is specified. | [optional] |
| **reviewPublisherSiteFilter** | **String**| The review publisher site to filter results by, e.g. nytimes.com. | [optional] |

### Return type

[**GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse**](GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

