# TrailersMovieTelevisionShowTrailersApi

All URIs are relative to *https://api.hillbillysoftware.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**trailerCountByIDGet**](TrailersMovieTelevisionShowTrailersApi.md#trailerCountByIDGet) | **GET** /Trailers/CountByID/{AccessToken}/{imdbID} | Get trailer count for passed ID |
| [**trailerCountByNameGet**](TrailersMovieTelevisionShowTrailersApi.md#trailerCountByNameGet) | **GET** /Trailers/CountByName/{AccessToken}/{Name} | Get trailer count for passed name (Movie title or TVShow name) |
| [**trailerSearchGet**](TrailersMovieTelevisionShowTrailersApi.md#trailerSearchGet) | **GET** /Trailers/Search/{AccessToken}/{Phrase} | Gets trailers by search phrase (limited to 10 records) |
| [**trailersbyIDGet**](TrailersMovieTelevisionShowTrailersApi.md#trailersbyIDGet) | **GET** /Trailers/ByID/{AccessToken}/{imdbID} | Get Trailers for passed imdbID |


<a id="trailerCountByIDGet"></a>
# **trailerCountByIDGet**
> TrailerCount trailerCountByIDGet(accessToken, imdbID)

Get trailer count for passed ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrailersMovieTelevisionShowTrailersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TrailersMovieTelevisionShowTrailersApi apiInstance = new TrailersMovieTelevisionShowTrailersApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String imdbID = "imdbID_example"; // String | 
    try {
      TrailerCount result = apiInstance.trailerCountByIDGet(accessToken, imdbID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrailersMovieTelevisionShowTrailersApi#trailerCountByIDGet");
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

[**TrailerCount**](TrailerCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of trailers available for imdbID |  -  |

<a id="trailerCountByNameGet"></a>
# **trailerCountByNameGet**
> TrailerCount trailerCountByNameGet(accessToken, name)

Get trailer count for passed name (Movie title or TVShow name)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrailersMovieTelevisionShowTrailersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TrailersMovieTelevisionShowTrailersApi apiInstance = new TrailersMovieTelevisionShowTrailersApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String name = "name_example"; // String | 
    try {
      TrailerCount result = apiInstance.trailerCountByNameGet(accessToken, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrailersMovieTelevisionShowTrailersApi#trailerCountByNameGet");
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

[**TrailerCount**](TrailerCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of trailers available for passed name |  -  |

<a id="trailerSearchGet"></a>
# **trailerSearchGet**
> List&lt;Trailer&gt; trailerSearchGet(accessToken, phrase)

Gets trailers by search phrase (limited to 10 records)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrailersMovieTelevisionShowTrailersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TrailersMovieTelevisionShowTrailersApi apiInstance = new TrailersMovieTelevisionShowTrailersApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String phrase = "phrase_example"; // String | Trailer you like to search for
    try {
      List<Trailer> result = apiInstance.trailerSearchGet(accessToken, phrase);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrailersMovieTelevisionShowTrailersApi#trailerSearchGet");
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
| **phrase** | **String**| Trailer you like to search for | |

### Return type

[**List&lt;Trailer&gt;**](Trailer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of trailers |  -  |

<a id="trailersbyIDGet"></a>
# **trailersbyIDGet**
> List&lt;Trailer&gt; trailersbyIDGet(accessToken, imdbID)

Get Trailers for passed imdbID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrailersMovieTelevisionShowTrailersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TrailersMovieTelevisionShowTrailersApi apiInstance = new TrailersMovieTelevisionShowTrailersApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String imdbID = "imdbID_example"; // String | 
    try {
      List<Trailer> result = apiInstance.trailersbyIDGet(accessToken, imdbID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrailersMovieTelevisionShowTrailersApi#trailersbyIDGet");
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

[**List&lt;Trailer&gt;**](Trailer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of trailers |  -  |

