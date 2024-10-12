# ChannelsSyncApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoChannelSync**](ChannelsSyncApi.md#addVideoChannelSync) | **POST** /api/v1/video-channel-syncs | Create a synchronization for a video channel |
| [**apiV1AccountsNameVideoChannelSyncsGet_0**](ChannelsSyncApi.md#apiV1AccountsNameVideoChannelSyncsGet_0) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account |
| [**apiV1VideoChannelsChannelHandleImportVideosPost_0**](ChannelsSyncApi.md#apiV1VideoChannelsChannelHandleImportVideosPost_0) | **POST** /api/v1/video-channels/{channelHandle}/import-videos | Import videos in channel |
| [**delVideoChannelSync**](ChannelsSyncApi.md#delVideoChannelSync) | **DELETE** /api/v1/video-channel-syncs/{channelSyncId} | Delete a video channel synchronization |
| [**triggerVideoChannelSync**](ChannelsSyncApi.md#triggerVideoChannelSync) | **POST** /api/v1/video-channel-syncs/{channelSyncId}/sync | Triggers the channel synchronization job, fetching all the videos from the remote channel |


<a id="addVideoChannelSync"></a>
# **addVideoChannelSync**
> AddVideoChannelSync200Response addVideoChannelSync(videoChannelSyncCreate)

Create a synchronization for a video channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsSyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ChannelsSyncApi apiInstance = new ChannelsSyncApi(defaultClient);
    VideoChannelSyncCreate videoChannelSyncCreate = new VideoChannelSyncCreate(); // VideoChannelSyncCreate | 
    try {
      AddVideoChannelSync200Response result = apiInstance.addVideoChannelSync(videoChannelSyncCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsSyncApi#addVideoChannelSync");
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
| **videoChannelSyncCreate** | [**VideoChannelSyncCreate**](VideoChannelSyncCreate.md)|  | [optional] |

### Return type

[**AddVideoChannelSync200Response**](AddVideoChannelSync200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1AccountsNameVideoChannelSyncsGet_0"></a>
# **apiV1AccountsNameVideoChannelSyncsGet_0**
> VideoChannelSyncList apiV1AccountsNameVideoChannelSyncsGet_0(name, start, count, sort)

List the synchronizations of video channels of an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsSyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    ChannelsSyncApi apiInstance = new ChannelsSyncApi(defaultClient);
    String name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      VideoChannelSyncList result = apiInstance.apiV1AccountsNameVideoChannelSyncsGet_0(name, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsSyncApi#apiV1AccountsNameVideoChannelSyncsGet_0");
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

<a id="apiV1VideoChannelsChannelHandleImportVideosPost_0"></a>
# **apiV1VideoChannelsChannelHandleImportVideosPost_0**
> apiV1VideoChannelsChannelHandleImportVideosPost_0(channelHandle, importVideosInChannelCreate)

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
import org.openapitools.client.api.ChannelsSyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ChannelsSyncApi apiInstance = new ChannelsSyncApi(defaultClient);
    String channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
    ImportVideosInChannelCreate importVideosInChannelCreate = new ImportVideosInChannelCreate(); // ImportVideosInChannelCreate | 
    try {
      apiInstance.apiV1VideoChannelsChannelHandleImportVideosPost_0(channelHandle, importVideosInChannelCreate);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsSyncApi#apiV1VideoChannelsChannelHandleImportVideosPost_0");
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

<a id="delVideoChannelSync"></a>
# **delVideoChannelSync**
> delVideoChannelSync(channelSyncId)

Delete a video channel synchronization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsSyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ChannelsSyncApi apiInstance = new ChannelsSyncApi(defaultClient);
    Integer channelSyncId = 56; // Integer | Channel Sync id
    try {
      apiInstance.delVideoChannelSync(channelSyncId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsSyncApi#delVideoChannelSync");
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
| **channelSyncId** | **Integer**| Channel Sync id | |

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

<a id="triggerVideoChannelSync"></a>
# **triggerVideoChannelSync**
> triggerVideoChannelSync(channelSyncId)

Triggers the channel synchronization job, fetching all the videos from the remote channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsSyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ChannelsSyncApi apiInstance = new ChannelsSyncApi(defaultClient);
    Integer channelSyncId = 56; // Integer | Channel Sync id
    try {
      apiInstance.triggerVideoChannelSync(channelSyncId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsSyncApi#triggerVideoChannelSync");
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
| **channelSyncId** | **Integer**| Channel Sync id | |

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

