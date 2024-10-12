# ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistAPIApi

All URIs are relative to *https://listen-api.listennotes.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPlaylistById**](PlaylistAPIApi.md#getPlaylistById) | **GET** /playlists/{id} | Fetch a playlist&#39;s info and items (i.e., episodes or podcasts).
[**getPlaylists**](PlaylistAPIApi.md#getPlaylists) | **GET** /playlists | Fetch a list of your playlists.



## getPlaylistById

> PlaylistResponse getPlaylistById(xListenAPIKey, id, opts)

Fetch a playlist&#39;s info and items (i.e., episodes or podcasts).

A playlist can be an episode list (i.e., all items are episodes) or a podcast list (i.e., all items are podcasts), which is essentially the same as those created via listennotes.com/listen/. This endpoint fetches a list of items (i.e., episodes or podcasts) in the playlist. You can use the **last_pub_date_ms** parameter to do pagination and fetch more items. A playlist can be **public** (discoverable on ListenNotes.com), **unlisted** (accessible to anyone who knows the playlist id), or **private** (accessible to its owner). You can fetch all playlists created by you, and **public** / **unlisted** playlists created by others. 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let id = "m1pe7z60bsw"; // String | Playlist id (always 11 characters, e.g., m1pe7z60bsw). You can get the podcast id from the url of a playlist, e.g., m1pe7z60bsw is the playlist id of listennotes.com/listen/podcasts-about-podcasting-m1pe7z60bsw 
let opts = {
  'type': "'episode_list'", // String | The type of this playlist, which should be either **episode_list** or **podcast_list**. 
  'lastTimestampMs': 0, // Number | For playlist items pagination. It's the value of **last_timestamp_ms** from the response of last request. If it's 0 or not specified, just return the latest or the oldest 20 items, depending on the value of the **sort** parameter. 
  'sort': "'recent_added_first'" // String | How do you want to sort playlist items? 
};
apiInstance.getPlaylistById(xListenAPIKey, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | 
 **id** | **String**| Playlist id (always 11 characters, e.g., m1pe7z60bsw). You can get the podcast id from the url of a playlist, e.g., m1pe7z60bsw is the playlist id of listennotes.com/listen/podcasts-about-podcasting-m1pe7z60bsw  | 
 **type** | **String**| The type of this playlist, which should be either **episode_list** or **podcast_list**.  | [optional] [default to &#39;episode_list&#39;]
 **lastTimestampMs** | **Number**| For playlist items pagination. It&#39;s the value of **last_timestamp_ms** from the response of last request. If it&#39;s 0 or not specified, just return the latest or the oldest 20 items, depending on the value of the **sort** parameter.  | [optional] [default to 0]
 **sort** | **String**| How do you want to sort playlist items?  | [optional] [default to &#39;recent_added_first&#39;]

### Return type

[**PlaylistResponse**](PlaylistResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlaylists

> PlaylistsResponse getPlaylists(xListenAPIKey, opts)

Fetch a list of your playlists.

This endpoint returns same data as listennotes.com/listen under your account. You can use the **page** parameter to do pagination and fetch more playlists. 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let opts = {
  'sort': "'recent_added_first'", // String | How do you want to sort playlists? 
  'page': 1 // Number | Page number of playlists. 
};
apiInstance.getPlaylists(xListenAPIKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | 
 **sort** | **String**| How do you want to sort playlists?  | [optional] [default to &#39;recent_added_first&#39;]
 **page** | **Number**| Page number of playlists.  | [optional] [default to 1]

### Return type

[**PlaylistsResponse**](PlaylistsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

