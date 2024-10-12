# SubtitleApi

All URIs are relative to *https://api.musixmatch.com/ws/1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**matcherSubtitleGetGet**](SubtitleApi.md#matcherSubtitleGetGet) | **GET** /matcher.subtitle.get |  |
| [**trackSubtitleGetGet**](SubtitleApi.md#trackSubtitleGetGet) | **GET** /track.subtitle.get |  |


<a id="matcherSubtitleGetGet"></a>
# **matcherSubtitleGetGet**
> MatcherSubtitleGetGet200Response matcherSubtitleGetGet(format, paramCallback, qTrack, qArtist, fSubtitleLength, fSubtitleLengthMaxDeviation)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubtitleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    SubtitleApi apiInstance = new SubtitleApi(defaultClient);
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    String qTrack = "qTrack_example"; // String | The song title
    String qArtist = "qArtist_example"; // String |  The song artist
    BigDecimal fSubtitleLength = new BigDecimal(78); // BigDecimal | Filter by subtitle length in seconds
    BigDecimal fSubtitleLengthMaxDeviation = new BigDecimal(78); // BigDecimal | Max deviation for a subtitle length in seconds
    try {
      MatcherSubtitleGetGet200Response result = apiInstance.matcherSubtitleGetGet(format, paramCallback, qTrack, qArtist, fSubtitleLength, fSubtitleLengthMaxDeviation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubtitleApi#matcherSubtitleGetGet");
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
| **qArtist** | **String**|  The song artist | [optional] |
| **fSubtitleLength** | **BigDecimal**| Filter by subtitle length in seconds | [optional] |
| **fSubtitleLengthMaxDeviation** | **BigDecimal**| Max deviation for a subtitle length in seconds | [optional] |

### Return type

[**MatcherSubtitleGetGet200Response**](MatcherSubtitleGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

<a id="trackSubtitleGetGet"></a>
# **trackSubtitleGetGet**
> MatcherSubtitleGetGet200Response trackSubtitleGetGet(trackId, format, paramCallback)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubtitleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    SubtitleApi apiInstance = new SubtitleApi(defaultClient);
    String trackId = "trackId_example"; // String | The musiXmatch track id
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    try {
      MatcherSubtitleGetGet200Response result = apiInstance.trackSubtitleGetGet(trackId, format, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubtitleApi#trackSubtitleGetGet");
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

[**MatcherSubtitleGetGet200Response**](MatcherSubtitleGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

