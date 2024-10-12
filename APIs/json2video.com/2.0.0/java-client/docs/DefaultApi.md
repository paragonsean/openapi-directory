# DefaultApi

All URIs are relative to *https://api.json2video.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMovies**](DefaultApi.md#getMovies) | **GET** /movies | Get the status of your movies |
| [**newMovie**](DefaultApi.md#newMovie) | **POST** /movies | Create a new movie |


<a id="getMovies"></a>
# **getMovies**
> getMovies()

Get the status of your movies

Get the status any of your movies by passing your project ID in the &lt;code&gt;project&lt;/code&gt; query parameter. You can get your project ID from the response of the POST request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.json2video.com/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getMovies();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMovies");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | Ok |  -  |

<a id="newMovie"></a>
# **newMovie**
> newMovie(movie)

Create a new movie

Submit a new movie rendering job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.json2video.com/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Movie movie = new Movie(); // Movie | 
    try {
      apiInstance.newMovie(movie);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#newMovie");
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
| **movie** | [**Movie**](Movie.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Added |  -  |

