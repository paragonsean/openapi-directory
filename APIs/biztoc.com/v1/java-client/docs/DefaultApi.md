# DefaultApi

All URIs are relative to *https://ai.biztoc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNews**](DefaultApi.md#getNews) | **GET** /ai/news | Retrieves the latest news whose content contains the query string. |


<a id="getNews"></a>
# **getNews**
> getNews(query)

Retrieves the latest news whose content contains the query string.

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
    defaultClient.setBasePath("https://ai.biztoc.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String query = "query_example"; // String | Used to query news articles on their title and body. For example, ?query=apple will return news stories that have 'apple' in their title or body.
    try {
      apiInstance.getNews(query);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getNews");
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
| **query** | **String**| Used to query news articles on their title and body. For example, ?query&#x3D;apple will return news stories that have &#39;apple&#39; in their title or body. | [optional] |

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
| **200** | OK |  -  |

