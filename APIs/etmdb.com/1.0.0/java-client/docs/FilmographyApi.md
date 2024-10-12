# FilmographyApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filmographySearchRead**](FilmographyApi.md#filmographySearchRead) | **GET** /api/v1/filmography/search/{movie_title} | Return filmography search result |
| [**filmographySearchallRead**](FilmographyApi.md#filmographySearchallRead) | **GET** /api/v1/filmography/searchall/{param} | Return filmography search result |


<a id="filmographySearchRead"></a>
# **filmographySearchRead**
> filmographySearchRead(movieTitle)

Return filmography search result

Return filmography search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movies * You can use both Amharic or English charset/font to search  For more details on how filmographies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilmographyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    FilmographyApi apiInstance = new FilmographyApi(defaultClient);
    String movieTitle = "movieTitle_example"; // String | 
    try {
      apiInstance.filmographySearchRead(movieTitle);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilmographyApi#filmographySearchRead");
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

<a id="filmographySearchallRead"></a>
# **filmographySearchallRead**
> filmographySearchallRead(param)

Return filmography search result

Return filmography search result  ### Response Class (Status 200) __{param}__ argument can be * artist first name * artist last name * artist username * movie title or * filmography description (such as director, actor, producer, etc)  For more details on how filmographies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilmographyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    FilmographyApi apiInstance = new FilmographyApi(defaultClient);
    String param = "param_example"; // String | 
    try {
      apiInstance.filmographySearchallRead(param);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilmographyApi#filmographySearchallRead");
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

