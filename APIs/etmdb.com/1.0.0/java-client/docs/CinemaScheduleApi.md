# CinemaScheduleApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cinemaScheduleSearchRead**](CinemaScheduleApi.md#cinemaScheduleSearchRead) | **GET** /api/v1/cinema-schedule/search/{movie_title} | Return cinema schedule search result |
| [**cinemaScheduleSearchallRead**](CinemaScheduleApi.md#cinemaScheduleSearchallRead) | **GET** /api/v1/cinema-schedule/searchall/{param} | Return cinema schedule search result |


<a id="cinemaScheduleSearchRead"></a>
# **cinemaScheduleSearchRead**
> cinemaScheduleSearchRead(movieTitle)

Return cinema schedule search result

Return cinema schedule search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movie cast * You can use both Amharic or English charset/font to search  For more details about cinema schedule, check each cinema from the cinema list [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CinemaScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    CinemaScheduleApi apiInstance = new CinemaScheduleApi(defaultClient);
    String movieTitle = "movieTitle_example"; // String | 
    try {
      apiInstance.cinemaScheduleSearchRead(movieTitle);
    } catch (ApiException e) {
      System.err.println("Exception when calling CinemaScheduleApi#cinemaScheduleSearchRead");
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

<a id="cinemaScheduleSearchallRead"></a>
# **cinemaScheduleSearchallRead**
> cinemaScheduleSearchallRead(param)

Return cinema schedule search result

Return cinema schedule search result  ### Response Class (Status 200) __{param}__ argument can be * movie title * cinema name * cinema hall name or * cinema technology  For more details about cinema schedule, check each cinema from the cinema list [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CinemaScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    CinemaScheduleApi apiInstance = new CinemaScheduleApi(defaultClient);
    String param = "param_example"; // String | 
    try {
      apiInstance.cinemaScheduleSearchallRead(param);
    } catch (ApiException e) {
      System.err.println("Exception when calling CinemaScheduleApi#cinemaScheduleSearchallRead");
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

