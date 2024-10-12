# NewsApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**newsSearchRead**](NewsApi.md#newsSearchRead) | **GET** /api/v1/news/search/{title} | Return news or article search result |


<a id="newsSearchRead"></a>
# **newsSearchRead**
> newsSearchRead(title)

Return news or article search result

Return news or article search result  ### Response Class (Status 200)  * __{title}__: Used as a key word to search news and articles,  For more details on how news &amp; articles are listed [see here][ref]. [ref]: https://etmdb.com/en/news-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    NewsApi apiInstance = new NewsApi(defaultClient);
    String title = "title_example"; // String | 
    try {
      apiInstance.newsSearchRead(title);
    } catch (ApiException e) {
      System.err.println("Exception when calling NewsApi#newsSearchRead");
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
| **title** | **String**|  | |

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
| **200** |  |  -  |

