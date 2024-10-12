# SearchApi

All URIs are relative to *http://www.bclaws.ca/civix*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchAspectIdFullsearchGet**](SearchApi.md#searchAspectIdFullsearchGet) | **GET** /search/{aspectId}/fullsearch | A listing of metadata available for the specified aspect and search term from the BCLaws legislative repository |


<a id="searchAspectIdFullsearchGet"></a>
# **searchAspectIdFullsearchGet**
> searchAspectIdFullsearchGet(aspectId, q, s, e, nFrag, lFrag)

A listing of metadata available for the specified aspect and search term from the BCLaws legislative repository

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.bclaws.ca/civix");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String aspectId = "complete"; // String | The identifier of the 'aspect' (content group) to search
    String q = "water"; // String | query term
    String s = "0"; // String | first hit (start index)
    Integer e = 20; // Integer | last hit (end index)
    Integer nFrag = 5; // Integer | number of fragment snippets to return (< 10)
    Integer lFrag = 100; // Integer | length of fragment snippets (< 200)
    try {
      apiInstance.searchAspectIdFullsearchGet(aspectId, q, s, e, nFrag, lFrag);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchAspectIdFullsearchGet");
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
| **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to complete] [enum: complete, corpreg, bcgaz1, bcgaz2, oic, psl, ecb, hscr, arch_oic] |
| **q** | **String**| query term | [default to water] |
| **s** | **String**| first hit (start index) | [default to 0] |
| **e** | **Integer**| last hit (end index) | [default to 20] |
| **nFrag** | **Integer**| number of fragment snippets to return (&lt; 10) | [default to 5] |
| **lFrag** | **Integer**| length of fragment snippets (&lt; 200) | [default to 100] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of metadata available for the specified aspect and search term |  -  |

