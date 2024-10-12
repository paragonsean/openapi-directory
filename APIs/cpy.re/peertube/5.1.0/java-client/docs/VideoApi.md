# VideoApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addLive_0**](VideoApi.md#addLive_0) | **POST** /api/v1/videos/live | Create a live |
| [**addView**](VideoApi.md#addView) | **POST** /api/v1/videos/{id}/views | Notify user is watching a video |
| [**apiV1VideosIdStudioEditPost_0**](VideoApi.md#apiV1VideosIdStudioEditPost_0) | **POST** /api/v1/videos/{id}/studio/edit | Create a studio task |
| [**apiV1VideosIdWatchingPut**](VideoApi.md#apiV1VideosIdWatchingPut) | **PUT** /api/v1/videos/{id}/watching | Set watching progress of a video |
| [**delVideo**](VideoApi.md#delVideo) | **DELETE** /api/v1/videos/{id} | Delete a video |
| [**getAccountVideos_0**](VideoApi.md#getAccountVideos_0) | **GET** /api/v1/accounts/{name}/videos | List videos of an account |
| [**getCategories**](VideoApi.md#getCategories) | **GET** /api/v1/videos/categories | List available video categories |
| [**getLanguages**](VideoApi.md#getLanguages) | **GET** /api/v1/videos/languages | List available video languages |
| [**getLicences**](VideoApi.md#getLicences) | **GET** /api/v1/videos/licences | List available video licences |
| [**getLiveId_0**](VideoApi.md#getLiveId_0) | **GET** /api/v1/videos/live/{id} | Get information about a live |
| [**getVideo**](VideoApi.md#getVideo) | **GET** /api/v1/videos/{id} | Get a video |
| [**getVideoChannelVideos**](VideoApi.md#getVideoChannelVideos) | **GET** /api/v1/video-channels/{channelHandle}/videos | List videos of a video channel |
| [**getVideoDesc**](VideoApi.md#getVideoDesc) | **GET** /api/v1/videos/{id}/description | Get complete video description |
| [**getVideoPrivacyPolicies**](VideoApi.md#getVideoPrivacyPolicies) | **GET** /api/v1/videos/privacies | List available video privacy policies |
| [**getVideoSource**](VideoApi.md#getVideoSource) | **POST** /api/v1/videos/{id}/source | Get video source file metadata |
| [**getVideos**](VideoApi.md#getVideos) | **GET** /api/v1/videos | List videos |
| [**putVideo**](VideoApi.md#putVideo) | **PUT** /api/v1/videos/{id} | Update a video |
| [**requestVideoToken**](VideoApi.md#requestVideoToken) | **POST** /api/v1/videos/{id}/token | Request video token |
| [**updateLiveId_0**](VideoApi.md#updateLiveId_0) | **PUT** /api/v1/videos/live/{id} | Update information about a live |
| [**uploadLegacy**](VideoApi.md#uploadLegacy) | **POST** /api/v1/videos/upload | Upload a video |
| [**uploadResumable**](VideoApi.md#uploadResumable) | **PUT** /api/v1/videos/upload-resumable | Send chunk for the resumable upload of a video |
| [**uploadResumableCancel**](VideoApi.md#uploadResumableCancel) | **DELETE** /api/v1/videos/upload-resumable | Cancel the resumable upload of a video, deleting any data uploaded so far |
| [**uploadResumableInit**](VideoApi.md#uploadResumableInit) | **POST** /api/v1/videos/upload-resumable | Initialize the resumable upload of a video |


<a id="addLive_0"></a>
# **addLive_0**
> VideoUploadResponse addLive_0(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile)

Create a live

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoApi apiInstance = new VideoApi(defaultClient);
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
      VideoUploadResponse result = apiInstance.addLive_0(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#addLive_0");
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

<a id="addView"></a>
# **addView**
> addView(id, userViewingVideo)

Notify user is watching a video

Call this endpoint regularly (every 5-10 seconds for example) to notify the server the user is watching the video. After a while, PeerTube will increase video&#39;s viewers counter. If the user is authenticated, PeerTube will also store the current player time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoApi apiInstance = new VideoApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    UserViewingVideo userViewingVideo = new UserViewingVideo(); // UserViewingVideo | 
    try {
      apiInstance.addView(id, userViewingVideo);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#addView");
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
| **userViewingVideo** | [**UserViewingVideo**](UserViewingVideo.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="apiV1VideosIdStudioEditPost_0"></a>
# **apiV1VideosIdStudioEditPost_0**
> apiV1VideosIdStudioEditPost_0(id)

Create a studio task

Create a task to edit a video  (cut, add intro/outro etc)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoApi apiInstance = new VideoApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      apiInstance.apiV1VideosIdStudioEditPost_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#apiV1VideosIdStudioEditPost_0");
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

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **400** | incorrect parameters |  -  |
| **404** | video not found |  -  |

<a id="apiV1VideosIdWatchingPut"></a>
# **apiV1VideosIdWatchingPut**
> apiV1VideosIdWatchingPut(id, userViewingVideo)

Set watching progress of a video

This endpoint has been deprecated. Use &#x60;/videos/{id}/views&#x60; instead

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoApi apiInstance = new VideoApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    UserViewingVideo userViewingVideo = new UserViewingVideo(); // UserViewingVideo | 
    try {
      apiInstance.apiV1VideosIdWatchingPut(id, userViewingVideo);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#apiV1VideosIdWatchingPut");
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
| **userViewingVideo** | [**UserViewingVideo**](UserViewingVideo.md)|  | |

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

<a id="delVideo"></a>
# **delVideo**
> delVideo(id)

Delete a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoApi apiInstance = new VideoApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      apiInstance.delVideo(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#delVideo");
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

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="getAccountVideos_0"></a>
# **getAccountVideos_0**
> VideoListResponse getAccountVideos_0(name, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched)

List videos of an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoApi apiInstance = new VideoApi(defaultClient);
    String name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
    GetAccountVideosCategoryOneOfParameter categoryOneOf = new GetAccountVideosCategoryOneOfParameter(); // GetAccountVideosCategoryOneOfParameter | category id of the video (see [/videos/categories](#operation/getCategories))
    Boolean isLive = true; // Boolean | whether or not the video is a live
    GetAccountVideosTagsOneOfParameter tagsOneOf = new GetAccountVideosTagsOneOfParameter(); // GetAccountVideosTagsOneOfParameter | tag(s) of the video
    GetAccountVideosTagsAllOfParameter tagsAllOf = new GetAccountVideosTagsAllOfParameter(); // GetAccountVideosTagsAllOfParameter | tag(s) of the video, where all should be present in the video
    GetAccountVideosLicenceOneOfParameter licenceOneOf = new GetAccountVideosLicenceOneOfParameter(); // GetAccountVideosLicenceOneOfParameter | licence id of the video (see [/videos/licences](#operation/getLicences))
    GetAccountVideosLanguageOneOfParameter languageOneOf = new GetAccountVideosLanguageOneOfParameter(); // GetAccountVideosLanguageOneOfParameter | language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language
    String nsfw = "true"; // String | whether to include nsfw videos, if any
    Boolean isLocal = true; // Boolean | **PeerTube >= 4.0** Display only local or remote videos
    Integer include = 0; // Integer | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
    VideoPrivacySet privacyOneOf = VideoPrivacySet.fromValue("1"); // VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
    Boolean hasHLSFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have HLS files
    Boolean hasWebtorrentFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have WebTorrent files
    String skipCount = "true"; // String | if you don't need the `total` in the response
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "name"; // String | 
    Boolean excludeAlreadyWatched = true; // Boolean | Whether or not to exclude videos that are in the user's video history
    try {
      VideoListResponse result = apiInstance.getAccountVideos_0(name, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#getAccountVideos_0");
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
| **name** | **String**| The username or handle of the account | |
| **categoryOneOf** | [**GetAccountVideosCategoryOneOfParameter**](.md)| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] |
| **isLive** | **Boolean**| whether or not the video is a live | [optional] |
| **tagsOneOf** | [**GetAccountVideosTagsOneOfParameter**](.md)| tag(s) of the video | [optional] |
| **tagsAllOf** | [**GetAccountVideosTagsAllOfParameter**](.md)| tag(s) of the video, where all should be present in the video | [optional] |
| **licenceOneOf** | [**GetAccountVideosLicenceOneOfParameter**](.md)| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] |
| **languageOneOf** | [**GetAccountVideosLanguageOneOfParameter**](.md)| language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language | [optional] |
| **nsfw** | **String**| whether to include nsfw videos, if any | [optional] [enum: true, false] |
| **isLocal** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] |
| **include** | **Integer**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] [enum: 0, 1, 2, 4, 8] |
| **privacyOneOf** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] [enum: 1, 2, 3, 4] |
| **hasHLSFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] |
| **hasWebtorrentFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] |
| **skipCount** | **String**| if you don&#39;t need the &#x60;total&#x60; in the response | [optional] [default to false] [enum: true, false] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**|  | [optional] [enum: name, -duration, -createdAt, -publishedAt, -views, -likes, -trending, -hot, -best] |
| **excludeAlreadyWatched** | **Boolean**| Whether or not to exclude videos that are in the user&#39;s video history | [optional] |

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getCategories"></a>
# **getCategories**
> List&lt;String&gt; getCategories()

List available video categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoApi apiInstance = new VideoApi(defaultClient);
    try {
      List<String> result = apiInstance.getCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#getCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getLanguages"></a>
# **getLanguages**
> List&lt;String&gt; getLanguages()

List available video languages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoApi apiInstance = new VideoApi(defaultClient);
    try {
      List<String> result = apiInstance.getLanguages();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#getLanguages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getLicences"></a>
# **getLicences**
> List&lt;String&gt; getLicences()

List available video licences

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoApi apiInstance = new VideoApi(defaultClient);
    try {
      List<String> result = apiInstance.getLicences();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#getLicences");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getLiveId_0"></a>
# **getLiveId_0**
> LiveVideoResponse getLiveId_0(id)

Get information about a live

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoApi apiInstance = new VideoApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      LiveVideoResponse result = apiInstance.getLiveId_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#getLiveId_0");
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

<a id="getVideo"></a>
# **getVideo**
> VideoDetails getVideo(id)

Get a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoApi apiInstance = new VideoApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      VideoDetails result = apiInstance.getVideo(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#getVideo");
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

[**VideoDetails**](VideoDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getVideoChannelVideos"></a>
# **getVideoChannelVideos**
> VideoListResponse getVideoChannelVideos(channelHandle, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched)

List videos of a video channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoApi apiInstance = new VideoApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    GetAccountVideosCategoryOneOfParameter categoryOneOf = new GetAccountVideosCategoryOneOfParameter(); // GetAccountVideosCategoryOneOfParameter | category id of the video (see [/videos/categories](#operation/getCategories))
    Boolean isLive = true; // Boolean | whether or not the video is a live
    GetAccountVideosTagsOneOfParameter tagsOneOf = new GetAccountVideosTagsOneOfParameter(); // GetAccountVideosTagsOneOfParameter | tag(s) of the video
    GetAccountVideosTagsAllOfParameter tagsAllOf = new GetAccountVideosTagsAllOfParameter(); // GetAccountVideosTagsAllOfParameter | tag(s) of the video, where all should be present in the video
    GetAccountVideosLicenceOneOfParameter licenceOneOf = new GetAccountVideosLicenceOneOfParameter(); // GetAccountVideosLicenceOneOfParameter | licence id of the video (see [/videos/licences](#operation/getLicences))
    GetAccountVideosLanguageOneOfParameter languageOneOf = new GetAccountVideosLanguageOneOfParameter(); // GetAccountVideosLanguageOneOfParameter | language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language
    String nsfw = "true"; // String | whether to include nsfw videos, if any
    Boolean isLocal = true; // Boolean | **PeerTube >= 4.0** Display only local or remote videos
    Integer include = 0; // Integer | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
    VideoPrivacySet privacyOneOf = VideoPrivacySet.fromValue("1"); // VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
    Boolean hasHLSFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have HLS files
    Boolean hasWebtorrentFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have WebTorrent files
    String skipCount = "true"; // String | if you don't need the `total` in the response
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "name"; // String | 
    Boolean excludeAlreadyWatched = true; // Boolean | Whether or not to exclude videos that are in the user's video history
    try {
      VideoListResponse result = apiInstance.getVideoChannelVideos(channelHandle, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#getVideoChannelVideos");
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
| **channelHandle** | **String**| The video channel handle | |
| **categoryOneOf** | [**GetAccountVideosCategoryOneOfParameter**](.md)| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] |
| **isLive** | **Boolean**| whether or not the video is a live | [optional] |
| **tagsOneOf** | [**GetAccountVideosTagsOneOfParameter**](.md)| tag(s) of the video | [optional] |
| **tagsAllOf** | [**GetAccountVideosTagsAllOfParameter**](.md)| tag(s) of the video, where all should be present in the video | [optional] |
| **licenceOneOf** | [**GetAccountVideosLicenceOneOfParameter**](.md)| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] |
| **languageOneOf** | [**GetAccountVideosLanguageOneOfParameter**](.md)| language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language | [optional] |
| **nsfw** | **String**| whether to include nsfw videos, if any | [optional] [enum: true, false] |
| **isLocal** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] |
| **include** | **Integer**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] [enum: 0, 1, 2, 4, 8] |
| **privacyOneOf** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] [enum: 1, 2, 3, 4] |
| **hasHLSFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] |
| **hasWebtorrentFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] |
| **skipCount** | **String**| if you don&#39;t need the &#x60;total&#x60; in the response | [optional] [default to false] [enum: true, false] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**|  | [optional] [enum: name, -duration, -createdAt, -publishedAt, -views, -likes, -trending, -hot, -best] |
| **excludeAlreadyWatched** | **Boolean**| Whether or not to exclude videos that are in the user&#39;s video history | [optional] |

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getVideoDesc"></a>
# **getVideoDesc**
> String getVideoDesc(id)

Get complete video description

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoApi apiInstance = new VideoApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      String result = apiInstance.getVideoDesc(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#getVideoDesc");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getVideoPrivacyPolicies"></a>
# **getVideoPrivacyPolicies**
> List&lt;String&gt; getVideoPrivacyPolicies()

List available video privacy policies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoApi apiInstance = new VideoApi(defaultClient);
    try {
      List<String> result = apiInstance.getVideoPrivacyPolicies();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#getVideoPrivacyPolicies");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getVideoSource"></a>
# **getVideoSource**
> VideoSource getVideoSource(id)

Get video source file metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoApi apiInstance = new VideoApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      VideoSource result = apiInstance.getVideoSource(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#getVideoSource");
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

[**VideoSource**](VideoSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getVideos"></a>
# **getVideos**
> VideoListResponse getVideos(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched)

List videos

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoApi apiInstance = new VideoApi(defaultClient);
    GetAccountVideosCategoryOneOfParameter categoryOneOf = new GetAccountVideosCategoryOneOfParameter(); // GetAccountVideosCategoryOneOfParameter | category id of the video (see [/videos/categories](#operation/getCategories))
    Boolean isLive = true; // Boolean | whether or not the video is a live
    GetAccountVideosTagsOneOfParameter tagsOneOf = new GetAccountVideosTagsOneOfParameter(); // GetAccountVideosTagsOneOfParameter | tag(s) of the video
    GetAccountVideosTagsAllOfParameter tagsAllOf = new GetAccountVideosTagsAllOfParameter(); // GetAccountVideosTagsAllOfParameter | tag(s) of the video, where all should be present in the video
    GetAccountVideosLicenceOneOfParameter licenceOneOf = new GetAccountVideosLicenceOneOfParameter(); // GetAccountVideosLicenceOneOfParameter | licence id of the video (see [/videos/licences](#operation/getLicences))
    GetAccountVideosLanguageOneOfParameter languageOneOf = new GetAccountVideosLanguageOneOfParameter(); // GetAccountVideosLanguageOneOfParameter | language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language
    String nsfw = "true"; // String | whether to include nsfw videos, if any
    Boolean isLocal = true; // Boolean | **PeerTube >= 4.0** Display only local or remote videos
    Integer include = 0; // Integer | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
    VideoPrivacySet privacyOneOf = VideoPrivacySet.fromValue("1"); // VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
    Boolean hasHLSFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have HLS files
    Boolean hasWebtorrentFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have WebTorrent files
    String skipCount = "true"; // String | if you don't need the `total` in the response
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "name"; // String | 
    Boolean excludeAlreadyWatched = true; // Boolean | Whether or not to exclude videos that are in the user's video history
    try {
      VideoListResponse result = apiInstance.getVideos(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#getVideos");
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
| **categoryOneOf** | [**GetAccountVideosCategoryOneOfParameter**](.md)| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] |
| **isLive** | **Boolean**| whether or not the video is a live | [optional] |
| **tagsOneOf** | [**GetAccountVideosTagsOneOfParameter**](.md)| tag(s) of the video | [optional] |
| **tagsAllOf** | [**GetAccountVideosTagsAllOfParameter**](.md)| tag(s) of the video, where all should be present in the video | [optional] |
| **licenceOneOf** | [**GetAccountVideosLicenceOneOfParameter**](.md)| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] |
| **languageOneOf** | [**GetAccountVideosLanguageOneOfParameter**](.md)| language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language | [optional] |
| **nsfw** | **String**| whether to include nsfw videos, if any | [optional] [enum: true, false] |
| **isLocal** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] |
| **include** | **Integer**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] [enum: 0, 1, 2, 4, 8] |
| **privacyOneOf** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] [enum: 1, 2, 3, 4] |
| **hasHLSFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] |
| **hasWebtorrentFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] |
| **skipCount** | **String**| if you don&#39;t need the &#x60;total&#x60; in the response | [optional] [default to false] [enum: true, false] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**|  | [optional] [enum: name, -duration, -createdAt, -publishedAt, -views, -likes, -trending, -hot, -best] |
| **excludeAlreadyWatched** | **Boolean**| Whether or not to exclude videos that are in the user&#39;s video history | [optional] |

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="putVideo"></a>
# **putVideo**
> putVideo(id, category, commentsEnabled, description, downloadEnabled, language, licence, name, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding)

Update a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoApi apiInstance = new VideoApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    Integer category = 56; // Integer | category id of the video (see [/videos/categories](#operation/getCategories))
    Boolean commentsEnabled = true; // Boolean | Enable or disable comments for this video
    String description = "description_example"; // String | Video description
    Boolean downloadEnabled = true; // Boolean | Enable or disable downloading for this video
    String language = "language_example"; // String | language id of the video (see [/videos/languages](#operation/getLanguages))
    Integer licence = 56; // Integer | licence id of the video (see [/videos/licences](#operation/getLicences))
    String name = "name_example"; // String | Video name
    Boolean nsfw = true; // Boolean | Whether or not this video contains sensitive content
    OffsetDateTime originallyPublishedAt = OffsetDateTime.now(); // OffsetDateTime | Date when the content was originally published
    File previewfile = new File("/path/to/file"); // File | Video preview file
    VideoPrivacySet privacy = VideoPrivacySet.fromValue("1"); // VideoPrivacySet | 
    VideoScheduledUpdate scheduleUpdate = new VideoScheduledUpdate(); // VideoScheduledUpdate | 
    String support = "support_example"; // String | A text tell the audience how to support the video creator
    List<String> tags = Arrays.asList(); // List<String> | Video tags (maximum 5 tags each between 2 and 30 characters)
    File thumbnailfile = new File("/path/to/file"); // File | Video thumbnail file
    String waitTranscoding = "waitTranscoding_example"; // String | Whether or not we wait transcoding before publish the video
    try {
      apiInstance.putVideo(id, category, commentsEnabled, description, downloadEnabled, language, licence, name, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#putVideo");
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
| **category** | **Integer**| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] |
| **commentsEnabled** | **Boolean**| Enable or disable comments for this video | [optional] |
| **description** | **String**| Video description | [optional] |
| **downloadEnabled** | **Boolean**| Enable or disable downloading for this video | [optional] |
| **language** | **String**| language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] |
| **licence** | **Integer**| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] |
| **name** | **String**| Video name | [optional] |
| **nsfw** | **Boolean**| Whether or not this video contains sensitive content | [optional] |
| **originallyPublishedAt** | **OffsetDateTime**| Date when the content was originally published | [optional] |
| **previewfile** | **File**| Video preview file | [optional] |
| **privacy** | [**VideoPrivacySet**](VideoPrivacySet.md)|  | [optional] [enum: 1, 2, 3, 4] |
| **scheduleUpdate** | [**VideoScheduledUpdate**](VideoScheduledUpdate.md)|  | [optional] |
| **support** | **String**| A text tell the audience how to support the video creator | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Video tags (maximum 5 tags each between 2 and 30 characters) | [optional] |
| **thumbnailfile** | **File**| Video thumbnail file | [optional] |
| **waitTranscoding** | **String**| Whether or not we wait transcoding before publish the video | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="requestVideoToken"></a>
# **requestVideoToken**
> VideoTokenResponse requestVideoToken(id)

Request video token

Request special tokens that expire quickly to use them in some context (like accessing private static files)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoApi apiInstance = new VideoApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      VideoTokenResponse result = apiInstance.requestVideoToken(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#requestVideoToken");
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

[**VideoTokenResponse**](VideoTokenResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | incorrect parameters |  -  |
| **404** | video not found |  -  |

<a id="updateLiveId_0"></a>
# **updateLiveId_0**
> updateLiveId_0(id, liveVideoUpdate)

Update information about a live

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoApi apiInstance = new VideoApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    LiveVideoUpdate liveVideoUpdate = new LiveVideoUpdate(); // LiveVideoUpdate | 
    try {
      apiInstance.updateLiveId_0(id, liveVideoUpdate);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#updateLiveId_0");
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

<a id="uploadLegacy"></a>
# **uploadLegacy**
> VideoUploadResponse uploadLegacy(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding)

Upload a video

Uses a single request to upload a video.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoApi apiInstance = new VideoApi(defaultClient);
    Integer channelId = 56; // Integer | Channel id that will contain this video
    String name = "name_example"; // String | Video name
    File videofile = new File("/path/to/file"); // File | Video file
    Integer category = 56; // Integer | category id of the video (see [/videos/categories](#operation/getCategories))
    Boolean commentsEnabled = true; // Boolean | Enable or disable comments for this video
    String description = "description_example"; // String | Video description
    Boolean downloadEnabled = true; // Boolean | Enable or disable downloading for this video
    String language = "language_example"; // String | language id of the video (see [/videos/languages](#operation/getLanguages))
    Integer licence = 56; // Integer | licence id of the video (see [/videos/licences](#operation/getLicences))
    Boolean nsfw = true; // Boolean | Whether or not this video contains sensitive content
    OffsetDateTime originallyPublishedAt = OffsetDateTime.now(); // OffsetDateTime | Date when the content was originally published
    File previewfile = new File("/path/to/file"); // File | Video preview file
    VideoPrivacySet privacy = VideoPrivacySet.fromValue("1"); // VideoPrivacySet | 
    VideoScheduledUpdate scheduleUpdate = new VideoScheduledUpdate(); // VideoScheduledUpdate | 
    String support = "support_example"; // String | A text tell the audience how to support the video creator
    Set<String> tags = Arrays.asList(); // Set<String> | Video tags (maximum 5 tags each between 2 and 30 characters)
    File thumbnailfile = new File("/path/to/file"); // File | Video thumbnail file
    Boolean waitTranscoding = true; // Boolean | Whether or not we wait transcoding before publish the video
    try {
      VideoUploadResponse result = apiInstance.uploadLegacy(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#uploadLegacy");
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
| **channelId** | **Integer**| Channel id that will contain this video | |
| **name** | **String**| Video name | |
| **videofile** | **File**| Video file | |
| **category** | **Integer**| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] |
| **commentsEnabled** | **Boolean**| Enable or disable comments for this video | [optional] |
| **description** | **String**| Video description | [optional] |
| **downloadEnabled** | **Boolean**| Enable or disable downloading for this video | [optional] |
| **language** | **String**| language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] |
| **licence** | **Integer**| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] |
| **nsfw** | **Boolean**| Whether or not this video contains sensitive content | [optional] |
| **originallyPublishedAt** | **OffsetDateTime**| Date when the content was originally published | [optional] |
| **previewfile** | **File**| Video preview file | [optional] |
| **privacy** | [**VideoPrivacySet**](VideoPrivacySet.md)|  | [optional] [enum: 1, 2, 3, 4] |
| **scheduleUpdate** | [**VideoScheduledUpdate**](VideoScheduledUpdate.md)|  | [optional] |
| **support** | **String**| A text tell the audience how to support the video creator | [optional] |
| **tags** | [**Set&lt;String&gt;**](String.md)| Video tags (maximum 5 tags each between 2 and 30 characters) | [optional] |
| **thumbnailfile** | **File**| Video thumbnail file | [optional] |
| **waitTranscoding** | **Boolean**| Whether or not we wait transcoding before publish the video | [optional] |

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
| **403** | video didn&#39;t pass upload filter |  -  |
| **408** | upload has timed out |  -  |
| **413** | If the response has no body, it means the reverse-proxy didn&#39;t let it through. Otherwise disambiguate via &#x60;type&#x60;: - &#x60;quota_reached&#x60; for quota limits whether daily or global  |  * X-File-Maximum-Size - Maximum file size for the video <br>  |
| **415** | video type unsupported |  -  |
| **422** | video unreadable |  -  |

<a id="uploadResumable"></a>
# **uploadResumable**
> VideoUploadResponse uploadResumable(uploadId, contentRange, contentLength, body)

Send chunk for the resumable upload of a video

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to continue, pause or resume the upload of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoApi apiInstance = new VideoApi(defaultClient);
    String uploadId = "uploadId_example"; // String | Created session id to proceed with. If you didn't send chunks in the last hour, it is not valid anymore and you need to initialize a new upload. 
    String contentRange = "bytes 0-262143/2469036"; // String | Specifies the bytes in the file that the request is uploading.  For example, a value of `bytes 0-262143/1000000` shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file. 
    BigDecimal contentLength = new BigDecimal("262144"); // BigDecimal | Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube's web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health. 
    File body = new File("/path/to/file"); // File | 
    try {
      VideoUploadResponse result = apiInstance.uploadResumable(uploadId, contentRange, contentLength, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#uploadResumable");
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
| **uploadId** | **String**| Created session id to proceed with. If you didn&#39;t send chunks in the last hour, it is not valid anymore and you need to initialize a new upload.  | |
| **contentRange** | **String**| Specifies the bytes in the file that the request is uploading.  For example, a value of &#x60;bytes 0-262143/1000000&#x60; shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file.  | |
| **contentLength** | **BigDecimal**| Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube&#39;s web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health.  | |
| **body** | **File**|  | [optional] |

### Return type

[**VideoUploadResponse**](VideoUploadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | last chunk received |  * Content-Length -  <br>  |
| **308** | resume incomplete |  * Content-Length -  <br>  * Range -  <br>  |
| **403** | video didn&#39;t pass upload filter |  -  |
| **404** | upload not found |  -  |
| **409** | chunk doesn&#39;t match range |  -  |
| **422** | video unreadable |  -  |
| **429** | too many concurrent requests |  -  |
| **503** | upload is already being processed |  * Retry-After -  <br>  |

<a id="uploadResumableCancel"></a>
# **uploadResumableCancel**
> uploadResumableCancel(uploadId, contentLength)

Cancel the resumable upload of a video, deleting any data uploaded so far

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoApi apiInstance = new VideoApi(defaultClient);
    String uploadId = "uploadId_example"; // String | Created session id to proceed with. If you didn't send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-) 
    BigDecimal contentLength = new BigDecimal("0"); // BigDecimal | 
    try {
      apiInstance.uploadResumableCancel(uploadId, contentLength);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#uploadResumableCancel");
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
| **uploadId** | **String**| Created session id to proceed with. If you didn&#39;t send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-)  | |
| **contentLength** | **BigDecimal**|  | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | upload cancelled |  * Content-Length -  <br>  |
| **404** | upload not found |  -  |

<a id="uploadResumableInit"></a>
# **uploadResumableInit**
> uploadResumableInit(xUploadContentLength, xUploadContentType, videoUploadRequestResumable)

Initialize the resumable upload of a video

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to initialize the upload of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoApi apiInstance = new VideoApi(defaultClient);
    BigDecimal xUploadContentLength = new BigDecimal("2469036"); // BigDecimal | Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading.
    String xUploadContentType = "video/mp4"; // String | MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary.
    VideoUploadRequestResumable videoUploadRequestResumable = new VideoUploadRequestResumable(); // VideoUploadRequestResumable | 
    try {
      apiInstance.uploadResumableInit(xUploadContentLength, xUploadContentType, videoUploadRequestResumable);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#uploadResumableInit");
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
| **xUploadContentLength** | **BigDecimal**| Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading. | |
| **xUploadContentType** | **String**| MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary. | |
| **videoUploadRequestResumable** | [**VideoUploadRequestResumable**](VideoUploadRequestResumable.md)|  | [optional] |

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
| **200** | file already exists, send a [&#x60;resume&#x60;](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) request instead |  -  |
| **201** | created |  * Content-Length -  <br>  * Location -  <br>  |
| **413** | Disambiguate via &#x60;type&#x60;: - &#x60;max_file_size_reached&#x60; for the absolute file size limit - &#x60;quota_reached&#x60; for quota limits whether daily or global  |  -  |
| **415** | video type unsupported |  -  |

