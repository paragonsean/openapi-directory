# MovieApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**movieSearchRead**](MovieApi.md#movieSearchRead) | **GET** /api/v1/movie/search/{movie_title} | Return movie search result |


<a id="movieSearchRead"></a>
# **movieSearchRead**
> movieSearchRead(movieTitle)

Return movie search result

Return movie search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movies * You can use both Amharic or English charset/font to search  For more details on how movies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MovieApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    MovieApi apiInstance = new MovieApi(defaultClient);
    String movieTitle = "movieTitle_example"; // String | 
    try {
      apiInstance.movieSearchRead(movieTitle);
    } catch (ApiException e) {
      System.err.println("Exception when calling MovieApi#movieSearchRead");
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

