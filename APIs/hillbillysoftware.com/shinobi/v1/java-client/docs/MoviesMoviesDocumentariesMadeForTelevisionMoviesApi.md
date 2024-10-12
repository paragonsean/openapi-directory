# MoviesMoviesDocumentariesMadeForTelevisionMoviesApi

All URIs are relative to *https://api.hillbillysoftware.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**movieIDGet**](MoviesMoviesDocumentariesMadeForTelevisionMoviesApi.md#movieIDGet) | **GET** /Movie/ByID/{accesstoken}/{imdbID} |  |
| [**movieSearchGetAsync**](MoviesMoviesDocumentariesMadeForTelevisionMoviesApi.md#movieSearchGetAsync) | **GET** /Movie/Search/{AccessToken}/{Query} | Searches for movies, result set limited to 5 records |


<a id="movieIDGet"></a>
# **movieIDGet**
> MovieInformation movieIDGet(accesstoken, imdbID)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesMoviesDocumentariesMadeForTelevisionMoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MoviesMoviesDocumentariesMadeForTelevisionMoviesApi apiInstance = new MoviesMoviesDocumentariesMadeForTelevisionMoviesApi(defaultClient);
    String accesstoken = "accesstoken_example"; // String | 
    String imdbID = "imdbID_example"; // String | 
    try {
      MovieInformation result = apiInstance.movieIDGet(accesstoken, imdbID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesMoviesDocumentariesMadeForTelevisionMoviesApi#movieIDGet");
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
| **accesstoken** | **String**|  | |
| **imdbID** | **String**|  | |

### Return type

[**MovieInformation**](MovieInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Movie information |  -  |

<a id="movieSearchGetAsync"></a>
# **movieSearchGetAsync**
> List&lt;MovieInformation&gt; movieSearchGetAsync(accessToken, query)

Searches for movies, result set limited to 5 records

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesMoviesDocumentariesMadeForTelevisionMoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MoviesMoviesDocumentariesMadeForTelevisionMoviesApi apiInstance = new MoviesMoviesDocumentariesMadeForTelevisionMoviesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String query = "query_example"; // String | 
    try {
      List<MovieInformation> result = apiInstance.movieSearchGetAsync(accessToken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesMoviesDocumentariesMadeForTelevisionMoviesApi#movieSearchGetAsync");
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
| **accessToken** | **String**|  | |
| **query** | **String**|  | |

### Return type

[**List&lt;MovieInformation&gt;**](MovieInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of information about queried movie(s) |  -  |

