# WatchlistApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**watchlistSearchRead**](WatchlistApi.md#watchlistSearchRead) | **GET** /api/v1/watchlist/search/{movie_title} | Return watchlist search result |
| [**watchlistSearchallRead**](WatchlistApi.md#watchlistSearchallRead) | **GET** /api/v1/watchlist/searchall/{param} | Return watchlist search result |


<a id="watchlistSearchRead"></a>
# **watchlistSearchRead**
> watchlistSearchRead(movieTitle)

Return watchlist search result

Return watchlist search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movies on watchlist * You can use both Amharic or English charset/font to search  For more details on how watchlist are listed [see here][ref]. [ref]: https://etmdb.com/en/movies/watchlist/id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WatchlistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    WatchlistApi apiInstance = new WatchlistApi(defaultClient);
    String movieTitle = "movieTitle_example"; // String | 
    try {
      apiInstance.watchlistSearchRead(movieTitle);
    } catch (ApiException e) {
      System.err.println("Exception when calling WatchlistApi#watchlistSearchRead");
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
| **movieTitle** | **String**|  | |

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

<a id="watchlistSearchallRead"></a>
# **watchlistSearchallRead**
> watchlistSearchallRead(param)

Return watchlist search result

Return watchlist search result  ### Response Class (Status 200) __{param}__ argument can be * artist first name * artist last name * artist username * movie title or  For more details on how watchlist are listed [see here][ref]. [ref]: https://etmdb.com/en/movies/watchlist/id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WatchlistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    WatchlistApi apiInstance = new WatchlistApi(defaultClient);
    String param = "param_example"; // String | 
    try {
      apiInstance.watchlistSearchallRead(param);
    } catch (ApiException e) {
      System.err.println("Exception when calling WatchlistApi#watchlistSearchallRead");
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
| **param** | **String**|  | |

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

