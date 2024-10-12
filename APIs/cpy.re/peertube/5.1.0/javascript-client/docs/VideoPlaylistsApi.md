# PeerTube.VideoPlaylistsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addPlaylist**](VideoPlaylistsApi.md#addPlaylist) | **POST** /api/v1/video-playlists | Create a video playlist
[**addVideoPlaylistVideo_0**](VideoPlaylistsApi.md#addVideoPlaylistVideo_0) | **POST** /api/v1/video-playlists/{playlistId}/videos | Add a video in a playlist
[**apiV1AccountsNameVideoPlaylistsGet**](VideoPlaylistsApi.md#apiV1AccountsNameVideoPlaylistsGet) | **GET** /api/v1/accounts/{name}/video-playlists | List playlists of an account
[**apiV1UsersMeVideoPlaylistsVideosExistGet**](VideoPlaylistsApi.md#apiV1UsersMeVideoPlaylistsVideosExistGet) | **GET** /api/v1/users/me/video-playlists/videos-exist | Check video exists in my playlists
[**apiV1VideoChannelsChannelHandleVideoPlaylistsGet**](VideoPlaylistsApi.md#apiV1VideoChannelsChannelHandleVideoPlaylistsGet) | **GET** /api/v1/video-channels/{channelHandle}/video-playlists | List playlists of a channel
[**apiV1VideoPlaylistsPlaylistIdDelete**](VideoPlaylistsApi.md#apiV1VideoPlaylistsPlaylistIdDelete) | **DELETE** /api/v1/video-playlists/{playlistId} | Delete a video playlist
[**apiV1VideoPlaylistsPlaylistIdGet**](VideoPlaylistsApi.md#apiV1VideoPlaylistsPlaylistIdGet) | **GET** /api/v1/video-playlists/{playlistId} | Get a video playlist
[**apiV1VideoPlaylistsPlaylistIdPut**](VideoPlaylistsApi.md#apiV1VideoPlaylistsPlaylistIdPut) | **PUT** /api/v1/video-playlists/{playlistId} | Update a video playlist
[**delVideoPlaylistVideo**](VideoPlaylistsApi.md#delVideoPlaylistVideo) | **DELETE** /api/v1/video-playlists/{playlistId}/videos/{playlistElementId} | Delete an element from a playlist
[**getPlaylistPrivacyPolicies**](VideoPlaylistsApi.md#getPlaylistPrivacyPolicies) | **GET** /api/v1/video-playlists/privacies | List available playlist privacy policies
[**getPlaylists**](VideoPlaylistsApi.md#getPlaylists) | **GET** /api/v1/video-playlists | List video playlists
[**getVideoPlaylistVideos_0**](VideoPlaylistsApi.md#getVideoPlaylistVideos_0) | **GET** /api/v1/video-playlists/{playlistId}/videos | List videos of a playlist
[**putVideoPlaylistVideo**](VideoPlaylistsApi.md#putVideoPlaylistVideo) | **PUT** /api/v1/video-playlists/{playlistId}/videos/{playlistElementId} | Update a playlist element
[**reorderVideoPlaylist**](VideoPlaylistsApi.md#reorderVideoPlaylist) | **POST** /api/v1/video-playlists/{playlistId}/videos/reorder | Reorder a playlist



## addPlaylist

> AddPlaylist200Response addPlaylist(displayName, opts)

Create a video playlist

If the video playlist is set as public, &#x60;videoChannelId&#x60; is mandatory.

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let displayName = "displayName_example"; // String | Video playlist display name
let opts = {
  'description': "description_example", // String | Video playlist description
  'privacy': new PeerTube.VideoPlaylistPrivacySet(), // VideoPlaylistPrivacySet | 
  'thumbnailfile': "/path/to/file", // File | Video playlist thumbnail file
  'videoChannelId': null // Number | Video channel in which the playlist will be published
};
apiInstance.addPlaylist(displayName, opts, (error, data, response) => {
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
 **displayName** | **String**| Video playlist display name | 
 **description** | **String**| Video playlist description | [optional] 
 **privacy** | [**VideoPlaylistPrivacySet**](VideoPlaylistPrivacySet.md)|  | [optional] 
 **thumbnailfile** | **File**| Video playlist thumbnail file | [optional] 
 **videoChannelId** | [**Number**](Number.md)| Video channel in which the playlist will be published | [optional] 

### Return type

[**AddPlaylist200Response**](AddPlaylist200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## addVideoPlaylistVideo_0

> AddVideoPlaylistVideo200Response addVideoPlaylistVideo_0(playlistId, opts)

Add a video in a playlist

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let playlistId = 56; // Number | Playlist id
let opts = {
  'addVideoPlaylistVideoRequest': new PeerTube.AddVideoPlaylistVideoRequest() // AddVideoPlaylistVideoRequest | 
};
apiInstance.addVideoPlaylistVideo_0(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **Number**| Playlist id | 
 **addVideoPlaylistVideoRequest** | [**AddVideoPlaylistVideoRequest**](AddVideoPlaylistVideoRequest.md)|  | [optional] 

### Return type

[**AddVideoPlaylistVideo200Response**](AddVideoPlaylistVideo200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiV1AccountsNameVideoPlaylistsGet

> ApiV1AccountsNameVideoPlaylistsGet200Response apiV1AccountsNameVideoPlaylistsGet(name, opts)

List playlists of an account

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let name = "chocobozzz | chocobozzz@example.org"; // String | The username or handle of the account
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt", // String | Sort column
  'search': "search_example", // String | Plain text search, applied to various parts of the model depending on endpoint
  'playlistType': new PeerTube.VideoPlaylistTypeSet() // VideoPlaylistTypeSet | 
};
apiInstance.apiV1AccountsNameVideoPlaylistsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The username or handle of the account | 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 
 **search** | **String**| Plain text search, applied to various parts of the model depending on endpoint | [optional] 
 **playlistType** | [**VideoPlaylistTypeSet**](.md)|  | [optional] 

### Return type

[**ApiV1AccountsNameVideoPlaylistsGet200Response**](ApiV1AccountsNameVideoPlaylistsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1UsersMeVideoPlaylistsVideosExistGet

> ApiV1UsersMeVideoPlaylistsVideosExistGet200Response apiV1UsersMeVideoPlaylistsVideosExistGet(videoIds)

Check video exists in my playlists

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let videoIds = [42]; // [Number] | The video ids to check
apiInstance.apiV1UsersMeVideoPlaylistsVideosExistGet(videoIds, (error, data, response) => {
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
 **videoIds** | [**[Number]**](Number.md)| The video ids to check | 

### Return type

[**ApiV1UsersMeVideoPlaylistsVideosExistGet200Response**](ApiV1UsersMeVideoPlaylistsVideosExistGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1VideoChannelsChannelHandleVideoPlaylistsGet

> ApiV1AccountsNameVideoPlaylistsGet200Response apiV1VideoChannelsChannelHandleVideoPlaylistsGet(channelHandle, opts)

List playlists of a channel

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let channelHandle = "my_username | my_username@example.com"; // String | The video channel handle
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt", // String | Sort column
  'playlistType': new PeerTube.VideoPlaylistTypeSet() // VideoPlaylistTypeSet | 
};
apiInstance.apiV1VideoChannelsChannelHandleVideoPlaylistsGet(channelHandle, opts, (error, data, response) => {
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
 **channelHandle** | **String**| The video channel handle | 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 
 **playlistType** | [**VideoPlaylistTypeSet**](.md)|  | [optional] 

### Return type

[**ApiV1AccountsNameVideoPlaylistsGet200Response**](ApiV1AccountsNameVideoPlaylistsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1VideoPlaylistsPlaylistIdDelete

> apiV1VideoPlaylistsPlaylistIdDelete(playlistId)

Delete a video playlist

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let playlistId = 56; // Number | Playlist id
apiInstance.apiV1VideoPlaylistsPlaylistIdDelete(playlistId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlistId** | **Number**| Playlist id | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1VideoPlaylistsPlaylistIdGet

> VideoPlaylist apiV1VideoPlaylistsPlaylistIdGet(playlistId)

Get a video playlist

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let playlistId = 56; // Number | Playlist id
apiInstance.apiV1VideoPlaylistsPlaylistIdGet(playlistId, (error, data, response) => {
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
 **playlistId** | **Number**| Playlist id | 

### Return type

[**VideoPlaylist**](VideoPlaylist.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1VideoPlaylistsPlaylistIdPut

> apiV1VideoPlaylistsPlaylistIdPut(playlistId, opts)

Update a video playlist

If the video playlist is set as public, the playlist must have a assigned channel.

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let playlistId = 56; // Number | Playlist id
let opts = {
  'description': "description_example", // String | Video playlist description
  'displayName': "displayName_example", // String | Video playlist display name
  'privacy': new PeerTube.VideoPlaylistPrivacySet(), // VideoPlaylistPrivacySet | 
  'thumbnailfile': "/path/to/file", // File | Video playlist thumbnail file
  'videoChannelId': null // Number | Video channel in which the playlist will be published
};
apiInstance.apiV1VideoPlaylistsPlaylistIdPut(playlistId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlistId** | **Number**| Playlist id | 
 **description** | **String**| Video playlist description | [optional] 
 **displayName** | **String**| Video playlist display name | [optional] 
 **privacy** | [**VideoPlaylistPrivacySet**](VideoPlaylistPrivacySet.md)|  | [optional] 
 **thumbnailfile** | **File**| Video playlist thumbnail file | [optional] 
 **videoChannelId** | [**Number**](Number.md)| Video channel in which the playlist will be published | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## delVideoPlaylistVideo

> delVideoPlaylistVideo(playlistId, playlistElementId)

Delete an element from a playlist

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let playlistId = 56; // Number | Playlist id
let playlistElementId = 56; // Number | Playlist element id
apiInstance.delVideoPlaylistVideo(playlistId, playlistElementId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlistId** | **Number**| Playlist id | 
 **playlistElementId** | **Number**| Playlist element id | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPlaylistPrivacyPolicies

> [String] getPlaylistPrivacyPolicies()

List available playlist privacy policies

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoPlaylistsApi();
apiInstance.getPlaylistPrivacyPolicies((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlaylists

> ApiV1AccountsNameVideoPlaylistsGet200Response getPlaylists(opts)

List video playlists

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt", // String | Sort column
  'playlistType': new PeerTube.VideoPlaylistTypeSet() // VideoPlaylistTypeSet | 
};
apiInstance.getPlaylists(opts, (error, data, response) => {
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
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 
 **playlistType** | [**VideoPlaylistTypeSet**](.md)|  | [optional] 

### Return type

[**ApiV1AccountsNameVideoPlaylistsGet200Response**](ApiV1AccountsNameVideoPlaylistsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoPlaylistVideos_0

> VideoListResponse getVideoPlaylistVideos_0(playlistId, opts)

List videos of a playlist

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let playlistId = 56; // Number | Playlist id
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15 // Number | Number of items to return
};
apiInstance.getVideoPlaylistVideos_0(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **Number**| Playlist id | 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putVideoPlaylistVideo

> putVideoPlaylistVideo(playlistId, playlistElementId, opts)

Update a playlist element

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let playlistId = 56; // Number | Playlist id
let playlistElementId = 56; // Number | Playlist element id
let opts = {
  'putVideoPlaylistVideoRequest': new PeerTube.PutVideoPlaylistVideoRequest() // PutVideoPlaylistVideoRequest | 
};
apiInstance.putVideoPlaylistVideo(playlistId, playlistElementId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlistId** | **Number**| Playlist id | 
 **playlistElementId** | **Number**| Playlist element id | 
 **putVideoPlaylistVideoRequest** | [**PutVideoPlaylistVideoRequest**](PutVideoPlaylistVideoRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## reorderVideoPlaylist

> reorderVideoPlaylist(playlistId, opts)

Reorder a playlist

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoPlaylistsApi();
let playlistId = 56; // Number | Playlist id
let opts = {
  'reorderVideoPlaylistRequest': new PeerTube.ReorderVideoPlaylistRequest() // ReorderVideoPlaylistRequest | 
};
apiInstance.reorderVideoPlaylist(playlistId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlistId** | **Number**| Playlist id | 
 **reorderVideoPlaylistRequest** | [**ReorderVideoPlaylistRequest**](ReorderVideoPlaylistRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

