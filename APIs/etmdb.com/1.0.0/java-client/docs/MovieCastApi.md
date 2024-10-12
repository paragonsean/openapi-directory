# MovieCastApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**movieCastSearchRead**](MovieCastApi.md#movieCastSearchRead) | **GET** /api/v1/movie-cast/search/{movie_title} | Return movie cast search result |
| [**movieCastSearchallRead**](MovieCastApi.md#movieCastSearchallRead) | **GET** /api/v1/movie-cast/searchall/{param} | Return movie cast search result |


<a id="movieCastSearchRead"></a>
# **movieCastSearchRead**
> movieCastSearchRead(movieTitle)

Return movie cast search result

Return movie cast search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movie cast * You can use both Amharic or English charset/font to search  For more details on how movie casts are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MovieCastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    MovieCastApi apiInstance = new MovieCastApi(defaultClient);
    String movieTitle = "movieTitle_example"; // String | 
    try {
      apiInstance.movieCastSearchRead(movieTitle);
    } catch (ApiException e) {
      System.err.println("Exception when calling MovieCastApi#movieCastSearchRead");
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

<a id="movieCastSearchallRead"></a>
# **movieCastSearchallRead**
> movieCastSearchallRead(param)

Return movie cast search result

Return movie cast search result  ### Response Class (Status 200) __{param}__ argument can be * artist first name * artist last name * artist username * movie title or * character name  For more details on how movie casts are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MovieCastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    MovieCastApi apiInstance = new MovieCastApi(defaultClient);
    String param = "param_example"; // String | 
    try {
      apiInstance.movieCastSearchallRead(param);
    } catch (ApiException e) {
      System.err.println("Exception when calling MovieCastApi#movieCastSearchallRead");
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

