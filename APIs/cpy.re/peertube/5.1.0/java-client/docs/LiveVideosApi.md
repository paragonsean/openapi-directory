# LiveVideosApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addLive**](LiveVideosApi.md#addLive) | **POST** /api/v1/videos/live | Create a live |
| [**apiV1VideosIdLiveSessionGet**](LiveVideosApi.md#apiV1VideosIdLiveSessionGet) | **GET** /api/v1/videos/{id}/live-session | Get live session of a replay |
| [**apiV1VideosLiveIdSessionsGet**](LiveVideosApi.md#apiV1VideosLiveIdSessionsGet) | **GET** /api/v1/videos/live/{id}/sessions | List live sessions |
| [**getLiveId**](LiveVideosApi.md#getLiveId) | **GET** /api/v1/videos/live/{id} | Get information about a live |
| [**updateLiveId**](LiveVideosApi.md#updateLiveId) | **PUT** /api/v1/videos/live/{id} | Update information about a live |


<a id="addLive"></a>
# **addLive**
> VideoUploadResponse addLive(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile)

Create a live

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    LiveVideosApi apiInstance = new LiveVideosApi(defaultClient);
    Integer channelId = 56; // Integer | Channel id that will contain this live video
    String name = "name_example"; // String | Live video/replay name
    Integer category = 56; // Integer | category id of the video (see [/videos/categories](#operation/getCategories))
    Boolean commentsEnabled = true; // Boolean | Enable or disable comments for this live video/replay
    String description = "description_example"; // String | Live video/replay description
    Boolean downloadEnabled = true; // Boolean | Enable or disable downloading for the replay of this live video
    String language = "language_example"; // String | language id of the video (see [/videos/languages](#operation/getLanguages))
    LiveVideoLatencyMode latencyMode = LiveVideoLatencyMode.fromValue("1"); // LiveVideoLatencyMode | 
    Integer licence = 56; // Integer | licence id of the video (see [/videos/licences](#operation/getLicences))
    Boolean nsfw = true; // Boolean | Whether or not this live video/replay contains sensitive content
    Boolean permanentLive = true; // Boolean | User can stream multiple times in a permanent live
    File previewfile = new File("/path/to/file"); // File | Live video/replay preview file
    VideoPrivacySet privacy = VideoPrivacySet.fromValue("1"); // VideoPrivacySet | 
    LiveVideoReplaySettings replaySettings = new LiveVideoReplaySettings(); // LiveVideoReplaySettings | 
    Boolean saveReplay = true; // Boolean | 
    String support = "support_example"; // String | A text tell the audience how to support the creator
    List<String> tags = Arrays.asList(); // List<String> | Live video/replay tags (maximum 5 tags each between 2 and 30 characters)
    File thumbnailfile = new File("/path/to/file"); // File | Live video/replay thumbnail file
    try {
      VideoUploadResponse result = apiInstance.addLive(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveVideosApi#addLive");
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
| **channelId** | **Integer**| Channel id that will contain this live video | |
| **name** | **String**| Live video/replay name | |
| **category** | **Integer**| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] |
| **commentsEnabled** | **Boolean**| Enable or disable comments for this live video/replay | [optional] |
| **description** | **String**| Live video/replay description | [optional] |
| **downloadEnabled** | **Boolean**| Enable or disable downloading for the replay of this live video | [optional] |
| **language** | **String**| language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] |
| **latencyMode** | [**LiveVideoLatencyMode**](LiveVideoLatencyMode.md)|  | [optional] [enum: 1, 2, 3] |
| **licence** | **Integer**| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] |
| **nsfw** | **Boolean**| Whether or not this live video/replay contains sensitive content | [optional] |
| **permanentLive** | **Boolean**| User can stream multiple times in a permanent live | [optional] |
| **previewfile** | **File**| Live video/replay preview file | [optional] |
| **privacy** | [**VideoPrivacySet**](VideoPrivacySet.md)|  | [optional] [enum: 1, 2, 3, 4] |
| **replaySettings** | [**LiveVideoReplaySettings**](LiveVideoReplaySettings.md)|  | [optional] |
| **saveReplay** | **Boolean**|  | [optional] |
| **support** | **String**| A text tell the audience how to support the creator | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Live video/replay tags (maximum 5 tags each between 2 and 30 characters) | [optional] |
| **thumbnailfile** | **File**| Live video/replay thumbnail file | [optional] |

### Return type

[**VideoUploadResponse**](VideoUploadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Disambiguate via &#x60;type&#x60;: - default type for a validation error - &#x60;live_conflicting_permanent_and_save_replay&#x60; for conflicting parameters set  |  -  |
| **403** | Disambiguate via &#x60;type&#x60;: - &#x60;live_not_enabled&#x60; for a disabled live feature - &#x60;live_not_allowing_replay&#x60; for a disabled replay feature - &#x60;max_instance_lives_limit_reached&#x60; for the absolute concurrent live limit - &#x60;max_user_lives_limit_reached&#x60; for the user concurrent live limit  |  -  |

<a id="apiV1VideosIdLiveSessionGet"></a>
# **apiV1VideosIdLiveSessionGet**
> LiveVideoSessionResponse apiV1VideosIdLiveSessionGet(id)

Get live session of a replay

If the video is a replay of a live, you can find the associated live session using this endpoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    LiveVideosApi apiInstance = new LiveVideosApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      LiveVideoSessionResponse result = apiInstance.apiV1VideosIdLiveSessionGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveVideosApi#apiV1VideosIdLiveSessionGet");
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
| **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | |

### Return type

[**LiveVideoSessionResponse**](LiveVideoSessionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1VideosLiveIdSessionsGet"></a>
# **apiV1VideosLiveIdSessionsGet**
> ApiV1VideosLiveIdSessionsGet200Response apiV1VideosLiveIdSessionsGet(id)

List live sessions

List all sessions created in a particular live

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    LiveVideosApi apiInstance = new LiveVideosApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      ApiV1VideosLiveIdSessionsGet200Response result = apiInstance.apiV1VideosLiveIdSessionsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveVideosApi#apiV1VideosLiveIdSessionsGet");
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
| **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | |

### Return type

[**ApiV1VideosLiveIdSessionsGet200Response**](ApiV1VideosLiveIdSessionsGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getLiveId"></a>
# **getLiveId**
> LiveVideoResponse getLiveId(id)

Get information about a live

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    LiveVideosApi apiInstance = new LiveVideosApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      LiveVideoResponse result = apiInstance.getLiveId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveVideosApi#getLiveId");
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
| **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | |

### Return type

[**LiveVideoResponse**](LiveVideoResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="updateLiveId"></a>
# **updateLiveId**
> updateLiveId(id, liveVideoUpdate)

Update information about a live

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    LiveVideosApi apiInstance = new LiveVideosApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    LiveVideoUpdate liveVideoUpdate = new LiveVideoUpdate(); // LiveVideoUpdate | 
    try {
      apiInstance.updateLiveId(id, liveVideoUpdate);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveVideosApi#updateLiveId");
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
| **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | |
| **liveVideoUpdate** | [**LiveVideoUpdate**](LiveVideoUpdate.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **400** | bad parameters or trying to update a live that has already started |  -  |
| **403** | trying to save replay of the live but saving replay is not enabled on the instance |  -  |

