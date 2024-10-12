# VideoPlaylistsApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addPlaylist**](VideoPlaylistsApi.md#addPlaylist) | **POST** /api/v1/video-playlists | Create a video playlist |
| [**addVideoPlaylistVideo_0**](VideoPlaylistsApi.md#addVideoPlaylistVideo_0) | **POST** /api/v1/video-playlists/{playlistId}/videos | Add a video in a playlist |
| [**apiV1AccountsNameVideoPlaylistsGet**](VideoPlaylistsApi.md#apiV1AccountsNameVideoPlaylistsGet) | **GET** /api/v1/accounts/{name}/video-playlists | List playlists of an account |
| [**apiV1UsersMeVideoPlaylistsVideosExistGet**](VideoPlaylistsApi.md#apiV1UsersMeVideoPlaylistsVideosExistGet) | **GET** /api/v1/users/me/video-playlists/videos-exist | Check video exists in my playlists |
| [**apiV1VideoChannelsChannelHandleVideoPlaylistsGet**](VideoPlaylistsApi.md#apiV1VideoChannelsChannelHandleVideoPlaylistsGet) | **GET** /api/v1/video-channels/{channelHandle}/video-playlists | List playlists of a channel |
| [**apiV1VideoPlaylistsPlaylistIdDelete**](VideoPlaylistsApi.md#apiV1VideoPlaylistsPlaylistIdDelete) | **DELETE** /api/v1/video-playlists/{playlistId} | Delete a video playlist |
| [**apiV1VideoPlaylistsPlaylistIdGet**](VideoPlaylistsApi.md#apiV1VideoPlaylistsPlaylistIdGet) | **GET** /api/v1/video-playlists/{playlistId} | Get a video playlist |
| [**apiV1VideoPlaylistsPlaylistIdPut**](VideoPlaylistsApi.md#apiV1VideoPlaylistsPlaylistIdPut) | **PUT** /api/v1/video-playlists/{playlistId} | Update a video playlist |
| [**delVideoPlaylistVideo**](VideoPlaylistsApi.md#delVideoPlaylistVideo) | **DELETE** /api/v1/video-playlists/{playlistId}/videos/{playlistElementId} | Delete an element from a playlist |
| [**getPlaylistPrivacyPolicies**](VideoPlaylistsApi.md#getPlaylistPrivacyPolicies) | **GET** /api/v1/video-playlists/privacies | List available playlist privacy policies |
| [**getPlaylists**](VideoPlaylistsApi.md#getPlaylists) | **GET** /api/v1/video-playlists | List video playlists |
| [**getVideoPlaylistVideos_0**](VideoPlaylistsApi.md#getVideoPlaylistVideos_0) | **GET** /api/v1/video-playlists/{playlistId}/videos | List videos of a playlist |
| [**putVideoPlaylistVideo**](VideoPlaylistsApi.md#putVideoPlaylistVideo) | **PUT** /api/v1/video-playlists/{playlistId}/videos/{playlistElementId} | Update a playlist element |
| [**reorderVideoPlaylist**](VideoPlaylistsApi.md#reorderVideoPlaylist) | **POST** /api/v1/video-playlists/{playlistId}/videos/reorder | Reorder a playlist |


<a id="addPlaylist"></a>
# **addPlaylist**
> AddPlaylist200Response addPlaylist(displayName, description, privacy, thumbnailfile, videoChannelId)

Create a video playlist

If the video playlist is set as public, &#x60;videoChannelId&#x60; is mandatory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    String displayName = "displayName_example"; // String | Video playlist display name
    String description = "description_example"; // String | Video playlist description
    VideoPlaylistPrivacySet privacy = VideoPlaylistPrivacySet.fromValue("1"); // VideoPlaylistPrivacySet | 
    File thumbnailfile = new File("/path/to/file"); // File | Video playlist thumbnail file
    Integer videoChannelId = 56; // Integer | Video channel in which the playlist will be published
    try {
      AddPlaylist200Response result = apiInstance.addPlaylist(displayName, description, privacy, thumbnailfile, videoChannelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#addPlaylist");
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
| **displayName** | **String**| Video playlist display name | |
| **description** | **String**| Video playlist description | [optional] |
| **privacy** | [**VideoPlaylistPrivacySet**](VideoPlaylistPrivacySet.md)|  | [optional] [enum: 1, 2, 3] |
| **thumbnailfile** | **File**| Video playlist thumbnail file | [optional] |
| **videoChannelId** | [**Integer**](Integer.md)| Video channel in which the playlist will be published | [optional] |

### Return type

[**AddPlaylist200Response**](AddPlaylist200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="addVideoPlaylistVideo_0"></a>
# **addVideoPlaylistVideo_0**
> AddVideoPlaylistVideo200Response addVideoPlaylistVideo_0(playlistId, addVideoPlaylistVideoRequest)

Add a video in a playlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    Integer playlistId = 56; // Integer | Playlist id
    AddVideoPlaylistVideoRequest addVideoPlaylistVideoRequest = new AddVideoPlaylistVideoRequest(); // AddVideoPlaylistVideoRequest | 
    try {
      AddVideoPlaylistVideo200Response result = apiInstance.addVideoPlaylistVideo_0(playlistId, addVideoPlaylistVideoRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#addVideoPlaylistVideo_0");
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

<a id="apiV1AccountsNameVideoPlaylistsGet"></a>
# **apiV1AccountsNameVideoPlaylistsGet**
> ApiV1AccountsNameVideoPlaylistsGet200Response apiV1AccountsNameVideoPlaylistsGet(name, start, count, sort, search, playlistType)

List playlists of an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    String name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    String search = "search_example"; // String | Plain text search, applied to various parts of the model depending on endpoint
    VideoPlaylistTypeSet playlistType = VideoPlaylistTypeSet.fromValue("1"); // VideoPlaylistTypeSet | 
    try {
      ApiV1AccountsNameVideoPlaylistsGet200Response result = apiInstance.apiV1AccountsNameVideoPlaylistsGet(name, start, count, sort, search, playlistType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#apiV1AccountsNameVideoPlaylistsGet");
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
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |
| **search** | **String**| Plain text search, applied to various parts of the model depending on endpoint | [optional] |
| **playlistType** | [**VideoPlaylistTypeSet**](.md)|  | [optional] [enum: 1, 2] |

### Return type

[**ApiV1AccountsNameVideoPlaylistsGet200Response**](ApiV1AccountsNameVideoPlaylistsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1UsersMeVideoPlaylistsVideosExistGet"></a>
# **apiV1UsersMeVideoPlaylistsVideosExistGet**
> ApiV1UsersMeVideoPlaylistsVideosExistGet200Response apiV1UsersMeVideoPlaylistsVideosExistGet(videoIds)

Check video exists in my playlists

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    List<Integer> videoIds = Arrays.asList(); // List<Integer> | The video ids to check
    try {
      ApiV1UsersMeVideoPlaylistsVideosExistGet200Response result = apiInstance.apiV1UsersMeVideoPlaylistsVideosExistGet(videoIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#apiV1UsersMeVideoPlaylistsVideosExistGet");
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
| **videoIds** | [**List&lt;Integer&gt;**](Integer.md)| The video ids to check | |

### Return type

[**ApiV1UsersMeVideoPlaylistsVideosExistGet200Response**](ApiV1UsersMeVideoPlaylistsVideosExistGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1VideoChannelsChannelHandleVideoPlaylistsGet"></a>
# **apiV1VideoChannelsChannelHandleVideoPlaylistsGet**
> ApiV1AccountsNameVideoPlaylistsGet200Response apiV1VideoChannelsChannelHandleVideoPlaylistsGet(channelHandle, start, count, sort, playlistType)

List playlists of a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    VideoPlaylistTypeSet playlistType = VideoPlaylistTypeSet.fromValue("1"); // VideoPlaylistTypeSet | 
    try {
      ApiV1AccountsNameVideoPlaylistsGet200Response result = apiInstance.apiV1VideoChannelsChannelHandleVideoPlaylistsGet(channelHandle, start, count, sort, playlistType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#apiV1VideoChannelsChannelHandleVideoPlaylistsGet");
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
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |
| **playlistType** | [**VideoPlaylistTypeSet**](.md)|  | [optional] [enum: 1, 2] |

### Return type

[**ApiV1AccountsNameVideoPlaylistsGet200Response**](ApiV1AccountsNameVideoPlaylistsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1VideoPlaylistsPlaylistIdDelete"></a>
# **apiV1VideoPlaylistsPlaylistIdDelete**
> apiV1VideoPlaylistsPlaylistIdDelete(playlistId)

Delete a video playlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    Integer playlistId = 56; // Integer | Playlist id
    try {
      apiInstance.apiV1VideoPlaylistsPlaylistIdDelete(playlistId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#apiV1VideoPlaylistsPlaylistIdDelete");
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

<a id="apiV1VideoPlaylistsPlaylistIdGet"></a>
# **apiV1VideoPlaylistsPlaylistIdGet**
> VideoPlaylist apiV1VideoPlaylistsPlaylistIdGet(playlistId)

Get a video playlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    Integer playlistId = 56; // Integer | Playlist id
    try {
      VideoPlaylist result = apiInstance.apiV1VideoPlaylistsPlaylistIdGet(playlistId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#apiV1VideoPlaylistsPlaylistIdGet");
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

### Return type

[**VideoPlaylist**](VideoPlaylist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1VideoPlaylistsPlaylistIdPut"></a>
# **apiV1VideoPlaylistsPlaylistIdPut**
> apiV1VideoPlaylistsPlaylistIdPut(playlistId, description, displayName, privacy, thumbnailfile, videoChannelId)

Update a video playlist

If the video playlist is set as public, the playlist must have a assigned channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    Integer playlistId = 56; // Integer | Playlist id
    String description = "description_example"; // String | Video playlist description
    String displayName = "displayName_example"; // String | Video playlist display name
    VideoPlaylistPrivacySet privacy = VideoPlaylistPrivacySet.fromValue("1"); // VideoPlaylistPrivacySet | 
    File thumbnailfile = new File("/path/to/file"); // File | Video playlist thumbnail file
    Integer videoChannelId = 56; // Integer | Video channel in which the playlist will be published
    try {
      apiInstance.apiV1VideoPlaylistsPlaylistIdPut(playlistId, description, displayName, privacy, thumbnailfile, videoChannelId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#apiV1VideoPlaylistsPlaylistIdPut");
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
| **description** | **String**| Video playlist description | [optional] |
| **displayName** | **String**| Video playlist display name | [optional] |
| **privacy** | [**VideoPlaylistPrivacySet**](VideoPlaylistPrivacySet.md)|  | [optional] [enum: 1, 2, 3] |
| **thumbnailfile** | **File**| Video playlist thumbnail file | [optional] |
| **videoChannelId** | [**Integer**](Integer.md)| Video channel in which the playlist will be published | [optional] |

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

<a id="delVideoPlaylistVideo"></a>
# **delVideoPlaylistVideo**
> delVideoPlaylistVideo(playlistId, playlistElementId)

Delete an element from a playlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    Integer playlistId = 56; // Integer | Playlist id
    Integer playlistElementId = 56; // Integer | Playlist element id
    try {
      apiInstance.delVideoPlaylistVideo(playlistId, playlistElementId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#delVideoPlaylistVideo");
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
| **playlistElementId** | **Integer**| Playlist element id | |

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

<a id="getPlaylistPrivacyPolicies"></a>
# **getPlaylistPrivacyPolicies**
> List&lt;String&gt; getPlaylistPrivacyPolicies()

List available playlist privacy policies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    try {
      List<String> result = apiInstance.getPlaylistPrivacyPolicies();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#getPlaylistPrivacyPolicies");
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

<a id="getPlaylists"></a>
# **getPlaylists**
> ApiV1AccountsNameVideoPlaylistsGet200Response getPlaylists(start, count, sort, playlistType)

List video playlists

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    VideoPlaylistTypeSet playlistType = VideoPlaylistTypeSet.fromValue("1"); // VideoPlaylistTypeSet | 
    try {
      ApiV1AccountsNameVideoPlaylistsGet200Response result = apiInstance.getPlaylists(start, count, sort, playlistType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#getPlaylists");
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
| **playlistType** | [**VideoPlaylistTypeSet**](.md)|  | [optional] [enum: 1, 2] |

### Return type

[**ApiV1AccountsNameVideoPlaylistsGet200Response**](ApiV1AccountsNameVideoPlaylistsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getVideoPlaylistVideos_0"></a>
# **getVideoPlaylistVideos_0**
> VideoListResponse getVideoPlaylistVideos_0(playlistId, start, count)

List videos of a playlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    Integer playlistId = 56; // Integer | Playlist id
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    try {
      VideoListResponse result = apiInstance.getVideoPlaylistVideos_0(playlistId, start, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#getVideoPlaylistVideos_0");
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

<a id="putVideoPlaylistVideo"></a>
# **putVideoPlaylistVideo**
> putVideoPlaylistVideo(playlistId, playlistElementId, putVideoPlaylistVideoRequest)

Update a playlist element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    Integer playlistId = 56; // Integer | Playlist id
    Integer playlistElementId = 56; // Integer | Playlist element id
    PutVideoPlaylistVideoRequest putVideoPlaylistVideoRequest = new PutVideoPlaylistVideoRequest(); // PutVideoPlaylistVideoRequest | 
    try {
      apiInstance.putVideoPlaylistVideo(playlistId, playlistElementId, putVideoPlaylistVideoRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#putVideoPlaylistVideo");
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
| **playlistElementId** | **Integer**| Playlist element id | |
| **putVideoPlaylistVideoRequest** | [**PutVideoPlaylistVideoRequest**](PutVideoPlaylistVideoRequest.md)|  | [optional] |

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

<a id="reorderVideoPlaylist"></a>
# **reorderVideoPlaylist**
> reorderVideoPlaylist(playlistId, reorderVideoPlaylistRequest)

Reorder a playlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoPlaylistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoPlaylistsApi apiInstance = new VideoPlaylistsApi(defaultClient);
    Integer playlistId = 56; // Integer | Playlist id
    ReorderVideoPlaylistRequest reorderVideoPlaylistRequest = new ReorderVideoPlaylistRequest(); // ReorderVideoPlaylistRequest | 
    try {
      apiInstance.reorderVideoPlaylist(playlistId, reorderVideoPlaylistRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoPlaylistsApi#reorderVideoPlaylist");
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
| **reorderVideoPlaylistRequest** | [**ReorderVideoPlaylistRequest**](ReorderVideoPlaylistRequest.md)|  | [optional] |

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

