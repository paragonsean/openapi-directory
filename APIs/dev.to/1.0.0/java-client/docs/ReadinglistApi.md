# ReadinglistApi

All URIs are relative to *https://dev.to/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getReadinglist**](ReadinglistApi.md#getReadinglist) | **GET** /api/readinglist | Readinglist |


<a id="getReadinglist"></a>
# **getReadinglist**
> List&lt;ArticleIndex&gt; getReadinglist(page, perPage)

Readinglist

This endpoint allows the client to retrieve a list of articles that were saved to a Users readinglist.         It supports pagination, each page will contain &#x60;30&#x60; articles by default

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReadinglistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ReadinglistApi apiInstance = new ReadinglistApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<ArticleIndex> result = apiInstance.getReadinglist(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReadinglistApi#getReadinglist");
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
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of articles in the users readinglist |  -  |
| **401** | Unauthorized |  -  |

