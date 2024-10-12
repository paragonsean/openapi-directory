# RecommendationsApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMovieRecommendations**](RecommendationsApi.md#getMovieRecommendations) | **GET** /recommendations/movies | Get movie recommendations |
| [**getShowRecommendations**](RecommendationsApi.md#getShowRecommendations) | **GET** /recommendations/shows | Get show recommendations |
| [**hideAMovieRecommendation**](RecommendationsApi.md#hideAMovieRecommendation) | **DELETE** /recommendations/movies/{id} | Hide a movie recommendation |
| [**hideAShowRecommendation**](RecommendationsApi.md#hideAShowRecommendation) | **DELETE** /recommendations/shows/{id} | Hide a show recommendation |


<a id="getMovieRecommendations"></a>
# **getMovieRecommendations**
> getMovieRecommendations(ignoreCollected, ignoreWatchlisted, traktApiVersion, traktApiKey)

Get movie recommendations

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info  Movie recommendations for a user. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page. Set &#x60;ignore_collected&#x3D;true&#x60; to filter out movies the user has already collected or &#x60;ignore_watchlisted&#x3D;true&#x60; to filter out movies the user has already watchlisted.  The &#x60;recommended_by&#x60; array contains all users who recommended the item along with any notes they added.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String ignoreCollected = "true"; // String | filter out collected movies
    String ignoreWatchlisted = "true"; // String | filter out watchlisted movies
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getMovieRecommendations(ignoreCollected, ignoreWatchlisted, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#getMovieRecommendations");
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
| **ignoreCollected** | **String**| filter out collected movies | [optional] [enum: true, false] |
| **ignoreWatchlisted** | **String**| filter out watchlisted movies | [optional] [enum: true, false] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  |

<a id="getShowRecommendations"></a>
# **getShowRecommendations**
> getShowRecommendations(ignoreCollected, ignoreWatchlisted, traktApiVersion, traktApiKey)

Get show recommendations

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info  TV show recommendations for a user. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page. Set &#x60;ignore_collected&#x3D;true&#x60; to filter out shows the user has already collected or &#x60;ignore_watchlisted&#x3D;true&#x60; to filter out shows the user has already watchlisted.  The &#x60;recommended_by&#x60; array contains all users who recommended the item along with any notes they added.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String ignoreCollected = "true"; // String | filter out collected shows
    String ignoreWatchlisted = "true"; // String | filter out watchlisted movies
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getShowRecommendations(ignoreCollected, ignoreWatchlisted, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#getShowRecommendations");
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
| **ignoreCollected** | **String**| filter out collected shows | [optional] [enum: true, false] |
| **ignoreWatchlisted** | **String**| filter out watchlisted movies | [optional] [enum: true, false] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  |

<a id="hideAMovieRecommendation"></a>
# **hideAMovieRecommendation**
> hideAMovieRecommendation(id, traktApiVersion, traktApiKey)

Hide a movie recommendation

#### &amp;#128274; OAuth Required  Hide a movie from getting recommended anymore.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String id = "922"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.hideAMovieRecommendation(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#hideAMovieRecommendation");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="hideAShowRecommendation"></a>
# **hideAShowRecommendation**
> hideAShowRecommendation(id, traktApiVersion, traktApiKey)

Hide a show recommendation

#### &amp;#128274; OAuth Required  Hide a show from getting recommended anymore.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String id = "922"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.hideAShowRecommendation(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#hideAShowRecommendation");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

