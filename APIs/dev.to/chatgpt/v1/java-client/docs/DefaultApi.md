# DefaultApi

All URIs are relative to *https://dev.to*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getArticles**](DefaultApi.md#getArticles) | **GET** /api/articles/search | Get a list of filtered articles |


<a id="getArticles"></a>
# **getArticles**
> GetArticlesResponse getArticles(q, page, perPage, top)

Get a list of filtered articles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String q = "q_example"; // String | Accepts keywords to use as a search query.
    Integer page = 0; // Integer | Pagination Page
    Integer perPage = 60; // Integer | Page size (the number of items to return per page).
    String top = "top_example"; // String | Returns the most popular articles in the last N days. 'top' indicates the number of days since publication of the articles returned. This param can be used in conjuction with q or tag.
    try {
      GetArticlesResponse result = apiInstance.getArticles(q, page, perPage, top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getArticles");
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
| **q** | **String**| Accepts keywords to use as a search query. | [optional] |
| **page** | **Integer**| Pagination Page | [optional] [default to 0] |
| **perPage** | **Integer**| Page size (the number of items to return per page). | [optional] [default to 60] |
| **top** | **String**| Returns the most popular articles in the last N days. &#39;top&#39; indicates the number of days since publication of the articles returned. This param can be used in conjuction with q or tag. | [optional] |

### Return type

[**GetArticlesResponse**](GetArticlesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.forem.api-v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

