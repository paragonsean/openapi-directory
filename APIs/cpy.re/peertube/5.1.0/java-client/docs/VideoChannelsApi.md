# VideoChannelsApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoChannel**](VideoChannelsApi.md#addVideoChannel) | **POST** /api/v1/video-channels | Create a video channel |
| [**apiV1AccountsNameVideoChannelSyncsGet**](VideoChannelsApi.md#apiV1AccountsNameVideoChannelSyncsGet) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account |
| [**apiV1AccountsNameVideoChannelsGet**](VideoChannelsApi.md#apiV1AccountsNameVideoChannelsGet) | **GET** /api/v1/accounts/{name}/video-channels | List video channels of an account |
| [**apiV1VideoChannelsChannelHandleAvatarDelete**](VideoChannelsApi.md#apiV1VideoChannelsChannelHandleAvatarDelete) | **DELETE** /api/v1/video-channels/{channelHandle}/avatar | Delete channel avatar |
| [**apiV1VideoChannelsChannelHandleAvatarPickPost**](VideoChannelsApi.md#apiV1VideoChannelsChannelHandleAvatarPickPost) | **POST** /api/v1/video-channels/{channelHandle}/avatar/pick | Update channel avatar |
| [**apiV1VideoChannelsChannelHandleBannerDelete**](VideoChannelsApi.md#apiV1VideoChannelsChannelHandleBannerDelete) | **DELETE** /api/v1/video-channels/{channelHandle}/banner | Delete channel banner |
| [**apiV1VideoChannelsChannelHandleBannerPickPost**](VideoChannelsApi.md#apiV1VideoChannelsChannelHandleBannerPickPost) | **POST** /api/v1/video-channels/{channelHandle}/banner/pick | Update channel banner |
| [**apiV1VideoChannelsChannelHandleImportVideosPost**](VideoChannelsApi.md#apiV1VideoChannelsChannelHandleImportVideosPost) | **POST** /api/v1/video-channels/{channelHandle}/import-videos | Import videos in channel |
| [**apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0**](VideoChannelsApi.md#apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0) | **GET** /api/v1/video-channels/{channelHandle}/video-playlists | List playlists of a channel |
| [**delVideoChannel**](VideoChannelsApi.md#delVideoChannel) | **DELETE** /api/v1/video-channels/{channelHandle} | Delete a video channel |
| [**getVideoChannel**](VideoChannelsApi.md#getVideoChannel) | **GET** /api/v1/video-channels/{channelHandle} | Get a video channel |
| [**getVideoChannelFollowers**](VideoChannelsApi.md#getVideoChannelFollowers) | **GET** /api/v1/video-channels/{channelHandle}/followers | List followers of a video channel |
| [**getVideoChannelVideos_0**](VideoChannelsApi.md#getVideoChannelVideos_0) | **GET** /api/v1/video-channels/{channelHandle}/videos | List videos of a video channel |
| [**getVideoChannels**](VideoChannelsApi.md#getVideoChannels) | **GET** /api/v1/video-channels | List video channels |
| [**putVideoChannel**](VideoChannelsApi.md#putVideoChannel) | **PUT** /api/v1/video-channels/{channelHandle} | Update a video channel |


<a id="addVideoChannel"></a>
# **addVideoChannel**
> AddVideoChannel200Response addVideoChannel(videoChannelCreate)

Create a video channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    VideoChannelCreate videoChannelCreate = new VideoChannelCreate(); // VideoChannelCreate | 
    try {
      AddVideoChannel200Response result = apiInstance.addVideoChannel(videoChannelCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#addVideoChannel");
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
| **videoChannelCreate** | [**VideoChannelCreate**](VideoChannelCreate.md)|  | [optional] |

### Return type

[**AddVideoChannel200Response**](AddVideoChannel200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1AccountsNameVideoChannelSyncsGet"></a>
# **apiV1AccountsNameVideoChannelSyncsGet**
> VideoChannelSyncList apiV1AccountsNameVideoChannelSyncsGet(name, start, count, sort)

List the synchronizations of video channels of an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    String name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      VideoChannelSyncList result = apiInstance.apiV1AccountsNameVideoChannelSyncsGet(name, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#apiV1AccountsNameVideoChannelSyncsGet");
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

### Return type

[**VideoChannelSyncList**](VideoChannelSyncList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1AccountsNameVideoChannelsGet"></a>
# **apiV1AccountsNameVideoChannelsGet**
> VideoChannelList apiV1AccountsNameVideoChannelsGet(name, withStats, start, count, sort)

List video channels of an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    String name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
    Boolean withStats = true; // Boolean | include daily view statistics for the last 30 days and total views (only if authentified as the account user)
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      VideoChannelList result = apiInstance.apiV1AccountsNameVideoChannelsGet(name, withStats, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#apiV1AccountsNameVideoChannelsGet");
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
| **withStats** | **Boolean**| include daily view statistics for the last 30 days and total views (only if authentified as the account user) | [optional] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |

### Return type

[**VideoChannelList**](VideoChannelList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1VideoChannelsChannelHandleAvatarDelete"></a>
# **apiV1VideoChannelsChannelHandleAvatarDelete**
> apiV1VideoChannelsChannelHandleAvatarDelete(channelHandle)

Delete channel avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    try {
      apiInstance.apiV1VideoChannelsChannelHandleAvatarDelete(channelHandle);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#apiV1VideoChannelsChannelHandleAvatarDelete");
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

<a id="apiV1VideoChannelsChannelHandleAvatarPickPost"></a>
# **apiV1VideoChannelsChannelHandleAvatarPickPost**
> ApiV1UsersMeAvatarPickPost200Response apiV1VideoChannelsChannelHandleAvatarPickPost(channelHandle, avatarfile)

Update channel avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    File avatarfile = new File("/path/to/file"); // File | The file to upload.
    try {
      ApiV1UsersMeAvatarPickPost200Response result = apiInstance.apiV1VideoChannelsChannelHandleAvatarPickPost(channelHandle, avatarfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#apiV1VideoChannelsChannelHandleAvatarPickPost");
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
| **avatarfile** | **File**| The file to upload. | [optional] |

### Return type

[**ApiV1UsersMeAvatarPickPost200Response**](ApiV1UsersMeAvatarPickPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **413** | image file too large |  * X-File-Maximum-Size - Maximum file size for the video <br>  |

<a id="apiV1VideoChannelsChannelHandleBannerDelete"></a>
# **apiV1VideoChannelsChannelHandleBannerDelete**
> apiV1VideoChannelsChannelHandleBannerDelete(channelHandle)

Delete channel banner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    try {
      apiInstance.apiV1VideoChannelsChannelHandleBannerDelete(channelHandle);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#apiV1VideoChannelsChannelHandleBannerDelete");
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

<a id="apiV1VideoChannelsChannelHandleBannerPickPost"></a>
# **apiV1VideoChannelsChannelHandleBannerPickPost**
> ApiV1VideoChannelsChannelHandleBannerPickPost200Response apiV1VideoChannelsChannelHandleBannerPickPost(channelHandle, bannerfile)

Update channel banner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    File bannerfile = new File("/path/to/file"); // File | The file to upload.
    try {
      ApiV1VideoChannelsChannelHandleBannerPickPost200Response result = apiInstance.apiV1VideoChannelsChannelHandleBannerPickPost(channelHandle, bannerfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#apiV1VideoChannelsChannelHandleBannerPickPost");
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
| **bannerfile** | **File**| The file to upload. | [optional] |

### Return type

[**ApiV1VideoChannelsChannelHandleBannerPickPost200Response**](ApiV1VideoChannelsChannelHandleBannerPickPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **413** | image file too large |  * X-File-Maximum-Size - Maximum file size for the video <br>  |

<a id="apiV1VideoChannelsChannelHandleImportVideosPost"></a>
# **apiV1VideoChannelsChannelHandleImportVideosPost**
> apiV1VideoChannelsChannelHandleImportVideosPost(channelHandle, importVideosInChannelCreate)

Import videos in channel

Import a remote channel/playlist videos into a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    ImportVideosInChannelCreate importVideosInChannelCreate = new ImportVideosInChannelCreate(); // ImportVideosInChannelCreate | 
    try {
      apiInstance.apiV1VideoChannelsChannelHandleImportVideosPost(channelHandle, importVideosInChannelCreate);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#apiV1VideoChannelsChannelHandleImportVideosPost");
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
| **importVideosInChannelCreate** | [**ImportVideosInChannelCreate**](ImportVideosInChannelCreate.md)|  | [optional] |

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

<a id="apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0"></a>
# **apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0**
> ApiV1AccountsNameVideoPlaylistsGet200Response apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0(channelHandle, start, count, sort, playlistType)

List playlists of a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    VideoPlaylistTypeSet playlistType = VideoPlaylistTypeSet.fromValue("1"); // VideoPlaylistTypeSet | 
    try {
      ApiV1AccountsNameVideoPlaylistsGet200Response result = apiInstance.apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0(channelHandle, start, count, sort, playlistType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0");
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

<a id="delVideoChannel"></a>
# **delVideoChannel**
> delVideoChannel(channelHandle)

Delete a video channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    try {
      apiInstance.delVideoChannel(channelHandle);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#delVideoChannel");
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

<a id="getVideoChannel"></a>
# **getVideoChannel**
> VideoChannel getVideoChannel(channelHandle)

Get a video channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    try {
      VideoChannel result = apiInstance.getVideoChannel(channelHandle);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#getVideoChannel");
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

### Return type

[**VideoChannel**](VideoChannel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getVideoChannelFollowers"></a>
# **getVideoChannelFollowers**
> GetAccountFollowers200Response getVideoChannelFollowers(channelHandle, start, count, sort, search)

List followers of a video channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "createdAt"; // String | Sort followers by criteria
    String search = "search_example"; // String | Plain text search, applied to various parts of the model depending on endpoint
    try {
      GetAccountFollowers200Response result = apiInstance.getVideoChannelFollowers(channelHandle, start, count, sort, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#getVideoChannelFollowers");
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
| **sort** | **String**| Sort followers by criteria | [optional] [enum: createdAt] |
| **search** | **String**| Plain text search, applied to various parts of the model depending on endpoint | [optional] |

### Return type

[**GetAccountFollowers200Response**](GetAccountFollowers200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getVideoChannelVideos_0"></a>
# **getVideoChannelVideos_0**
> VideoListResponse getVideoChannelVideos_0(channelHandle, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched)

List videos of a video channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
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
      VideoListResponse result = apiInstance.getVideoChannelVideos_0(channelHandle, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#getVideoChannelVideos_0");
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

<a id="getVideoChannels"></a>
# **getVideoChannels**
> VideoChannelList getVideoChannels(start, count, sort)

List video channels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      VideoChannelList result = apiInstance.getVideoChannels(start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#getVideoChannels");
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

[**VideoChannelList**](VideoChannelList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="putVideoChannel"></a>
# **putVideoChannel**
> putVideoChannel(channelHandle, videoChannelUpdate)

Update a video channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoChannelsApi apiInstance = new VideoChannelsApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    VideoChannelUpdate videoChannelUpdate = new VideoChannelUpdate(); // VideoChannelUpdate | 
    try {
      apiInstance.putVideoChannel(channelHandle, videoChannelUpdate);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoChannelsApi#putVideoChannel");
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
| **videoChannelUpdate** | [**VideoChannelUpdate**](VideoChannelUpdate.md)|  | [optional] |

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

