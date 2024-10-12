# VideosApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoPlaylistVideo**](VideosApi.md#addVideoPlaylistVideo) | **POST** /api/v1/video-playlists/{playlistId}/videos | Add a video in a playlist |
| [**apiV1UsersMeSubscriptionsVideosGet_0**](VideosApi.md#apiV1UsersMeSubscriptionsVideosGet_0) | **GET** /api/v1/users/me/subscriptions/videos | List videos of subscriptions of my user |
| [**apiV1UsersMeVideosGet_0**](VideosApi.md#apiV1UsersMeVideosGet_0) | **GET** /api/v1/users/me/videos | Get videos of my user |
| [**apiV1UsersMeVideosImportsGet**](VideosApi.md#apiV1UsersMeVideosImportsGet) | **GET** /api/v1/users/me/videos/imports | Get video imports of my user |
| [**getVideoPlaylistVideos**](VideosApi.md#getVideoPlaylistVideos) | **GET** /api/v1/video-playlists/{playlistId}/videos | List videos of a playlist |


<a id="addVideoPlaylistVideo"></a>
# **addVideoPlaylistVideo**
> AddVideoPlaylistVideo200Response addVideoPlaylistVideo(playlistId, addVideoPlaylistVideoRequest)

Add a video in a playlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    Integer playlistId = 56; // Integer | Playlist id
    AddVideoPlaylistVideoRequest addVideoPlaylistVideoRequest = new AddVideoPlaylistVideoRequest(); // AddVideoPlaylistVideoRequest | 
    try {
      AddVideoPlaylistVideo200Response result = apiInstance.addVideoPlaylistVideo(playlistId, addVideoPlaylistVideoRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#addVideoPlaylistVideo");
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
| **playlistId** | **Integer**| Playlist id | |
| **addVideoPlaylistVideoRequest** | [**AddVideoPlaylistVideoRequest**](AddVideoPlaylistVideoRequest.md)|  | [optional] |

### Return type

[**AddVideoPlaylistVideo200Response**](AddVideoPlaylistVideo200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1UsersMeSubscriptionsVideosGet_0"></a>
# **apiV1UsersMeSubscriptionsVideosGet_0**
> VideoListResponse apiV1UsersMeSubscriptionsVideosGet_0(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched)

List videos of subscriptions of my user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
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
      VideoListResponse result = apiInstance.apiV1UsersMeSubscriptionsVideosGet_0(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#apiV1UsersMeSubscriptionsVideosGet_0");
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1UsersMeVideosGet_0"></a>
# **apiV1UsersMeVideosGet_0**
> VideoListResponse apiV1UsersMeVideosGet_0(start, count, sort)

Get videos of my user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      VideoListResponse result = apiInstance.apiV1UsersMeVideosGet_0(start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#apiV1UsersMeVideosGet_0");
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
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1UsersMeVideosImportsGet"></a>
# **apiV1UsersMeVideosImportsGet**
> VideoImportsList apiV1UsersMeVideosImportsGet(start, count, sort, targetUrl, videoChannelSyncId, search)

Get video imports of my user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    String targetUrl = "targetUrl_example"; // String | Filter on import target URL
    BigDecimal videoChannelSyncId = new BigDecimal(78); // BigDecimal | Filter on imports created by a specific channel synchronization
    String search = "search_example"; // String | Search in video names
    try {
      VideoImportsList result = apiInstance.apiV1UsersMeVideosImportsGet(start, count, sort, targetUrl, videoChannelSyncId, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#apiV1UsersMeVideosImportsGet");
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
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |
| **targetUrl** | **String**| Filter on import target URL | [optional] |
| **videoChannelSyncId** | **BigDecimal**| Filter on imports created by a specific channel synchronization | [optional] |
| **search** | **String**| Search in video names | [optional] |

### Return type

[**VideoImportsList**](VideoImportsList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getVideoPlaylistVideos"></a>
# **getVideoPlaylistVideos**
> VideoListResponse getVideoPlaylistVideos(playlistId, start, count)

List videos of a playlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideosApi apiInstance = new VideosApi(defaultClient);
    Integer playlistId = 56; // Integer | Playlist id
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    try {
      VideoListResponse result = apiInstance.getVideoPlaylistVideos(playlistId, start, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#getVideoPlaylistVideos");
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
| **playlistId** | **Integer**| Playlist id | |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |

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

