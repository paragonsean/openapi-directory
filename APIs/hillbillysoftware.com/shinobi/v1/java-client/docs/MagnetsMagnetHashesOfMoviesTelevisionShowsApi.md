# MagnetsMagnetHashesOfMoviesTelevisionShowsApi

All URIs are relative to *https://api.hillbillysoftware.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**magnetsByDateGetAsync**](MagnetsMagnetHashesOfMoviesTelevisionShowsApi.md#magnetsByDateGetAsync) | **GET** /Magnets/ByDate/{AccessToken}/{Date} | Gets available magnet hashes on passed date (yyyy-mm-dd).  Feature not available on free plan, please donate to be able to use this feature. |
| [**magnetsByimdbIDGetAsync**](MagnetsMagnetHashesOfMoviesTelevisionShowsApi.md#magnetsByimdbIDGetAsync) | **GET** /Magnets/ByIMDB/{AccessToken}/{imdbID} | Returns list of magnet hashes for passed IMDBID.  Feature not available on free plan, please donate to be able to use this feature. |
| [**magnetsMovieByIDGetAsync**](MagnetsMagnetHashesOfMoviesTelevisionShowsApi.md#magnetsMovieByIDGetAsync) | **GET** /Magnets/Search/{AccessToken}/{Query} | Try and find magnet links for queried movie.  Feature not available on free plan, please donate to be able to use this feature |
| [**tVShowsearchGet**](MagnetsMagnetHashesOfMoviesTelevisionShowsApi.md#tVShowsearchGet) | **GET** /Magnets/TVShow/{AccessToken}/{TVShow} | Returns results based on query, Feature not available on free plan, please donate to be able to use this feature. |


<a id="magnetsByDateGetAsync"></a>
# **magnetsByDateGetAsync**
> List&lt;Magnets&gt; magnetsByDateGetAsync(accessToken, date)

Gets available magnet hashes on passed date (yyyy-mm-dd).  Feature not available on free plan, please donate to be able to use this feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MagnetsMagnetHashesOfMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MagnetsMagnetHashesOfMoviesTelevisionShowsApi apiInstance = new MagnetsMagnetHashesOfMoviesTelevisionShowsApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String date = "date_example"; // String | 
    try {
      List<Magnets> result = apiInstance.magnetsByDateGetAsync(accessToken, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MagnetsMagnetHashesOfMoviesTelevisionShowsApi#magnetsByDateGetAsync");
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
| **date** | **String**|  | |

### Return type

[**List&lt;Magnets&gt;**](Magnets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of magnet hashes |  -  |

<a id="magnetsByimdbIDGetAsync"></a>
# **magnetsByimdbIDGetAsync**
> List&lt;Magnets&gt; magnetsByimdbIDGetAsync(accessToken, imdbID)

Returns list of magnet hashes for passed IMDBID.  Feature not available on free plan, please donate to be able to use this feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MagnetsMagnetHashesOfMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MagnetsMagnetHashesOfMoviesTelevisionShowsApi apiInstance = new MagnetsMagnetHashesOfMoviesTelevisionShowsApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String imdbID = "imdbID_example"; // String | ID with or without tt prefix
    try {
      List<Magnets> result = apiInstance.magnetsByimdbIDGetAsync(accessToken, imdbID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MagnetsMagnetHashesOfMoviesTelevisionShowsApi#magnetsByimdbIDGetAsync");
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
| **imdbID** | **String**| ID with or without tt prefix | |

### Return type

[**List&lt;Magnets&gt;**](Magnets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of magnet hashes |  -  |

<a id="magnetsMovieByIDGetAsync"></a>
# **magnetsMovieByIDGetAsync**
> List&lt;Magnets&gt; magnetsMovieByIDGetAsync(accessToken, query)

Try and find magnet links for queried movie.  Feature not available on free plan, please donate to be able to use this feature

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MagnetsMagnetHashesOfMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MagnetsMagnetHashesOfMoviesTelevisionShowsApi apiInstance = new MagnetsMagnetHashesOfMoviesTelevisionShowsApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String query = "query_example"; // String | Name or part of name of movie or tv show
    try {
      List<Magnets> result = apiInstance.magnetsMovieByIDGetAsync(accessToken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MagnetsMagnetHashesOfMoviesTelevisionShowsApi#magnetsMovieByIDGetAsync");
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
| **query** | **String**| Name or part of name of movie or tv show | |

### Return type

[**List&lt;Magnets&gt;**](Magnets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of magnet hashes |  -  |

<a id="tVShowsearchGet"></a>
# **tVShowsearchGet**
> List&lt;Magnets&gt; tVShowsearchGet(accessToken, tvShow)

Returns results based on query, Feature not available on free plan, please donate to be able to use this feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MagnetsMagnetHashesOfMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MagnetsMagnetHashesOfMoviesTelevisionShowsApi apiInstance = new MagnetsMagnetHashesOfMoviesTelevisionShowsApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String tvShow = "tvShow_example"; // String | 
    try {
      List<Magnets> result = apiInstance.tVShowsearchGet(accessToken, tvShow);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MagnetsMagnetHashesOfMoviesTelevisionShowsApi#tVShowsearchGet");
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
| **tvShow** | **String**|  | |

### Return type

[**List&lt;Magnets&gt;**](Magnets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of magnet hashes |  -  |

