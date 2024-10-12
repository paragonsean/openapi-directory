# LyricsApi

All URIs are relative to *https://api.musixmatch.com/ws/1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**matcherLyricsGetGet**](LyricsApi.md#matcherLyricsGetGet) | **GET** /matcher.lyrics.get |  |
| [**trackLyricsGetGet**](LyricsApi.md#trackLyricsGetGet) | **GET** /track.lyrics.get |  |


<a id="matcherLyricsGetGet"></a>
# **matcherLyricsGetGet**
> MatcherLyricsGetGet200Response matcherLyricsGetGet(format, paramCallback, qTrack, qArtist)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LyricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    LyricsApi apiInstance = new LyricsApi(defaultClient);
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    String qTrack = "qTrack_example"; // String | The song title
    String qArtist = "qArtist_example"; // String | The song artist
    try {
      MatcherLyricsGetGet200Response result = apiInstance.matcherLyricsGetGet(format, paramCallback, qTrack, qArtist);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LyricsApi#matcherLyricsGetGet");
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

### Return type

[**MatcherLyricsGetGet200Response**](MatcherLyricsGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

<a id="trackLyricsGetGet"></a>
# **trackLyricsGetGet**
> MatcherLyricsGetGet200Response trackLyricsGetGet(trackId, format, paramCallback)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LyricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    LyricsApi apiInstance = new LyricsApi(defaultClient);
    String trackId = "trackId_example"; // String | The musiXmatch track id
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    try {
      MatcherLyricsGetGet200Response result = apiInstance.trackLyricsGetGet(trackId, format, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LyricsApi#trackLyricsGetGet");
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

[**MatcherLyricsGetGet200Response**](MatcherLyricsGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

