# PodcastEpisodesApi

All URIs are relative to *https://dev.to/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPodcastEpisodes**](PodcastEpisodesApi.md#getPodcastEpisodes) | **GET** /api/podcast_episodes | Podcast Episodes |


<a id="getPodcastEpisodes"></a>
# **getPodcastEpisodes**
> List&lt;PodcastEpisodeIndex&gt; getPodcastEpisodes(page, perPage, username)

Podcast Episodes

This endpoint allows the client to retrieve a list of podcast episodes.         \&quot;Podcast episodes\&quot; are episodes belonging to podcasts.         It will only return active (reachable) podcast episodes that belong to published podcasts available on the platform, ordered by descending publication date.         It supports pagination, each page will contain 30 articles by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodcastEpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");

    PodcastEpisodesApi apiInstance = new PodcastEpisodesApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    String username = "codenewbie"; // String | Using this parameter will retrieve episodes belonging to a specific podcast.
    try {
      List<PodcastEpisodeIndex> result = apiInstance.getPodcastEpisodes(page, perPage, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodcastEpisodesApi#getPodcastEpisodes");
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
| **username** | **String**| Using this parameter will retrieve episodes belonging to a specific podcast. | [optional] |

### Return type

[**List&lt;PodcastEpisodeIndex&gt;**](PodcastEpisodeIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of Podcast episodes filtered by username |  -  |
| **404** | Unknown Podcast username |  -  |

