# RatingsMovieTelevisionShowRatingsApi

All URIs are relative to *https://api.hillbillysoftware.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ratingByNameGet**](RatingsMovieTelevisionShowRatingsApi.md#ratingByNameGet) | **GET** /Rating/ByName/{AccessToken}/{Name} |  |
| [**ratingGet**](RatingsMovieTelevisionShowRatingsApi.md#ratingGet) | **GET** /Rating/ByID/{AccessToken}/{imdbID} | Returns ratings from various resources(IMDB,Rotten Tomatoes, metaCritics, TVMaze etc) of passed IMDBid |


<a id="ratingByNameGet"></a>
# **ratingByNameGet**
> List&lt;RatingItem&gt; ratingByNameGet(accessToken, name)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatingsMovieTelevisionShowRatingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    RatingsMovieTelevisionShowRatingsApi apiInstance = new RatingsMovieTelevisionShowRatingsApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String name = "name_example"; // String | 
    try {
      List<RatingItem> result = apiInstance.ratingByNameGet(accessToken, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatingsMovieTelevisionShowRatingsApi#ratingByNameGet");
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
| **name** | **String**|  | |

### Return type

[**List&lt;RatingItem&gt;**](RatingItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ratings |  -  |

<a id="ratingGet"></a>
# **ratingGet**
> RatingItem ratingGet(accessToken, imdbID)

Returns ratings from various resources(IMDB,Rotten Tomatoes, metaCritics, TVMaze etc) of passed IMDBid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatingsMovieTelevisionShowRatingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    RatingsMovieTelevisionShowRatingsApi apiInstance = new RatingsMovieTelevisionShowRatingsApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String imdbID = "imdbID_example"; // String | 
    try {
      RatingItem result = apiInstance.ratingGet(accessToken, imdbID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatingsMovieTelevisionShowRatingsApi#ratingGet");
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
| **imdbID** | **String**|  | |

### Return type

[**RatingItem**](RatingItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ratings |  -  |

