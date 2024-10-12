# VideosApi

All URIs are relative to *https://dev.to/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**videos**](VideosApi.md#videos) | **GET** /api/videos | Articles with a video |


<a id="videos"></a>
# **videos**
> List&lt;VideoArticle&gt; videos(page, perPage)

Articles with a video

This endpoint allows the client to retrieve a list of articles that are uploaded with a video.  It will only return published video articles ordered by descending popularity.  It supports pagination, each page will contain 24 articles by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");

    VideosApi apiInstance = new VideosApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 24; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<VideoArticle> result = apiInstance.videos(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#videos");
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
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 24] |

### Return type

[**List&lt;VideoArticle&gt;**](VideoArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of all articles with videos |  -  |

