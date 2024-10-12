# PlaylistApiApi

All URIs are relative to *https://listen-api.listennotes.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPlaylistById**](PlaylistApiApi.md#getPlaylistById) | **GET** /playlists/{id} | Fetch a playlist&#39;s info and items (i.e., episodes or podcasts). |
| [**getPlaylists**](PlaylistApiApi.md#getPlaylists) | **GET** /playlists | Fetch a list of your playlists. |


<a id="getPlaylistById"></a>
# **getPlaylistById**
> PlaylistResponse getPlaylistById(xListenAPIKey, id, type, lastTimestampMs, sort)

Fetch a playlist&#39;s info and items (i.e., episodes or podcasts).

A playlist can be an episode list (i.e., all items are episodes) or a podcast list (i.e., all items are podcasts), which is essentially the same as those created via listennotes.com/listen/. This endpoint fetches a list of items (i.e., episodes or podcasts) in the playlist. You can use the **last_pub_date_ms** parameter to do pagination and fetch more items. A playlist can be **public** (discoverable on ListenNotes.com), **unlisted** (accessible to anyone who knows the playlist id), or **private** (accessible to its owner). You can fetch all playlists created by you, and **public** / **unlisted** playlists created by others. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaylistApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    PlaylistApiApi apiInstance = new PlaylistApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String id = "m1pe7z60bsw"; // String | Playlist id (always 11 characters, e.g., m1pe7z60bsw). You can get the podcast id from the url of a playlist, e.g., m1pe7z60bsw is the playlist id of listennotes.com/listen/podcasts-about-podcasting-m1pe7z60bsw 
    String type = "episode_list"; // String | The type of this playlist, which should be either **episode_list** or **podcast_list**. 
    Integer lastTimestampMs = 0; // Integer | For playlist items pagination. It's the value of **last_timestamp_ms** from the response of last request. If it's 0 or not specified, just return the latest or the oldest 20 items, depending on the value of the **sort** parameter. 
    String sort = "recent_added_first"; // String | How do you want to sort playlist items? 
    try {
      PlaylistResponse result = apiInstance.getPlaylistById(xListenAPIKey, id, type, lastTimestampMs, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaylistApiApi#getPlaylistById");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **id** | **String**| Playlist id (always 11 characters, e.g., m1pe7z60bsw). You can get the podcast id from the url of a playlist, e.g., m1pe7z60bsw is the playlist id of listennotes.com/listen/podcasts-about-podcasting-m1pe7z60bsw  | |
| **type** | **String**| The type of this playlist, which should be either **episode_list** or **podcast_list**.  | [optional] [default to episode_list] [enum: episode_list, podcast_list] |
| **lastTimestampMs** | **Integer**| For playlist items pagination. It&#39;s the value of **last_timestamp_ms** from the response of last request. If it&#39;s 0 or not specified, just return the latest or the oldest 20 items, depending on the value of the **sort** parameter.  | [optional] [default to 0] |
| **sort** | **String**| How do you want to sort playlist items?  | [optional] [default to recent_added_first] [enum: recent_added_first, oldest_added_first, recent_published_first, oldest_published_first] |

### Return type

[**PlaylistResponse**](PlaylistResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **404** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getPlaylists"></a>
# **getPlaylists**
> PlaylistsResponse getPlaylists(xListenAPIKey, sort, page)

Fetch a list of your playlists.

This endpoint returns same data as listennotes.com/listen under your account. You can use the **page** parameter to do pagination and fetch more playlists. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaylistApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    PlaylistApiApi apiInstance = new PlaylistApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String sort = "recent_added_first"; // String | How do you want to sort playlists? 
    Integer page = 1; // Integer | Page number of playlists. 
    try {
      PlaylistsResponse result = apiInstance.getPlaylists(xListenAPIKey, sort, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaylistApiApi#getPlaylists");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **sort** | **String**| How do you want to sort playlists?  | [optional] [default to recent_added_first] [enum: recent_added_first, oldest_added_first, name_a_to_z, name_z_to_a] |
| **page** | **Integer**| Page number of playlists.  | [optional] [default to 1] |

### Return type

[**PlaylistsResponse**](PlaylistsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

