# ScrobbleApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pauseWatchingInAMediaCenter**](ScrobbleApi.md#pauseWatchingInAMediaCenter) | **POST** /scrobble/pause | Pause watching in a media center |
| [**startWatchingInAMediaCenter**](ScrobbleApi.md#startWatchingInAMediaCenter) | **POST** /scrobble/start | Start watching in a media center |
| [**stopOrFinishWatchingInAMediaCenter**](ScrobbleApi.md#stopOrFinishWatchingInAMediaCenter) | **POST** /scrobble/stop | Stop or finish watching in a media center |


<a id="pauseWatchingInAMediaCenter"></a>
# **pauseWatchingInAMediaCenter**
> pauseWatchingInAMediaCenter(traktApiVersion, traktApiKey, pauseWatchingInAMediaCenterRequest)

Pause watching in a media center

#### &amp;#128274; OAuth Required  Use this method when the video is paused. The playback progress will be saved and [**_/sync/playback**](/reference/sync/playback/) can be used to resume the video from this exact position. Unpause a video by calling the [**_/scrobble/start**](/reference/scrobble/start/) method again.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60; or &#x60;episode&#x60; object. (see examples &amp;#8594;) | | &#x60;progress&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | float | Progress percentage between 0 and 100. | | &#x60;app_version&#x60; | string | Version number of the app. | | &#x60;app_date&#x60; | string | Build date of the app. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScrobbleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScrobbleApi apiInstance = new ScrobbleApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    PauseWatchingInAMediaCenterRequest pauseWatchingInAMediaCenterRequest = new PauseWatchingInAMediaCenterRequest(); // PauseWatchingInAMediaCenterRequest | 
    try {
      apiInstance.pauseWatchingInAMediaCenter(traktApiVersion, traktApiKey, pauseWatchingInAMediaCenterRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScrobbleApi#pauseWatchingInAMediaCenter");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **pauseWatchingInAMediaCenterRequest** | [**PauseWatchingInAMediaCenterRequest**](PauseWatchingInAMediaCenterRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="startWatchingInAMediaCenter"></a>
# **startWatchingInAMediaCenter**
> startWatchingInAMediaCenter(traktApiVersion, traktApiKey, startWatchingInAMediaCenterRequest)

Start watching in a media center

#### &amp;#128274; OAuth Required  Use this method when the video initially starts playing or is unpaused. This will remove any playback progress if it exists.  **Note:** A watching status will auto expire after the remaining runtime has elapsed. There is no need to call this method again while continuing to watch the same item.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60; or &#x60;episode&#x60; object. (see examples &amp;#8594;) | | &#x60;progress&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | float | Progress percentage between 0 and 100. | | &#x60;app_version&#x60; | string | Version number of the app. | | &#x60;app_date&#x60; | string | Build date of the app. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScrobbleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScrobbleApi apiInstance = new ScrobbleApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    StartWatchingInAMediaCenterRequest startWatchingInAMediaCenterRequest = new StartWatchingInAMediaCenterRequest(); // StartWatchingInAMediaCenterRequest | 
    try {
      apiInstance.startWatchingInAMediaCenter(traktApiVersion, traktApiKey, startWatchingInAMediaCenterRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScrobbleApi#startWatchingInAMediaCenter");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **startWatchingInAMediaCenterRequest** | [**StartWatchingInAMediaCenterRequest**](StartWatchingInAMediaCenterRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="stopOrFinishWatchingInAMediaCenter"></a>
# **stopOrFinishWatchingInAMediaCenter**
> stopOrFinishWatchingInAMediaCenter(traktApiVersion, traktApiKey, stopOrFinishWatchingInAMediaCenterRequest)

Stop or finish watching in a media center

#### &amp;#128274; OAuth Required  Use this method when the video is stopped or finishes playing on its own. If the progress is above 80%, the video will be scrobbled and the &#x60;action&#x60; will be set to **scrobble**. A unique history &#x60;id&#x60; (64-bit integer) will be returned and can be used to reference this &#x60;scrobble&#x60; directly.  If the progress is less than 80%, it will be treated as a *pause* and the &#x60;action&#x60; will be set to **pause**. The playback progress will be saved and [**_/sync/playback**](/reference/sync/playback/) can be used to resume the video from this exact position.  **Note:** If you prefer to use a threshold higher than 80%, you should use [**_/scrobble/pause**](/reference/scrobble/pause/) yourself so it doesn&#39;t create duplicate scrobbles.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60; or &#x60;episode&#x60; object. (see examples &amp;#8594;) | | &#x60;progress&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | flloat | Progress percentage between 0 and 100. | | &#x60;app_version&#x60; | string | Version number of the app. | | &#x60;app_date&#x60; | string | Build date of the app. |  **Note:** If the same item was just scrobbled, a &#x60;409&#x60; HTTP status code will returned to avoid scrobbling a duplicate. The response will contain a &#x60;watched_at&#x60; timestamp when the item was last scrobbled and a &#x60;expires_at&#x60; timestamp when the item can be scrobbled again.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScrobbleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScrobbleApi apiInstance = new ScrobbleApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    StopOrFinishWatchingInAMediaCenterRequest stopOrFinishWatchingInAMediaCenterRequest = new StopOrFinishWatchingInAMediaCenterRequest(); // StopOrFinishWatchingInAMediaCenterRequest | 
    try {
      apiInstance.stopOrFinishWatchingInAMediaCenter(traktApiVersion, traktApiKey, stopOrFinishWatchingInAMediaCenterRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScrobbleApi#stopOrFinishWatchingInAMediaCenter");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **stopOrFinishWatchingInAMediaCenterRequest** | [**StopOrFinishWatchingInAMediaCenterRequest**](StopOrFinishWatchingInAMediaCenterRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **409** | The same item was recently scrobbled. |  -  |

