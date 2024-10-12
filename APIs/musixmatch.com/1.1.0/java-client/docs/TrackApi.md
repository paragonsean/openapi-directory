# TrackApi

All URIs are relative to *https://api.musixmatch.com/ws/1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**albumTracksGetGet**](TrackApi.md#albumTracksGetGet) | **GET** /album.tracks.get |  |
| [**chartTracksGetGet**](TrackApi.md#chartTracksGetGet) | **GET** /chart.tracks.get |  |
| [**matcherTrackGetGet**](TrackApi.md#matcherTrackGetGet) | **GET** /matcher.track.get |  |
| [**trackGetGet**](TrackApi.md#trackGetGet) | **GET** /track.get |  |
| [**trackSearchGet**](TrackApi.md#trackSearchGet) | **GET** /track.search |  |


<a id="albumTracksGetGet"></a>
# **albumTracksGetGet**
> AlbumTracksGetGet200Response albumTracksGetGet(albumId, format, paramCallback, fHasLyrics, page, pageSize)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    TrackApi apiInstance = new TrackApi(defaultClient);
    String albumId = "albumId_example"; // String | The musiXmatch album id
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    String fHasLyrics = "fHasLyrics_example"; // String | When set, filter only contents with lyrics
    BigDecimal page = new BigDecimal(78); // BigDecimal | Define the page number for paginated results
    BigDecimal pageSize = new BigDecimal(78); // BigDecimal | Define the page size for paginated results.Range is 1 to 100.
    try {
      AlbumTracksGetGet200Response result = apiInstance.albumTracksGetGet(albumId, format, paramCallback, fHasLyrics, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrackApi#albumTracksGetGet");
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
| **albumId** | **String**| The musiXmatch album id | |
| **format** | **String**| output format: json, jsonp, xml. | [optional] [default to json] |
| **paramCallback** | **String**| jsonp callback | [optional] |
| **fHasLyrics** | **String**| When set, filter only contents with lyrics | [optional] |
| **page** | **BigDecimal**| Define the page number for paginated results | [optional] |
| **pageSize** | **BigDecimal**| Define the page size for paginated results.Range is 1 to 100. | [optional] |

### Return type

[**AlbumTracksGetGet200Response**](AlbumTracksGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

<a id="chartTracksGetGet"></a>
# **chartTracksGetGet**
> ChartTracksGetGet200Response chartTracksGetGet(format, paramCallback, page, pageSize, country, fHasLyrics)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    TrackApi apiInstance = new TrackApi(defaultClient);
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    BigDecimal page = new BigDecimal(78); // BigDecimal | Define the page number for paginated results
    BigDecimal pageSize = new BigDecimal(78); // BigDecimal | Define the page size for paginated results.Range is 1 to 100.
    String country = "us"; // String | A valid ISO 3166 country code
    String fHasLyrics = "fHasLyrics_example"; // String | When set, filter only contents with lyrics
    try {
      ChartTracksGetGet200Response result = apiInstance.chartTracksGetGet(format, paramCallback, page, pageSize, country, fHasLyrics);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrackApi#chartTracksGetGet");
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
| **format** | **String**| output format: json, jsonp, xml. | [optional] [default to json] |
| **paramCallback** | **String**| jsonp callback | [optional] |
| **page** | **BigDecimal**| Define the page number for paginated results | [optional] |
| **pageSize** | **BigDecimal**| Define the page size for paginated results.Range is 1 to 100. | [optional] |
| **country** | **String**| A valid ISO 3166 country code | [optional] [default to us] |
| **fHasLyrics** | **String**| When set, filter only contents with lyrics | [optional] |

### Return type

[**ChartTracksGetGet200Response**](ChartTracksGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

<a id="matcherTrackGetGet"></a>
# **matcherTrackGetGet**
> MatcherTrackGetGet200Response matcherTrackGetGet(format, paramCallback, qArtist, qTrack, fHasLyrics, fHasSubtitle)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    TrackApi apiInstance = new TrackApi(defaultClient);
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    String qArtist = "qArtist_example"; // String | The song artist
    String qTrack = "qTrack_example"; // String | The song title
    BigDecimal fHasLyrics = new BigDecimal(78); // BigDecimal | When set, filter only contents with lyrics
    BigDecimal fHasSubtitle = new BigDecimal(78); // BigDecimal | When set, filter only contents with subtitles
    try {
      MatcherTrackGetGet200Response result = apiInstance.matcherTrackGetGet(format, paramCallback, qArtist, qTrack, fHasLyrics, fHasSubtitle);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrackApi#matcherTrackGetGet");
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
| **format** | **String**| output format: json, jsonp, xml. | [optional] [default to json] |
| **paramCallback** | **String**| jsonp callback | [optional] |
| **qArtist** | **String**| The song artist | [optional] |
| **qTrack** | **String**| The song title | [optional] |
| **fHasLyrics** | **BigDecimal**| When set, filter only contents with lyrics | [optional] |
| **fHasSubtitle** | **BigDecimal**| When set, filter only contents with subtitles | [optional] |

### Return type

[**MatcherTrackGetGet200Response**](MatcherTrackGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

<a id="trackGetGet"></a>
# **trackGetGet**
> MatcherTrackGetGet200Response trackGetGet(trackId, format, paramCallback)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    TrackApi apiInstance = new TrackApi(defaultClient);
    String trackId = "trackId_example"; // String | The musiXmatch track id
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    try {
      MatcherTrackGetGet200Response result = apiInstance.trackGetGet(trackId, format, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrackApi#trackGetGet");
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
| **trackId** | **String**| The musiXmatch track id | |
| **format** | **String**| output format: json, jsonp, xml. | [optional] [default to json] |
| **paramCallback** | **String**| jsonp callback | [optional] |

### Return type

[**MatcherTrackGetGet200Response**](MatcherTrackGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

<a id="trackSearchGet"></a>
# **trackSearchGet**
> ChartTracksGetGet200Response trackSearchGet(format, paramCallback, qTrack, qArtist, qLyrics, fArtistId, fMusicGenreId, fLyricsLanguage, fHasLyrics, sArtistRating, sTrackRating, quorumFactor, pageSize, page)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    TrackApi apiInstance = new TrackApi(defaultClient);
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    String qTrack = "qTrack_example"; // String | The song title
    String qArtist = "qArtist_example"; // String | The song artist
    String qLyrics = "qLyrics_example"; // String | Any word in the lyrics
    BigDecimal fArtistId = new BigDecimal(78); // BigDecimal | When set, filter by this artist id
    BigDecimal fMusicGenreId = new BigDecimal(78); // BigDecimal | When set, filter by this music category id
    BigDecimal fLyricsLanguage = new BigDecimal(78); // BigDecimal | Filter by the lyrics language (en,it,..)
    BigDecimal fHasLyrics = new BigDecimal(78); // BigDecimal | When set, filter only contents with lyrics
    String sArtistRating = "sArtistRating_example"; // String | Sort by our popularity index for artists (asc|desc)
    String sTrackRating = "sTrackRating_example"; // String | Sort by our popularity index for tracks (asc|desc)
    BigDecimal quorumFactor = new BigDecimal("1.0"); // BigDecimal | Search only a part of the given query string.Allowed range is (0.1 – 0.9)
    BigDecimal pageSize = new BigDecimal(78); // BigDecimal | Define the page size for paginated results.Range is 1 to 100.
    BigDecimal page = new BigDecimal(78); // BigDecimal | Define the page number for paginated results
    try {
      ChartTracksGetGet200Response result = apiInstance.trackSearchGet(format, paramCallback, qTrack, qArtist, qLyrics, fArtistId, fMusicGenreId, fLyricsLanguage, fHasLyrics, sArtistRating, sTrackRating, quorumFactor, pageSize, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrackApi#trackSearchGet");
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
| **format** | **String**| output format: json, jsonp, xml. | [optional] [default to json] |
| **paramCallback** | **String**| jsonp callback | [optional] |
| **qTrack** | **String**| The song title | [optional] |
| **qArtist** | **String**| The song artist | [optional] |
| **qLyrics** | **String**| Any word in the lyrics | [optional] |
| **fArtistId** | **BigDecimal**| When set, filter by this artist id | [optional] |
| **fMusicGenreId** | **BigDecimal**| When set, filter by this music category id | [optional] |
| **fLyricsLanguage** | **BigDecimal**| Filter by the lyrics language (en,it,..) | [optional] |
| **fHasLyrics** | **BigDecimal**| When set, filter only contents with lyrics | [optional] |
| **sArtistRating** | **String**| Sort by our popularity index for artists (asc|desc) | [optional] |
| **sTrackRating** | **String**| Sort by our popularity index for tracks (asc|desc) | [optional] |
| **quorumFactor** | **BigDecimal**| Search only a part of the given query string.Allowed range is (0.1 – 0.9) | [optional] [default to 1.0] |
| **pageSize** | **BigDecimal**| Define the page size for paginated results.Range is 1 to 100. | [optional] |
| **page** | **BigDecimal**| Define the page number for paginated results | [optional] |

### Return type

[**ChartTracksGetGet200Response**](ChartTracksGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

