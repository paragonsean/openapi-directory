# VideosTextTracksApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTextTrack**](VideosTextTracksApi.md#createTextTrack) | **POST** /videos/{video_id}/texttracks | Add a text track to a video |
| [**createTextTrackAlt1**](VideosTextTracksApi.md#createTextTrackAlt1) | **POST** /channels/{channel_id}/videos/{video_id}/texttracks | Add a text track to a video |
| [**deleteTextTrack**](VideosTextTracksApi.md#deleteTextTrack) | **DELETE** /videos/{video_id}/texttracks/{texttrack_id} | Delete a text track |
| [**editTextTrack**](VideosTextTracksApi.md#editTextTrack) | **PATCH** /videos/{video_id}/texttracks/{texttrack_id} | Edit a text track |
| [**getTextTrack**](VideosTextTracksApi.md#getTextTrack) | **GET** /videos/{video_id}/texttracks/{texttrack_id} | Get a specific text track |
| [**getTextTracks**](VideosTextTracksApi.md#getTextTracks) | **GET** /videos/{video_id}/texttracks | Get all the text tracks of a video |
| [**getTextTracksAlt1**](VideosTextTracksApi.md#getTextTracksAlt1) | **GET** /channels/{channel_id}/videos/{video_id}/texttracks | Get all the text tracks of a video |


<a id="createTextTrack"></a>
# **createTextTrack**
> TextTrack createTextTrack(videoId, createTextTrackAlt1Request)

Add a text track to a video

For additional information, see our [text track upload guide](https://developer.vimeo.com/api/upload/texttracks).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTextTracksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosTextTracksApi apiInstance = new VideosTextTracksApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    CreateTextTrackAlt1Request createTextTrackAlt1Request = new CreateTextTrackAlt1Request(); // CreateTextTrackAlt1Request | 
    try {
      TextTrack result = apiInstance.createTextTrack(videoId, createTextTrackAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTextTracksApi#createTextTrack");
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
| **videoId** | **BigDecimal**| The ID of the video. | |
| **createTextTrackAlt1Request** | [**CreateTextTrackAlt1Request**](CreateTextTrackAlt1Request.md)|  | |

### Return type

[**TextTrack**](TextTrack.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.video.texttrack+json
 - **Accept**: application/vnd.vimeo.video.texttrack+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The text track was added. |  -  |
| **403** | * The authenticated user can&#39;t edit the text track. * Error code 2204: The request contains errors. |  -  |

<a id="createTextTrackAlt1"></a>
# **createTextTrackAlt1**
> TextTrack createTextTrackAlt1(channelId, videoId, createTextTrackAlt1Request)

Add a text track to a video

For additional information, see our [text track upload guide](https://developer.vimeo.com/api/upload/texttracks).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTextTracksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosTextTracksApi apiInstance = new VideosTextTracksApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    CreateTextTrackAlt1Request createTextTrackAlt1Request = new CreateTextTrackAlt1Request(); // CreateTextTrackAlt1Request | 
    try {
      TextTrack result = apiInstance.createTextTrackAlt1(channelId, videoId, createTextTrackAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTextTracksApi#createTextTrackAlt1");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **createTextTrackAlt1Request** | [**CreateTextTrackAlt1Request**](CreateTextTrackAlt1Request.md)|  | |

### Return type

[**TextTrack**](TextTrack.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.video.texttrack+json
 - **Accept**: application/vnd.vimeo.video.texttrack+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The text track was added. |  -  |
| **403** | * The authenticated user can&#39;t edit the text track. * Error code 2204: The request contains errors. |  -  |

<a id="deleteTextTrack"></a>
# **deleteTextTrack**
> deleteTextTrack(texttrackId, videoId)

Delete a text track

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTextTracksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosTextTracksApi apiInstance = new VideosTextTracksApi(defaultClient);
    BigDecimal texttrackId = new BigDecimal("12345"); // BigDecimal | The ID of the text track.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteTextTrack(texttrackId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTextTracksApi#deleteTextTrack");
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
| **texttrackId** | **BigDecimal**| The ID of the text track. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video.texttrack+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The text track was deleted. |  -  |
| **403** | * Error code 3430: You don&#39;t have permission to access this text track. * Error code 3431: This text track is disabled. |  -  |
| **404** | * No such video or text track exists. * The authenticated user can&#39;t delete the text track. * Error code 5014: The text track that you specified doesn&#39;t exist. * Error code 5015: The text track that you specified belongs to a different video. |  -  |

<a id="editTextTrack"></a>
# **editTextTrack**
> TextTrack editTextTrack(texttrackId, videoId, editTextTrackRequest)

Edit a text track

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTextTracksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosTextTracksApi apiInstance = new VideosTextTracksApi(defaultClient);
    BigDecimal texttrackId = new BigDecimal("12345"); // BigDecimal | The ID of the text track.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    EditTextTrackRequest editTextTrackRequest = new EditTextTrackRequest(); // EditTextTrackRequest | 
    try {
      TextTrack result = apiInstance.editTextTrack(texttrackId, videoId, editTextTrackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTextTracksApi#editTextTrack");
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
| **texttrackId** | **BigDecimal**| The ID of the text track. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **editTextTrackRequest** | [**EditTextTrackRequest**](EditTextTrackRequest.md)|  | [optional] |

### Return type

[**TextTrack**](TextTrack.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.video.texttrack+json
 - **Accept**: application/vnd.vimeo.video.texttrack+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The text track was edited. |  -  |
| **403** | * The authenticated user can&#39;t edit the text track. * Error code 2204: There are errors in the request. * Error code 3430: You don&#39;t have permission to access this text track. * Error code 3431: This text track is disabled. |  -  |
| **404** | * No such video or text track exists. * Error code 5014: The text track that you specified doesn&#39;t exist. * Error code 5015: The text track that you specified belongs to a different video. |  -  |

<a id="getTextTrack"></a>
# **getTextTrack**
> TextTrack getTextTrack(texttrackId, videoId)

Get a specific text track

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTextTracksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosTextTracksApi apiInstance = new VideosTextTracksApi(defaultClient);
    BigDecimal texttrackId = new BigDecimal("12345"); // BigDecimal | The ID of the text track.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      TextTrack result = apiInstance.getTextTrack(texttrackId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTextTracksApi#getTextTrack");
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
| **texttrackId** | **BigDecimal**| The ID of the text track. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**TextTrack**](TextTrack.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video.texttrack+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The text track was returned. |  -  |
| **403** | * Error code 3430: You don&#39;t have permission to access this text track. * Error code 3431: This text track is disabled. |  -  |
| **404** | * No such video or text track exists. * Error code 5014: The text track that you specified doesn&#39;t exist. * Error code 5015: The text track that you specified belongs to a different video. |  -  |

<a id="getTextTracks"></a>
# **getTextTracks**
> List&lt;TextTrack&gt; getTextTracks(videoId)

Get all the text tracks of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTextTracksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosTextTracksApi apiInstance = new VideosTextTracksApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      List<TextTrack> result = apiInstance.getTextTracks(videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTextTracksApi#getTextTracks");
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
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**List&lt;TextTrack&gt;**](TextTrack.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video.texttrack+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The text tracks were returned. |  -  |
| **404** | No such video exists. |  -  |

<a id="getTextTracksAlt1"></a>
# **getTextTracksAlt1**
> List&lt;TextTrack&gt; getTextTracksAlt1(channelId, videoId)

Get all the text tracks of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTextTracksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosTextTracksApi apiInstance = new VideosTextTracksApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      List<TextTrack> result = apiInstance.getTextTracksAlt1(channelId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTextTracksApi#getTextTracksAlt1");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**List&lt;TextTrack&gt;**](TextTrack.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video.texttrack+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The text tracks were returned. |  -  |
| **404** | No such video exists. |  -  |

