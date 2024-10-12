# MoviesApi

All URIs are relative to *https://hydramovies.com/api-v2/%3Fsource&#x3D;http:/hydramovies.com/api-v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**currentMovieDataCsvGet**](MoviesApi.md#currentMovieDataCsvGet) | **GET** /current-Movie-Data.csv&amp;imdb_id&#x3D;{IMDBid} | getMovieByIMDBid |
| [**currentMovieDataCsvGet2**](MoviesApi.md#currentMovieDataCsvGet2) | **GET** /current-Movie-Data.csv&amp;movie_year&#x3D;{MovieYear} | getMovieByYear |


<a id="currentMovieDataCsvGet"></a>
# **currentMovieDataCsvGet**
> currentMovieDataCsvGet(imDBid)

getMovieByIMDBid

Returns a movie using the films unique IMDB identifier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hydramovies.com/api-v2/%3Fsource=http:/hydramovies.com/api-v2");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String imDBid = "imDBid_example"; // String | IMDB ID of the movie to return
    try {
      apiInstance.currentMovieDataCsvGet(imDBid);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#currentMovieDataCsvGet");
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
| **imDBid** | **String**| IMDB ID of the movie to return | |

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
| **200** | successful operation |  -  |

<a id="currentMovieDataCsvGet2"></a>
# **currentMovieDataCsvGet2**
> currentMovieDataCsvGet2(movieYear)

getMovieByYear

Returns a movie based on the year of its release

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hydramovies.com/api-v2/%3Fsource=http:/hydramovies.com/api-v2");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String movieYear = "movieYear_example"; // String | Release year of the movies to return
    try {
      apiInstance.currentMovieDataCsvGet2(movieYear);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#currentMovieDataCsvGet2");
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
| **movieYear** | **String**| Release year of the movies to return | |

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
| **200** | successful operation |  -  |

