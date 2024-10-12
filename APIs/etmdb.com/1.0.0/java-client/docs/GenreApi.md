# GenreApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**genreSearchRead**](GenreApi.md#genreSearchRead) | **GET** /api/v1/genre/search/{movie_title} | Return movie genre search result |
| [**genreSearchallRead**](GenreApi.md#genreSearchallRead) | **GET** /api/v1/genre/searchall/{movie_genre_type} | Return movie genre search result |


<a id="genreSearchRead"></a>
# **genreSearchRead**
> genreSearchRead(movieTitle)

Return movie genre search result

Return movie genre search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movie genres * You can use both Amharic or English charset/font to search  For more details on how movies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    GenreApi apiInstance = new GenreApi(defaultClient);
    String movieTitle = "movieTitle_example"; // String | 
    try {
      apiInstance.genreSearchRead(movieTitle);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenreApi#genreSearchRead");
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

<a id="genreSearchallRead"></a>
# **genreSearchallRead**
> genreSearchallRead(movieGenreType)

Return movie genre search result

Return movie genre search result  ### Response Class (Status 200)  * __{movie_genre_type}__: Used as a key word to search movie genres  For more details on how movies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    GenreApi apiInstance = new GenreApi(defaultClient);
    String movieGenreType = "movieGenreType_example"; // String | 
    try {
      apiInstance.genreSearchallRead(movieGenreType);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenreApi#genreSearchallRead");
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
| **movieGenreType** | **String**|  | |

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

